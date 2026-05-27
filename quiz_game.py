import pgzrun
WIDTH=1000
HEIGHT=650
questions=[]
score=0
tiem_left=10
meesage=""
game_over=False
count=0
index=0
def load_questions():
    global count,questions
    file=open("Quiz.txt","r")
    for i in file:
        questions.append((i))
        count+=1
    file.close()
def read_next_question():
    global index
    index+=1
    return questions.pop(0).split(",")


load_questions()
question=read_next_question()
print(questions)


marquee_box=Rect(0,0,1000,100)
question_box=Rect(0,0,750,150)
time_box=Rect(0,0,250,150)
answer_box_1=Rect(0,0,350,150)
answer_box_2=Rect(0,0,350,150)
answer_box_3=Rect(0,0,350,150)
answer_box_4=Rect(0,0,350,150)
skip_box=Rect(0,0,250,350)

marquee_box.move_ip(0,0)
question_box.move_ip(0,110)
time_box.move_ip(760,110)
answer_box_1.move_ip(0,270)
answer_box_2.move_ip(0,470)
answer_box_3.move_ip(400,270)
answer_box_4.move_ip(400,470)
skip_box.move_ip(760,270)
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
    meesage="Welcome to quiz game"
    meesage=meesage+f"Q:{index} of{count}"
    screen.draw.textbox(meesage,marquee_box,color="white")
    screen.draw.textbox("Skip",skip_box,color="white")
    screen.draw.textbox(str(tiem_left),time_box,color="white")
    screen.draw.textbox(question[0].strip(),question_box,color="white")
    i=1
    for j in answer_boxes:
        screen.draw.textbox(question[i].strip(),j,color="white")
        i+=1
def on_mouse_down(pos):
    i=1
    for j in answer_boxes:
        if j.collidepoint(pos):
            if i is int(question[5]):
                correct_answer()
            else:
                gameover()
        i+=1
    if skip_box.collidepoint(pos):
        skip_question()
def correct_answer():
    global score,question,tiem_left,questions
    score+=1
    if questions:
        question=read_next_question()
        tiem_left=10
    else:
        gameover()
def gameover():
    global question,tiem_left,game_over
    meesage=f"game over you got {score} questions correct"
    question=[meesage,"-","-","-","-",5]
    tiem_left=0
    game_over=True
def skip_question():
    global question,tiem_left
    if questions and not game_over:
        question=read_next_question()
        tiem_left=10
    else:
        gameover()

def update_time():
    global tiem_left
    if tiem_left:
        tiem_left-=1
    else:
        gameover()
clock.schedule_interval(update_time,1)



    

    

pgzrun.go()