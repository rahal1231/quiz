import pgzrun
WIDTH=1000
HEIGHT=650
questions=[]
def load_questions():
    file=open("Quiz.txt","r")
    for i in file:
        line=i.strip().split(",")
        q=line[0]
        o=line[1:5]
        a=line[5]
        questions.append((q,o,a))
load_questions()
print(questions)

marquee_box=Rect(0,0,1000,100)
question_box=Rect(0,0,750,150)
time_box=Rect(0,0,250,150)
answer_box_1=Rect(0,0,300,250)
answer_box_2=Rect(0,0,300,250)
answer_box_3=Rect(0,0,300,250)
answer_box_4=Rect(0,0,300,250)
skip_box=Rect(0,0,50,400)

marquee_box.move_ip(0,0)
question_box.move_ip(0,110)
time_box.move_ip(760,110)
answer_box_1.move_ip(0,370)
answer_box_2.move_ip(300,370)
answer_box_3.move_ip(0,630)
answer_box_4.move_ip(300,630)
skip_box.move_ip(600,370)
answer_boxes=[answer_box_1,answer_box_2,answer_box_3,answer_box_4]

def draw():
    screen.clear()
    screen.fill("blue")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"black")
    screen.draw.filled_rect(time_box,"black")
    screen.draw.filled_rect(skip_box,"black")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"black")

pgzrun.go()