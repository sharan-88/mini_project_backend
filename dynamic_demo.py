"""
Dynamic Learning System Demo
===========================

This demo showcases the fully dynamic learning system that creates
lessons and curricula using LLM without any hardcoded content.
"""

import asyncio
import json
from datetime import datetime
from enhanced_tutoring_system import EnhancedTutoringSystem, SystemConfig
from models import UserProfile, UserProgress
from dynamic_lesson_generator import DynamicLessonGenerator

async def demo_dynamic_lesson_creation():
    """Demonstrate dynamic lesson creation"""
    
    print("🎯 Dynamic Lesson Creation Demo")
    print("=" * 50)
    
    # Initialize system
    config = SystemConfig(
        llm_provider="google",
        llm_api_key="demo-key",
        llm_model="gemini-pro",
        enable_analytics=True,
        enable_gap_analysis=True,
        enable_learning_curves=True,
        enable_mdp_recommendations=True
    )
    
    system = EnhancedTutoringSystem(config)
    
    # Create user profile
    user_profile = UserProfile(
        user_id="demo_user_001",
        name="Alex Johnson",
        email="alex@example.com",
        learning_style="visual",
        preferred_difficulty="intermediate",
        available_time=90,
        learning_goals=["Master Python programming", "Build web applications", "Learn data science"],
        interests=["Web development", "Machine learning", "Data visualization"]
    )
    
    system.user_profiles["demo_user_001"] = user_profile
    
    # Example 1: Create a single dynamic lesson
    print("\n📖 Creating single dynamic lesson...")
    lesson = await system.create_dynamic_lesson(
        subject="Python Programming",
        topic="Decorators and Context Managers",
        difficulty="intermediate",
        user_profile=user_profile
    )
    
    print(f"✅ Lesson created: {lesson.title}")
    print(f"📝 Content length: {len(lesson.content)} characters")
    print(f"🎯 Learning objectives: {len(lesson.learning_objectives)}")
    print(f"❓ Assessment questions: {len(lesson.assessment_questions)}")
    print(f"💪 Practice exercises: {len(lesson.practice_exercises)}")
    
    # Show lesson details
    print(f"\n📋 Lesson Details:")
    print(f"   - ID: {lesson.lesson_id}")
    print(f"   - Duration: {lesson.duration} minutes")
    print(f"   - Difficulty: {lesson.difficulty}")
    print(f"   - Prerequisites: {lesson.prerequisites}")
    
    # Example 2: Create a complete curriculum
    print(f"\n📚 Creating dynamic curriculum...")
    curriculum = await system.create_dynamic_curriculum(
        subject="Machine Learning",
        level="beginner",
        duration_weeks=6,
        user_profile=user_profile
    )
    
    print(f"✅ Curriculum created: {len(curriculum)} lessons")
    print(f"📋 Curriculum overview:")
    for i, lesson in enumerate(curriculum[:5], 1):
        print(f"   {i}. {lesson.title} ({lesson.difficulty})")
    
    # Example 3: Create personalized learning path
    print(f"\n🛤️ Creating personalized learning path...")
    path_id = await system.create_personalized_learning_path(
        user_id="demo_user_001",
        user_request="I want to learn Python for data science in 4 months with hands-on projects and weekly assessments",
        user_profile=user_profile
    )
    
    print(f"✅ Learning path created: {path_id}")
    
    # Get learning path details
    learning_path = system.learning_paths[path_id]
    print(f"📋 Path details:")
    print(f"   - Title: {learning_path.title}")
    print(f"   - Description: {learning_path.description[:100]}...")
    print(f"   - Lessons: {len(learning_path.lessons)}")
    print(f"   - Duration: {learning_path.estimated_duration} minutes")
    print(f"   - Status: {learning_path.status}")
    
    return system

