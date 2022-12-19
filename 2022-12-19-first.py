from tkinter import*
import tkinter as tk,os,sys,random

#유닛 리스트
전설=["검수전설","나미전설","네코마무시","드래곤전설","라분전설","레이쥬전설","레일리전설","로우전설","루치전설","루피jet","루나메","마르코전설","모리아전설","바르톨전설","상디쿤전설","shangus(전설)","센고쿠전설","슈가","스모커","시노부전설","시저","시키전설","에이스전설","울티","제파전설","조로전설","징베전설","카르가라","코비","쿠마폭군","크래커","킹전설","토키","핸콕전설","중력검","흰수염전설","히루루크"]
히든=["미호크히든","레드포스호","레베카히든","류마히든","모비딕호","반더데켄","발라티에","방주맥심","베르고","봉쿠레히든","사보히든","시류히든","써니호","아오키지(히든)","아카히든","이완히든","캐럿","노알라히든","킨에몬히든","킬러히든","페로나히든","피셔히든","료쿠규히든"]  
제한=["레필제한","레베카제한","시노부제한","아인제한","애널제한","카타쿠리제한","크로커제한","킹제한"]
초월=["검수초월","나미초월","도플초월","로빈초월","로우초월","루치초월","루피초월","바질초월","브룩초월","사보초월","상디쿤","shangus(초월)","스네이크맨","시라호시초월","아오키지(초월)","아카이누초월","야마토초월","우솝초월","조로초월","징베초월","쵸파초월!","키드초월","키자루초월","태시기초월","프랑키초월","중력검"]
불멸=["거프ㅋㅋ불멸","드래곤불멸","레일리불멸","로져불멸","빅맘불멸","센고쿠불멸","가반불멸","시키불멸","제트불멸","카이도불멸","흰수염불멸"]
영원=["미호크영원","버기영원","비비영원","에이스영원","오뎅영원","카벤딧슈영원","핸콕영원"]
랜유=["료우기시키","미나토","바쿠야","보릉냐","유카리","좆타로","키쿄우","타츠마키","히그마"]
강원랜디리스트=["인생의 고도(7+dice)","랜유강제","노보상","천룡인","강제 전설 히든","초월 위습 버리기","중급도박(10~30)"]

main_count=0
kangwon_count1=0 #강원랜디에 쓰이는 카운트
kangwon_count2=0 #강원랜디에 쓰이는 카운트
kangwon_count3=0 #강원랜디에 쓰이는 카운트
kangwon_count4=0 #강원랜디에 쓰이는 카운트

ORD = Tk()
ORD.resizable(False, False)
ORD.title("원랜디 룰렛 프로그램")
ORD.geometry("600x1000+200+100")

#지츠 다이스룰 버튼 클릭 이벤트
def jitsu_event1():
    a=random.randint(0,len(초월)-1)
    지츠다이스1['text']=초월[a]
def jitsu_event2():
    a=random.randint(0,len(불멸)-1)
    지츠다이스2['text']=불멸[a]
def jitsu_event3():
    a=random.randint(0,len(영원)-1)
    지츠다이스3['text']=영원[a]
def jitsu_event4():
    a=random.randint(0,len(제한)-1)
    지츠다이스4['text']=제한[a]

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
    global kangwon_count1
    kangwon_count1+=1
    if kangwon_count1==1:
        강원랜디1["text"]=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
    if kangwon_count1>=2:
        if  강원랜디1["text"]==강원랜디리스트[0]:
            a=random.randint(1,10)
            강원랜디1['text']="고급도박"+"7"+"+"+str(a)
        elif 강원랜디1["text"]==강원랜디리스트[1]:
            a=random.randint(0,len(랜유)-1)
            강원랜디1['text']="강제"+" "+랜유[a]
        elif 강원랜디1["text"]==강원랜디리스트[4]:
            a=random.randint(0,len(전설)-1)
            b=random.randint(0,len(히든)-1)
            강원랜디1['text']="강제"+" "+전설[a]+" "+히든[b]
        elif 강원랜디1["text"]==강원랜디리스트[6]:   
            a=random.randint(10,30)
            강원랜디1['text']="중급도박"+str(a)+"회"
def kangwon_event2():
    global kangwon_count2
    kangwon_count2+=1
    if kangwon_count2==1:
        강원랜디2["text"]=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
    if kangwon_count2>=2:
        if 강원랜디2["text"]==강원랜디리스트[0]:
            a=random.randint(1,10)
            강원랜디2['text']="고급도박"+"7"+"+"+str(a)
        elif 강원랜디2["text"]==강원랜디리스트[1]:
            a=random.randint(0,len(랜유)-1)
            강원랜디2['text']="강제"+" "+랜유[a]
        elif 강원랜디2["text"]==강원랜디리스트[4]:
            a=random.randint(0,len(전설)-1)
            b=random.randint(0,len(히든)-1)
            강원랜디2['text']="강제"+" "+전설[a]+" "+히든[b]
        elif 강원랜디2["text"]==강원랜디리스트[6]:   
            a=random.randint(10,30)
            강원랜디2['text']="중급도박"+str(a)+"회"
