import git, os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#

repo = git.Repo(f'{currentdir}/../../../../')  # if repo is CWD just do '.'

repo.index.add(['ergosite/ergo/feed/dbs/apiscrape.py','ergosite/ergo/feed/dbs/cronjob.py'])
repo.index.commit('gitpython test')
origin = repo.remote('origin')
origin.push()