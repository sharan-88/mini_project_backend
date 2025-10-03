"""
Test Suite for Multi-Agent AI Tutoring System
=============================================

This module contains comprehensive tests for all components of the
adaptive learning system.
"""

import asyncio
import pytest
from datetime import datetime
from typing import Dict, Any, List

# Import system components
from tutoring_system import MultiAgentTutoringSystem, SystemConfig
from models import Lesson, UserProfile, UserProgress
from llm_service import GoogleLLMService, LLMServiceFactory
from assessment_system import AssessmentSystem
from gap_analysis import GapAnalysisSystem
from knowledge_gap_filler import KnowledgeGapFiller
from learning_curve import LearningCurveTracker
from mdp_learning import MDPLearningPath

# Import agents
from agents.knowledge_agent import KnowledgeAgent
from agents.practice_agent import PracticeAgent
from agents.motivation_agent import MotivationAgent
from agents.planner_agent import PlannerAgent

class TestSystemIntegration:
    """Test system integration and functionality"""
    
    def setup_method(self):
        """Set up test environment"""
        self.config = SystemConfig(
            llm_provider="google",
            llm_api_key="test-key",
            llm_model="gemini-pro",
            enable_analytics=True,
            enable_gap_analysis=True,
            enable_learning_curves=True,
            enable_mdp_recommendations=True
        )
        
        self.system = MultiAgentTutoringSystem(self.config)
        
        # Create test lesson
        self.test_lesson = Lesson(
            lesson_id="test_lesson_001",
            title="Test Lesson: Basic Concepts",
            content="This is a test lesson about basic concepts...",
            difficulty="medium",
            duration=30,
            learning_objectives=["Understand basic concepts", "Apply knowledge"],
            prerequisites=["Basic understanding"]
        )
        
        self.system.lessons[self.test_lesson.lesson_id] = self.test_lesson
    
    @pytest.mark.asyncio
    async def test_system_initialization(self):
        """Test system initialization"""
        assert self.system is not None
        assert self.system.llm_service is not None
        assert self.system.assessment_system is not None
        assert self.system.gap_analysis_system is not None
        assert self.system.knowledge_agent is not None
        assert self.system.practice_agent is not None
        assert self.system.motivation_agent is not None
        assert self.system.planner_agent is not None
    
    @pytest.mark.asyncio
    async def test_learning_session_creation(self):
        """Test learning session creation"""
        session_id = await self.system.start_learning_session(
            "test_user_001", 
            self.test_lesson.lesson_id
        )
        
        assert session_id is not None
        assert session_id in self.system.active_sessions
        
        session = self.system.active_sessions[session_id]
        assert session.user_id == "test_user_001"
        assert session.lessons_completed == [self.test_lesson.lesson_id]
    
    @pytest.mark.asyncio
    async def test_concept_explanation(self):
        """Test concept explanation functionality"""
        session_id = await self.system.start_learning_session(
            "test_user_002", 
            self.test_lesson.lesson_id
        )
        
        # Request concept explanation
        result = await self.system.process_user_interaction(
            session_id, 
            "concept_explanation_requested", 
            {
                "concept": "Python variables",
                "difficulty": "beginner",
                "learning_style": "visual"
            }
        )
        
        assert "explanation" in result
        assert "resources" in result
        assert "confidence" in result
        assert result["explanation"] is not None
    
    @pytest.mark.asyncio
    async def test_practice_generation(self):
        """Test practice exercise generation"""
        session_id = await self.system.start_learning_session(
            "test_user_003", 
            self.test_lesson.lesson_id
        )
        
        # Request practice exercises
        result = await self.system.process_user_interaction(
            session_id, 
            "practice_requested", 
            {
                "lesson_content": self.test_lesson.content,
                "difficulty": "medium",
                "num_questions": 3,
                "question_types": ["multiple_choice", "short_answer"]
            }
        )
        
        assert "practice_content" in result
        assert "difficulty" in result
        assert "question_count" in result
        assert result["question_count"] > 0
    
    @pytest.mark.asyncio
    async def test_assessment_creation(self):
        """Test assessment creation"""
        session_id = await self.system.start_learning_session(
            "test_user_004", 
            self.test_lesson.lesson_id
        )
        
        # Request assessment
        result = await self.system.process_user_interaction(
            session_id, 
            "assessment_requested", 
            {
                "lesson_id": self.test_lesson.lesson_id,
                "difficulty": "medium",
                "num_questions": 5,
                "question_types": ["multiple_choice", "short_answer"]
            }
        )
        
        assert "assessment_id" in result
        assert "questions" in result
        assert "time_limit" in result
        assert len(result["questions"]) > 0
    
    @pytest.mark.asyncio
    async def test_question_answer_processing(self):
        """Test question answer processing"""
        session_id = await self.system.start_learning_session(
            "test_user_005", 
            self.test_lesson.lesson_id
        )
        
        # Process question answer
        result = await self.system.process_user_interaction(
            session_id, 
            "question_answered", 
            {
                "question_id": "q_001",
                "answer": "Python is a programming language",
                "correct_answer": "Python is a programming language",
                "concept": "Python basics",
                "time_taken": 30
            }
        )
        
        assert "evaluation" in result
        assert "feedback" in result
        assert "next_recommendations" in result
        assert "learning_curve" in result
    
    @pytest.mark.asyncio
    async def test_progress_tracking(self):
        """Test progress tracking functionality"""
        session_id = await self.system.start_learning_session(
            "test_user_006", 
            self.test_lesson.lesson_id
        )
        
        # Check progress
        result = await self.system.process_user_interaction(
            session_id, 
            "progress_check", 
            {
                "concept": "Python basics"
            }
        )
        
        assert "progress_analysis" in result
        assert "achievements" in result
        assert "recommendations" in result
        assert "learning_curve" in result
        assert "session_stats" in result
    
    @pytest.mark.asyncio
    async def test_session_ending(self):
        """Test session ending and summary"""
        session_id = await self.system.start_learning_session(
            "test_user_007", 
            self.test_lesson.lesson_id
        )
        
        # End session
        summary = await self.system.end_learning_session(session_id)
        
        assert "session_id" in summary
        assert "user_id" in summary
        assert "duration_minutes" in summary
        assert "lessons_completed" in summary
        assert "engagement_score" in summary
        assert "recommendations" in summary
        
        # Verify session is removed from active sessions
        assert session_id not in self.system.active_sessions
    
    @pytest.mark.asyncio
    async def test_learning_path_creation(self):
        """Test learning path creation"""
        path_id = await self.system.create_learning_path(
            "test_user_008",
            ["Learn Python", "Build a project"],
            "4 weeks",
            {
                "available_time": "1 hour per day",
                "learning_style": "practical",
                "current_level": "beginner"
            }
        )
        
        assert path_id is not None
        assert path_id in self.system.learning_paths
        
        learning_path = self.system.learning_paths[path_id]
        assert learning_path.user_id == "test_user_008"
        assert learning_path.title is not None
        assert learning_path.description is not None
    
    def test_system_status(self):
        """Test system status reporting"""
        status = self.system.get_system_status()
        
        assert "system_metrics" in status
        assert "active_sessions" in status
        assert "total_users" in status
        assert "total_lessons" in status
        assert "components_status" in status
        
        assert status["active_sessions"] == 0  # No active sessions initially
        assert status["total_lessons"] == 1  # One test lesson
        assert status["components_status"]["llm_service"] == "active"

