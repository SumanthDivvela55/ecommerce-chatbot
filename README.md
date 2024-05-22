# E-commerce Sales Chatbot

This project implements an interactive sales chatbot for an e-commerce platform specializing in a specific product category. It includes a frontend built with React.js and a backend built with Flask.

## Project Structure

- **Frontend:** React.js
- **Backend:** Flask
- **Database:** SQLite

## Setup Instructions

### Backend

1. Install the necessary Python packages:
    ```bash
    pip install -r backend/requirements.txt
    ```

2. Run the Flask application:
    ```bash
    cd backend
    python app.py
    ```

### Frontend

1. Install the necessary npm packages:
    ```bash
    cd frontend
    npm install
    ```

2. Run the React application:
    ```bash
    npm start
    ```

## Key Features

- User authentication with JWT.
- Chatbot interface for product search and exploration.
- Responsive design compatible with desktop, tablet, and mobile devices.
- Modular and clean code structure with robust error handling.

## Challenges and Solutions

- **Challenge:** Maintaining session continuity.
    - **Solution:** Used JWT tokens to manage user sessions securely.

- **Challenge:** Ensuring responsive design.
    - **Solution:** Utilized Bootstrap for consistent and responsive styling.

## Technology Stack

- **Frontend:** React.js, HTML5, CSS3, Bootstrap
- **Backend:** Flask, SQLAlchemy
- **Database:** SQLite
