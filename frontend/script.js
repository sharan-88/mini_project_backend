// Global state
let currentPlan = null;
let currentSession = null;
let progressData = {
    lessonsCompleted: 0,
    averageScore: 0,
    timeSpent: 0,
    currentWeek: 1,
    weeklyScores: [],
    recommendations: []
};

// DOM Elements
const learningRequestForm = document.getElementById('learningRequestForm');
const planSection = document.getElementById('planSection');
const progressSection = document.getElementById('progressSection');
const sessionSection = document.getElementById('sessionSection');
const loadingOverlay = document.getElementById('loadingOverlay');
const statusMessage = document.getElementById('statusMessage');

// Form elements
const userRequestInput = document.getElementById('userRequest');
const createPlanBtn = document.getElementById('createPlanBtn');

// Plan display elements
const planTitle = document.getElementById('planTitle');
const planTimeline = document.getElementById('planTimeline');
const planLessons = document.getElementById('planLessons');
const planGoalsList = document.getElementById('planGoalsList');

// Progress elements
const lessonsCompleted = document.getElementById('lessonsCompleted');
const averageScore = document.getElementById('averageScore');
const timeSpent = document.getElementById('timeSpent');
const currentWeek = document.getElementById('currentWeek');
const scoreChart = document.getElementById('scoreChart');
const recommendationsList = document.getElementById('recommendationsList');

// Session elements
const startSessionBtn = document.getElementById('startSessionBtn');
const takeTestBtn = document.getElementById('takeTestBtn');
const endSessionBtn = document.getElementById('endSessionBtn');
const sessionStatus = document.getElementById('sessionStatus');

// Event Listeners
learningRequestForm.addEventListener('submit', handleCreatePlan);
startSessionBtn.addEventListener('click', startLearningSession);
takeTestBtn.addEventListener('click', takeWeeklyTest);
endSessionBtn.addEventListener('click', endLearningSession);

// Example requests
const examples = {
    python: "I want to learn Python for 3 months with weekly tests",
    javascript: "I need to master JavaScript in 6 weeks for a job interview",
    ml: "I want to learn Machine Learning for 6 months with projects",
    webdev: "I need to become a web developer in 1 year"
};

