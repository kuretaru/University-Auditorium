# University Auditorium Booking System

## Description

This project is a web application built with Flask that allows users to book university auditoriums. It supports multiple languages and provides a user-friendly interface for managing bookings. The application features user authentication, auditorium listing, booking creation, and a basic profile page.

## Features

*   **User Authentication:**
    *   Registration with username, email, password, and optional teacher status.
    *   Login with email and password.
    *   Password hashing for security.
    *   "Remember Me" functionality.
    *   Logout.
*   **Auditorium Booking:**
    *   Authenticated users can book auditoriums.
    *   Booking form includes:
        *   Title
        *   Auditorium Number (from a predefined list)
        *   Date
        *   Time
    *   Displays upcoming bookings for the logged-in user.
    *   Basic deletion of own bookings.
*   **Multi-language Support:**
    *   English (en)
    *   Chinese (cn)
    *   German (de)
    *   Russian (ru)
    *   Language selection persists across sessions (using Flask sessions). User's language preferences upon registration
*   **Database:**
    *   Uses SQLAlchemy for database interactions.
    *   SQLite database for development (easily switchable to other databases).
    *   Database migrations with Flask-Migrate.
*   **Basic UI:**
      * Simple HTML/CSS styling.
      * Basic responsiveness.
*   Error Handling:
    * Basic validation of forms.
    * Displays error messages to the user.

## Technologies Used

*   **Python:** The core programming language.
*   **Flask:** A micro web framework for Python.
*   **Flask-SQLAlchemy:** Flask extension for easy SQLAlchemy integration.
*   **Flask-Migrate:** Flask extension for database migrations.
*   **Flask-WTF:** Flask extension for form handling and validation.
*   **Flask-Login:** Flask extension for user session management.
*   **Werkzeug:** Provides utilities for WSGI applications, including password hashing.
*   **python-dotenv:** Loads environment variables from a `.env` file.
*   **HTML/CSS:** For the front-end structure and styling.
*   **SQLite:** Database engine.

## Project Structure

```
University-Auditorium/
├── core/                        # Main application logic
│   ├── __init__.py              # Initializes the core application
│   ├── auth/                    # Authentication module
│   │   ├── __init__.py          # Initializes the auth blueprint
│   │   ├── forms.py             # Authentication forms (Login, Registration)
│   │   ├── models.py            # User model
│   │   ├── templates/           # Authentication templates
│   │   │   ├── de/             # German Translation
│   │   │   ├── base.html
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── views.py             # Authentication views (login, register, logout)
│   ├── audithory/                # Auditorium booking module
│   │   ├── __init__.py          # Initializes the courses blueprint
│   │   ├── forms.py             # Booking form
│   │   ├── models.py            # Number model (for auditorium numbers)
│   │   ├── templates/           # Booking templates
│   │   │   └── audithory/
│   │   │       └── book-audithory.html   # Main booking page
│   │   └── views.py             # Booking views
│   ├── static/                  # Static files (CSS)
│   │   └── style.css
│   ├── templates/               # Base and language-specific templates
│   │    ├── audithory/
│   │    │     └──book-audithory.html
│   │    ├── cn/                  # Chinese templates
│   │    │   ├── classes.html
│   │    │   ├── contact.html
│   │    │   └── index.html
│   │    ├── de/                  # German templates
│   │    │   ├── classes.html
│   │    │   ├── contact.html
│   │    │   └── index.html
│   │    ├── base.html            # Base template
│   │    └── index.html             # Main index page
│   ├── models.py                # Main application models (Users, Audithories)
│   ├── views.py             # Main application views(language changer)
│   └── utils.py              # Utility functions
├── migrations/                  # Database migration files
├── venv/                        # Virtual environment (not included in the provided file list, but essential)
├── config.py                    # Application configuration
├── main.py                      # Application entry point
└── users.db                     # SQLite database file (created automatically)
└── .env                         #Contains FLASK_SECRET_KEY and DATABASE_URL

```

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd University-Auditorium
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create `requirements.txt` based on the provided code:  `Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF Flask-Login Werkzeug python-dotenv`)

4.  **Set up environment variables:**

    *   Create a `.env` file in the root directory.
    *   Add the following variables to the `.env` file:

        ```
        FLASK_SECRET_KEY=<your_secret_key>  # Generate a strong, random secret key
        DATABASE_URL=sqlite:///users.db     # Or your preferred database URL
        ```
    * It is crucial to keep FLASK_SECRET_KEY secret in production.

5.  **Initialize and migrate the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6.  **Run the application:**

    ```bash
    python main.py
    ```

    The application will be accessible at `http://localhost:8080`.

## Database Migrations

Whenever you make changes to your database models (in `core/models.py` or `core/audithory/models.py`), you need to create and apply a migration:

1.  **Create a migration:**

    ```bash
    flask db migrate -m "Description of your changes"
    ```

2.  **Apply the migration:**

    ```bash
    flask db upgrade
    ```

##  Improvements and Future Enhancements

*   **Auditorium Availability:**
    *   Implement a system to check for conflicting bookings.
    *   Show available time slots visually (e.g., a calendar).
*   **Admin Panel:**
    *   Create an admin interface to manage users, auditoriums, and bookings.
    *   Allow admins to approve/reject booking requests.
*   **Email Notifications:**
    *   Send email confirmations and reminders for bookings.
    *   Notify users about booking status changes.
* **User Roles:**
    *   Implement more granular user roles (e.g., student, faculty, staff).
    *   Restrict access to certain features based on roles.
*   **Search and Filtering:**
    *   Allow users to search for auditoriums based on capacity, features, etc.
    *   Add filtering options to the booking list.
*   **Improved UI/UX:**
    *   Use a front-end framework (e.g., Bootstrap, Tailwind CSS) for a more polished look.
    *   Add JavaScript for dynamic interactions.
    *   Improve responsiveness for different screen sizes.
*   **Testing:**
    *   Write unit and integration tests to ensure code quality and prevent regressions.
* **Deployment:**
     * Provide instructions for deploying the application to a production environment (e.g., using Gunicorn, Nginx, and a database server like PostgreSQL).
* **Error Handling:**
    * Implement more robust error handling and logging.
* **Security:**
    * Add protection against common web vulnerabilities (e.g., CSRF, XSS).
    * Implement rate limiting to prevent abuse.
    * Consider using HTTPS.
* **Refactoring:**
    * Break down large functions into smaller, more manageable ones.
    * Improve code organization and readability.

This comprehensive README provides a solid foundation for understanding, installing, running, and extending the University Auditorium Booking System. It clearly outlines the features, technologies, setup steps, and potential improvements, making it a valuable resource for developers and users alike.
