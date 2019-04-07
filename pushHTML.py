## This file will create a function that wiil upload the new index to GitHub when called
## Using GitPython

### DEFINE FUNCTION:
def push():
    from git import Repo
    path = "/Users/parulagarwal/Documents/Code/GitHub/Pantone_ColorOfTheDay"

    try:
        repo = Repo(path)
        file_list = [
            "index.html",
            "Colors.csv"
        ]
        commit_message = 'Add new color'
        #repo.git.add(update=True)
        repo.index.add(file_list)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        print('Code push from script succeeded')
    except:
        print('Some error occured while pushing the code')

## RUN FUNCTION:
push()
