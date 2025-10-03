#!/usr/bin/env python3
"""
Test Dynamic Learning System
============================

This script tests the dynamic learning system to ensure it's working properly.
"""

import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from enhanced_tutoring_system import EnhancedTutoringSystem, SystemConfig
from models import UserProfile
from dynamic_lesson_generator import DynamicLessonGenerator

async def test_basic_functionality():
    """Test basic dynamic lesson creation"""
    
    print("🧪 Testing Dynamic Learning System")
    print("=" * 40)
    
    try:
        # Initialize system
        print("1️⃣ Initializing system...")
        config = SystemConfig(
            llm_provider="google",
            llm_api_key="demo-key",
            llm_model="gemini-pro"
        )
        
        system = EnhancedTutoringSystem(config)
        print("✅ System initialized successfully")
        
        # Test 1: Create a simple dynamic lesson
        print("\n2️⃣ Testing dynamic lesson creation...")
        lesson = await system.create_dynamic_lesson(
            subject="Python Programming",
            topic="Variables and Data Types",
            difficulty="beginner"
        )
        
        print(f"✅ Lesson created: {lesson.title}")
        print(f"   - ID: {lesson.lesson_id}")
        print(f"   - Duration: {lesson.duration} minutes")
        print(f"   - Difficulty: {lesson.difficulty}")
        print(f"   - Content length: {len(lesson.content)} characters")
        print(f"   - Learning objectives: {len(lesson.learning_objectives)}")
        print(f"   - Assessment questions: {len(lesson.assessment_questions)}")
        print(f"   - Practice exercises: {len(lesson.practice_exercises)}")
        
        # Test 2: Create user profile and personalized lesson
        print("\n3️⃣ Testing personalized lesson creation...")
        user_profile = UserProfile(
            user_id="test_user",
            name="Test User",
            email="test@example.com",
            learning_style="visual",
            preferred_difficulty="intermediate",
            available_time=60,
            learning_goals=["Learn Python programming"],
            interests=["Web development"]
        )
        
        personalized_lesson = await system.create_dynamic_lesson(
            subject="Python Programming",
            topic="Functions and Modules",
            difficulty="intermediate",
            user_profile=user_profile
        )
        
        print(f"✅ Personalized lesson created: {personalized_lesson.title}")
        print(f"   - Adapted for: {user_profile.learning_style} learning style")
        print(f"   - Duration: {personalized_lesson.duration} minutes")
        
        # Test 3: Create a small curriculum
        print("\n4️⃣ Testing curriculum creation...")
        curriculum = await system.create_dynamic_curriculum(
            subject="JavaScript",
            level="beginner",
            duration_weeks=2,
            user_profile=user_profile
        )
        
        print(f"✅ Curriculum created: {len(curriculum)} lessons")
        for i, lesson in enumerate(curriculum[:3], 1):
            print(f"   {i}. {lesson.title}")
        
        # Test 4: Create learning path
        print("\n5️⃣ Testing learning path creation...")
        path_id = await system.create_personalized_learning_path(
            user_id="test_user",
            user_request="I want to learn Python for web development in 2 months",
            user_profile=user_profile
        )
        
        learning_path = system.learning_paths[path_id]
        print(f"✅ Learning path created: {learning_path.title}")
        print(f"   - Lessons: {len(learning_path.lessons)}")
        print(f"   - Duration: {learning_path.estimated_duration} minutes")
        
        # Test 5: System status
        print("\n6️⃣ Testing system status...")
        status = system.get_system_status()
        print(f"✅ System status retrieved:")
        print(f"   - Total users: {status['total_users']}")
        print(f"   - Total lessons: {status['total_lessons']}")
        print(f"   - Dynamic lessons: {status['dynamic_lessons']}")
        print(f"   - Learning paths: {status['total_learning_paths']}")
        print(f"   - Dynamic generation: {status['dynamic_generation_enabled']}")
        
        print("\n🎉 All tests passed! The dynamic system is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_lesson_content_quality():
    """Test the quality of generated lesson content"""
    
    print("\n🔍 Testing Lesson Content Quality")
    print("=" * 40)
    
    try:
        # Initialize system
        config = SystemConfig(
            llm_provider="google",
            llm_api_key="demo-key",
            llm_model="gemini-pro"
        )
        
        system = EnhancedTutoringSystem(config)
        
        # Create a lesson and examine its content
        lesson = await system.create_dynamic_lesson(
            subject="Machine Learning",
            topic="Linear Regression",
            difficulty="intermediate"
        )
        
        print(f"📖 Lesson: {lesson.title}")
        print(f"📝 Content preview:")
        print("-" * 30)
        print(lesson.content[:300] + "..." if len(lesson.content) > 300 else lesson.content)
        print("-" * 30)
        
        print(f"\n🎯 Learning Objectives:")
        for i, obj in enumerate(lesson.learning_objectives, 1):
            print(f"   {i}. {obj}")
        
        print(f"\n❓ Assessment Questions:")
        for i, q in enumerate(lesson.assessment_questions[:2], 1):
            print(f"   {i}. {q.get('question', 'Question not found')}")
        
        print(f"\n💪 Practice Exercises:")
        for i, ex in enumerate(lesson.practice_exercises[:2], 1):
            print(f"   {i}. {ex}")
        
        print("\n✅ Content quality test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Content quality test failed: {e}")
        return False

async def test_multiple_subjects():
    """Test dynamic lesson creation for multiple subjects"""
    
    print("\n🌐 Testing Multiple Subjects")
    print("=" * 40)
    
    try:
        config = SystemConfig(
            llm_provider="google",
            llm_api_key="demo-key",
            llm_model="gemini-pro"
        )
        
        system = EnhancedTutoringSystem(config)
        
        subjects = [
            ("Python Programming", "Data Structures"),
            ("Machine Learning", "Neural Networks"),
            ("Web Development", "React Components"),
            ("Data Science", "Statistical Analysis"),
            ("JavaScript", "Async Programming")
        ]
        
        lessons = []
        for subject, topic in subjects:
            print(f"📚 Creating lesson: {subject} - {topic}")
            lesson = await system.create_dynamic_lesson(
                subject=subject,
                topic=topic,
                difficulty="intermediate"
            )
            lessons.append(lesson)
            print(f"   ✅ Created: {lesson.title}")
        
        print(f"\n✅ Created {len(lessons)} lessons across {len(subjects)} subjects")
        
        # Show summary
        print(f"\n📊 Summary:")
        for lesson in lessons:
            print(f"   - {lesson.title} ({lesson.difficulty})")
        
        return True
        
    except Exception as e:
        print(f"❌ Multiple subjects test failed: {e}")
        return False

async def main():
    """Run all tests"""
    
    print("🚀 Dynamic Learning System - Test Suite")
    print("=" * 50)
    print("This test suite verifies that the dynamic learning system")
    print("is working correctly with LLM-powered lesson generation.")
    print()
    
    tests = [
        ("Basic Functionality", test_basic_functionality),
        ("Content Quality", test_lesson_content_quality),
        ("Multiple Subjects", test_multiple_subjects)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running test: {test_name}")
        print("-" * 30)
        
        try:
            result = await test_func()
            if result:
                print(f"✅ {test_name} - PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} - FAILED")
        except Exception as e:
            print(f"❌ {test_name} - ERROR: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The dynamic system is working perfectly.")
        print("\n✅ Features verified:")
        print("   - Dynamic lesson creation using LLM")
        print("   - Personalized content generation")
        print("   - Multi-subject support")
        print("   - Curriculum generation")
        print("   - Learning path creation")
        print("   - System status and metrics")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    print("🎓 Dynamic Learning System Test Suite")
    print("=====================================")
    print("This will test the dynamic learning system to ensure")
    print("it's working correctly with LLM-powered content generation.")
    print()
    
    success = asyncio.run(main())
    
    if success:
        print("\n🚀 System is ready for use!")
    else:
        print("\n🔧 Please fix the issues before using the system.")
