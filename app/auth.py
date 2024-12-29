from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import UserMixin, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app import login_manager

bp = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# For simplicity, we'll use a hardcoded admin user
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = generate_password_hash("admin123")  # In production, use environment variables

@login_manager.user_loader
def load_user(user_id):
    if user_id == ADMIN_USERNAME:
        return User(ADMIN_USERNAME)
    return None

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD, password):
            user = User(username)
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin_dashboard'))
        flash('Invalid username or password')
    
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) 