async def demo_adaptive_learning():
    """Demonstrate adaptive learning features"""
    
    print("\n🎯 Adaptive Learning Demo")
    print("=" * 50)
    
    # Initialize system
    config = SystemConfig(
        llm_provider="google",
        llm_api_key="demo-key",
        llm_model="gemini-pro"
    )
    
    system = EnhancedTutoringSystem(config)
    
    # Create user with specific learning style
    user_profile = UserProfile(
        user_id="adaptive_user",
        name="Sarah Chen",
        email="sarah@example.com",
        learning_style="kinesthetic",
        preferred_difficulty="beginner",
        available_time=45,
        learning_goals=["Learn programming fundamentals", "Build first mobile app"],
        interests=["Mobile development", "User interface design"]
    )
    
    system.user_profiles["adaptive_user"] = user_profile
    
    # Create user progress
    user_progress = UserProgress(
        user_id="adaptive_user",
        completed_lessons=["intro_001", "basics_002"],
        test_scores=[0.75, 0.82, 0.68],
        current_difficulty="intermediate",
        learning_style="kinesthetic",
        total_time_spent=180,
        streak_days=5,
        learning_goals=["Learn programming fundamentals", "Build first mobile app"]
    )
    
    system.user_progress["adaptive_user"] = user_progress
    
    # Get adaptive lesson
    print("🎯 Getting adaptive lesson for user...")
    adaptive_lesson = await system.get_adaptive_lesson(
        user_id="adaptive_user",
        subject="Mobile Development",
        topic="React Native Basics"
    )
    
    print(f"✅ Adaptive lesson created: {adaptive_lesson.title}")
    print(f"📝 Adapted for: {user_profile.learning_style} learning style")
    print(f"🎯 Difficulty: {adaptive_lesson.difficulty}")
    print(f"⏱️ Duration: {adaptive_lesson.duration} minutes")
    
    # Show adaptation details
    print(f"\n📋 Adaptation Details:")
    print(f"   - Original lesson adapted for user preferences")
    print(f"   - Learning style: {user_profile.learning_style}")
    print(f"   - Available time: {user_profile.available_time} minutes")
    print(f"   - User progress considered: {len(user_progress.completed_lessons)} lessons completed")
    
    return system

async def demo_multiple_subjects():
    """Demonstrate dynamic lesson creation for multiple subjects"""
    
    print("\n🎯 Multi-Subject Dynamic Learning Demo")
    print("=" * 50)
    
    # Initialize system
    config = SystemConfig(
        llm_provider="google",
        llm_api_key="demo-key",
        llm_model="gemini-pro"
    )
    
    system = EnhancedTutoringSystem(config)
    
    # Create different user profiles for different subjects
    users = [
        {
            "user_id": "python_learner",
            "profile": UserProfile(
                user_id="python_learner",
                name="Mike Python",
                email="mike@example.com",
                learning_style="analytical",
                preferred_difficulty="intermediate",
                available_time=120,
                learning_goals=["Master Python", "Build web apps"],
                interests=["Backend development", "APIs"]
            ),
            "subject": "Python Programming",
            "topic": "Advanced Data Structures"
        },
        {
            "user_id": "ml_learner",
            "profile": UserProfile(
                user_id="ml_learner",
                name="Lisa ML",
                email="lisa@example.com",
                learning_style="practical",
                preferred_difficulty="beginner",
                available_time=60,
                learning_goals=["Learn machine learning", "Build ML models"],
                interests=["Data science", "AI applications"]
            ),
            "subject": "Machine Learning",
            "topic": "Neural Networks Fundamentals"
        },
        {
            "user_id": "web_learner",
            "profile": UserProfile(
                user_id="web_learner",
                name="Tom Web",
                email="tom@example.com",
                learning_style="visual",
                preferred_difficulty="beginner",
                available_time=90,
                learning_goals=["Learn web development", "Build websites"],
                interests=["Frontend development", "User experience"]
            ),
            "subject": "Web Development",
            "topic": "React Components and State Management"
        }
    ]
    
    # Create lessons for each user
    lessons = []
    for user_data in users:
        print(f"\n👤 Creating lesson for {user_data['profile'].name}...")
        
        # Add user to system
        system.user_profiles[user_data["user_id"]] = user_data["profile"]
        
        # Create dynamic lesson
        lesson = await system.create_dynamic_lesson(
            subject=user_data["subject"],
            topic=user_data["topic"],
            difficulty=user_data["profile"].preferred_difficulty,
            user_profile=user_data["profile"]
        )
        
        lessons.append(lesson)
        
        print(f"✅ Created: {lesson.title}")
        print(f"   - Subject: {user_data['subject']}")
        print(f"   - Learning style: {user_data['profile'].learning_style}")
        print(f"   - Duration: {lesson.duration} minutes")
        print(f"   - Objectives: {len(lesson.learning_objectives)}")
    
    # Show summary
    print(f"\n📊 Summary:")
    print(f"   - Total lessons created: {len(lessons)}")
    print(f"   - Subjects covered: {len(set(lesson.title.split(' - ')[0] for lesson in lessons))}")
    print(f"   - Learning styles: {len(set(user_data['profile'].learning_style for user_data in users))}")
    
    return system

