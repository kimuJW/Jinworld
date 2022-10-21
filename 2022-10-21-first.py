import sys,random
from tkinter import*

#유닛 리스트
전설=["검수전설","나미전설","네코마무시","드래곤전설","라분전설","레이쥬전설","레일리전설","로우전설","루치전설","루피jet","루나메","마르코전설","모리아전설","바르톨전설","상디쿤전설","샹크스(전설)","센고쿠전설","슈가","스모커","시노부전설","시저","시키전설","에이스전설","울티","제파전설","조로전설","징베전설","카르가라","코비","쿠마폭군","크래커","킹전설","토키","핸콕전설","중력검","흰수염전설","히루루크"]
히든=["미호크히든","레드포스호","레베카히든","류마히든","모비딕호","반더데켄","발라티에","방주맥심","베르고","봉쿠레히든","사보히든","시류히든","써니호","아오키지(히든)","아카히든","이완히든","캐럿","코알라히든","킨에몬히든","킬러히든","페로나히든","피셔히든"]
제한=["레필제한","레베카제한","시노부제한","아인제한","애널제한","카타쿠리제한","크로커제한","킹제한"]
초월=["검수초월","나미초월","도플초월","로빈초월","로우초월","루치초월","루피초월","바질초월","브룩초월","사보초월","상디초월","샹크스(초월)","스네이크맨","시라호시초월","아오키지(초월)","아카이누초월","야마토초월","우솝초월","조로초월","징베초월","쵸파초월!","키드초월","키자루초월","태시기초월","프랑키초월","중력검"]
불멸=["거프ㅋㅋ불멸","드래곤불멸","레일리불멸","로져불멸","빅맘불멸","센고쿠불멸","가반불멸","시키불멸","제트불멸","카이도불멸","흰수염불멸"]
영원=["미호크영원","버기영원","비비영원","에이스영원","오뎅영원","카벤딧슈영원","핸콕영원"]
랜유=["료우기시키","미나토","바쿠야","보릉냐","유카리","좆타로","키쿄우","타츠마키","히그마"]
강원랜디리스트=["인생의 고도(10+dice)","랜유강제","노보상","천룡인","강제 전설 히든","초월 위습 버리기","중급도박(10~30)"]
원딜전리스트=["물딜","마딜"]
강제전리스트=["레드필제한","레베카제한","시노부제한","아인제한","애넬제한","카타쿠리제한","크로커제한","킹제한","검수초월","나미초월","도플초월","로빈초월","로우초월","루치초월","루피초월","바질초월","브룩초월","사보초월","상디초월","샹크스(초월)","스네이크맨","시라호시","아오키지(초월)","아카이누(초월)","야마토초월","우솝초월","조로초월","징베초월","쵸파초월!","키드초월","키자루","태시기초월","프랑키초월","중력검","거프ㅋㅋ불멸","드래곤불멸","레일리불멸","로져불멸","빅맘불멸","센고쿠불멸","가반불멸","시키불멸","제트불멸","카이도불멸","흰수염불멸","미호크영원","버기영원","비비영원","에이스영원","오뎅영원","카벤영원","핸콕영원"]
꼭가야할캐릭리스트=["레필제한","레베카제한","시노부제한","아인제한","애널제한","카타쿠리제한","크로커제한","킹제한","검수초월","나미초월","도플초월","로빈초월","로우초월","루치초월","루피초월","바질초월","브룩초월","사보초월","상디초월","샹크스(초월)","스네이크맨","시라호시","아오키지(초월)","아카이누(초월)","야마토초월","우솝초월","조로초월","징베초월","쵸파초월!","키드초월","키자루","태시기초월","프랑키초월","중력검","거프ㅋㅋ불멸","드래곤불멸","레일리불멸","로져불멸","빅맘불멸","센고쿠불멸","가반불멸","시키불멸","제트불멸","카이도불멸","흰수염불멸","미호크영원","버기영원","비비영원","에이스영원","오뎅영원","카벤영원","핸콕영원"]
전설리스트=[]
히든리스트=[]


