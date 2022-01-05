import git, os, sys, time, apiscrape
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
def updaterepo():
    repo = git.Repo(f'{currentdir}/../../../../')  # if repo is CWD just do '.'
    repo.index.add([f'{currentdir}/.'])
    repo.index.commit('AUTOMATED REMOTE UPDATES')
    origin = repo.remote('origin')
    origin.push()
####
def runcron():
    apiscrape.scrape()
    time.sleep(10)
    #Commented out until .gitignore issue is fixed
    #updaterepo()
    ####
runcron()