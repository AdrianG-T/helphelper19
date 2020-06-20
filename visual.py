from tkinter import *

root = Tk()

title = Label(root, text="BMR and TDEE Calculator")
title.grid(row=0, column=1)

x=12

# Units selection
unitsLabel = Label(root, text="Units")
unitsLabel.grid(row=1, column=1)

imperialButton = Button(root, text="Imperial")
metricButton = Button(root, text="Metic")

imperialButton.grid(row=3, column=0)
metricButton.grid(row=3, column=2)

# Sex selection
sexLabel = Label(root, text="Sex")
sexLabel.grid(row=4, column=1)

maleButton = Button(root, text="Male")
femaleButton = Button(root, text="Female")

maleButton.grid(row=5, column=0)
femaleButton.grid(row=5, column=2)

#Weight specification
weightLabel = Label(root, text="Weight", text=x, text="test")
weightLabel.grid(row=6, column=0)

weightEntry = Entry(root, width=20)
weightEntry.grid(row=6, column=1)


def weightInput():
    global w
    w = int(weightEntry.get())


weightButton = Button(root, text="Enter", command=weightInput)
weightButton.grid(row=6, column=2)


def outputTest():
    outputLabel = Label(root, text=w)
    outputLabel.grid(row=10, column=2)


outputButton = Button(root, text="output", command=outputTest)
outputButton.grid(row=9, column=2)
#Height specification
heightLabel = Label(root, text="Height\ntest test test")
heightLabel.grid(row=7, column=0)

heightEntry = Entry(root, width=20)
heightEntry.grid(row=7, column=1)

heightButton = Button(root, text="Enter")
heightButton.grid(row=7, column=2)

#Age specification
ageLabel = Label(root, text="Age")
ageLabel.grid(row=8, column=0)

ageEntry = Entry(root, width=20)
ageEntry.grid(row=8, column=1)

ageButton = Button(root, text="Enter")
ageButton.grid(row=8, column=2)

root.mainloop()