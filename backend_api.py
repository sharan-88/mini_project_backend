"""
Backend API for AI Learning Planner
===================================

Simple Flask API to connect the frontend with the dynamic learning planner system.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import asyncio
import json
import os
from dynamic_learning_planner import DynamicLearningPlanner

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Initialize the learning planner
planner = DynamicLearningPlanner()

@app.route('/')
def index():
    """Serve the frontend"""
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('../frontend', filename)

@app.route('/api/create-plan', methods=['POST'])
def create_learning_plan():
    """Create a new learning plan based on user request"""
    try:
        data = request.get_json()
        user_request = data.get('userRequest', '')
        
        if not user_request:
            return jsonify({'error': 'User request is required'}), 400
        
        # Create user ID
        user_id = f"user_{hash(user_request) % 10000}"
        
        # Create learning plan (simplified for demo)
        plan = {
            'id': f"plan_{hash(user_request) % 10000}",
            'title': extract_plan_title(user_request),
            'timeline': extract_timeline(user_request),
            'lessons': extract_lesson_count(user_request),
            'goals': extract_goals(user_request),
            'subject': extract_subject(user_request),
            'user_id': user_id
        }
        
        return jsonify({
            'success': True,
            'plan': plan,
            'message': 'Learning plan created successfully!'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/start-session', methods=['POST'])
def start_learning_session():
    """Start a learning session"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        
        # Simulate session start
        session = {
            'id': f"session_{hash(user_id) % 10000}",
            'user_id': user_id,
            'start_time': '2024-01-01T00:00:00Z',
            'status': 'active',
            'lessons': get_current_lessons(user_id)
        }
        
        return jsonify({
            'success': True,
            'session': session,
            'message': 'Learning session started!'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/take-test', methods=['POST'])
def take_weekly_test():
    """Take a weekly test"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        
        # Simulate test
        score = simulate_test_score(user_id)
        
        return jsonify({
            'success': True,
            'score': score,
            'message': f'Test completed! Score: {score}%'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/end-session', methods=['POST'])
def end_learning_session():
    """End a learning session"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        
        return jsonify({
            'success': True,
            'message': 'Learning session ended successfully!'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/progress/<user_id>')
def get_progress(user_id):
    """Get user progress"""
    try:
        # Simulate progress data
        progress = {
            'lessons_completed': 12,
            'average_score': 75.5,
            'time_spent': 540,  # minutes
            'current_week': 4,
            'weekly_scores': [65, 70, 75, 82],
            'recommendations': [
                'Good progress! Continue with current pace',
                'Focus on areas where you scored lower'
            ]
        }
        
        return jsonify({
            'success': True,
            'progress': progress
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Helper functions
def extract_plan_title(user_request):
    """Extract plan title from user request"""
    if 'python' in user_request.lower():
        return 'Python Programming Mastery'
    elif 'javascript' in user_request.lower():
        return 'JavaScript Development'
    elif 'machine learning' in user_request.lower():
        return 'Machine Learning Journey'
    elif 'web development' in user_request.lower():
        return 'Web Development Path'
    else:
        return 'Personalized Learning Plan'

def extract_timeline(user_request):
    """Extract timeline from user request"""
    if '3 months' in user_request.lower():
        return '3 months'
    elif '6 months' in user_request.lower():
        return '6 months'
    elif '1 year' in user_request.lower():
        return '1 year'
    elif '6 weeks' in user_request.lower():
        return '6 weeks'
    else:
        return '3 months'

def extract_lesson_count(user_request):
    """Extract lesson count based on timeline"""
    if '3 months' in user_request.lower():
        return 10
    elif '6 months' in user_request.lower():
        return 20
    elif '1 year' in user_request.lower():
        return 40
    elif '6 weeks' in user_request.lower():
        return 8
    else:
        return 10

def extract_goals(user_request):
    """Extract goals from user request"""
    goals = ['Master the subject', 'Build practical skills']
    if 'job' in user_request.lower():
        goals.append('Prepare for job interviews')
    if 'project' in user_request.lower():
        goals.append('Build real-world projects')
    if 'certification' in user_request.lower():
        goals.append('Prepare for certification')
    return goals

def extract_subject(user_request):
    """Extract subject from user request"""
    if 'python' in user_request.lower():
        return 'Python'
    elif 'javascript' in user_request.lower():
        return 'JavaScript'
    elif 'machine learning' in user_request.lower():
        return 'Machine Learning'
    elif 'web development' in user_request.lower():
        return 'Web Development'
    else:
        return 'Programming'

def get_current_lessons(user_id):
    """Get current week's lessons"""
    return [
        'Introduction to Variables',
        'Control Structures',
        'Functions and Modules'
    ]

def simulate_test_score(user_id):
    """Simulate a test score"""
    import random
    base_score = 60
    variation = random.randint(-15, 25)
    return max(0, min(100, base_score + variation))

if __name__ == '__main__':
    print("🚀 Starting AI Learning Planner Backend API")
    print("📡 API will be available at: http://localhost:5000")
    print("🌐 Frontend will be available at: http://localhost:5000")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

