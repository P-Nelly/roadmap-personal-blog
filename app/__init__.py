from flask import Flask
from flask_login import LoginManager, current_user
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['ARTICLES_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'articles')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Ensure articles directory exists
if not os.path.exists(app.config['ARTICLES_PATH']):
    os.makedirs(app.config['ARTICLES_PATH'])

# Add template context processors
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.context_processor
def inject_user():
    return {'current_user': current_user}

# Import routes after app is created
from app import routes, auth
app.register_blueprint(auth.bp)

if __name__ == '__main__':
    app.run(debug=True) 