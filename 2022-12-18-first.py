from tkinter import*
import tkinter as tk,os,sys,random

#유닛 리스트 
제한=["레필제한","레베카제한","시노부제한","아인제한","애넬제한","카타쿠리제한","크로커제한","킹제한"]
초월=["검수초월","나미초월","도플초월","로빈초월","로우초월","루치초월","루피초월","바질초월","브룩초월","사보초월","상디쿤","샹크스(초월)","스네이크맨","시라호시초월","아오키지(초월)","아카이누초월","야마토초월","우솝초월","조로초월","징베초월","쵸파초월!","키드초월","키자루초월","태시기초월","프랑키초월","중력검"]
불멸=["거프ㅋㅋ불멸","드래곤불멸","레일리불멸","로져불멸","빅맘불멸","센고쿠불멸","가반불멸","시키불멸","제트불멸","카이도불멸","흰수염불멸"]
영원=["미호크영원","버기영원","비비영원","에이스영원","오뎅영원","카벤딧슈영원","핸콕영원"]

main_count=0

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

#이벤트를 적용시킨 버튼들
지츠다이스1 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event1)
지츠다이스2 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event2)
지츠다이스3 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event3)
지츠다이스4 = Button(ORD,width=20,height=4, fg="black", bg="white", text="눌러서 결과 확인",command=jitsu_event4)
dice = Button(ORD,width=20,height=4, fg="white", bg="red", text="눌러서 결과 확인",command=dice_event1)        
dice2 = Button(ORD,width=20,height=4, fg="white", bg="blue", text="눌러서 결과 확인",command=dice_event2)              
dice3 = Button(ORD,width=20,height=4, fg="white", bg="purple", text="눌러서 결과 확인",command=dice_event3) 
dice4 = Button(ORD,width=20,height=4, fg="black", bg="yellow", text="눌러서 결과 확인",command=dice_event4)

def rule_button_click_event():    
    global main_count
    main_count+=1
    if main_count>1:
        return
    a=random.randint(1,1)
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

button = Button(ORD,width=15,height=5, fg="black", bg="white", text='룰 뽑기',command=rule_button_click_event)
button.pack(padx=60,pady=60)
ORD.mainloop()