# GITHUB USER ACTIVITY 
https://roadmap.sh/projects/github-user-activity

# Requirements
1. build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal.
2. App should be able to run from CLI
3. Github username as argument
    -> github-activity <username>
4. fetch recent activity from Github API
    -> # https://api.github.com/users/<username>/events : use this endpoint to fetch recent user activity
5. display in terminal
    -> Output:
        - Pushed 3 commits to kamranahmedse/developer-roadmap
        - Opened a new issue in kamranahmedse/developer-roadmap
        - Starred kamranahmedse/developer-roadmap
        - ...


Notes:
- Handle errors gracefully, such as invalid usernames or API failures.
- Do not use any external libraries or frameworks to fetch the GitHub activity.


# Creating a new repo
1. Create a new repo on GitHub
2. Initialise Git in terminal
    git init
    git add .
    git commit -m "Initial commit"
3. Add Remote and push (SSH)
    git remote add origin git@github.com:codingpracs/your-repo.git
    git branch -M main
    git push -u origin main