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

    if len(temp)<4:
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
                
    if len(finalresult)>800000000000000:
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
        if len(numresult)==14000000:
            break
        else:
            pass
    else:
        pass


f=open("택배새파일.txt",'w')
# 현재상태
state=["집화처리","간성상차","터미널 간선상차","간선하차","배달출발","배달도착"]


# 현재위치
loc_hub=["곤지암HUB","용인HUB","군포HUB","옥천HUB","청원HUB","가산콘솔HUB","토평콘솔HUB","원삼1CP","도척2CP","고촌3CP","부곡4CP"]


# 물품정보
data_pro=["농/수/축산물(일반)","농/수/축산물(냉동/냉장)","전자제품","서적","의류/패션잡화","의료/건강식품","생활용품","기타"]

j=1
# 출력
for i in range(7000000):
    temp=random.choice(state)  
    temp2=random.choice(finalresult)
    if temp== "집화처리" or temp== "배달출발":
        a=(" ".join(temp2[1:3]))+"우체국"
    elif temp=="배달완료":
        a=temp
    else:
        a=random.choice(loc_hub)
    
    f.write("""INSERT INTO PARCEL(REGINO,TO_NAME,TO_ADDR,TO_TEL,FROM_NAME,FROM_ADDR,FROM_TEL,CURRENT_LOC,DELIVERY_STATE,PRODUCT_DATA,RECEPTION_TIME,FK_PTYPENO,FK_DELNO,FK_EMPNO,FK_CUSTID)
VALUES({0},\'{1}\', \'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\',\'{8}\',\'{9}\',\'{10}\',{11},{12},{13},{14});"""
          .format(j,
                  random.choice(fresult)+random.choice(mresult),
                  " ".join(temp2[1:5]),
                  numresult[2*i],
                  random.choice(fresult)+random.choice(mresult),
                  " ".join(temp2[1:5]),
                  numresult[2*i+1],
                  a,
                  temp,
                  random.choice(data_pro),
                  "2019-12"+"-"+str(random.randrange(1,7)).rjust(2,'0')+" "+str(random.randrange(9,23)).rjust(2,'0')
                  +":"+str(random.randrange(0,61)).rjust(2,'0')+":"+str(random.randrange(0,61)).rjust(2,'0'),
                  random.randrange(1,3),
                  random.randrange(1,300),
                  random.randrange(1,300),
                  random.randrange(1,288)
                  ))
    f.write('\n')
    j=j+1

    
