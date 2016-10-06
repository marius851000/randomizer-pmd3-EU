import os
import shutil
from random import randrange

def randompor():
    """fonction pour randomizer les sprites"""
    rep=os.getcwd()
    os.chdir(rep)
    a=os.listdir(rep+'/portraits')
    try:
        os.mkdir('porrandom')
    except:
        pass
    for loop in range(len(a)):
        randomn=randrange(0,len(a))
        b=os.listdir(rep+"/portraits/"+a[randomn])
        print('---')
        print(b)
        try:
            os.mkdir(rep+'/porrandom/'+a[loop])
        except:
            pass
        
        for loop2 in range(len(b)):
            print('copy')
            shutil.copy(rep+"/portraits/"+a[randomn]+"/"+b[loop2],rep+"/porrandom/"+a[loop]+"/"+b[loop2])

    for loop in range(len(a)):
        b=os.listdir(rep+"/portraits/"+a[loop])
        for loop2 in range(len(b)):
            os.remove(rep+"/portraits/"+a[loop]+'/'+b[loop2])
        os.rmdir(rep+"/portraits/"+a[loop])
    os.rmdir(rep+"/portraits")
    
    os.mkdir(rep+"/portraits")
    for loop in range(len(a)):
        b=os.listdir(rep+"/porrandom/"+a[loop])
        os.mkdir(rep+"/portraits/"+a[loop])
        for loop2 in range(len(b)):
            shutil.copy(rep+"/porrandom/"+a[loop]+"/"+b[loop2],rep+"/portraits/"+a[loop]+"/"+b[loop2])
        for loop2 in range(30):
            if loop2<10:
                try:
                    shutil.copy(rep+"/portraits/"+a[loop]+"/0000.png",rep+"/portraits/"+a[loop]+"/000"+str(loop2)+".png")
                except:
                    pass
            else:
                try:
                    shutil.copy(rep+"/portraits/"+a[loop]+"/0000.png",rep+"/portraits/"+a[loop]+"/00"+str(loop2)+".png")
                except:
                    pass
    
