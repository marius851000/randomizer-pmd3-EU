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

def overworld():
    total="/7 : "
    rep=os.getcwd()
    file=open('equiv.txt')
    temp="None"
    table=[]
    while temp != "":
        print("1"+total+"?")
        temp=file.readline()
        if temp!="":
            temp2=temp.split("\n")
            temp2=temp2[0]
            table.append(temp2.split("-"))
    file.close()
    
    """"code basé sur la fonction portrait"""
    rep=os.getcwd()
    os.chdir(rep)
    try:
        os.mkdir('porrandom')
    except:
        pass
    a=os.listdir('portraits')
    c=os.listdir(rep+'/rom/data/MONSTER/m_ground/')

    try:
        os.mkdir('m_go')
    except:
        pass
    portemp=0
    
    for loop in range(len(table)):
        print("2"+total+str(loop)+"/"+str(len(table)))
        randomn=randrange(0,len(table))
        spor=table[randomn][1]
        poror=table[randomn][0]
        porto=table[loop][0]
        spto=table[loop][1]
        select=1
        

        if select!=0:
            b=os.listdir(rep+"/portraits/"+poror)
            try:
                os.mkdir(rep+'/porrandom/'+porto)
            except:
                pass
            for loop2 in range(len(b)):
                shutil.copy(rep+"/portraits/"+poror+"/"+b[loop2],rep+"/porrandom/"+porto+"/"+b[loop2])
            shutil.copy(rep+"/rom/data/MONSTER/m_ground/"+spor+".wan",rep+"/m_go/"+spto+".wan")

    for loop in range(len(c)):
        print("3"+total+str(loop)+"/"+str(len(c)))
        if os.path.isfile(rep+"/m_go/"+c[loop])==False:
            randomn=randrange(0,len(c))
            shutil.copy(rep+"/rom/data/MONSTER/m_ground/"+c[randomn],rep+"/m_go/"+c[loop])

    
    for loop in range(len(a)):
        print("4"+total+str(loop)+"/"+str(len(c)))
        if os.path.exists(rep+'/porrandom/'+a[loop])==False:
            
            randomn=randrange(0,len(c))
            b=os.listdir(rep+"/portraits/"+a[loop])
            os.mkdir(rep+"/porrandom/"+a[loop])
            for loop2 in range(len(b)):
                try:
                    shutil.copy(rep+"/portraits/"+a[randomn]+"/"+b[loop2],rep+"/porrandom/"+a[loop]+"/"+b[loop2])
                except:
                    pass
                          
    
    for loop in range(len(a)):
        print("5"+total+str(loop)+"/"+str(len(a)))
        b=os.listdir(rep+"/portraits/"+a[loop])
        for loop2 in range(len(b)):
            os.remove(rep+"/portraits/"+a[loop]+'/'+b[loop2])
        os.rmdir(rep+"/portraits/"+a[loop])
    os.rmdir(rep+"/portraits")

    a=os.listdir(rep+'/porrandom')
    os.mkdir(rep+"/portraits")
    
    for loop in range(len(a)):
        print("6"+total+str(loop)+"/"+str(len(a)))
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

    c=os.listdir(rep+'/m_go')
    for loop in range(len(c)):
        print("7"+total+str(loop)+"/"+str(len(c)))
        os.remove(rep+"/rom/data/MONSTER/m_ground/"+c[loop])
    for loop in range(len(c)):
        print("8"+total+str(loop)+"/"+str(len(c)))
        shutil.copy(rep+"/m_go/"+c[loop],rep+"/rom/data/MONSTER/m_ground/"+c[loop])



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
