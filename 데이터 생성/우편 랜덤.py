import random
import string





# 이름 랜덤 리스트
f = open("firstname.txt","r")
fresult=[]

for i in f.readlines():
    temp=i.strip().split()
    fresult.append(temp[1])


f.close()


f = open("middlename.txt","r")
mresult=[]

for line in f.readlines():
    temp=line.strip().split()
    mresult.append(temp[0])
f.close()


# 지역 랜덤 리스트
f = open("please.txt","r")

finalresult=[]

for line in f.readlines():
  
    temp=line.strip().split()
    if len(temp)<5:
        continue
    
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
                
    if len(finalresult)>800000000:
        break

random.shuffle(finalresult)

f.close()


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
        if len(numresult)==12000:
            break
        else:
            pass
    else:
        pass


# 수신여부
getresult=["수신","수신대기","수신거부"]

f=open("우편새파일.txt","w")

# 출력
for i in range(6000):
    
    f.write("""INSERT INTO MAIL(REGINO,TO_NAME,TO_ADDR,TO_TEL,FROM_NAME,FROM_ADDR,FROM_TEL,REG_TIME,REC_STATUS,FK_MTYPENO,FK_DELNO,FK_EMPNO,FK_CUSTID)
VALUES({0},\'{1}\', \'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\',\'{8}\',{9},{10},{11},{12});"""
          .format(i+1,
                  random.choice(fresult)+random.choice(mresult),
                  " ".join(finalresult[i][1:5]),
                  numresult[i],
                  random.choice(fresult)+random.choice(mresult),
                  " ".join(finalresult[i][1:5]),
                  numresult[i+1],
                  "2019-12"+"-"+str(random.randrange(1,7)).rjust(2,'0')+" "+str(random.randrange(9,23)).rjust(2,'0')
                  +":"+str(random.randrange(0,61)).rjust(2,'0')+":"+str(random.randrange(0,61)).rjust(2,'0'),
                  random.choice(getresult),
                  random.randrange(1,3),
                  random.randrange(1,300),
                  random.randrange(1,300),
                  random.randrange(1,287)
                  ))
    f.write('\n')
