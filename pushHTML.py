## This file will create a function that wiil upload the new index to GitHub when called
## Using GitPython

### DEFINE FUNCTION:
def push():
    from git import Repo, Actor
    path = "/Users/parulagarwal/Documents/Projects/Code/GitHub/Pantone_ColorOfTheDay" # runs, but no upload
    #path = "https://github.com/polk54/Pantone_ColorOfTheDay.git" # has an error

    try:
        repo = Repo(path)
        file_list = ["index.html", "Colors.csv"]
        commit_message = 'test3'
        #repo.git.add(update=True)
        repo.index.add(file_list)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        print('Code push from script succeeded')
    except:
        print('Some error occured while pushing the code')


    #for commit in repo.iter_commits():
    #    print ("Author: ", commit.author)
    #    print ("Summary: ", commit.summary)


## RUN FUNCTION:
#path = "/Users/parulagarwal/Documents/Projects/Code/GitHub/Pantone_ColorOfTheDay"
#path = r'https://github.com/polk54/Pantone_ColorOfTheDay.git'
push()