// Main Functions
async function handleCreatePlan(e) {
    e.preventDefault();
    
    const userRequest = userRequestInput.value.trim();
    if (!userRequest) {
        showStatus('Please enter a learning request', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        // Simulate API call to backend
        const plan = await createLearningPlan(userRequest);
        
        currentPlan = plan;
        displayPlan(plan);
        showStatus('Learning plan created successfully!', 'success');
        
        // Show progress section
        progressSection.style.display = 'block';
        sessionSection.style.display = 'block';
        
    } catch (error) {
        showStatus('Error creating learning plan: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}

async function createLearningPlan(userRequest) {
    // Call the backend API
    const response = await fetch('/api/create-plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userRequest })
    });
    
    if (!response.ok) {
        throw new Error('Failed to create learning plan');
    }
    
    const data = await response.json();
    return data.plan;
}

function displayPlan(plan) {
    planTitle.textContent = plan.title;
    planTimeline.textContent = plan.timeline;
    planLessons.textContent = `${plan.lessons} lessons`;
    
    // Display goals
    planGoalsList.innerHTML = '';
    plan.goals.forEach(goal => {
        const li = document.createElement('li');
        li.textContent = goal;
        planGoalsList.appendChild(li);
    });
    
    planSection.style.display = 'block';
    updateProgressDisplay();
}

async function startLearningSession() {
    if (!currentPlan) {
        showStatus('Please create a learning plan first', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        // Call backend API to start session
        const response = await fetch('/api/start-session', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: currentPlan.user_id })
        });
        
        if (!response.ok) {
            throw new Error('Failed to start learning session');
        }
        
        const data = await response.json();
        currentSession = {
            id: data.session.id,
            startTime: Date.now(),
            lessons: data.session.lessons
        };
        
        sessionStatus.textContent = `Learning session started! Working on ${currentSession.lessons.length} lessons this week.`;
        startSessionBtn.disabled = true;
        takeTestBtn.disabled = false;
        endSessionBtn.disabled = false;
        
        showStatus('Learning session started!', 'success');
        
    } catch (error) {
        showStatus('Error starting session: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}

async function takeWeeklyTest() {
    if (!currentSession) {
        showStatus('Please start a learning session first', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        // Call backend API to take test
        const response = await fetch('/api/take-test', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: currentPlan.user_id })
        });
        
        if (!response.ok) {
            throw new Error('Failed to take test');
        }
        
        const data = await response.json();
        const score = data.score;
        
        // Update progress
        progressData.weeklyScores.push(score);
        progressData.lessonsCompleted += currentSession.lessons.length;
        progressData.timeSpent += 45 * currentSession.lessons.length + 30; // 45 min per lesson + 30 min test
        progressData.currentWeek++;
        
        // Calculate average score
        progressData.averageScore = progressData.weeklyScores.reduce((a, b) => a + b, 0) / progressData.weeklyScores.length;
        
        // Generate recommendations
        progressData.recommendations = generateRecommendations(score);
        
        updateProgressDisplay();
        updateScoreChart();
        
        sessionStatus.textContent = `Weekly test completed! Score: ${score}%`;
        takeTestBtn.disabled = true;
        
        showStatus(`Test completed! Score: ${score}%`, 'success');
        
    } catch (error) {
        showStatus('Error taking test: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}

async function endLearningSession() {
    if (!currentSession) {
        showStatus('No active session to end', 'error');
        return;
    }
    
    const duration = Math.round((Date.now() - currentSession.startTime) / 1000 / 60);
    
    sessionStatus.textContent = `Session ended. Duration: ${duration} minutes`;
    startSessionBtn.disabled = false;
    takeTestBtn.disabled = true;
    endSessionBtn.disabled = true;
    
    currentSession = null;
    showStatus('Learning session ended', 'info');
}

// Helper Functions
function extractTitle(request) {
    if (request.toLowerCase().includes('python')) return 'Python Programming Mastery';
    if (request.toLowerCase().includes('javascript')) return 'JavaScript Development';
    if (request.toLowerCase().includes('machine learning')) return 'Machine Learning Journey';
    if (request.toLowerCase().includes('web development')) return 'Web Development Path';
    return 'Personalized Learning Plan';
}

function extractTimeline(request) {
    if (request.includes('3 months')) return '3 months';
    if (request.includes('6 months')) return '6 months';
    if (request.includes('1 year')) return '1 year';
    if (request.includes('6 weeks')) return '6 weeks';
    return '3 months';
}

function extractLessons(request) {
    if (request.includes('3 months')) return 10;
    if (request.includes('6 months')) return 20;
    if (request.includes('1 year')) return 40;
    if (request.includes('6 weeks')) return 8;
    return 10;
}

function extractGoals(request) {
    const goals = ['Master the subject', 'Build practical skills'];
    if (request.toLowerCase().includes('job')) goals.push('Prepare for job interviews');
    if (request.toLowerCase().includes('project')) goals.push('Build real-world projects');
    if (request.toLowerCase().includes('certification')) goals.push('Prepare for certification');
    return goals;
}

function extractSubject(request) {
    if (request.toLowerCase().includes('python')) return 'Python';
    if (request.toLowerCase().includes('javascript')) return 'JavaScript';
    if (request.toLowerCase().includes('machine learning')) return 'Machine Learning';
    if (request.toLowerCase().includes('web development')) return 'Web Development';
    return 'Programming';
}

function getCurrentWeekLessons() {
    const lessons = [
        'Introduction to Variables',
        'Control Structures',
        'Functions and Modules'
    ];
    return lessons;
}

function simulateTestScore() {
    // Simulate improving scores over time
    const baseScore = 60;
    const weekBonus = progressData.currentWeek * 2;
    const randomVariation = Math.floor(Math.random() * 20) - 10;
    return Math.max(0, Math.min(100, baseScore + weekBonus + randomVariation));
}

function generateRecommendations(score) {
    const recommendations = [];
    
    if (score >= 85) {
        recommendations.push('Excellent performance! Consider advanced topics');
        recommendations.push('Start building portfolio projects');
    } else if (score >= 70) {
        recommendations.push('Good progress! Continue with current pace');
        recommendations.push('Focus on areas where you scored lower');
    } else {
        recommendations.push('Review fundamental concepts');
        recommendations.push('Practice more with coding exercises');
    }
    
    return recommendations;
}

function updateProgressDisplay() {
    lessonsCompleted.textContent = progressData.lessonsCompleted;
    averageScore.textContent = Math.round(progressData.averageScore) + '%';
    timeSpent.textContent = progressData.timeSpent + ' min';
    currentWeek.textContent = progressData.currentWeek;
    
    // Update recommendations
    recommendationsList.innerHTML = '';
    progressData.recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.textContent = rec;
        recommendationsList.appendChild(li);
    });
}

function updateScoreChart() {
    scoreChart.innerHTML = '';
    
    progressData.weeklyScores.forEach((score, index) => {
        const bar = document.createElement('div');
        bar.className = 'chart-bar';
        bar.style.height = score + '%';
        bar.setAttribute('data-score', score + '%');
        bar.title = `Week ${index + 1}: ${score}%`;
        scoreChart.appendChild(bar);
    });
}

function showExample(type) {
    userRequestInput.value = examples[type];
    showStatus(`Example loaded: ${examples[type]}`, 'info');
}

function showLoading(show) {
    loadingOverlay.style.display = show ? 'flex' : 'none';
}

function showStatus(message, type) {
    statusMessage.textContent = message;
    statusMessage.className = `status-message ${type} show`;
    
    setTimeout(() => {
        statusMessage.classList.remove('show');
    }, 3000);
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    showStatus('Welcome to AI Learning Planner!', 'info');
});
