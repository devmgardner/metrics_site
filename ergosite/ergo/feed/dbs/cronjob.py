import git
repo = git.Repo('path/to/git/repo')  # if repo is CWD just do '.'

repo.index.add([''])
repo.index.commit('my commit description')
origin = repo.remote('origin')
origin.push()