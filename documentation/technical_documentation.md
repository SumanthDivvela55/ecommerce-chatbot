# Technical Documentation

## Project Overview

This project implements a comprehensive sales chatbot tailored for an e-commerce platform specializing in a specific product category. The aim is to enhance the shopping experience by enabling efficient search, exploration, and purchase processes.

## Architecture

The project is divided into two main parts: the frontend and the backend.

### Frontend

- **Framework:** React.js
- **Styling:** HTML5, CSS3, Bootstrap
- **Components:**
  - **Chatbot.js:** Manages the chatbot interface and handles user queries.
  - **Login.js:** Manages user authentication.
  - **AuthProvider.js:** Provides authentication context to other components.
  - **App.js:** Main application component that routes between login and chatbot components.
  - **index.js:** Entry point for the React application.

### Backend

- **Framework:** Flask
- **Database:** SQLite
- **Modules:**
  - **app.py:** Main application file that initializes the Flask app and sets up routes.
  - **models.py:** Defines the database models for users and products.
  - **database.py:** Initializes the SQLAlchemy database connection.
  - **auth.py:** Handles user authentication and authorization.
  - **config.py:** Configuration file for the Flask application.

## Database Schema

### User

- **id:** Integer, primary key
- **username:** String, unique, not null
- **password:** String, not null

### Product

- **id:** Integer, primary key
- **name:** String, not null
- **description:** String, not null
- **price:** Float, not null

## Setup and Execution

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

## Challenges and Solutions

- **Challenge:** Maintaining session continuity.
  - **Solution:** Used JWT tokens to manage user sessions securely.
  
- **Challenge:** Ensuring responsive design.
  - **Solution:** Utilized Bootstrap for consistent and responsive styling.

## Conclusion

This project demonstrates the implementation of a sales chatbot for an e-commerce platform, with a focus on enhancing user experience through efficient product search and exploration. The modular architecture and clean code structure ensure maintainability and scalability.

## Future Enhancements

- Implement more advanced natural language processing for better query understanding.
- Add more features to the chatbot, such as recommendations and personalized offers.
- Improve the authentication system with features like password hashing and OAuth integration.
