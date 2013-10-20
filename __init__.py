from tkinter import *
from tkinter import filedialog

def showhandinfo():
    newwin = Toplevel(root)
    handinfo = Message(newwin, bg='white', text="Corresponding values for the hand:\n\nStraight Flush: 1,000x\nFour of a kind: 100x\nFull House: 50x\nFlush: 15x\nStraight: 10x\nThree of a kind: 5x\nTwo Pair: 3x\nOne Pair: 1x")
    handinfo.pack()
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
    
def open_file():
    openfdialog = filedialog.askopenfile(filetypes=[("Text files","*.txt*")], mode='r', title="Choose your game.")
    
def save_file():
    savefdialog = filedialog.asksaveasfile(filetypes=[("Text files","*.txt*")],mode='w',title="Save your game.")  
    
def show_instr():
    newwin = Toplevel(root)
    instructions = Message(newwin, bg='white', padx=5, pady=5, text="To play:\n\nSelect the cards to keep, and click 'Draw' to get new cards. You can only draw once.\n\nClick 'Replay' to deal out a new hand. The object is to get as much money as possible. Have fun!")
    instructions.pack()
   
root = Tk()
root.title("Video Poker v0.10a")
root.resizable(width=False, height=False)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
#filemenu.add_command(label="Save as...", command=donothing)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

notify_on = IntVar()
optionmenu = Menu(menubar, tearoff=0)
optionmenu.add_checkbutton(label="Display Hand info", variable=notify_on)
optionmenu.add_command(label="Preferences", command=donothing)
menubar.add_cascade(label="Options", menu=optionmenu)
notify_on.initialize(1)

infomenu= Menu(menubar, tearoff=0)
infomenu.add_command(label="How to play",command=show_instr)
infomenu.add_command(label="Hand Values", command=showhandinfo)
menubar.add_cascade(label="Info", menu=infomenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command= lambda: messagebox.showinfo("About the author:","Written by Matthew Fiedor\nAll rights preserved for infinity."))
helpmenu.add_command(label="Pending", command= lambda: messagebox.showinfo("Things not yet Implemented","1: Saving game\n2: Opening/loading game\n3: Stopping 'Replay' abuse\n4: Out of money function\n5:Prettifying the GUI"))
helpmenu.add_command(label="Help", command= lambda: messagebox.showinfo("What help?","Pfft, you're on your own, man."))
menubar.add_cascade(label="Help", menu=helpmenu)

#button = Button(text="Explode", command=donothing, anchor="w")
#button_win = boo.create_window(100, 100, anchor="nw", window = button)
root.config(menu=menubar)