b=str(초월[random.randint(0,len(초월)-1)])
c=str(불멸[random.randint(0,len(불멸)-1)])
d=str(영원[random.randint(0,len(영원)-1)])
e=str(제한[random.randint(0,len(제한)-1)])
f=str(강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)])
g=str(원딜전리스트[random.randint(0,len(원딜전리스트)-1)])
h=str(강제전리스트[random.randint(0,len(강제전리스트)-1)])
while True:
    전설리스트=list(set(전설리스트))
    if len(전설리스트)==7:
        break
    a=random.randint(0,len(전설)-1)
    전설리스트.append(전설[a])


while True:
    히든리스트=list(set(히든리스트))
    if len(히든리스트)==7:
        break
    a=random.randint(0,len(히든)-1)
    히든리스트.append(히든[a])


#창 생성
ORD = Tk()
ORD.title("원랜디 룰렛 프로그램")
ORD.geometry("600x1000+200+100")

강원랜디1의텍스트=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
강원랜디2의텍스트=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
강원랜디3의텍스트=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
강원랜디4의텍스트=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]

#뽑기 버튼 클릭 이벤트
def click_event():
    rule_button_click_event()

#지츠 다이스룰 다이스 이벤트
def dice_event1():
    a=random.randint(0,100)
    dice['text']=a
def dice_event2():
    a=random.randint(0,100)
    dice2['text']=a
def dice_event3():
    a=random.randint(0,100)
    dice3['text']=a
def dice_event4():
    a=random.randint(0,100)
    dice4['text']=a

#강원랜디 버튼 클릭 이벤트
def kangwon_event1():
    if  강원랜디1의텍스트==강원랜디리스트[0]:
        a=random.randint(1,10)
        강원랜디1['text']="10"+"+"+str(a)
    elif 강원랜디1의텍스트==강원랜디리스트[1]:
        a=random.randint(0,len(랜유)-1)
        강원랜디1['text']=랜유[a]
    elif 강원랜디1의텍스트==강원랜디리스트[4]:
        a=random.randint(0,len(전설리스트)-1)
        b=random.randint(0,len(히든리스트)-1)
        강원랜디1['text']=전설리스트[a]+" "+히든리스트[b]
    elif 강원랜디1의텍스트==강원랜디리스트[6]:   
        a=random.randint(10,30)
        강원랜디1['text']="중급도박"+str(a)+"회"
def kangwon_event2():
    if 강원랜디2의텍스트==강원랜디리스트[0]:
        a=random.randint(1,10)
        강원랜디2['text']="10"+"+"+str(a)
    elif 강원랜디2의텍스트==강원랜디리스트[1]:
        a=random.randint(0,len(랜유)-1)
        강원랜디2['text']=랜유[a]
    elif 강원랜디2의텍스트==강원랜디리스트[4]:
        a=random.randint(0,len(전설리스트)-1)
        b=random.randint(0,len(히든리스트)-1)
        강원랜디2['text']=전설리스트[a]+" "+히든리스트[b]
    elif 강원랜디2의텍스트==강원랜디리스트[6]:   
        a=random.randint(10,30)
        강원랜디2['text']="중급도박"+str(a)+"회"
def kangwon_event3():
    if 강원랜디3의텍스트==강원랜디리스트[0]:
        a=random.randint(1,10)
        강원랜디3['text']="10"+"+"+str(a)
    elif 강원랜디3의텍스트==강원랜디리스트[1]:
        a=random.randint(0,len(랜유)-1)
        강원랜디3['text']=랜유[a]
    elif 강원랜디3의텍스트==강원랜디리스트[4]:
        a=random.randint(0,len(전설리스트)-1)
        b=random.randint(0,len(히든리스트)-1)
        강원랜디3['text']=전설리스트[a]+" "+히든리스트[b]
    elif 강원랜디3의텍스트==강원랜디리스트[6]:   
        a=random.randint(10,30)
        강원랜디3['text']="중급도박"+str(a)+"회"
