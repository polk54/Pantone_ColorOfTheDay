## This file will create a function that wiil upload the new index to GitHub when called
## Using the package GitPython

### DEFINE FUNCTION:
def push(repo_dir):
    from git import Repo
    import os

    #repo_dir = "Pantone_ColorOfTheDay"
    repo = Repo(repo_dir)
    file_list = [
        "index.html",
        "Colors.csv"
    ]
    commit_message = 'Added new color'
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()

## RUN FUNCTION:
#repo_dir = "Pantone_ColorOfTheDay"
#push(repo_dir)
