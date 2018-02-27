import textwrap
from text_1 import *
from functions_1 import *
from story import *
import re
import os

def skip_to_story(x):
  if x.lower()=="arthur":
    arthur()
  elif x.lower()=="bambi":
    bambi()
    arthur()

ans=raw_input("Do you want to skip to a specific story? \n[y,n]\n\n")
if ans=="n":
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    all_story()
else:
    skip_to=raw_input("Where do you want to skip to?\n Type: Arthur or ...")
skip_to_story(skip_to)

raw_input("END")
