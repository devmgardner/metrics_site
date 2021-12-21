import git, os, sys, time, apiscrape
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
apiscrape.scrape()
time.sleep()
repo = git.Repo(f'{currentdir}/../../../../')  # if repo is CWD just do '.'
repo.index.add([f'{currentdir}/.'])
repo.index.commit('gitpython test')
origin = repo.remote('origin')
origin.push()