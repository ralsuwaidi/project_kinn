import textwrap
from text_1 import *
from functions_1 import *
import re



def cprint(strs):
    for x in strs.splitlines():
        print '\n'.join(line.strip() for line in re.findall(r'.{1,79}(?:\s+|$)', x))
        raw_input("")

def choice(lst,ans):
    for i in lst:
        print i
    picked=False

    while picked==False:
        ch=raw_input("")
        if ch.lower()=="a":
            cprint(ans[0])
            picked=True
        elif ch.lower()=="b":
            cprint(ans[1])
            picked=True
        elif ch.lower()=="c":
            cprint(ans[2])
            picked=True
        else:
            print "Pick one of them by typing its letter :)"


