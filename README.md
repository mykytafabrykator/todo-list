# Todo List Project

## Description
This project implements a simple todo list website. It allows users to create, edit, delete, and mark tasks as complete. Each task can have multiple tags, allowing for categorization.

# Installation

Python3 must be already installed

```shell
git clone https://github.com/mykytafabrykator/todo-list.git
cd todo-list
python3 -m venv venv
source venv/bin/activate (on macOS)
venv/Scripts/activate (on Windows)
pip install -r requirements.txt
```

Create a `.env` file in the root directory of the project and copy the contents from `.env.sample`, replacing the placeholder values with your own:

```shell
cp .env.sample .env
```

You`re ready to start

```shell
python manage.py migrate
python manage.py runserver
```

## Features

- **Tasks**
  - Each task has content, a creation date, an optional deadline, a completion status, and relevant tags.
  - Tasks are displayed from the most recent to the oldest and grouped by their completion status (incomplete tasks first).
  
- **Tags**
  - Tags represent themes or categories for tasks.
  - Each task can be associated with multiple tags, and a tag can be linked to multiple tasks.

- **Pages**
  - **Home page**: Displays the todo list with options to add new tasks, edit, delete, and mark tasks as complete or incomplete.
  - **Tag list page**: Shows all tags with options to add, edit, or delete tags.
