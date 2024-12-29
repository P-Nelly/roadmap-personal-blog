from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import app
import os
import json
import markdown
from datetime import datetime

def get_articles():
    articles = []
    for filename in os.listdir(app.config['ARTICLES_PATH']):
        if filename.endswith('.json'):
            with open(os.path.join(app.config['ARTICLES_PATH'], filename), 'r') as f:
                article = json.load(f)
                article['id'] = filename[:-5]  # Remove .json extension
                article['content'] = markdown.markdown(article['content'])
                articles.append(article)
    return sorted(articles, key=lambda x: x['date'], reverse=True)

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    try:
        with open(os.path.join(app.config['ARTICLES_PATH'], f'{article_id}.json'), 'r') as f:
            article = json.load(f)
            article['id'] = article_id
            article['content'] = markdown.markdown(article['content'])
            return render_template('article.html', article=article)
    except FileNotFoundError:
        flash('Article not found')
        return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    articles = get_articles()
    return render_template('admin/dashboard.html', articles=articles)

@app.route('/admin/article/new', methods=['GET', 'POST'])
@login_required
def add_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required')
            return redirect(url_for('add_article'))
        
        article = {
            'title': title,
            'content': content,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Generate a simple ID from the title
        article_id = title.lower().replace(' ', '-')
        
        with open(os.path.join(app.config['ARTICLES_PATH'], f'{article_id}.json'), 'w') as f:
            json.dump(article, f)
        
        flash('Article created successfully')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/edit_article.html', article=None)

@app.route('/admin/article/<article_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article_path = os.path.join(app.config['ARTICLES_PATH'], f'{article_id}.json')
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required')
            return redirect(url_for('edit_article', article_id=article_id))
        
        article = {
            'title': title,
            'content': content,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        with open(article_path, 'w') as f:
            json.dump(article, f)
        
        flash('Article updated successfully')
        return redirect(url_for('admin_dashboard'))
    
    try:
        with open(article_path, 'r') as f:
            article = json.load(f)
            article['id'] = article_id
            return render_template('admin/edit_article.html', article=article)
    except FileNotFoundError:
        flash('Article not found')
        return redirect(url_for('admin_dashboard'))

@app.route('/admin/article/<article_id>/delete')
@login_required
def delete_article(article_id):
    try:
        os.remove(os.path.join(app.config['ARTICLES_PATH'], f'{article_id}.json'))
        flash('Article deleted successfully')
    except FileNotFoundError:
        flash('Article not found')
    return redirect(url_for('admin_dashboard')) 