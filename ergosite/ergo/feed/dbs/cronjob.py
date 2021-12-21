import git
repo = git.Repo('../../../')  # if repo is CWD just do '.'

repo.index.add(['.'])
repo.index.commit('remote db updates')
origin = repo.remote('origin')
origin.push()