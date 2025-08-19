# Project: Personal Learning Tracker with Git 📚

**Goal**: Build a simple learning tracker while practicing real-world Git workflows

**Difficulty**: Beginner-Intermediate  

**Time**: 2-3 hours (can be spread over multiple sessions)

**Skills You'll Practice**:
- Git repository setup and management
- Branching and merging
- Commit best practices
- Documenting your learning journey

## Project Overview

You'll create a digital learning tracker that helps you:
- Track progress across all your subjects (Chinese, AI, Python, Philosophy, etc.)
- Log daily learning activities
- Set and monitor learning goals
- Practice Git while building something useful!

## Project Structure
```
learning_tracker/
├── README.md                 # Project documentation
├── subjects/                 # Individual subject tracking
│   ├── chinese.md           # Chinese learning progress
│   ├── python.md            # Python learning progress  
│   ├── ai.md                # AI learning progress
│   └── philosophy.md        # Philosophy learning progress
├── daily_logs/              # Daily learning entries
│   ├── 2024-01-15.md       # Example daily log
│   └── template.md          # Template for new days
├── goals/                   # Learning goals and milestones
│   ├── weekly_goals.md      # Short-term goals
│   └── monthly_goals.md     # Longer-term objectives
└── scripts/                 # Helper scripts (Python)
    ├── new_day.py          # Script to create new daily log
    └── progress_summary.py  # Generate progress reports
```

## Git Workflow You'll Practice

### Phase 1: Repository Setup
- Initialize repository
- Create initial project structure
- Make first commit with proper message

### Phase 2: Feature Branches  
- Create separate branches for each feature
- Practice merging branches
- Handle potential merge conflicts

### Phase 3: Collaboration Simulation
- Push to GitHub/GitLab
- Practice pull requests (even with yourself!)
- Document your Git learning journey

## Step-by-Step Implementation

### Step 1: Initialize the Project
```bash
# Create project directory
mkdir learning_tracker
cd learning_tracker

# Initialize Git repository
git init

# Create basic structure
mkdir subjects daily_logs goals scripts

# Create initial README
echo "# My Learning Journey Tracker" > README.md
echo "Tracking my progress across multiple subjects using Git!" >> README.md

# First commit
git add README.md
git commit -m "Initial commit: Set up learning tracker project"
```

### Step 2: Create Subject Tracking Files
**Branch**: `feature/subject-tracking`

```bash
# Create a new branch for this feature
git checkout -b feature/subject-tracking

# Create subject files
echo "# Chinese Learning Progress" > subjects/chinese.md
echo "# Python Learning Progress" > subjects/python.md  
echo "# AI Learning Progress" > subjects/ai.md
echo "# Philosophy Learning Progress" > subjects/philosophy.md

# Add content to one subject file
cat >> subjects/chinese.md << EOF

## Current Level
- HSK Level: Working toward HSK 2
- Characters learned: ~50
- Study method: Flashcards + coding projects

## Recent Accomplishments
- Set up Chinese subject directory in brain repo
- Planning CLI flashcard app project

## Next Goals
- Learn 20 new HSK 2 characters this week
- Start building flashcard application
EOF

# Commit this feature
git add subjects/
git commit -m "Add subject tracking files with Chinese progress"
```

### Step 3: Daily Logging System
**Branch**: `feature/daily-logs`

```bash
# Switch to main and create new branch
git checkout main
git checkout -b feature/daily-logs

# Create daily log template
cat > daily_logs/template.md << EOF
# Daily Learning Log - [DATE]

## Time Spent
- Subject 1: X minutes
- Subject 2: Y minutes
- Total: Z minutes

## What I Learned
- Key concept/skill learned today
- Interesting discovery or insight

## What I Built/Practiced
- Code written
- Exercises completed
- Projects advanced

## Challenges Faced
- What was difficult
- How I overcame it (or plan to)

## Tomorrow's Plan
- What to focus on next
- Specific goals for tomorrow

## Git/Coding Notes
- New commands learned
- Programming concepts understood
- Tools or techniques discovered
EOF

# Create today's log (example)
cp daily_logs/template.md daily_logs/$(date +%Y-%m-%d).md

# Commit the daily logging system
git add daily_logs/
git commit -m "Add daily logging system with template"
```

### Step 4: Goals and Tracking
**Branch**: `feature/goals-tracking`

```bash
# Create goals branch
git checkout main  
git checkout -b feature/goals-tracking

# Create goals files
cat > goals/weekly_goals.md << EOF
# Weekly Learning Goals

## Week of [DATE]

### Chinese
- [ ] Learn 15 new HSK 2 characters
- [ ] Complete 3 coding exercises in Chinese context
- [ ] Practice writing characters daily

### Python  
- [ ] Complete 2 coding challenges
- [ ] Build one small utility script
- [ ] Read about one new Python library

### Git
- [ ] Master branching and merging
- [ ] Practice good commit messages
- [ ] Set up GitHub repository

### AI
- [ ] Read about one AI concept
- [ ] Experiment with one AI tool
- [ ] Connect AI learning to other subjects
EOF

cat > goals/monthly_goals.md << EOF
# Monthly Learning Goals

## [MONTH YEAR]

### Big Picture Goals
- Build a complete Chinese learning app
- Create a personal learning dashboard
- Contribute to an open source project
- Master Git workflow

### Subject-Specific Milestones
- Chinese: Reach HSK 2 level vocabulary
- Python: Build 3 complete projects  
- AI: Understand neural network basics
- Philosophy: Read and summarize 2 major works

### Skills to Develop
- Version control with Git
- Web development basics
- Project documentation
- Code organization and best practices
EOF

# Commit goals tracking
git add goals/
git commit -m "Add weekly and monthly goal tracking system"
```

