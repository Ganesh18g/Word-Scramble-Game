import tkinter as tk
import random
from tkinter import messagebox


# Window creation
root = tk.Tk()
root.config(bg="#3F045C",bd=15,relief='ridge')
root.title("Word Scramble Game")
root.geometry('700x650')
root.bell()


# Arrangement of Frames
frame1 = tk.Frame(root,height=250,width=200,bg="#3F045C")
frame1.pack(pady=10)

frame2 = tk.Frame(root,height=200,width=200,bg="#3F045C")
frame2.pack(pady=10)

frame3 = tk.Frame(root,height=200,width=200,bg="#3F045C")
frame3.pack(pady=10,side='top')

frame4 = tk.Frame(root,height=200,width=200,bg="#3F045C")
frame4.pack(pady=10)


# Variable declaration
score = 0
click = 0
hintLetters = ""


# Labels
heading = tk.Label(frame1,text=f'Find The Word      ',font=('Times New Roman',20,'bold'),fg="#ddf070",bg="#3F045C")
heading.grid(padx=10,pady=15,row=0,column=0)

scoreLabel = tk.Label(frame1,text=f'◈Score {score:03d}',font=('Times New Roman',20,'bold'),fg="#FF4A2A",bg="#3F045C")
scoreLabel.grid(padx=10,pady=15,row=0,column=1)

resultLabel = tk.Label(frame4,text='',font=('Times New Roman',20,'bold'),bg='#3F045C')
resultLabel.grid(row=1,column=0,columnspan=4,padx=10,pady= 15)
    
lettersLabel = tk.Label(frame1,text="",font=('Times New Roman',20,'bold'),fg='#0ffaa0',bg="#3F045C")
lettersLabel.grid(padx=10,pady=15,row=1,column=0,columnspan=2)

hintLabel = tk.Label(frame3,text= "",font=('Times New Roman',20,'bold'),fg="#d9ff00",bg="#3F045C",)
hintLabel.grid(padx=10,row=0,column=1,columnspan=2)


#EntryBox
entryBox = tk.Entry(frame1,font=('Times New Roman',24,'bold'),bg="#61c9e9",bd=5,relief='ridge')
entryBox.grid(padx=10,pady= 15,row=2,column=0,columnspan=2)

# List of word almost 150
wordsList = [ "APPLE","TRAIN","CHAIR","HOUSE","TIGER","RIVER","PLANT","BREAD","BEACH","BICYCLE","DIAMOND",
    "RAINBOW","PENGUIN","LAPTOP","LIBRARY","KITCHEN","GREEN","MUSIC","PIZZA",
    "JOURNEY","TEACHER","DOLPHIN","BUTTERFLY","ADVENTURE","CHOCOLATE","FRIENDSHIP",
    "NEWSPAPER","COMMUNICATION","MATHEMATICS","PROGRAMMING","MANGO","CLOCK","BRUSH",
    "MOUSE","SHIRT","TABLE","ZEBRA","LIGHT","STONE","SMILE","GLASS","BALLOON","AIRPORT",
    "CRICKET","RECTANGLE","ELEPHANT","YELLOW","TEMPERATURE","LOYAL","BLUEPRINT","NOTE",
    "TREE","PROJECT","BOTTLE","ELEMENT","ANIME","WEBSERIES","MOVIES","CARTOON","DOOR","EARTH",
    "ROCKET","LOCK","KEY","BAG","MIRROR","SWEET","MADAM","TOGETHER","PLAN","LUCK",
    "QUEEN","BOX","TOWER","PHONE","BRIGHT","BLANKET","EXAM","BENCH","TAPE","FLOWER","WATCH","CARD",
    "PENCIL","THREAD","ORANGE","LION","LENGTH","GARDEN","BLACK","WHITE",
    "GALAXY","PYRAMID","CANDLE","BRIDGE","FOREST","DESERT","PLANET","OCEAN","VOLCANO","ISLAND",
    "CASTLE","PRINCE","PRINCESS","DRAGON","WIZARD","MAGIC","SPELL","CROWN","KINGDOM","TREASURE",
    "GUITAR","VIOLIN","DRUM","TRUMPET","DANCE","SONG","OPERA","CONCERT","MELODY","RHYTHM",
    "PYTHON","ROBOT","SERVER","NETWORK","BINARY","ALGORITHM","DATABASE","SOFTWARE","HARDWARE",
    "HOSPITAL","DOCTOR","NURSE","PATIENT","MEDICINE","SURGERY","HEALTH","CLINIC","VACCINE","BLOOD",
    "SUNSET","SUNRISE","CLOUD","STORM","THUNDER","LIGHTNING","SNOW","RAIN","WIND","WEATHER"
]


