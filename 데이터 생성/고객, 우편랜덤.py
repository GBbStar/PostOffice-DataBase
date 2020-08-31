import random
import string

# 지역 랜덤 리스트
f = open("please.txt","r")

finalresult=[]

for line in f.readlines():
  
    temp=line.strip().split()

    if len(temp)<5:
        continue
    else :
        pass
    
    if len(finalresult)==0:
        finalresult.append(temp)
    else:
        state=True
        for j in range(len(finalresult)):
            if temp[4] in finalresult[j] or temp[0] in finalresult[j]:
                state=False
            else:
                pass
        if state ==True:      
            finalresult.append(temp)    
            
        else:
            pass
                
    if len(finalresult)>800000000000000:
        break

random.shuffle(finalresult)

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

# id 랜덤 리스트
idresult=[]
for i in range(300):
    idresult.append(i+1)



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
        if len(numresult)==332:
            break
        else:
            pass
    else:
        pass

# 비밀번호 랜덤 리스트
string_pool = string.ascii_letters + string.digits
passresult=[]

f=open("고객새파일.txt",'w')
f2=open("주소새파일.txt",'w')
for i in range(332):
    pw2 = "".join([random.choice(string_pool) for _ in range(20)])
    passresult.append(pw2)

#형식 출력
for i in range(332):
    temp=finalresult[i]
    f2.write("INSERT INTO POST_CODE(ADDR,POST_CODE)\tVALUES(\'{0}\',{1});"
          .format(" ".join(temp[1:5]), temp[0]))
    f2.write('\n')
    
    f.write("INSERT INTO CUSTOMER(CUSTID,NAME,FK_ADDR,TEL,PASSWORD)\tVALUES({0},\'{1}{2}\', \'{3}\',\'{4}\',\'{5}\');"
          .format(i+1,random.choice(fresult),random.choice(mresult),
                  " ".join(temp[1:5]),numresult[i],passresult[i]))
    f.write('\n')
      

