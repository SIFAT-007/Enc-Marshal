import os,sys
try:
    os.system("git pull")
    __import__('p').main()
except:
    pass
