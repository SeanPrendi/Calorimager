from tkinter import *
from tkinter import filedialog
from WolframAlpha import getCals
refSize = ""
food = ""
filename1 = ""
filename2 = ""
calories = ""

def setRef(canvas, width, height, refInput):
    global refSize
    refSize = refInput
    draw(canvas, width, height)

def setFood(canvas, width, height, textInput):
    global food
    food = textInput
    draw(canvas, width, height)

def getFile1(canvas, width, height):
    global filename1
    filename1 = str(filedialog.askopenfilename())
    draw(canvas, width, height)

def getFile2(canvas, width, height):
    global filename2
    filename2 = str(filedialog.askopenfilename())
    draw(canvas, width, height)

def setCals(img1, img2, refSize, food, canvas, width, height):
    global calories
    if img1 != "" and img2 != "" and refSize != "" and food != "":
        calories = getCals(img1, img2, float(refSize), food)
        numPos = calories.find(" ")
        if numPos != -1:
            calories = calories[:numPos]
        else:
            calories = ""
        draw(canvas, width, height)
    else: pass

def draw(canvas, width, height):
    global refSize
    if refSize != '':
        try:
            float(refSize)
        except ValueError:
            refSize = ''
    global food
    global filename1
    global filename2
    canvas.create_rectangle(0, 0, width, height, fill='LightCyan3')

    canvas.create_rectangle(0, height // 2 - 280, width,
                            height // 2 - 190, fill='LemonChiffon2', width=0)
    canvas.create_rectangle(0, height // 2 - 170, width,
                            height // 2 - 80, fill='LemonChiffon2', width=0)
    canvas.create_rectangle(0, height // 2 - 60, width,
                            height // 2 + 30, fill='LemonChiffon2', width=0)
    canvas.create_rectangle(0, height // 2 + 50, width,
                            height // 2 + 140, fill='LemonChiffon2', width=0)
    canvas.create_text(5, height//2 - 235, text = "reference image size: %s" % refSize, anchor=W)
    canvas.create_text(5, height // 2 - 125, text="food: %s" % food, anchor=W)
    canvas.create_text(5, height // 2 - 15, text="image1: %s" % filename1, anchor=W)
    canvas.create_text(5, height // 2 + 95, text="image2: %s" % filename2, anchor=W)
    canvas.create_text(width//2, height // 2 + 190, text="Calories:",
                       font = "arial 32 bold", fill = "red", anchor=CENTER)
    canvas.create_text(width // 2, height // 2 + 240, text=calories,
                       font="arial 32 bold", fill="red", anchor=CENTER)

    ###########
    button1 = Button(text="choose first image", command = lambda:
                getFile1(canvas, width, height), anchor=CENTER)
    button1.configure(width=20)
    canvas.create_window(width - 200, height // 2 - 15, anchor=W,
                         window=button1)
    ###########
    button2 = Button(text="choose second image", command = lambda:
                getFile2(canvas, width, height), anchor=CENTER)
    button2.configure(width=20)
    canvas.create_window(width - 200, height // 2 + 95, anchor=W,
                         window=button2)
    ############
    foodEntry = Entry()
    foodEntry.pack()
    canvas.create_window(width-5, height//2 - 125, window=foodEntry, anchor=E)
    button3 = Button(text='confirm', command = lambda:
                     setFood(canvas, width, height, foodEntry.get()))
    button3.configure(width=10)
    canvas.create_window(width - 45, height // 2 - 97, anchor=E,
                         window=button3)
    ############
    refEntry = Entry()
    refEntry.pack()
    canvas.create_window(width-5, height//2 - 235, window=refEntry, anchor=E)
    button4 = Button(text='confirm', command = lambda:
                     setRef(canvas, width, height, refEntry.get()))
    button4.configure(width=10)
    canvas.create_window(width - 45, height // 2 - 207, anchor=E,
                         window=button4)
    ############
    button5 = Button(text='Find Calories', command=lambda:
        setCals(filename1, filename2, refSize, food, canvas, width, height))
    button5.configure(width=10)
    canvas.create_window(width//2, height//2 + 160, anchor=CENTER, window=button5)




def runDrawing(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(600, 600)