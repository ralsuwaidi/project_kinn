import textwrap
from text_1 import *
from functions_1 import *
import re

def all_story():
  bambi()
  arthur()

def bambi():
    cprint(bambi_1)
    choice(c_bambi_1, a_bambi_1)
    choice(c_bambi_2, a_bambi_2)

def arthur():
    cprint(arthur_1)
    choice(c_arthur_1, a_arthur_1)
    cprint(arthur_2)
    cprint(arthur_2_1)