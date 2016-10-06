import os
import shutil
from random import randrange
from zmusicf import randomizemusic
from zportrait import randompor
from zspritepkmn import pokesprite
from zoverworld import overworld
         




shutil.copy('ran.txt','filecopilpythonfilecomforextract.bin')
story=open('filecopilpythonfilecomforextract.bin')
end=True
while end:
    temp=story.readline()
    print(temp)
    if temp=="":
        end=False
    elif temp=="musicf\n":
        randomizemusic()
    elif temp=="portrait\n":
        randompor()
    elif temp=="spritepkmn\n":
        pokesprite()
    elif temp=="overworld\n":
        overworld()
story.close()
