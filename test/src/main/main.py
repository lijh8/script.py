import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
    "hello"))
from src.foo_dir import foo

print("main")
foo.fun()
