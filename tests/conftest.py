import os
import tempfile
import pytest
from app import app as flask_app
from flask_login import login_user
from app.auth import User

@pytest.fixture
def app():
    # Create a temporary file to store test articles
    db_fd, db_path = tempfile.mkstemp()
    test_articles_path = tempfile.mkdtemp()
    
    flask_app.config.update({
        'TESTING': True,
        'ARTICLES_PATH': test_articles_path,
        'SECRET_KEY': 'test-key'
    })

    yield flask_app

    # Clean up temporary files
    os.close(db_fd)
    os.unlink(db_path)
    for root, dirs, files in os.walk(test_articles_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(test_articles_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def auth(client):
    class AuthActions:
        def __init__(self, client):
            self._client = client

        def login(self, username="admin", password="admin123"):
            return self._client.post(
                '/login',
                data={'username': username, 'password': password}
            )

        def logout(self):
            return self._client.get('/logout')

    return AuthActions(client)

@pytest.fixture
def authenticated_client(client, auth):
    auth.login()
    return client 