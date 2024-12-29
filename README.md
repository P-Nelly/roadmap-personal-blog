<div align="left" style="position: relative;">
<img src="https://img.icons8.com/?size=512&id=55494&format=png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>ROADMAP-PERSONAL-BLOG</h1>
<p align="left">
	<em><code>❯ A modern, minimalist blog platform built with Flask, featuring Markdown support and secure admin controls</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/P-Nelly/roadmap-personal-blog?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/P-Nelly/roadmap-personal-blog?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/P-Nelly/roadmap-personal-blog?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/P-Nelly/roadmap-personal-blog?style=default&color=0080ff" alt="repo-language-count">
</p>
</div>
<br clear="right">

##  Table of Contents

- [ Overview](#overview)
- [ Features](#features)
- [ Project Structure](#project-structure)
  - [ Project Index](#project-index)
- [ Getting Started](#getting-started)
  - [ Prerequisites](#prerequisites)
  - [ Installation](#installation)
  - [ Usage](#usage)
  - [ Testing](#testing)
- [ Project Roadmap](#project-roadmap)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)

---

##  Overview

<code>❯ A Flask-based personal blog platform that allows you to write and publish articles with Markdown support. The application features a public-facing blog interface and a secure admin section for content management. Articles are stored as JSON files, making it lightweight and easy to deploy.</code>

---

##  Features

<code>❯ Key features of the blog platform include:
- Public article viewing with a clean, responsive interface
- Markdown support for rich content formatting
- Secure admin authentication system
- Article management (create, edit, delete)
- JSON-based storage for simplicity
- Modern UI with responsive design
- Comprehensive test coverage</code>

---

##  Project Structure

```sh
└── roadmap-personal-blog/
    ├── LICENSE
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── articles
    │   ├── auth.py
    │   ├── routes.py
    │   ├── static
    │   └── templates
    ├── pytest.ini
    ├── requirements.txt
    └── tests
        ├── conftest.py
        ├── test_articles.py
        └── test_auth.py
```

###  Project Index
<details open>
	<summary><b><code>ROADMAP-PERSONAL-BLOG/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/pytest.ini'>pytest.ini</a></b></td>
				<td><code>❯ Configuration file for pytest with coverage settings</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ Project dependencies and their versions</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details>
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/routes.py'>routes.py</a></b></td>
				<td><code>❯ Main application routes and article management logic</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/auth.py'>auth.py</a></b></td>
				<td><code>❯ Authentication system with login/logout functionality</code></td>
			</tr>
			</table>
			<details>
				<summary><b>articles</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/articles/welcome.json'>welcome.json</a></b></td>
						<td><code>❯ Default welcome article for new installations</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/templates/article.html'>article.html</a></b></td>
						<td><code>❯ Template for displaying individual articles</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/templates/login.html'>login.html</a></b></td>
						<td><code>❯ Admin login page template</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/templates/index.html'>index.html</a></b></td>
						<td><code>❯ Home page template with article list</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/templates/base.html'>base.html</a></b></td>
						<td><code>❯ Base template with common layout elements</code></td>
					</tr>
					</table>
					<details>
						<summary><b>admin</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/templates/admin/edit_article.html'>edit_article.html</a></b></td>
								<td><code>❯ Template for creating and editing articles</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/P-Nelly/roadmap-personal-blog/blob/master/app/templates/admin/dashboard.html'>dashboard.html</a></b></td>
								<td><code>❯ Admin dashboard template for article management</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with roadmap-personal-blog, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.7+
- **Package Manager:** Pip
- **Operating System:** Linux, macOS, or Windows


###  Installation

Install roadmap-personal-blog using one of the following methods:

**Build from source:**

1. Clone the roadmap-personal-blog repository:
```sh
❯ git clone https://github.com/P-Nelly/roadmap-personal-blog
```

2. Navigate to the project directory:
```sh
❯ cd roadmap-personal-blog
```

3. Install the project dependencies:

```sh
❯ python -m venv venv
❯ source venv/bin/activate  # On Windows: venv\Scripts\activate
❯ pip install -r requirements.txt
```

###  Usage
Run roadmap-personal-blog using the following commands:

```sh
❯ export FLASK_APP=app
❯ export FLASK_ENV=development
❯ export SECRET_KEY=your-secret-key-here
❯ flask run
```

The blog will be available at `http://localhost:5000`. Use these credentials for admin access:
- Username: `admin`
- Password: `admin123`

###  Testing
Run the test suite using the following command:

```sh
❯ python -m pytest
```

---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement basic blog functionality with article management</strike>
- [X] **`Task 2`**: <strike>Add authentication system for admin access</strike>
- [X] **`Task 3`**: <strike>Create responsive UI with modern design</strike>
- [ ] **`Task 4`**: Add image upload support for articles
- [ ] **`Task 5`**: Implement article categories and tags
- [ ] **`Task 6`**: Add user comments system
- [ ] **`Task 7`**: Implement search functionality
- [ ] **`Task 8`**: Add RSS feed support

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/P-Nelly/roadmap-personal-blog/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/P-Nelly/roadmap-personal-blog/issues)**: Submit bugs found or log feature requests for the `roadmap-personal-blog` project.
- **💡 [Submit Pull Requests](https://github.com/P-Nelly/roadmap-personal-blog/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/P-Nelly/roadmap-personal-blog
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/P-Nelly/roadmap-personal-blog/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=P-Nelly/roadmap-personal-blog">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](LICENSE) file.

---

##  Acknowledgments

- Flask framework and its contributors
- Python Markdown library
- Bootstrap for UI components
- Icons8 for the project icon
- The open-source community for inspiration and tools
- Build as a Roadmap Project: https://roadmap.sh/projects/personal-blog

--- 