from tkinter import *

root = Tk()

title = Label(root, text="BMR and TDEE Calculator")
title.grid(row=0, column=1)

# BMR formulas, TDEE calculation, and output strings
def i_malebmr(w, h, a, al):
    bmr = (66 + (6.2*w) + (12.7*h) - (6.76*a))
    tdee = bmr * al
    bmrResult = Label(root, text=bmr)
    bmrResult.grid(row=11, column=1)
    tdeeResult = Label(root, text=tdee)
    tdeeResult.grid(row=12, column=1)


def m_malebmr(w, h, a, al):
    bmr = (66.5 + (13.75*w) + (5.003*h) - (6.775*a))
    tdee = bmr*al
    bmrResult = Label(root, text=bmr)
    bmrResult.grid(row=11, column=1)
    tdeeResult = Label(root, text=tdee)
    tdeeResult.grid(row=12, column=1)


def i_femalebmr(w, h, a, al):
    bmr = (655 + (4.35*w) + (4.7*h) - (4.7*a))
    tdee = bmr*al
    bmrResult = Label(root, text=bmr)
    bmrResult.grid(row=11, column=1)
    tdeeResult = Label(root, text=tdee)
    tdeeResult.grid(row=12, column=1)


def m_femalebmr(w, h, a, al):
    bmr = (655 + (9.563*w) + (1.850*h) - (4.676*a))
    tdee = bmr*al
    bmrResult = Label(root, text=bmr)
    bmrResult.grid(row=11, column=1)
    tdeeResult = Label(root, text=tdee)
    tdeeResult.grid(row=12, column=1)

# Units selection
unitsLabel = Label(root, text="Units")
unitsLabel.grid(row=1, column=1)


def unitsI():
    global units
    units = "I"
    unitsDebug = Label(root, text=units)
    unitsDebug.grid(row=1, column=2)


def unitsM():
    global units
    units = "M"
    unitsDebug = Label(root, text=units)
    unitsDebug.grid(row=1, column=2)


imperialButton = Button(root, text="Imperial", command=unitsI)
metricButton = Button(root, text="Metic", command=unitsM)

imperialButton.grid(row=3, column=0)
metricButton.grid(row=3, column=2)

# Sex selection
sexLabel = Label(root, text="Sex")
sexLabel.grid(row=4, column=1)


def sexM():
    global sex
    sex = "M"


def sexF():
    global sex
    sex = "F"


maleButton = Button(root, text="Male", command=sexM)
femaleButton = Button(root, text="Female", command=sexF)

maleButton.grid(row=5, column=0)
femaleButton.grid(row=5, column=2)

#Weight specification
weightLabel = Label(root, text="Weight")
weightLabel.grid(row=6, column=0)

weightEntry = Entry(root, width=20)
weightEntry.grid(row=6, column=1)


def weightInput():
    global w
    w = float(weightEntry.get())


weightButton = Button(root, text="Enter", command=weightInput)
weightButton.grid(row=6, column=2)

#Height specification
heightLabel = Label(root, text="Height")
heightLabel.grid(row=7, column=0)

heightEntry = Entry(root, width=20)
heightEntry.grid(row=7, column=1)


def heightInput():
    global h
    h = float(weightEntry.get())


heightButton = Button(root, text="Enter", command=heightInput)
heightButton.grid(row=7, column=2)

#Age specification
ageLabel = Label(root, text="Age")
ageLabel.grid(row=8, column=0)

ageEntry = Entry(root, width=20)
ageEntry.grid(row=8, column=1)


def ageInput():
    global a
    a = float(ageEntry.get())


ageButton = Button(root, text="Enter", command=ageInput)
ageButton.grid(row=8, column=2)


# Physical Activity levels
activityLabel = Label(root, text="Please Specify Your Physical Activity Level")
activityLabel.grid(row=9, column=1)


def sedentaryActivity():
    global al
    al = float(1.53)


def onehourActivity():
    global al
    al = float(1.76)


def twohourActivity():
    global al
    al = float(2.25)


sedentaryButton = Button(root, text="Sedentary or Light Activity", command=sedentaryActivity)
sedentaryButton.grid(row=10, column=0)

onehourButton = Button(root, text="One Hour of Excercise Daily", command=onehourActivity)
onehourButton.grid(row=10, column=1)

twohourButton = Button(root, text="Two Hours of Excercise Daily", command=twohourActivity)
twohourButton.grid(row=10, column=2)

# Deciding which function to run
def calculate():
    global sex, units
    if "F" == sex:
        if "I" == units:
            i_femalebmr(w, h, a, al)
        else:
            m_femalebmr(w, h, a, al)
    else:
        if "I" == units:
            i_malebmr(w, h, a, al)
        else:
            m_malebmr(w, h, a, al)

bmrLabel = Label(root, text="BMR:")
bmrLabel.grid(row=11, column=0)

tdeeLabel = Label(root, text="TDEE:")
tdeeLabel.grid(row=12, column=0)

calculateButton = Button(root, text="CALCULATE", command=calculate)
calculateButton.grid(row=13, column=1)


root.mainloop()
