# Getting OS installed using sys.platform and os module
# Use samples from this script to detect your OS

##### Documentation #####
# Platform module has a finer granularity
# Platform	: https://docs.python.org/3/library/platform.html
# OS 		: https://docs.python.org/3/library/os.html

import platform, os

def using_os():
	if os.name == 'nt':
		print('Windows')
	else:
		print('Linux')

def using_platform():
	print(platform.system())	

using_os()
using_platform()
