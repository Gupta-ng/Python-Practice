"""
import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments")
"""
"""
import sys
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])
"""  
""" 
import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")
else:
    print("hello, my name is", sys.argv[1])
""" 

import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)



