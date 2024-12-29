# Personal Blog

A simple personal blog built with Flask that allows you to write and publish articles. The blog has both guest and admin sections.

## Features

- **Guest Section**
  - View list of published articles
  - Read individual articles
- **Admin Section**
  - Secure login
  - Dashboard to manage articles
  - Add new articles with Markdown support
  - Edit existing articles
  - Delete articles

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd personal-blog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   export SECRET_KEY=your-secret-key-here  # Change this in production
   ```

5. Run the application:
   ```bash
   flask run
   ```

The blog will be available at `http://localhost:5000`

## Usage

### Guest Access
- Visit the home page to see all published articles
- Click on an article title to read the full article

### Admin Access
1. Visit `/login` and use these credentials:
   - Username: `admin`
   - Password: `admin123`
2. After logging in, you'll have access to:
   - Dashboard: View all articles
   - Add Article: Create new articles
   - Edit/Delete: Manage existing articles

## Article Format

Articles are written in Markdown format, which supports:
- Headers
- Lists
- Links
- Code blocks
- And more!

## File Structure

```
personal-blog/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── auth.py
│   ├── articles/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── article.html
│   │   ├── login.html
│   │   └── admin/
│   │       ├── dashboard.html
│   │       └── edit_article.html
│   └── static/
│       └── css/
│           └── style.css
├── requirements.txt
└── README.md
```

## Security Notes

For production deployment:
1. Change the default admin credentials
2. Use a strong secret key
3. Enable HTTPS
4. Consider using a proper database instead of file storage
5. Implement proper session management

## License

This project is open source and available under the MIT License. 