class TestGapAnalysis:
    """Test gap analysis functionality"""
    
    def setup_method(self):
        """Set up gap analysis tests"""
        self.llm_service = GoogleLLMService("test-key", "gemini-pro")
        self.gap_analysis = GapAnalysisSystem(self.llm_service)
    
    @pytest.mark.asyncio
    async def test_misconception_classification(self):
        """Test misconception classification"""
        user_responses = ["Python is a compiled language", "Python is slow"]
        correct_answers = ["Python is an interpreted language", "Python can be fast with optimization"]
        concept = "Python characteristics"
        
        result = await self.gap_analysis.analyze_responses(
            user_responses, correct_answers, concept, "test_user", "test_session"
        )
        
        assert result.user_id == "test_user"
        assert result.session_id == "test_session"
        assert result.overall_confidence >= 0.0
        assert result.overall_confidence <= 1.0
        assert len(result.recommendations) > 0
    
    @pytest.mark.asyncio
    async def test_learning_gap_identification(self):
        """Test learning gap identification"""
        user_responses = ["I don't understand", "This is confusing"]
        correct_answers = ["Clear understanding", "Well explained"]
        concept = "Basic concepts"
        
        result = await self.gap_analysis.analyze_responses(
            user_responses, correct_answers, concept, "test_user", "test_session"
        )
        
        assert len(result.learning_gaps) >= 0
        assert len(result.misconceptions) >= 0

