from fabric.api import local


def new_repository(repo, username = "cconeil"):
	init()
	update_files()
	commit()
	add(username, repo)
	push()


def init():
	local("git init")
def update_files():
	local("git add .")
def commit(message = '\"first commit\"'):
	local("git commit -m %s" % message)
def add(username, repo):
	local("git remote add origin https://github.com/%s/%s.git" % (username, repo))
def push():
	local("git push -u origin master")