async def demo_learning_path_creation():
    """Demonstrate dynamic learning path creation"""
    
    print("\n🛤️ Dynamic Learning Path Creation Demo")
    print("=" * 50)
    
    # Initialize system
    config = SystemConfig(
        llm_provider="google",
        llm_api_key="demo-key",
        llm_model="gemini-pro"
    )
    
    system = EnhancedTutoringSystem(config)
    
    # Different learning requests
    requests = [
        {
            "user_id": "career_changer",
            "request": "I want to transition from marketing to data science. I need to learn Python, statistics, and machine learning in 6 months with hands-on projects.",
            "profile": UserProfile(
                user_id="career_changer",
                name="Emma Career",
                email="emma@example.com",
                learning_style="practical",
                preferred_difficulty="beginner",
                available_time=120,
                learning_goals=["Career transition", "Data science skills"],
                interests=["Data analysis", "Business intelligence"]
            )
        },
        {
            "user_id": "student_developer",
            "request": "I'm a computer science student who wants to specialize in web development. I need to learn modern frameworks like React and Node.js in 3 months.",
            "profile": UserProfile(
                user_id="student_developer",
                name="Jake Student",
                email="jake@example.com",
                learning_style="analytical",
                preferred_difficulty="intermediate",
                available_time=90,
                learning_goals=["Web development specialization", "Modern frameworks"],
                interests=["Frontend development", "Full-stack development"]
            )
        },
        {
            "user_id": "entrepreneur",
            "request": "I want to build my own startup and need to learn both technical and business skills. Focus on Python for backend, React for frontend, and business fundamentals in 1 year.",
            "profile": UserProfile(
                user_id="entrepreneur",
                name="Alex Entrepreneur",
                email="alex@example.com",
                learning_style="balanced",
                preferred_difficulty="intermediate",
                available_time=180,
                learning_goals=["Startup development", "Full-stack skills"],
                interests=["Entrepreneurship", "Technology", "Business"]
            )
        }
    ]
    
    # Create learning paths for each request
    paths = []
    for req_data in requests:
        print(f"\n👤 Creating learning path for {req_data['profile'].name}...")
        print(f"📝 Request: {req_data['request'][:100]}...")
        
        # Add user to system
        system.user_profiles[req_data["user_id"]] = req_data["profile"]
        
        # Create personalized learning path
        path_id = await system.create_personalized_learning_path(
            user_id=req_data["user_id"],
            user_request=req_data["request"],
            user_profile=req_data["profile"]
        )
        
        paths.append(path_id)
        
        # Get path details
        learning_path = system.learning_paths[path_id]
        print(f"✅ Path created: {learning_path.title}")
        print(f"   - Lessons: {len(learning_path.lessons)}")
        print(f"   - Duration: {learning_path.estimated_duration} minutes")
        print(f"   - Status: {learning_path.status}")
    
    # Show system status
    print(f"\n📊 System Status:")
    status = system.get_system_status()
    print(f"   - Total users: {status['total_users']}")
    print(f"   - Total lessons: {status['total_lessons']}")
    print(f"   - Dynamic lessons: {status['dynamic_lessons']}")
    print(f"   - Learning paths: {status['total_learning_paths']}")
    print(f"   - Dynamic generation: {status['dynamic_generation_enabled']}")
    
    return system

async def main():
    """Run all dynamic learning demos"""
    
    print("🚀 Dynamic Learning System - Complete Demo")
    print("=" * 60)
    print("This demo showcases a fully dynamic learning system that creates")
    print("lessons and curricula using LLM without any hardcoded content.")
    print()
    
    try:
        # Demo 1: Basic dynamic lesson creation
        print("🎯 DEMO 1: Dynamic Lesson Creation")
        print("-" * 40)
        await demo_dynamic_lesson_creation()
        
        # Demo 2: Adaptive learning
        print("\n🎯 DEMO 2: Adaptive Learning")
        print("-" * 40)
        await demo_adaptive_learning()
        
        # Demo 3: Multiple subjects
        print("\n🎯 DEMO 3: Multi-Subject Learning")
        print("-" * 40)
        await demo_multiple_subjects()
        
        # Demo 4: Learning path creation
        print("\n🎯 DEMO 4: Dynamic Learning Paths")
        print("-" * 40)
        await demo_learning_path_creation()
        
        print("\n🎉 All demos completed successfully!")
        print("=" * 60)
        print("The dynamic learning system is now fully operational!")
        print("✅ No hardcoded lessons - everything generated by LLM")
        print("✅ Personalized content based on user profiles")
        print("✅ Adaptive difficulty and learning styles")
        print("✅ Complete curriculum generation")
        print("✅ Multi-subject support")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        print("Please check your configuration and try again.")

if __name__ == "__main__":
    print("🎓 Dynamic Learning System Demo")
    print("==============================")
    print("This demo showcases the key features of the dynamic learning system.")
    print("Note: This uses mock LLM responses for demonstration purposes.")
    print("In production, you would need valid API keys for LLM services.")
    print()
    
    asyncio.run(main())