def kangwon_event4():
    if 강원랜디4의텍스트==강원랜디리스트[0]:
        a=random.randint(1,10)
        강원랜디4['text']="10"+"+"+str(a)
    elif 강원랜디4의텍스트==강원랜디리스트[1]:
        a=random.randint(0,len(랜유)-1)
        강원랜디4['text']=랜유[a]
    elif 강원랜디4의텍스트==강원랜디리스트[4]:
        a=random.randint(0,len(전설리스트)-1)
        b=random.randint(0,len(히든리스트)-1)
        강원랜디4['text']=전설리스트[a]+" "+히든리스트[b]
    elif 강원랜디4의텍스트==강원랜디리스트[6]:   
        a=random.randint(10,30)
        강원랜디4['text']="중급도박"+str(a)+"회"
#원딜전 버튼 이벤트
def one():
    a=random.randint(0,len(원딜전리스트)-1)
    원딜전1['text']=원딜전리스트[a]

#이캐릭들필수에요 버튼 이벤트
def leg():
    전설목록['text']=전설리스트[0]+" "+전설리스트[1]+" "+전설리스트[2]+" "+전설리스트[3]+" "+전설리스트[4]+" "+전설리스트[5]+" "+전설리스트[6]
def hid():
    히든목록['text']=히든리스트[0]+" "+히든리스트[1]+" "+히든리스트[2]+" "+히든리스트[3]+" "+히든리스트[4]+" "+히든리스트[5]+" "+히든리스트[6]

#너의 상위는 버튼 이벤트
def your_name1():
    a=random.randint(0,4)
    너의상위는1['text']=a
def your_name2():
    a=random.randint(0,4)
    너의상위는2['text']=a
def your_name3():
    a=random.randint(0,4)
    너의상위는3['text']=a
def your_name4():
    a=random.randint(0,4)
    너의상위는4['text']=a

#4인강제전 버튼 이벤트
def resraint_war():
    a=random.randint(0,len(강제전리스트)-1)
    강제전1['text']=강제전리스트[a]

#꼭가야할캐릭 버튼 이벤트
def necessary():
    while True:
        a=random.randint(0,len(꼭가야할캐릭리스트)-1)
        b=random.randint(0,len(꼭가야할캐릭리스트)-1)
        if a!=b:
            break
    꼭갈캐['text']=꼭가야할캐릭리스트[a]+" "+꼭가야할캐릭리스트[b]

#이벤트를 적용시킨 버튼들
강원랜디1=Button(ORD,width=20,height=4, fg="white", bg="red", text=강원랜디1의텍스트,command=kangwon_event1)
강원랜디2=Button(ORD,width=20,height=4, fg="white", bg="blue", text=강원랜디2의텍스트,command=kangwon_event2)
강원랜디3=Button(ORD,width=20,height=4, fg="black", bg="yellow", text=강원랜디3의텍스트,command=kangwon_event3)
강원랜디4=Button(ORD,width=20,height=4, fg="white", bg="purple", text=강원랜디4의텍스트,command=kangwon_event4)

전설목록=Button(ORD,width=500,height=5, fg="black", bg="white", text="눌러서 확인",command=leg)
히든목록=Button(ORD,width=500,height=5, fg="black", bg="white", text="눌러서 확인",command=hid)

원딜전1=Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 확인",command=one)

dice = Button(ORD,width=20,height=4, fg="white", bg="red", text="눌러서 결과 확인",command=dice_event1)        
dice2 = Button(ORD,width=20,height=4, fg="white", bg="blue", text="눌러서 결과 확인",command=dice_event2)              
dice3 = Button(ORD,width=20,height=4, fg="black", bg="yellow", text="눌러서 결과 확인",command=dice_event3) 
dice4 = Button(ORD,width=20,height=4, fg="white", bg="purple", text="눌러서 결과 확인",command=dice_event4)

