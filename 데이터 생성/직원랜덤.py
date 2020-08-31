import random
import string

# 지역 랜덤 리스트
f = open("please.txt","r")

finalresult=[]

for line in f.readlines():
  
    temp=line.strip().split()
    
    if len(finalresult)==0:
        finalresult.append(temp)
    else:
        state=True
        for j in range(len(finalresult)):
            if temp[4] in finalresult[j]:
                state=False
            else:
                pass
        if state ==True:      
            finalresult.append(temp)    
            
        else:
            pass
                
    if len(finalresult)>200000000:
        break

random.shuffle(finalresult)

# 이름 랜덤 리스트
f = open("firstname.txt","r")
fresult=[]

for i in f.readlines():
    temp=i.strip().split()
    fresult.append(temp[1])


f.close()

random.shuffle(fresult)

f = open("middlename.txt","r")
mresult=[]

for line in f.readlines():
    temp=line.strip().split()
    mresult.append(temp[0])
f.close()

random.shuffle(mresult)




# 전화번호 랜덤 리스트
numresult=[]


while True:
    num1=random.randrange(0,10000)
    num2=random.randrange(0,10000)
    strtemp1=str(num1).rjust(4,'0')     
    strtemp2=str(num2).rjust(4,'0')
    strtemp = "010-"+strtemp1+"-"+strtemp2

    if strtemp not in numresult:
        numresult.append(strtemp)
        if len(numresult)==1000:
            break
        else:
            pass
    else:
        pass

# 주민번호 랜덤 리스트
sf1=["1","2","3","4"]

resiresult=[]
while len(resiresult)<=1000:
    f2 =random.randrange(50,100)
    m2 = random.randrange(1,13)
    l2 = random.randrange(1,29)
    sl6 = random.randrange(1,1000000)

    if i==0:
        pass
    else:
        temp = str(f2).rjust(2,'0')+str(m2).rjust(2,'0')+str(l2).rjust(2,'0')+"-"+random.choice(sf1)+str(sl6).rjust(6,'0')
        if temp not in resiresult:
            resiresult.append(temp)
        else:
            pass

f=open("직원새파일.txt","w")

for i in range(335):    
    f.write("INSERT INTO EMPLOYEE(EMPNO,NAME,ADDR,TEL,RESIDENT_NO,FK_DEPTNO)\tVALUES({0},\'{1}\', \'{2}\',\'{3}\',\'{4}\',{5});"
          .format(i+1,
                  random.choice(fresult)+random.choice(mresult),
                   " ".join(finalresult[i][1:5]),
                  numresult[i],
                  resiresult[i],
                  random.randrange(1,15)
                  ))
    f.write('\n')
