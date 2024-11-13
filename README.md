# German-Language-Flashcards

import tkinter as tk
from tkinter import ttk
#randint helps get random integers, randomising the flashcards
from random import randint


#window is the master/parent to other widgets
window = tk.Tk()

window.geometry('600x500')
#title
window.title('German Language Flashcards')
window.config(bg='CadetBlue1')


# notebook widget
#the master for this is 'window'
notebook = ttk.Notebook(window)

# tab 1
#master for all the tabs is 'notebook'
#allows for each category to be held within one frame
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='Test your German vocabulary at a A2 level')
#.pack is needed for all widgets
label1.pack()


#flashcards are in 'touples', two sets of touples
flashcards1 = [
    (('Hallo'), ('Hello')),
    (('Danke'), ('Thank you')),
    (('Ja'), ('Yes')),
    (('Nein'), ('No')),
    (('Bitte'), ('Please')),
    (('Tschuss'), ('Bye')),
    (('Ich'), ('I')),
    (('Du'), ('You')),
    (('Nicht'), ('Not')),
    (('Hund'), ('Dog')),
    (('Katze'), ('Cat')),
    (('Haus'), ('House'))
]

# get count of word list
count1 = len(flashcards1)

def next_tab1():
    # clear the screen when you click next
    answer_label1.config(text='')
    # deletes the entry box
    entry_box1.delete(0, 15)
    # need to make global as 'german_word.config' doesn't know what 'random_word' means
    global random_word1
    # create random selection
    random_word1 = randint(0, count1-1)
    # update label with German word
    german_word1.config(text=flashcards1[random_word1][0])

def answer_tab1():
    if entry_box1.get().capitalize() == flashcards1[random_word1][1]:
        answer_label1.config(text=f'Correct! {flashcards1[random_word1][0]} is {flashcards1[random_word1][1]}')
    else:
        answer_label1.config(text=f'Incorrect! {flashcards1[random_word1][0]} is not {entry_box1.get().capitalize()}')

# label for tab1
german_word1 = tk.Label(tab1, text='', font=('Arial', 36))
german_word1.pack(pady=50)

answer_label1 = tk.Label(tab1, text='')
answer_label1.pack(pady=20)

# entry box
entry_box1 = tk.Entry(tab1, font=('Arial', 18))
entry_box1.pack(pady=20)

# create buttons
button_frame1 = tk.Frame(tab1)
button_frame1.pack(pady=20)

# padx gives space between the next button
answer_button1 = tk.Button(button_frame1, text='Answer', command=answer_tab1)
answer_button1.grid(row=0, column=0, padx=20)

next_button1 = tk.Button(button_frame1, text='Next', command=next_tab1)
next_button1.grid(row=0, column=1)

# helps run next button function
next_tab1()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='Guess the gender of the nouns, is it der, die or das?')
label2.pack(pady=10)

label21 = ttk.Label (tab2, text = 'Hint: der is Masculine, die is feminine, das is neutral')
label21.pack(pady=10)

flashcards2 = [
    (('Tisch'), ('Der')),
    (('Bett'), ('Das')),
    (('Straße'), ('Die')),
    (('Buch'), ('Das')),
    (('Geld'), ('Das')),
    (('Telefon'), ('Das')),
    (('Stuhl'), ('Der')),
    (('Sonne'), ('Die')),
    (('Himmel'), ('Der')),
    (('Essen'), ('Das'))
]

# get count of word list
count2 = len(flashcards2)

def next_tab2():
    # clear the screen when you click next
    answer_label2.config(text='')
    # deletes the entry box
    entry_box2.delete(0, 15)
    # need to make global as 'german_word.config' doesn't know what 'random_word' means
    #global variable is accessible to others
    global random_word2
    # create random selection
    random_word2 = randint(0, count2-1)
    # update label with German word
    german_word2.config(text=flashcards2[random_word2][0])

def answer_tab2():
    if entry_box2.get().capitalize() == flashcards2[random_word2][1]:
        answer_label2.config(text=f'Correct! {flashcards2[random_word2][1]} {flashcards2[random_word2][0]}')
    else:
        answer_label2.config(text=f'Incorrect!')

# label for tab2
german_word2 = tk.Label(tab2, text='', font=('Arial', 36))
german_word2.pack(pady=50)

#removes answer for next flashcard
answer_label2 = tk.Label(tab2, text='')
answer_label2.pack(pady=20)

# entry box
entry_box2 = tk.Entry(tab2, font=('Arial', 18))
entry_box2.pack(pady=20)

# create buttons
button_frame2 = tk.Frame(tab2)
button_frame2.pack(pady=20)

#answer button
answer_button2 = tk.Button(button_frame2, text='Answer', command=answer_tab2)
answer_button2.grid(row=0, column=0, padx=20)

#next button
next_button2 = tk.Button(button_frame2, text='Next', command=next_tab2)
next_button2.grid(row=0, column=1)

# helps run next button function
next_tab2()

# tab 3
tab3 = ttk.Frame(notebook)
label3 = ttk.Label(tab3, text='Learn colours in German')
label3.pack()

flashcards3 = [
    (('Rot'), ('Red')),
    (('Grün'), ('Green')),
    (('Gelb'), ('Yellow')),
    (('Blau'), ('Blue')),
    (('Rosa'), ('Pink')),
    (('Schwartz'), ('Black')),
    (('Weiß'), ('White')),
    (('Lila'), ('Purple')),
    (('Orange'), ('Orange')),
    (('Grau'), ('Grey')),
    (('Braun'), ('Brown'))
]

# get count of word list
count3 = len(flashcards3)

def next_tab3():
    # clear the screen when you click next
    answer_label3.config(text='')
    # deletes the entry box
    entry_box3.delete(0, 15)
    # need to make global as 'german_word.config' doesn't know what 'random_word' means
    global random_word3
    # create random selection
    random_word3 = randint(0, count3-1)
    # update label with German word
    german_word3.config(text=flashcards3[random_word3][0])

def answer_tab3():
    if entry_box3.get().capitalize() == flashcards3[random_word3][1]:
        answer_label3.config(text=f'Correct! {flashcards3[random_word3][0]} is {flashcards3[random_word3][1]}')
    else:
        answer_label3.config(text=f'Incorrect! {flashcards3[random_word3][0]} is not {entry_box3.get().capitalize()}')

# label for tab3
german_word3 = tk.Label(tab3, text='', font=('Arial', 36))
german_word3.pack(pady=50)

answer_label3 = tk.Label(tab3, text='')
answer_label3.pack(pady=20)

# entry box
entry_box3 = tk.Entry(tab3, font=('Arial', 18))
entry_box3.pack(pady=20)

# create buttons
button_frame3 = tk.Frame(tab3)
button_frame3.pack(pady=20)

answer_button3 = tk.Button(button_frame3, text='Answer', command=answer_tab3)
answer_button3.grid(row=0, column=0, padx=20)

next_button3 = tk.Button(button_frame3, text='Next', command=next_tab3)
next_button3.grid(row=0, column=1)

# helps run next button function
next_tab3()

# Add tabs to the notebook
notebook.add(tab1, text='Basic Vocab')
notebook.add(tab2, text='Guess the Gender')
notebook.add(tab3, text='Colours')
notebook.pack()


#code will not run without this line of code
window.mainloop()
