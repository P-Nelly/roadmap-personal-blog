import pytest
import json
import os

def test_empty_articles_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'No articles published yet' in response.data

def test_create_article(authenticated_client, app):
    response = authenticated_client.post('/admin/article/new', data={
        'title': 'Test Article',
        'content': '# Test Content\n\nThis is a test article.'
    })
    assert response.headers['Location'] == '/admin'
    
    # Verify article was created
    article_path = os.path.join(app.config['ARTICLES_PATH'], 'test-article.json')
    assert os.path.exists(article_path)
    
    with open(article_path, 'r') as f:
        article = json.load(f)
        assert article['title'] == 'Test Article'
        assert article['content'] == '# Test Content\n\nThis is a test article.'

def test_view_article(authenticated_client, app):
    # Create test article
    article_data = {
        'title': 'Test Article',
        'content': '# Test Content\n\nThis is a test article.',
        'date': '2023-12-29 14:00:00'
    }
    article_path = os.path.join(app.config['ARTICLES_PATH'], 'test-article.json')
    with open(article_path, 'w') as f:
        json.dump(article_data, f)
    
    # Test viewing the article
    response = authenticated_client.get('/article/test-article')
    assert response.status_code == 200
    assert b'Test Article' in response.data
    assert b'Test Content' in response.data

def test_edit_article(authenticated_client, app):
    # Create test article
    article_data = {
        'title': 'Original Title',
        'content': 'Original content',
        'date': '2023-12-29 14:00:00'
    }
    article_path = os.path.join(app.config['ARTICLES_PATH'], 'original-title.json')
    with open(article_path, 'w') as f:
        json.dump(article_data, f)
    
    # Test editing the article
    response = authenticated_client.post('/admin/article/original-title/edit', data={
        'title': 'Updated Title',
        'content': 'Updated content'
    })
    assert response.headers['Location'] == '/admin'
    
    # Verify article was updated
    with open(article_path, 'r') as f:
        article = json.load(f)
        assert article['title'] == 'Updated Title'
        assert article['content'] == 'Updated content'

def test_delete_article(authenticated_client, app):
    # Create test article
    article_data = {
        'title': 'Test Article',
        'content': 'Test content',
        'date': '2023-12-29 14:00:00'
    }
    article_path = os.path.join(app.config['ARTICLES_PATH'], 'test-article.json')
    with open(article_path, 'w') as f:
        json.dump(article_data, f)
    
    # Test deleting the article
    response = authenticated_client.get('/admin/article/test-article/delete')
    assert response.headers['Location'] == '/admin'
    assert not os.path.exists(article_path)

def test_article_not_found(client):
    response = client.get('/article/non-existent')
    assert response.headers['Location'] == '/'

def test_markdown_rendering(client, app):
    # Create test article with Markdown content
    article_data = {
        'title': 'Markdown Test',
        'content': '# Header\n\n- List item 1\n- List item 2\n\n**Bold text**',
        'date': '2023-12-29 14:00:00'
    }
    article_path = os.path.join(app.config['ARTICLES_PATH'], 'markdown-test.json')
    with open(article_path, 'w') as f:
        json.dump(article_data, f)
    
    # Test viewing the rendered article
    response = client.get('/article/markdown-test')
    assert response.status_code == 200
    assert b'<h1>Header</h1>' in response.data
    assert b'<ul>' in response.data
    assert b'<li>List item 1</li>' in response.data
    assert b'<strong>Bold text</strong>' in response.data

def test_article_validation(authenticated_client):
    # Test empty title
    response = authenticated_client.post('/admin/article/new', data={
        'title': '',
        'content': 'Test content'
    })
    assert response.headers['Location'] == '/admin/article/new'
    
    # Test empty content
    response = authenticated_client.post('/admin/article/new', data={
        'title': 'Test Title',
        'content': ''
    })
    assert response.headers['Location'] == '/admin/article/new' 