# Function Part
def next_word():
    global word,click,hintLetters
    entryBox.delete(0,tk.END)
    word = random.choice(wordsList)
    letters = "  ".join(random.sample(word,k=len(word)))
    lettersLabel.config(text=letters)
    letters = ""
    hintLabel.config(text="__  "*len(word))
    click = 0
    hintLetters = ""
    if resultLabel.cget("text") == "Nice try! Thats not correct!":
        resultLabel.config(text='',bg='#3F045C',bd=0)

# For the first word
next_word()

def clear():
    entryBox.delete(0,tk.END)
    resultLabel.config(text="",bg="#3F045C",bd=0)

def check():

    value = entryBox.get().upper().strip()
    if value == "":
        messagebox.showwarning('Warning','You should enter word!')
    elif word == value:
        global score
        score += 1
        scoreLabel.config(text=f'◈Score {score:03d}')
        wordsList.remove(word)
        if len(wordsList) == 0:
            messagebox.showinfo('Awesome','Thats great! You finished all the words ☺')
            root.destroy()
        else:
            if messagebox.askquestion(message="Wow! Thats correct \nDo you want to proceed to the next word?",title="You Got This Word",icon='info') == 'yes':
                next_word()
                hintLabel.config(text="__  "*len(word))
            else:
                score = max(0,score - 1)
                entryBox.delete(0,tk.END)
        
    else:
        root.bell()
        resultLabel.config(text="Nice try! Thats not correct!",fg='white',bg="#d40000",relief='ridge',bd=5)
        
def msg(event):
    resultLabel.config(text="",bg="#3F045C",bd=0)

def hint():
    global click,hintLetters
    hintLetters += word[click] + "  "
    hintLabel.config(text=hintLetters + "__  " * (len(word) - click - 1))
    click += 1
    if click == len(word):
        hintLetters = ""
        click = 0
        messagebox.showinfo('No hint needed!','The word was completed')
        hintLabel.config(text="__  "* len(word))


# Buttons  
submitButton = tk.Button(frame2,text='Submit ↲',font=('Times New Roman', 14),bg="#ff2146",relief='ridge',bd=5,activebackground="#ddb3f8",padx=18,command=check)
submitButton.grid(row=0,column=0,padx=20,pady=10)

resetButton = tk.Button(frame2,text='Reset ↻',font=('Times New Roman', 14),bg="#f29913",relief='ridge',bd=5,activebackground='#ddb3f8',padx=28,command=clear)
resetButton.grid(row=0,column=1,padx=20,pady=10)

nextButton = tk.Button(frame2,text='Next Word ⫸',font=('Times New Roman', 14),bg='#21fa2c',relief='ridge',bd=5,activebackground='#ddb3f8',command=next)
nextButton.grid(row=0,column=2,padx=20,pady=10)

hintButton = tk.Button(frame2,text='Hint💡',font=('Times New Roman', 14),bg="#0f8ef0",relief='ridge',bd=5,activebackground='#ddb3f8',padx=30,command=hint)
hintButton.grid(row=1,column=1,padx=20,pady=10)


# Binding Part
root.bind("<Return>",lambda e: check())
root.bind('<Key>',msg)


# mainloop excution
root.mainloop()