#!/usr/bin/env python3
"""
Run Dynamic Learning System
===========================

This script runs the dynamic learning system with LLM-powered lesson generation.
"""

import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from dynamic_demo import main as run_dynamic_demo
from enhanced_tutoring_system import EnhancedTutoringSystem, SystemConfig
from models import UserProfile

async def quick_demo():
    """Quick demo of dynamic lesson creation"""
    
    print("🚀 Quick Dynamic Learning Demo")
    print("=" * 40)
    
    # Initialize system
    config = SystemConfig(
        llm_provider="google",
        llm_api_key="demo-key",
        llm_model="gemini-pro"
    )
    
    system = EnhancedTutoringSystem(config)
    
    # Create a user profile
    user_profile = UserProfile(
        user_id="demo_user",
        name="Demo User",
        email="demo@example.com",
        learning_style="visual",
        preferred_difficulty="intermediate",
        available_time=60,
        learning_goals=["Learn Python programming"],
        interests=["Web development"]
    )
    
    # Create dynamic lesson
    print("🤖 Creating dynamic lesson...")
    lesson = await system.create_dynamic_lesson(
        subject="Python Programming",
        topic="Object-Oriented Programming",
        difficulty="intermediate",
        user_profile=user_profile
    )
    
    print(f"✅ Lesson created: {lesson.title}")
    print(f"📝 Content: {lesson.content[:200]}...")
    print(f"🎯 Objectives: {lesson.learning_objectives}")
    print(f"❓ Questions: {len(lesson.assessment_questions)}")
    print(f"💪 Exercises: {len(lesson.practice_exercises)}")
    
    # Create curriculum
    print("\n📚 Creating curriculum...")
    curriculum = await system.create_dynamic_curriculum(
        subject="Machine Learning",
        level="beginner",
        duration_weeks=4,
        user_profile=user_profile
    )
    
    print(f"✅ Curriculum created: {len(curriculum)} lessons")
    for i, lesson in enumerate(curriculum[:3], 1):
        print(f"   {i}. {lesson.title}")
    
    print("\n🎉 Dynamic system is working!")

def main():
    """Main function"""
    
    print("🎓 Dynamic Learning System")
    print("=" * 30)
    print("Choose an option:")
    print("1. Quick demo")
    print("2. Full demo")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        asyncio.run(quick_demo())
    elif choice == "2":
        asyncio.run(run_dynamic_demo())
    elif choice == "3":
        print("👋 Goodbye!")
        return
    else:
        print("❌ Invalid choice. Please run again.")

if __name__ == "__main__":
    main()
