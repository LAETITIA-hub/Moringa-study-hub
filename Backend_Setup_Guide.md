# Backend Setup and Run Guide - Moringa Study Hub

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- `python3-venv` package (install with `sudo apt install python3-venv` on Ubuntu/Debian if needed)

## Step-by-Step Setup Instructions

### 1. Navigate to the Project Root
```bash
cd /workspace
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

For SQLite (recommended for development):
```bash
pip install Flask==2.3.3 Flask-SQLAlchemy==3.0.5 Flask-Migrate==4.0.5 Flask-CORS==4.0.0 python-dotenv==1.0.0 email-validator==2.0.0
```

**Note**: If you encounter issues with `psycopg2-binary` from requirements.txt, skip it as it's only needed for PostgreSQL production setups. The app uses SQLite by default.

For full requirements (including PostgreSQL support):
```bash
# Install PostgreSQL development headers first (Ubuntu/Debian)
sudo apt install libpq-dev

# Then install all requirements
pip install -r requirements.txt
```

### 4. Set Up Database
The application uses SQLite by default. You have two options:

#### Option A: Use Existing Database
If you want to use the existing database:
```bash
# The database file already exists at instance/moringa_study_hub.db
# No additional setup needed
```

#### Option B: Fresh Database Setup
If you want to start fresh:
```bash
# Navigate to server directory
cd server

# Initialize database migrations (if not already done)
flask db init

# Create migration files
flask db migrate -m "Initial migration"

# Apply migrations
flask db upgrade
```

### 5. Seed Database (Optional)
To populate the database with sample data:
```bash
# From the server directory
python seed.py
```

This will create:
- Sample users (instructors and students)
- Sample courses
- Sample enrollments
- Sample discussions

### 6. Run the Backend Server

#### Method 1: Run from server directory
```bash
cd server
python app.py
```

#### Method 2: Run the seed file (includes server start)
```bash
cd server
python seed.py
```

## Server Configuration

- **Port**: 5001
- **Debug Mode**: Enabled
- **Database**: SQLite (moringa_study_hub.db)
- **API Base URL**: `http://localhost:5001`

## Available API Endpoints

Once the server is running, you can access:

- **Home**: `GET http://localhost:5001/` - Welcome message
- **Users**: `http://localhost:5001/api/users`
- **Courses**: `http://localhost:5001/api/courses`
- **Enrollments**: `http://localhost:5001/api/enrollments`
- **Discussions**: `http://localhost:5001/api/discussions`

## Project Structure

```
server/
├── __init__.py         # Flask app factory
├── app.py             # Main application entry point
├── seed.py            # Database seeding script
├── models/            # Database models
│   ├── user.py
│   ├── course.py
│   ├── enrollment.py
│   └── discussion.py
└── routes/            # API route blueprints
    ├── users.py
    ├── courses.py
    ├── enrollments.py
    └── discussions.py
```

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 5001 is busy, modify the port in `app.py`:
   ```python
   app.run(port=5002, debug=True)  # Change to different port
   ```

2. **Database errors**: Make sure you're in the `server` directory when running the application

3. **Import errors**: Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

4. **Permission errors**: Make sure you have write permissions in the project directory

### Environment Variables (Optional)

You can set a custom database URL using:
```bash
export DATABASE_URL="your_database_url_here"
```

By default, it uses SQLite at `sqlite:///moringa_study_hub.db`

## Development Notes

- The application uses Flask-CORS for cross-origin requests
- SQLAlchemy for ORM
- Flask-Migrate for database migrations
- Debug mode is enabled for development

## Quick Start Commands

```bash
# Quick setup and run (Recommended)
cd /workspace
python3 -m venv venv
source venv/bin/activate
pip install Flask==2.3.3 Flask-SQLAlchemy==3.0.5 Flask-Migrate==4.0.5 Flask-CORS==4.0.0 python-dotenv==1.0.0 email-validator==2.0.0
cd server
python seed.py  # This seeds the database and starts the server

# Alternative: Just run the server (without seeding)
cd server
python app.py
```

The backend will be running at `http://localhost:5001` and ready to serve API requests to your React frontend!

## ✅ Verification

Once your server is running, you can verify it's working by testing these endpoints:

```bash
# Test the home endpoint
curl http://localhost:5001/

# Test the API endpoints
curl http://localhost:5001/api/users
curl http://localhost:5001/api/courses
curl http://localhost:5001/api/enrollments
curl http://localhost:5001/api/discussions
```

**Expected Response Examples:**

- Home: `{"message": "Welcome to MoringaStudyHub API!"}`
- Users: Array of user objects with sample data
- Courses: Array of course objects with sample data
- And so on...

## ✅ Success! 

Your Moringa Study Hub backend is now successfully running and ready to connect with your React frontend!