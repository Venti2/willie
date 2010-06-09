"""
version.py
Author: Silas Baronda
Phenny (About): http://inamidst.com/phenny/
"""

from subprocess import *

def version(phenny, input):
	p = Popen(["git", "log", "-n 1"], stdout=PIPE, close_fds=True)

	commit = p.stdout.readline()
	author = p.stdout.readline()
	date = p.stdout.readline()
	
	phenny.say(str(input.nick) + ": running version:")
	phenny.say("  " + commit)
	phenny.say("  " + author)
	phenny.say("  " + date)

version.commands = ['version']
version.priority = 'medium'

if __name__ == '__main__': 
	print __doc__.strip()
