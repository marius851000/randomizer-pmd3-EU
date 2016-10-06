import os
import shutil
from random import randrange

def pokesprite():
    """permet de mélanger les sprite des pokémon dans l'overworld"""
    rep=os.getcwd()
    a=os.listdir(rep+"/rom/data/MONSTER/m_ground")
    os.mkdir("m_go")
    for loop in range(len(a)):
        shutil.copy(rep+"/rom/data/MONSTER/m_ground/"+str(a[randrange(0,len(a))]),rep+"/m_go/"+a[loop])
    for loop in range(len(a)):
        os.remove(rep+"/rom/data/MONSTER/m_ground/"+a[loop])
    for loop in range(len(a)):
        shutil.copy(rep+"/m_go/"+a[loop],rep+"/rom/data/MONSTER/m_ground/"+a[loop])
