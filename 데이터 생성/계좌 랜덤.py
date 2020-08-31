import random
import string

000000-00-000000

# 비밀번호 랜덤 리스트
string_pool = string.ascii_letters + string.digits
passresult=[]

for i in range(6000):
    pw2 = "".join([random.choice(string_pool) for _ in range(18)])+random.choice(['`','!','@','#','$','%','^','&','*','_','-','+','='])
    passresult.append(pw2)

f=open("계좌새파일.txt","w")

# 출력
for i in range(6000):
    
    f.write("""INSERT INTO ACCOUNT_DATA(ACCNO,PASSWD, BALANCE, OPEN_DATE, FK_CUSTID, FK_DEPONO, FK_EMPNO)
VALUES(\'{0}\',\'{1}\',{2},\'{3}\',{4},{5},{6})
/"""
          .format(str(random.randrange(0,1000000)).rjust(6,'0')+"-"+str(random.randrange(0,1000000)).rjust(2,'0')+"-"+str(random.randrange(0,1000000)).rjust(6,'0'),
                  passresult[i],
                  random.randrange(100000,10000000),
                  str(random.randrange(2017,2020))+"-"+str(random.randrange(1,13)).rjust(2,'0')+"-"+str(random.randrange(1,29)).rjust(2,'0')
                  +" "+str(random.randrange(9,23)).rjust(2,'0')+":"+str(random.randrange(0,61)).rjust(2,'0')+":"+str(random.randrange(0,61)).rjust(2,'0'),
                  random.randrange(1,284),
                  random.randrange(1,13),
                  random.randrange(1,300)
                  ))
    f.write('\n')
