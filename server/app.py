from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///moringa_study_hub.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import models
from server.models.user import User
from server.models.course import Course
from server.models.enrollment import Enrollment
from server.models.discussion import Discussion

# Import routes
from server.routes.users import users_bp
from server.routes.courses import courses_bp
from server.routes.enrollments import enrollments_bp
from server.routes.discussions import discussions_bp

# Register blueprints
app.register_blueprint(users_bp, url_prefix='/api/users')
app.register_blueprint(courses_bp, url_prefix='/api/courses')
app.register_blueprint(enrollments_bp, url_prefix='/api/enrollments')
app.register_blueprint(discussions_bp, url_prefix='/api/discussions')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to MoringaStudyHub API!"})

if __name__ == '__main__':
    app.run(port=5001, debug=True) 