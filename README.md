# Forum (Django)

The Django Forum Demo Project is a robust and user-friendly web application that showcases the power and versatility of Django, a high-level Python web framework. This demo forum provides a platform for users to engage in discussions, share ideas, and collaborate within a community setting. The project features essential forum functionalities such as user registration and authentication, threaded discussions, post creation and editing, as well as moderation tools for administrators. The design is responsive, ensuring a seamless user experience across various devices. With a clean and intuitive interface, the Django Forum Demo Project exemplifies the efficiency of Django in building scalable and dynamic web applications, making it an excellent resource for developers looking to understand and implement forum functionalities within their own projects.

## Requirements

- python 3
- database: Sqlite, MySQL or PostgreSQL
- web browser
- code editor
- git

## Installation

- git clone https://github.com/6hislain/forum
- cd forum
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- edit _forum/settings.py_ accordingly
- python manage.py migrate
- python manage.py serve

## TODO

- [ ] pages
 - [ ] home page
 - [ ] question detail
 - [ ] question list
 - [ ] topic detail
 - [ ] page detail