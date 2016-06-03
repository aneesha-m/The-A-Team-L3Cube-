import shelve
import sys

fs = shelve.open('filesystem.fs', writeback=True)
current_dir = []

def install(fs):
	# create root and others
	username = raw_input('What do you want your username to be? ')
	print username+ " directory created in Users\n"
	fs[""] = {"System": {}, "Users": {username: {}}}

def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    d = fs[""]
    for key in current_dir:
        d = d[key]
    return d 

def ls(args):
    print 'Contents of directory', "/" + "/".join(current_dir) + ':'
    for i in current_dictionary():
        print i 
    fs.sync()

def cd(args):

    if len(args) != 1:

        print "Usage: cd "
        return

    if args[0] == "..":
        if len(current_dir) == 0:
            print "Cannot go above root"
        else:
            current_dir.pop()
    elif args[0] not in current_dictionary():
        print "Directory " + args[0] + " not found"
    else:
        current_dir.append(args[0])

def mkdir(args):
    if len(args) != 1:
        print "Usage: mkdir "
        return

#To create an empty directory there and sync back to shelve dictionary!

    d = current_dictionary()[args[0]] = {}
    print d
    print current_dictionary()
    print current_dictionary()[args[0]]
    print args[0]
    print current_dir
    fs.sync()
    print fs
    
def rmdir(args):
	if len(args) != 1:
		print "Usage: rmdir"
		return
		
	print args[0]
	print current_dir
	if args[0] in current_dir:
		print "in if"
		current_dir.remove(args[0])
		d=current_dictionary()
		del d[args[0]]
	fs.sync()
	
def pwd(args):

    d=current_dir
    if len(current_dir) == 0:
            print "Cannot go above root"
	    #break
    else:
        print d[-1]

def createf(args):
    if len(args) != 1:
        print "Usage: createf <file name with extension> "
        return

    print "Enter text"
    text = raw_input()
    sz=len(text)
    mdsz="**size:"+str(sz)+" "
    mdpm="permission:6"
    md=text+mdsz+mdpm
    d = current_dictionary()[args[0]] = {md}
    fs.sync()

def readf(args):
	if len(args) != 1:
		print "Usage readf <filename>"
		return

	if args[0] not in current_dictionary():
		print "File " + args[0] + " not found"
	else:
		current_dir.append(args[0])

	for i in current_dictionary():
		con,md=i.split("**")
		print con
	n = input("press 1 to see metadata, 0 to skip")
	if n==1:
		print md
	current_dir.pop()


def quit(args):
    sys.exit(0)

COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir,'pwd':pwd,'quit':quit,'rmdir':rmdir,'createf':createf,'readf':readf}

install(fs)
print "Commands available in TextFS: \n ls:listing \n cd:change directory \n createf:create file \n readf:read file\n mkdir:make file \n rmdir:remove directory \n pwd:present working directory \n "

while True:
	raw = raw_input('>')
	cmd = raw.split()[0]
	if cmd in COMMANDS:
		COMMANDS[cmd](raw.split()[1:])
	else:
		print "Invalid command"

#Use break instead of exit, so you will get to this point.
raw_input('Press the Enter key to shutdown...')

