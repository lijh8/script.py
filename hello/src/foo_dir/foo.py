import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
from foo2_dir import foo2
import foo3

def fun():
    print("foo")
    foo2.fun()
    foo3.fun()