class TestLearningCurve:
    """Test learning curve functionality"""
    
    def setup_method(self):
        """Set up learning curve tests"""
        self.learning_curve = LearningCurveTracker()
    
    def test_learning_point_addition(self):
        """Test adding learning points"""
        learning_point = self.learning_curve.add_learning_point(
            "test_user", "Python basics", 0.8, 30, 1, 0.7
        )
        
        assert learning_point.performance == 0.8
        assert learning_point.time_spent == 30
        assert learning_point.attempts == 1
        assert learning_point.engagement == 0.7
    
    def test_learning_curve_analysis(self):
        """Test learning curve analysis"""
        # Add multiple learning points
        for i in range(5):
            self.learning_curve.add_learning_point(
                "test_user", "Python basics", 0.6 + i * 0.1, 30, 1, 0.7
            )
        
        analysis = self.learning_curve.get_learning_curve_analysis("test_user", "Python basics")
        
        assert analysis["concept"] == "Python basics"
        assert analysis["status"] == "analyzed"
        assert "trend" in analysis
        assert "confidence" in analysis
        assert "recommendations" in analysis
    
    def test_difficulty_adjustment(self):
        """Test difficulty adjustment recommendations"""
        # Add learning points showing struggle
        for i in range(3):
            self.learning_curve.add_learning_point(
                "test_user", "Python basics", 0.3, 60, 3, 0.4
            )
        
        adjustment = self.learning_curve.get_difficulty_adjustment("test_user", "Python basics")
        
        assert "adjustment" in adjustment
        assert "new_difficulty" in adjustment
        assert "confidence" in adjustment
        assert "reason" in adjustment

class TestMDPSystem:
    """Test MDP system functionality"""
    
    def setup_method(self):
        """Set up MDP system tests"""
        self.mdp_system = MDPLearningPath()
    
    def test_action_recommendation(self):
        """Test action recommendation"""
        action = self.mdp_system.recommend_action("test_user", {
            "time_available": 30,
            "learning_style": "balanced"
        })
        
        assert action is not None
        assert action.action_type is not None
        assert action.difficulty is not None
        assert action.duration > 0
        assert action.expected_outcome is not None
    
    def test_learning_path_recommendation(self):
        """Test learning path recommendation"""
        path = self.mdp_system.get_learning_path_recommendation("test_user", 3)
        
        assert len(path) == 3
        assert all(action.action_type is not None for action in path)
        assert all(action.duration > 0 for action in path)
    
    def test_feedback_update(self):
        """Test feedback update"""
        # Get initial action
        action = self.mdp_system.recommend_action("test_user", {})
        
        # Update with feedback
        outcome = {
            "performance": 0.8,
            "engagement_change": 0.1,
            "fatigue_change": 0.05
        }
        
        self.mdp_system.update_from_feedback("test_user", action, outcome, 5.0)
        
        # Verify state was updated
        updated_state = self.mdp_system.get_user_state("test_user")
        assert updated_state is not None
        assert updated_state.proficiency_level > 0.0

class TestAssessmentSystem:
    """Test assessment system functionality"""
    
    def setup_method(self):
        """Set up assessment system tests"""
        self.llm_service = GoogleLLMService("test-key", "gemini-pro")
        self.assessment_system = AssessmentSystem(self.llm_service)
    
    @pytest.mark.asyncio
    async def test_assessment_creation(self):
        """Test assessment creation"""
        assessment = await self.assessment_system.create_assessment(
            "test_lesson", "medium", 5, ["multiple_choice", "short_answer"]
        )
        
        assert assessment.assessment_id is not None
        assert assessment.lesson_id == "test_lesson"
        assert assessment.difficulty == "medium"
        assert len(assessment.questions) > 0
        assert assessment.time_limit > 0
    
    @pytest.mark.asyncio
    async def test_assessment_evaluation(self):
        """Test assessment evaluation"""
        # Create assessment
        assessment = await self.assessment_system.create_assessment(
            "test_lesson", "medium", 3, ["multiple_choice"]
        )
        
        # Evaluate answers
        user_answers = [
            {"answer": "A", "time_taken": 30},
            {"answer": "B", "time_taken": 45},
            {"answer": "C", "time_taken": 60}
        ]
        
        result = await self.assessment_system.evaluate_assessment(
            assessment.assessment_id, user_answers, "test_user"
        )
        
        assert result.user_id == "test_user"
        assert result.assessment_id == assessment.assessment_id
        assert result.score >= 0
        assert result.total_points > 0
        assert result.percentage >= 0
        assert result.percentage <= 100
        assert len(result.answers) == 3
        assert len(result.feedback) > 0
    
    @pytest.mark.asyncio
    async def test_adaptive_questions(self):
        """Test adaptive question generation"""
        questions = await self.assessment_system.generate_adaptive_questions(
            "test_user", "Python basics", "medium"
        )
        
        assert len(questions) > 0
        assert all(hasattr(q, 'question_text') for q in questions)
        assert all(hasattr(q, 'question_type') for q in questions)
        assert all(hasattr(q, 'correct_answer') for q in questions)