너의상위는1 = Button(ORD,width=20,height=4, fg="white", bg="red", text="눌러서 결과 확인",command=your_name1)        
너의상위는2 = Button(ORD,width=20,height=4, fg="white", bg="blue", text="눌러서 결과 확인",command=your_name2)              
너의상위는3 = Button(ORD,width=20,height=4, fg="black", bg="yellow", text="눌러서 결과 확인",command=your_name3) 
너의상위는4 = Button(ORD,width=20,height=4, fg="white", bg="purple", text="눌러서 결과 확인",command=your_name4)

강제전1=Button(ORD,width=15,height=4, fg="black", bg="white", text="눌러서 확인",command=resraint_war)

꼭갈캐=Button(ORD,width=30,height=4, fg="black", bg="white", text="눌러서 확인",command=necessary)
     
def rule_button_click_event():
    a=random.randint(1,7)
    if a==1:
            button['text']="지츠다이스룰"
            지츠다이스1 = Button(ORD,width=20,height=4, fg="black", bg="white", text=b)
            지츠다이스1.place(x=120,y=300)
            지츠다이스1.pack(padx=60,pady=60)
            지츠다이스2 = Button(ORD,width=20,height=4, fg="black", bg="white", text=c)
            지츠다이스2.place(x=240,y=300)
            지츠다이스2.pack(padx=60,pady=60)
            지츠다이스3 = Button(ORD,width=20,height=4, fg="black", bg="white", text=d)
            지츠다이스3.place(x=360,y=300)
            지츠다이스3.pack(padx=60,pady=60)
            지츠다이스4 = Button(ORD,width=20,height=4, fg="black", bg="white", text=e)
            지츠다이스4.place(x=480,y=300)
            지츠다이스4.pack(padx=60,pady=60)   
            dice.place(x=120,y=300)
            dice.pack(side="left") 
            dice2.place(x=240,y=300)
            dice2.pack(side="left")      
            dice3.place(x=360,y=300)
            dice3.pack(side="left")  
            dice4.place(x=480,y=300)
            dice4.pack(side="left")                    

    elif a==2:
        button['text']="강원랜디"
        강원랜디1.place(x=100,y=300)  
        강원랜디1.pack(padx=60,pady=60)
        강원랜디2.place(x=300,y=300)
        강원랜디2.pack(padx=60,pady=60)
        강원랜디3.place(x=500,y=300)   
        강원랜디3.pack(padx=60,pady=60)
        강원랜디4.place(x=700,y=300)
        강원랜디4.pack(padx=60,pady=60)
        
    elif a==3:
        button['text']="원딜전"
        원딜전1.place(x=120,y=300)
        원딜전1.pack(padx=60,pady=60)
    elif a==4:
        button['text']="이캐릭들필수에요"
        전설목록.place(x=120,y=300)
        전설목록.pack(padx=60,pady=60)
        히든목록.place(x=240,y=300)
        히든목록.pack(padx=60,pady=60)
    elif a==5:
        button['text']="너의상위는"
        너의상위는1.place(x=120,y=300)
        너의상위는1.pack(padx=60,pady=60)
        너의상위는2.place(x=240,y=300)
        너의상위는2.pack(padx=60,pady=60)
        너의상위는3.place(x=360,y=300)
        너의상위는3.pack(padx=60,pady=60)
        너의상위는4.place(x=480,y=300)
        너의상위는4.pack(padx=60,pady=60)
    elif a==6:
        button['text']="4인강제전"
        강제전1.place(x=120,y=300)
        강제전1.pack(padx=60,pady=60)
    else:
        button['text']="꼭가야할캐릭"
        꼭갈캐.place(x=120,y=300)
        꼭갈캐.pack(padx=60,pady=60)


button = Button(ORD,width=15,height=5, fg="black", bg="white", text='룰 뽑기',command=click_event)
button.pack(padx=60,pady=60)
ORD.mainloop()