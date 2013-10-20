'''
Created on 2013/08/11

@author: m4
'''
import tkinter as tk
from random import shuffle
from tkinter import messagebox
from __init__ import root, notify_on
from tkinter import *

class Purse(object):
    def __init__(self):
        self.account = 50
        
    def money_check(self):
        if self.account < 0:
            messagebox.showinfo("Broke!","You are out of money!")
            return
        if self.account - int(betbox.get()) < 0:
            messagebox.showinfo("Error","You cannot bet more than you have!")
            return
            
your_money = Purse()
        

class Suit(object):
    '''Creates a deck of 52 playing cards'''
    def __init__(self,suit):
        self.suit = suit
    type_cards = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    face_cards = ['J','Q','K','A']

clubs = Suit("clubs")
spades = Suit("spades")
hearts = Suit("hearts")
diamonds = Suit("diamonds")
deck = [clubs,spades,hearts,diamonds]

class Deck(object):
    def __init__(self):
        self.alldeck = [str(j)+'%s' % i.suit[0] for i in deck for j in i.type_cards]
        self.alldeck = [i.replace('11','J') for i in self.alldeck]
        self.alldeck = [i.replace('12','Q') for i in self.alldeck]
        self.alldeck = [i.replace('13','K') for i in self.alldeck]
        self.alldeck = [i.replace('14','A') for i in self.alldeck]

currentdeck = Deck()


class Photo(object):
    '''Establishes corresponding gifs to cards in deck'''
    def __init__(self):
        shuffle(currentdeck.alldeck)
        self.your_hand = currentdeck.alldeck[0:5]
        self.photo1 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[0])
        self.photo2 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[1])
        self.photo3 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[2])
        self.photo4 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[3])
        self.photo5 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[4])
        for i in self.your_hand:
            currentdeck.alldeck.remove(i)
    def refresh_cards(self):
        self.photo1 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[0])
        self.photo2 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[1])
        self.photo3 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[2])
        self.photo4 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[3])
        self.photo5 = tk.PhotoImage(file= r"deck\%s.gif" % self.your_hand[4])
       
handphoto = Photo()
cv = tk.Canvas(bg='slate gray',width=499,height=374)
moneybox = PhotoImage(file= r"moneybox.gif")

'''Displays the cards as checkbuttons, and draws cards'''
class Draw_cards(object):
    '''Displays the cards as checkbuttons, and draws cards'''
    def __init__(self):
        self.ChkVar1 = IntVar()
        self.ChkVar2 = IntVar()
        self.ChkVar3 = IntVar()
        self.ChkVar4 = IntVar()
        self.ChkVar5 = IntVar()     
        c1 = Checkbutton(cv,indicatoron=0, selectcolor='red', image=handphoto.photo1, variable = self.ChkVar1, \
                       onvalue=1, offvalue=0, bg='slate gray')
        c1_win = cv.create_window(30, 50, anchor='nw', window=c1)
        c2 = Checkbutton(cv,indicatoron=0, selectcolor='red', image=handphoto.photo2, variable = self.ChkVar2, \
                       onvalue=1, offvalue=0, bg='slate gray')
        c2_win = cv.create_window(110, 50, anchor='nw', window=c2)
        c3 = Checkbutton(cv,indicatoron=0, selectcolor='red', image=handphoto.photo3, variable = self.ChkVar3, \
                       onvalue=1, offvalue=0, bg='slate gray')
        c3_win = cv.create_window(190, 50, anchor='nw', window=c3)
        c4 = Checkbutton(cv,indicatoron=0, selectcolor='red', image=handphoto.photo4, variable = self.ChkVar4, \
                       onvalue=1, offvalue=0, bg='slate gray')
        c4_win = cv.create_window(270, 50, anchor='nw', window=c4)
        c5 = Checkbutton(cv,indicatoron=0, selectcolor='red', image=handphoto.photo5, variable = self.ChkVar5, \
                       onvalue=1, offvalue=0, bg='slate gray')
        c5_win = cv.create_window(350, 50, anchor='nw', window=c5)
    def drawcard(self):
        rmlist = []
        for i in self.ChkVar1,self.ChkVar2,self.ChkVar3,self.ChkVar4,self.ChkVar5:
            rmlist.append(i.get())
        for i,v in enumerate(rmlist):
            if v == 1:
                pass
            else:
                handphoto.your_hand.insert(i,currentdeck.alldeck[0])
                currentdeck.alldeck.remove(currentdeck.alldeck[0])
                handphoto.your_hand.remove(handphoto.your_hand[i+1])
        your_money.money_check()
        betting()
        handphoto.refresh_cards()
        hand_check()
        show_money()
        dealout.__init__()
        return draw.destroy()
    
dealout = Draw_cards()


def redeal():
    '''Replays the deal'''
    try:
        txtarea.destroy()
    except:
        pass
    try:
        show_winnings("")
    except:
        pass
    currentdeck.__init__()
    handphoto.__init__()
    global draw
    draw = tk.Button(text="Draw", bg='#09B554', activebackground='#09B554', command=dealout.drawcard, anchor="w")
    draw_win = cv.create_window(175, 195, anchor="nw", window= draw)
    #show_money()
    return dealout.__init__()