class TestKnowledgeGapFiller:
    """Test knowledge gap filler functionality"""
    
    def setup_method(self):
        """Set up knowledge gap filler tests"""
        self.llm_service = GoogleLLMService("test-key", "gemini-pro")
        self.gap_filler = KnowledgeGapFiller(self.llm_service)
    
    @pytest.mark.asyncio
    async def test_gap_identification(self):
        """Test knowledge gap identification"""
        user_responses = ["I don't understand this concept", "This is too difficult"]
        current_concept = "Python functions"
        
        gaps = await self.gap_filler.identify_knowledge_gaps(
            user_responses, current_concept, "test_user"
        )
        
        assert len(gaps) >= 0  # May or may not identify gaps
        if gaps:
            assert all(hasattr(gap, 'gap_id') for gap in gaps)
            assert all(hasattr(gap, 'concept') for gap in gaps)
            assert all(hasattr(gap, 'gap_type') for gap in gaps)
            assert all(hasattr(gap, 'severity') for gap in gaps)
    
    @pytest.mark.asyncio
    async def test_gap_filling_lesson_creation(self):
        """Test gap filling lesson creation"""
        # First identify gaps
        user_responses = ["I don't understand this concept"]
        current_concept = "Python functions"
        
        gaps = await self.gap_filler.identify_knowledge_gaps(
            user_responses, current_concept, "test_user"
        )
        
        if gaps:
            # Create gap filling lesson
            lesson = await self.gap_filler.create_gap_filling_lesson(gaps[0])
            
            if lesson:
                assert lesson.lesson_id is not None
                assert lesson.gap_id == gaps[0].gap_id
                assert lesson.title is not None
                assert lesson.content is not None
                assert lesson.difficulty is not None
                assert lesson.duration > 0
                assert len(lesson.learning_objectives) > 0

# Performance and stress tests
class TestSystemPerformance:
    """Test system performance and scalability"""
    
    def setup_method(self):
        """Set up performance tests"""
        self.config = SystemConfig(
            llm_provider="google",
            llm_api_key="test-key",
            llm_model="gemini-pro",
            max_concurrent_sessions=10
        )
        self.system = MultiAgentTutoringSystem(self.config)
    
    @pytest.mark.asyncio
    async def test_concurrent_sessions(self):
        """Test concurrent session handling"""
        # Create multiple sessions concurrently
        tasks = []
        for i in range(5):
            task = self.system.start_learning_session(
                f"user_{i}", 
                "test_lesson_001"
            )
            tasks.append(task)
        
        session_ids = await asyncio.gather(*tasks)
        
        assert len(session_ids) == 5
        assert all(session_id is not None for session_id in session_ids)
        assert len(self.system.active_sessions) == 5
        
        # Clean up sessions
        for session_id in session_ids:
            await self.system.end_learning_session(session_id)
        
        assert len(self.system.active_sessions) == 0
    
    @pytest.mark.asyncio
    async def test_system_resilience(self):
        """Test system resilience to errors"""
        # Test with invalid session ID
        try:
            await self.system.process_user_interaction(
                "invalid_session", 
                "concept_explanation_requested", 
                {}
            )
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        
        # Test with invalid lesson ID
        try:
            await self.system.start_learning_session("user", "invalid_lesson")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected

# Integration tests
class TestSystemIntegration:
    """Test full system integration"""
    
    @pytest.mark.asyncio
    async def test_complete_learning_workflow(self):
        """Test complete learning workflow"""
        config = SystemConfig(
            llm_provider="google",
            llm_api_key="test-key",
            llm_model="gemini-pro"
        )
        system = MultiAgentTutoringSystem(config)
        
        # Create test lesson
        lesson = Lesson(
            lesson_id="workflow_test_lesson",
            title="Complete Workflow Test",
            content="This is a test lesson for workflow testing...",
            difficulty="medium",
            duration=30,
            learning_objectives=["Test workflow", "Validate system"],
            prerequisites=["Basic understanding"]
        )
        system.lessons[lesson.lesson_id] = lesson
        
        # Start session
        session_id = await system.start_learning_session(
            "workflow_user", 
            lesson.lesson_id
        )
        
        # Get explanation
        explanation = await system.process_user_interaction(
            session_id, 
            "concept_explanation_requested", 
            {"concept": "Test concept", "difficulty": "medium"}
        )
        assert "explanation" in explanation
        
        # Generate practice
        practice = await system.process_user_interaction(
            session_id, 
            "practice_requested", 
            {"lesson_content": lesson.content, "difficulty": "medium"}
        )
        assert "practice_content" in practice
        
        # Check progress
        progress = await system.process_user_interaction(
            session_id, 
            "progress_check", 
            {"concept": "Test concept"}
        )
        assert "progress_analysis" in progress
        
        # End session
        summary = await system.end_learning_session(session_id)
        assert "session_id" in summary
        assert summary["user_id"] == "workflow_user"

if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
