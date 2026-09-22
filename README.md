# Django Bulletin Board

A web application built with Django (MVT architecture) for posting, managing, and searching classified ads.

## Key Features

- **Authentication System:** User registration, login, and logout.
- **Ad Management (CRUD):**
  - Create, view, edit, and delete ads.
  - Object-level permissions (users can only edit or delete their own posts).
- **Search and Filtering:**
  - Search listings by title and description.
  - Filter ads by category.
- **Admin Panel:** Management of users and categories via Django Admin.

## Repository Structure

- **ads/**: Core application containing views, models, forms, and URL routing.
- **board_project/**: Main project configuration (settings and root URL routing).
- **templates/**: HTML templates for ads and authentication pages.
- **requirements.txt**: Project dependencies and package list.

## Tech Stack

- **Python 3**
- **Django 5**
- **SQLite3**
- **HTML**