def kangwon_event3():
    global kangwon_count3
    kangwon_count3+=1
    if kangwon_count3==1:
        강원랜디3["text"]=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
    if kangwon_count3>=2:
        if 강원랜디3["text"]==강원랜디리스트[0]:
            a=random.randint(1,10)
            강원랜디3['text']="고급도박"+"7"+"+"+str(a)
        elif 강원랜디3["text"]==강원랜디리스트[1]:
            a=random.randint(0,len(랜유)-1)
            강원랜디3['text']="강제"+" "+랜유[a]
        elif 강원랜디3["text"]==강원랜디리스트[4]:
            a=random.randint(0,len(전설)-1)
            b=random.randint(0,len(히든)-1)
            강원랜디3['text']="강제"+" "+전설[a]+" "+히든[b]
        elif 강원랜디3["text"]==강원랜디리스트[6]:   
            a=random.randint(10,30)
            강원랜디3['text']="중급도박"+str(a)+"회"
def kangwon_event4():
    global kangwon_count4
    kangwon_count4+=1
    if kangwon_count4==1:
        강원랜디4["text"]=강원랜디리스트[random.randint(0,len(강원랜디리스트)-1)]
    if kangwon_count4>=2:
        if 강원랜디4["text"]==강원랜디리스트[0]:
            a=random.randint(1,10)
            강원랜디4['text']="고급도박"+"7"+"+"+str(a)
        elif 강원랜디4["text"]==강원랜디리스트[1]:
            a=random.randint(0,len(랜유)-1)
            강원랜디4['text']="강제"+" "+랜유[a]
        elif 강원랜디4["text"]==강원랜디리스트[4]:
            a=random.randint(0,len(전설)-1)
            b=random.randint(0,len(히든)-1)
            강원랜디4['text']="강제"+" "+전설[a]+" "+히든[b]
        elif 강원랜디4["text"]==강원랜디리스트[6]:   
            a=random.randint(10,30)
            강원랜디4['text']="중급도박"+str(a)+"회"

#이벤트를 적용시킨 버튼들
지츠다이스1 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event1)
지츠다이스2 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event2)
지츠다이스3 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event3)
지츠다이스4 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event4)
dice = Button(ORD,width=20,height=4, fg="white", bg="red", text="눌러서 결과 확인",command=dice_event1)        
dice2 = Button(ORD,width=20,height=4, fg="white", bg="blue", text="눌러서 결과 확인",command=dice_event2)              
dice3 = Button(ORD,width=20,height=4, fg="white", bg="purple", text="눌러서 결과 확인",command=dice_event3) 
dice4 = Button(ORD,width=20,height=4, fg="black", bg="yellow", text="눌러서 결과 확인",command=dice_event4)
강원랜디1=Button(ORD,width=40,height=4, fg="white", bg="red", text="눌러서 결과 확인",command=kangwon_event1)
강원랜디2=Button(ORD,width=40,height=4, fg="white", bg="blue", text="눌러서 결과 확인",command=kangwon_event2)
강원랜디3=Button(ORD,width=40,height=4, fg="white", bg="purple", text="눌러서 결과 확인",command=kangwon_event3)
강원랜디4=Button(ORD,width=40,height=4, fg="black", bg="yellow", text="눌러서 결과 확인",command=kangwon_event4)

def rule_button_click_event():    
    global main_count
    main_count+=1
    if main_count>1:
        return
    a=random.randint(1,2)
    if a==1:
            button['text']="지츠다이스룰"
            지츠다이스1.place(x=120,y=300)
            지츠다이스1.pack(padx=60,pady=60)
            지츠다이스2.place(x=240,y=300)
            지츠다이스2.pack(padx=60,pady=60)
            지츠다이스3.place(x=360,y=300)
            지츠다이스3.pack(padx=60,pady=60)
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
        강원랜디1.pack(padx=100,pady=60)
        강원랜디2.place(x=300,y=300)
        강원랜디2.pack(padx=100,pady=60)
        강원랜디3.place(x=500,y=300)   
        강원랜디3.pack(padx=100,pady=60)
        강원랜디4.place(x=700,y=300)
        강원랜디4.pack(padx=100,pady=60)

button = Button(ORD,width=15,height=5, fg="black", bg="white", text='룰 뽑기',command=rule_button_click_event)
button.pack(padx=60,pady=60)
ORD.mainloop()