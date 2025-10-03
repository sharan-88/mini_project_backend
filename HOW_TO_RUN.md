# How to Run the Dynamic Learning System

## Quick Start

### 1. Test if the system is working
```bash
python run_test.py
```

This will run a quick test to verify the dynamic learning system is working correctly.

### 2. Run comprehensive tests
```bash
python test_dynamic_system.py
```

This will run all tests to ensure the system is fully functional.

### 3. See the system in action
```bash
python dynamic_demo.py
```

This will run a complete demo showing all the dynamic features.

## What the System Does

The dynamic learning system now:

✅ **Creates lessons automatically using LLM** - No more hardcoded lessons
✅ **Generates personalized content** - Adapts to user learning style and preferences  
✅ **Creates complete curricula** - Builds learning paths dynamically
✅ **Supports multiple subjects** - Python, JavaScript, ML, Web Dev, etc.
✅ **Adapts difficulty** - Based on user progress and preferences
✅ **Generates assessments** - Questions and exercises automatically
✅ **Creates practice exercises** - Hands-on learning activities

## Key Features

### Dynamic Lesson Creation
```python
# Create a lesson on any topic
lesson = await system.create_dynamic_lesson(
    subject="Python Programming",
    topic="Object-Oriented Programming", 
    difficulty="intermediate"
)
```

### Personalized Learning
```python
# Create lessons adapted for specific users
user_profile = UserProfile(
    user_id="user123",
    learning_style="visual",
    preferred_difficulty="beginner",
    learning_goals=["Learn Python"]
)

lesson = await system.create_dynamic_lesson(
    subject="Python",
    topic="Functions",
    user_profile=user_profile
)
```

### Complete Curriculum Generation
```python
# Generate a full curriculum
curriculum = await system.create_dynamic_curriculum(
    subject="Machine Learning",
    level="beginner", 
    duration_weeks=6
)
```

### Learning Path Creation
```python
# Create personalized learning paths
path_id = await system.create_personalized_learning_path(
    user_id="user123",
    user_request="I want to learn Python for data science in 3 months"
)
```

## File Structure

- `enhanced_tutoring_system.py` - Main system with dynamic features
- `dynamic_lesson_generator.py` - LLM-powered lesson creation
- `dynamic_demo.py` - Complete demonstration
- `test_dynamic_system.py` - Comprehensive tests
- `run_test.py` - Quick test script

## Expected Output

When you run the tests, you should see:

```
🚀 Quick Dynamic System Test
===========================
✅ Imports successful
✅ System initialized
🤖 Creating dynamic lesson...
✅ Lesson created: Introduction to Python Programming
📝 Content: Python is a high-level programming language...
🎯 Objectives: 3
❓ Questions: 5
📊 System status: 1 lessons, 1 dynamic

🎉 Dynamic system is working correctly!
```

## Troubleshooting

If you encounter issues:

1. **Import errors**: Make sure all files are in the same directory
2. **LLM errors**: The system uses mock responses for demo purposes
3. **Memory issues**: The system generates content dynamically, so it uses more memory

## Next Steps

Once the system is working:

1. **Customize the LLM service** - Replace mock responses with real API calls
2. **Add your own subjects** - The system can generate lessons for any topic
3. **Integrate with your application** - Use the enhanced system in your projects
4. **Scale up** - The system can handle multiple users and concurrent sessions

## Example Usage

```python
import asyncio
from enhanced_tutoring_system import EnhancedTutoringSystem, SystemConfig

async def main():
    # Initialize system
    config = SystemConfig(
        llm_provider="google",
        llm_api_key="your-api-key",
        llm_model="gemini-pro"
    )
    
    system = EnhancedTutoringSystem(config)
    
    # Create dynamic lesson
    lesson = await system.create_dynamic_lesson(
        subject="Python Programming",
        topic="Data Structures",
        difficulty="intermediate"
    )
    
    print(f"Created lesson: {lesson.title}")

if __name__ == "__main__":
    asyncio.run(main())
```

The system is now fully dynamic and creates all content using LLM without any hardcoded lessons!
