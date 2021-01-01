# Getting OS installed using sys.platform module
from sys import platform

if platform == "linux" or platform == "linux2":
    print("Linux")
elif platform == "darwin":
    print("Mac OS X")
elif platform == "win32":
	print("Windows")