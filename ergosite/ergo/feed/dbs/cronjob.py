import git, os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#

repo = git.Repo(f'{currentdir}/../../../../')  # if repo is CWD just do '.'

repo.index.add(['.'])
repo.index.commit('remote db updates')
origin = repo.remote('origin')
origin.push()