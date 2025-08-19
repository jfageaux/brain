# Exercise 1: Your First Git Repository and Commit 🎯

**Goal**: Create your first Git repository and make your first commit

**Time**: 15-20 minutes

**Prerequisites**: Git installed on your computer (run `git --version` to check)

## What You'll Learn
- How to create a Git repository
- The basic Git workflow (add → commit)
- How to check the status of your repository
- How to view your commit history

## Step-by-Step Instructions

### Part 1: Create a Test Repository
1. **Open your terminal/command prompt**
   - Windows: PowerShell or Command Prompt
   - Mac/Linux: Terminal

2. **Navigate to a folder where you want to practice**
   ```bash
   # Example: Navigate to your Desktop
   cd Desktop
   ```

3. **Create a new folder for this exercise**
   ```bash
   mkdir git_practice
   cd git_practice
   ```

4. **Initialize a Git repository**
   ```bash
   git init
   ```
   **Expected output**: `Initialized empty Git repository in .git/`
   
   **What happened**: Git created a hidden `.git` folder that will track all changes

### Part 2: Create Your First File
1. **Create a simple text file**
   ```bash
   # Windows PowerShell:
   echo "This is my first Git repository!" > README.txt
   
   # Mac/Linux:
   echo "This is my first Git repository!" > README.txt
   ```

2. **Check what Git sees**
   ```bash
   git status
   ```
   **Expected output**: Something like:
   ```
   On branch main
   No commits yet
   
   Untracked files:
     README.txt
   ```
   
   **Translation**: Git sees the file but isn't tracking it yet

### Part 3: Make Your First Commit
1. **Stage the file (prepare it for committing)**
   ```bash
   git add README.txt
   ```

2. **Check status again**
   ```bash
   git status
   ```
   **Expected output**: 
   ```
   On branch main
   No commits yet
   
   Changes to be committed:
     new file:   README.txt
   ```
   
   **Translation**: The file is now "staged" and ready to be committed

3. **Configure Git (if this is your first time)**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
   **Note**: Git needs to know who is making commits

4. **Create your first commit**
   ```bash
   git commit -m "Add README file with welcome message"
   ```
   **Expected output**: Something like:
   ```
   [main (root-commit) abc1234] Add README file with welcome message
    1 file changed, 1 insertion(+)
    create mode 100644 README.txt
   ```
   
   **Translation**: Git saved a snapshot of your project!

### Part 4: View Your History
1. **See your commit history**
   ```bash
   git log
   ```
   **You'll see**:
   - Commit hash (unique ID)
   - Author (you!)
   - Date and time
   - Your commit message

2. **Try a prettier version**
   ```bash
   git log --oneline
   ```
   **You'll see**: A condensed, one-line view of each commit

## Practice Exercises

### Exercise A: Add More Content
1. **Edit the README.txt file** (add a new line)
   ```bash
   echo "I'm learning Git step by step!" >> README.txt
   ```

2. **Check status**
   ```bash
   git status
   ```
   **Question**: What does Git show you? Why is it different from before?

3. **View the exact changes**
   ```bash
   git diff
   ```
   **This shows**: Exactly what lines were added (green +) or removed (red -)

4. **Stage and commit the changes**
   ```bash
   git add README.txt
   git commit -m "Add learning progress note"
   ```

### Exercise B: Multiple Files
1. **Create a second file**
   ```bash
   echo "Git commands I've learned:" > commands.txt
   echo "- git init" >> commands.txt
   echo "- git add" >> commands.txt
   echo "- git commit" >> commands.txt
   ```

2. **Stage and commit the new file**
   ```bash
   git add commands.txt
   git commit -m "Add list of Git commands learned"
   ```

3. **View your history**
   ```bash
   git log --oneline
   ```
   **You should see**: Three commits showing your progress!

## Check Your Understanding ✅

Answer these questions (write them down!):

1. **What does `git init` do?**
2. **What's the difference between the "working directory" and the "staging area"?**
3. **What does `git status` tell you?**
4. **Why do we use `git add` before `git commit`?**
5. **What makes a good commit message?**

## Common Issues and Solutions 🛠️

**Issue**: `git: command not found`
**Solution**: Git isn't installed. Download from https://git-scm.com/

**Issue**: `Please tell me who you are` error
**Solution**: Set your name and email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

**Issue**: Made a typo in commit message
**Solution**: For the last commit only:
```bash
git commit --amend -m "Corrected message"
```

## Congratulations! 🎉

You've successfully:
- ✅ Created your first Git repository
- ✅ Made your first commits
- ✅ Learned the basic Git workflow
- ✅ Viewed your project history

**Next**: Complete `02_staging_and_commits.md` to learn more about the staging area and commit best practices.

## Notes Section (For You to Fill Out)
Write down:
- Any commands you found confusing
- Questions you have
- What you want to practice more

---
*Remember: Git mastery comes from practice. Don't worry if it feels overwhelming at first!*