def hand_check():
    '''This analyzes the poker hand for value'''
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    word_cards = ["twos","threes","fours","fives","sixes","sevens","eights","nines","tens","jacks","queens","kings","aces"]

    value_assn = []
    suits = []
    str_flsh = [0,0]
    
    for i in handphoto.your_hand:
        for j in values:
            if i.startswith(j):
                value_assn.append(values.index(j)+2)
                
    value_assn.sort()
    
    '''This checks for a flush'''
    for i in handphoto.your_hand:
        suits.append(i[-1])
    
    if all(i == suits[0] for i in suits) == True:
        str_flsh.insert(0,1)
    else:
        pass   
       
    if value_assn == [2, 3, 4, 5, 14]:
        str_flsh.insert(1,2)
    else:
        pass
    
    for i in 4,3,2,1:
        if value_assn[i]-value_assn[i-1] == 1:
            pass
        else:
            break
    else:
        str_flsh.insert(1,2)
        
    if str_flsh[0]+str_flsh[1] == 3:
        your_money.account = your_money.account + int(betbox.get())*1000 + int(betbox.get())
        text_box("A straight flush.")
        show_winnings(int(betbox.get())*1000)
    elif str_flsh[1] == 2:
        your_money.account = your_money.account + int(betbox.get())*10 + int(betbox.get())
        text_box("A straight.")
        show_winnings(int(betbox.get())*10)
    elif str_flsh[0] == 1:
        your_money.account = your_money.account + int(betbox.get())*15 + int(betbox.get())
        text_box("A flush.")
        show_winnings(int(betbox.get())*15)
    else:
        pass
        
    '''This checks for duplicate cards'''
    pairs = {i:value_assn.count(i) for i in value_assn}
    pair_dict ={}
    tp = []
    fh = []

    for i in pairs:
        if pairs[i] == 1:
            pairs.update({i:0})
        if pairs[i] == 4:
            your_money.account = your_money.account + int(betbox.get())*100 + int(betbox.get())
            text_box("Four %s" % word_cards[i-2])
            show_winnings(int(betbox.get())*100)
            pairs.update({i:6})
        if pairs[i] == 3:
            fh.append(i)
            #print("You have three",word_cards[i-2])
        if pairs[i] == 2:
            tp.append(i)
            pair_dict.update({i:pairs[i]})
        else:
            pass
    
    if sum(pairs.values()) == 2:
        your_money.account = your_money.account + int(betbox.get())*1 + int(betbox.get())
        text_box("A pair of %s" % word_cards[tp[0]-2])
        show_winnings(int(betbox.get()))
    if sum(pairs.values()) == 3:
        your_money.account = your_money.account + int(betbox.get())*5 + int(betbox.get())
        text_box("Three of a kind of %s" % word_cards[fh[0]-2])
        show_winnings(int(betbox.get())*5)
        
    if sum(pairs.values()) == 4:
        your_money.account = your_money.account + int(betbox.get())*3 + int(betbox.get())
        text_box("Two pairs of %s and %s" % (word_cards[tp[0]-2],word_cards[tp[1]-2]))
        show_winnings(int(betbox.get())*3)
    if sum(pairs.values()) == 5:
        your_money.account = your_money.account + int(betbox.get())*50 + int(betbox.get())
        text_box("Full house of %s over %s" % (word_cards[fh[0]-2], word_cards[tp[0]-2]))
        show_winnings(int(betbox.get())*50)
        
    else:
        pass
        

 
def text_box(text1):
    '''This displays text to the canvas from hand_check'''
    global txtarea  
    txtarea = tk.Message(cv, bg='snow', text=text1)
    if notify_on.get() == 0:
        return
    if notify_on.get() == 1:
        pass
    cv.create_window(90,200,window=txtarea)
    
def betting():
    '''This subtracts the bet from your purse, and is called to rebind the variable.'''
    your_money.account = your_money.account - int(betbox.get())
    #betting_info = tk.Message(cv, bg='snow', text="Your current purse: %s." % your_money.account)
    #betting_info_win = cv.create_window(250, 220, window= betting_info)
    

def show_money():
    '''Shows the current money account (Test only)'''
    global show_mny
    show_mny = tk.Label(cv, image=moneybox, text="Current money: \n%s" % your_money.account, compound=tk.CENTER)
    show_mny_win = cv.create_window(400,300, window= show_mny)

def show_winnings(winnings):
    global show_wng
    show_wng = tk.Label(cv, image=moneybox, text="You have won: \n%s" % winnings, compound=tk.CENTER)
    show_wing_win = cv.create_window(250,300, window= show_wng)
    
'''The canvas layout'''
bg_img = PhotoImage(file= r"poker_table_5.gif")

cv.pack(side='top', fill='both', expand='yes',)
cv.create_image(0, 0, image= bg_img, anchor="nw")

'''Creates betting spinbox'''
betmsg = tk.Message(text="Your bet:", bg='snow')
betmsg_win = cv.create_window(90, 290, window=betmsg)
betbox = tk.Spinbox(values=(5, 10, 25, 50, 100, 200, 500, 1000), bg='snow', wrap=True, width=10, state='readonly')
betbox_win = cv.create_window(90, 320, window= betbox)

'''The buttons (may need to organize these)'''

draw = tk.Button(text="Draw", bg='#09B554', activebackground='#09B554', command=dealout.drawcard, anchor="w")
draw_win = cv.create_window(175, 195, anchor="nw", window= draw)

redealing = tk.Button(text="Replay", bg='#09B554', activebackground='#09B554', command=redeal, anchor="w")
redeal_win = cv.create_window(275, 195, anchor="nw", window = redealing)
root.after(100, dealout.__init__)
root.mainloop()