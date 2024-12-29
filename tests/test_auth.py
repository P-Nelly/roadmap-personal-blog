import pytest
from flask import session, g

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_login_success(client, auth):
    response = auth.login()
    assert response.headers['Location'] == '/admin'

def test_login_invalid_credentials(client, auth):
    response = auth.login('wrong', 'credentials')
    assert b'Invalid username or password' in response.data

def test_logout(client, auth):
    auth.login()
    response = auth.logout()
    assert response.headers['Location'] == '/'

def test_login_required(client):
    response = client.get('/admin')
    assert response.headers['Location'].startswith('/login')

def test_login_required_add_article(client):
    response = client.get('/admin/article/new')
    assert response.headers['Location'].startswith('/login')

def test_login_required_edit_article(client):
    response = client.get('/admin/article/test/edit')
    assert response.headers['Location'].startswith('/login')

def test_login_required_delete_article(client):
    response = client.get('/admin/article/test/delete')
    assert response.headers['Location'].startswith('/login') 