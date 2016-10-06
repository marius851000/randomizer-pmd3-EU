import os
import shutil
from random import randrange

def randomizemusic():
    """randomize la musique - pas de compilation
/!\ cette fonction peut faire buguer le jeu"""
    print('pikachu croise une bande de pijako')
    rep=os.getcwd()
    os.chdir(rep)
    a=os.listdir(rep+"/rom/data/SOUND/BGM/")
    print('pikachu les à tous reperer')
    try:
        os.mkdir('out_bgm')
    except:
        pass

    for loop in range(1,len(a)):
        print('combat contre le pijako n°'+str(loop))
        temp=""
        print()
        print('son nom originel est '+a[loop])
        for loop2 in range(len(a[loop])-4):
            temp=temp+a[loop][loop2]
        print("son nom est maintenant décrypté grace à son smartphone :"+temp)
        fichier=randrange(1,len(a))
        fichier=a[fichier]
        temp2=""
        print('annalise des donné du future clone :'+fichier)
        for loop2 in range(len(fichier)-4):
            temp2=temp2+fichier[loop2]
        print("le clone "+temp2+" vas le remplacer")
        shutil.copy(rep+"/rom/data/SOUND/BGM/"+temp2+".smd",rep+"/out_bgm/"+temp+".smd")
        shutil.copy(rep+"/rom/data/SOUND/BGM/"+temp2+".swd",rep+"/out_bgm/"+temp+".swd")
        print("le clone "+temp2+" la remplacer, est pijako est désorienter à cause de son clone")
        print()
        print('fin du combat contre pijako n°'+str(loop))
        print()
        print()

    a=os.listdir(rep+'/out_bgm')
    print('pijako totalement désorienté, pika va les tuer')
    for loop in range(len(a)):
        shutil.copy(rep+'/out_bgm/'+a[loop],rep+"/rom/data/SOUND/BGM/"+a[loop])
        print('pijako '+str(loop)+' tué')
    print('tout les pijako tué')
   
