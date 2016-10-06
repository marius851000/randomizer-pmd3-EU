import os
import shutil
from random import randrange

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
