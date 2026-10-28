# Django Bulletin Board Platform

A full-stack web application for managing bulletin boards, publishing announcements, and filtering listings by categories.

## Key Features

* Announcement Management: Full CRUD operations for user listings and posts
* Category Filtering: Filter announcements by specific topics and tags
* User Authentication: Secure user registration, authorization, and post ownership

## Tech Stack

* Python 3
* Django
* HTML/CSS
* SQLite3

## Getting Started

1. Clone the repository:
   git clone https://github.com/divarusa/bulletin-board-django.git
   cd bulletin-board-django

2. Setup virtual environment and dependencies:
   python3 -m venv venv
   source venv/bin/activate
   pip install django

3. Run migrations and start the server:
   python manage.py migrate
   python manage.py runserver
