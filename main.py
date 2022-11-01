from tkinter import*
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# DISPLAYING THE WORDS AND MEANING
try:
   french_words= pandas.read_csv('C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 31 Capstone project/words_to_learn.csv')
except FileNotFoundError:
    print('doing the same thing') 
    french_words=pandas.read_csv('C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 31 Capstone project/data/french_words.csv')
french_words= french_words.to_dict('records')

french = None
english = None

def rando_words():
    global french
    global english
    global timer
    window.after_cancel(timer)
    rando_words.num = random.choice(french_words)
    
    french= rando_words.num['French']
    english= rando_words.num['English']
    
    
    canvas.itemconfig(language,text='French')
    canvas.itemconfig(word,text=french)
    canvas.itemconfig(canvas_image,image=front)
    timer=window.after(3000,english_func)

    
    

# SAVING WORDS

def save():
    french_words.remove( rando_words.num )
    data = pandas.DataFrame(french_words)
    data.to_csv('words_to_learn.csv',index=False)
    rando_words()

# DISPLAYING THE ENGLISH MEANING
def english_func():

    canvas.itemconfig(canvas_image,image=back)
    canvas.itemconfig(language,text='English')
    canvas.itemconfig(word,text=english)
    

#UI 
window = Tk()
window.title("FLASH LEARNER")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer=window.after(3000,english_func)
canvas =Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front = PhotoImage(file='C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 31 Capstone project/images/card_front.png')
back = PhotoImage(file='C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 31 Capstone project/images/card_back.png')
canvas_image=canvas.create_image(400,269, image = front)
canvas.grid(row=0,column=0,columnspan=2)

language = canvas.create_text(400,150,text='French',font=("Ariel",40,'italic'))

word =canvas.create_text(400,263,font=("Ariel",60,'italic'))

correct = PhotoImage(file='C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 31 Capstone project/images/right.png')
right = Button(image=correct,highlightthickness=0,command=save).grid(row=1,column=1)

wrong_img= PhotoImage(file='C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 31 Capstone project/images/wrong.png')
wrong = Button(image=wrong_img,highlightthickness=0,command=rando_words).grid(row=1,column=0)

rando_words()
window.mainloop()