### Step 5: Automation Scripts
**Branch**: `feature/automation`

```bash
# Create automation branch
git checkout main
git checkout -b feature/automation

# Create script to generate new daily log
cat > scripts/new_day.py << EOF
#!/usr/bin/env python3
"""
Script to create a new daily learning log
Usage: python new_day.py
"""

import os
from datetime import datetime

def create_daily_log():
    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Read template
    with open("daily_logs/template.md", "r") as f:
        template = f.read()
    
    # Replace [DATE] with actual date
    content = template.replace("[DATE]", today)
    
    # Create new file
    filename = f"daily_logs/{today}.md"
    
    if os.path.exists(filename):
        print(f"Log for {today} already exists!")
        return
    
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"Created new daily log: {filename}")
    print("Don't forget to commit it to Git!")

if __name__ == "__main__":
    create_daily_log()
EOF

# Make script executable (Linux/Mac)
chmod +x scripts/new_day.py

# Test the script
python scripts/new_day.py

# Commit automation
git add scripts/
git commit -m "Add Python script to generate daily logs"
```

### Step 6: Merge Everything Together
```bash
# Switch to main branch
git checkout main

# Merge each feature branch
git merge feature/subject-tracking
git merge feature/daily-logs  
git merge feature/goals-tracking
git merge feature/automation

# Update README with complete project info
cat > README.md << EOF
# My Learning Journey Tracker 📚

A personal learning management system built while practicing Git workflows!

## Features
- Subject-specific progress tracking
- Daily learning logs with templates
- Weekly and monthly goal setting
- Automation scripts for common tasks

## Subjects Tracked
- Chinese Language Learning
- Python Programming
- Artificial Intelligence
- Philosophy Studies

## Git Skills Practiced
- Repository initialization
- Feature branching
- Merging workflows
- Commit message best practices
- Project documentation

## Usage
\`\`\`bash
# Create a new daily log
python scripts/new_day.py

# Update subject progress
# Edit files in subjects/ directory

# Set new goals
# Edit files in goals/ directory
\`\`\`

## Project Structure
See the directory tree above for complete organization.

## Future Enhancements
- Web interface for easier logging
- Progress visualization scripts
- Integration with external learning platforms
- Automated goal progress tracking
EOF

# Final commit
git add README.md
git commit -m "Complete learning tracker with full documentation"
```

## Git Skills Demonstrated 🎯

Through this project, you'll practice:

1. **Repository Management**
   - `git init`, `git add`, `git commit`
   - Creating meaningful project structure

2. **Branching Workflow**
   - `git checkout -b feature/name`
   - `git merge feature/name`
   - Organizing work by feature

3. **Commit Best Practices**
   - Descriptive commit messages
   - Logical grouping of changes
   - Atomic commits (one feature per commit)

4. **Project Documentation**
   - README files with clear instructions
   - Documenting Git workflow decisions
   - Explaining project structure

## Extending the Project 🚀

### Phase 2 Ideas:
- **GitHub Integration**: Push to GitHub, practice pull requests
- **Collaboration**: Invite a friend to contribute
- **Advanced Git**: Rebasing, cherry-picking, advanced merging
- **Automation**: GitHub Actions for automated progress tracking

### Cross-Subject Integration:
- **Python**: Build more sophisticated tracking scripts
- **AI**: Add AI-powered learning recommendations
- **Chinese**: Create Chinese-language version of tracker
- **Philosophy**: Add reflection prompts and philosophical journaling

## Troubleshooting Common Issues 🛠️

### Merge Conflicts
If you get conflicts during merging:
```bash
# See which files have conflicts
git status

# Edit conflicted files (look for <<<< and >>>>)
# Remove conflict markers and choose what to keep

# Stage resolved files
git add resolved_file.md

# Complete the merge
git commit
```

### Branch Management
```bash
# See all branches
git branch

# Delete a feature branch after merging
git branch -d feature/branch-name

# Switch between branches
git checkout branch-name
```

## Success Metrics ✅

By the end of this project, you should:
- [ ] Have a working learning tracker
- [ ] Understand Git branching and merging
- [ ] Write clear, meaningful commit messages
- [ ] Organize code projects effectively
- [ ] Feel confident using Git for real projects

## Reflection Questions 🤔

1. How did using Git change how you thought about organizing this project?
2. What was the most challenging Git concept to understand?
3. How could you apply this Git workflow to your other learning projects?
4. What features would you add to make this tracker more useful?

---
*This project combines practical Git skills with something genuinely useful for your learning journey!*
