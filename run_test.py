#!/usr/bin/env python3
"""
Simple Test Runner for Dynamic Learning System
==============================================

Run this script to test if the dynamic learning system is working.
"""

import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

async def quick_test():
    """Quick test to verify the system works"""
    
    print("🚀 Quick Dynamic System Test")
    print("=" * 35)
    
    try:
        # Import the enhanced system
        from enhanced_tutoring_system import EnhancedTutoringSystem, SystemConfig
        from models import UserProfile
        
        print("✅ Imports successful")
        
        # Initialize system
        config = SystemConfig(
            llm_provider="google",
            llm_api_key="demo-key",
            llm_model="gemini-pro"
        )
        
        system = EnhancedTutoringSystem(config)
        print("✅ System initialized")
        
        # Create a simple lesson
        print("🤖 Creating dynamic lesson...")
        lesson = await system.create_dynamic_lesson(
            subject="Python Programming",
            topic="Introduction to Python",
            difficulty="beginner"
        )
        
        print(f"✅ Lesson created: {lesson.title}")
        print(f"📝 Content: {lesson.content[:100]}...")
        print(f"🎯 Objectives: {len(lesson.learning_objectives)}")
        print(f"❓ Questions: {len(lesson.assessment_questions)}")
        
        # Test system status
        status = system.get_system_status()
        print(f"📊 System status: {status['total_lessons']} lessons, {status['dynamic_lessons']} dynamic")
        
        print("\n🎉 Dynamic system is working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function"""
    
    print("🎓 Dynamic Learning System - Quick Test")
    print("=" * 45)
    print("This will test if the dynamic learning system is working.")
    print()
    
    try:
        result = asyncio.run(quick_test())
        
        if result:
            print("\n✅ SUCCESS: Dynamic system is working!")
            print("\nYou can now:")
            print("1. Run 'python test_dynamic_system.py' for full tests")
            print("2. Run 'python dynamic_demo.py' for complete demo")
            print("3. Use the system in your own code")
        else:
            print("\n❌ FAILED: System has issues")
            print("Please check the error messages above")
            
    except KeyboardInterrupt:
        print("\n👋 Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
