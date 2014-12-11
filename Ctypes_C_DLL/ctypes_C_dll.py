from ctypes import *
mydll = cdll.LoadLibrary("C:\Python27\UserProj\dll.dll")
print mydll.Func(100)
