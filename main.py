import tkinter
import os
import random
import datetime




# FUNCTIONS ARE NOT ARRANGED IN CHRONOLOGICAL ORDER

# To initialise the tkinter interface and basic details such as screen dimensions and title of application
root = tkinter.Tk()
root.title('My Typing Test')
root.geometry("1366x768")
root.configure(background="green")

# Creating and displaying the welcome text on the screen
greet = tkinter.Label(root, font=('arial', 30, 'bold'), text=" Welcome To Typing Speed Text",fg= 'white')
greet.configure(background="green")
greet.place(relx=0.5, rely=0.1, anchor="center")

# Creating and displaying the caution text on the screen
caution =tkinter.Label(root, font=('arial', 20, 'bold'), text="Please play in full screen for a better experience",fg='white')
caution.configure(background="green")
caution.place(relx=0.5, rely=0.2, anchor="center")

# This is to add a number of passages to the list of passages so a random choice could be made from them for the player
listPSG = []

listPSG.append("""
Somehow I found myself admiring the man for his lack of modesty. 
For whatis modesty but inverted pride? We all think we are first-class people.
Modesty forbids us from saying so ourselves though, presumably, not from wanting
to hear it from others. Perhaps it was their impatience with this kind of hypocrisy
that made men like Nanga successful politicians while starry-eyed idealists strove 
vaingloriously to bring into politics niceties and delicate refinements thatbelonged elsewhere.""")
listPSG.append("""
Many touch typists also use keyboard shortcuts or hotkeys when typing on a computer. This allows them 
to edit their document without having to take their hands off the keyboard to use a mouse. An example 
of a keyboard shortcut is pressing the Ctrl key plus the S key to save a document as they type, 
or the Ctrl key plus the Z key to undo a mistake. Many experienced typists can feel or sense when they 
have made an error and can hit the Backspace key and make the correction with no increase in time 
between keystrokes.""")

listPSG.append("""
Some people combine touch typing and hunt and peck by using a buffering method. In the buffer method, 
the typist looks at the source copy, mentally stores one or several sentences, then looks at the 
keyboard and types out the buffer of sentences. This eliminates frequent up and down motions with the 
head and is used in typing competitions in which the typist is not well versed in touch typing. Not 
normally used in day-to-day contact with keyboards, this buffer method is used only when time is of 
the essence. (Wikipedia)""")

listPSG.append("""
Editing is a growing field of work in the service industry. Paid editing services may be provided by 
specialized editing firms or by self-employed (freelance) editors. Editing firms may employ a team of 
in-house editors, rely on a network of individual contractors or both. Such firms are able to handle 
editing in a wide range of topics and genres, depending on the skills of individual editors. The 
services provided by these editors may be varied and can include proofreading, copy editing, 
online editing, developmental editing, editing for search engine optimization (SEO), etc.""")

listPSG.append("""
December 17, 1903, is the birth date of all airplanes. Orville and Wilbur Wright started building 
gliders in 1900. In 1903, they built a motor and propeller for their glider. Orville made the first 
flight, which lasted 12 seconds, and flew 120 feet. Wilbur's flight was 852 feet in 59 seconds. These 
first flights in 1903 were just the start of the evolution of planes. By the year 1909, Bleriot had 
crossed the English Channel. By the year 1912, a two-piece plywood fuselage was built for greater 
strength. By the 1930s, the all-metal fuselage was tried, and it soon appeared in DC3s.""")

listPSG.append("""
Medical transcription, also known as MT, is an allied health profession dealing with the process of 
transcribing voice-recorded medical reports that are dictated by physicians, nurses and other 
healthcare practitioners. Medical reports can be voice files, notes taken during a lecture, 
or other spoken material. These are dictated over the phone or uploaded digitally via the Internet or 
through smart phone apps.""")

listPSG.append("""
Our project is Typing Speed Test. This is a way to improve education 
through technology and innovation. Computer skills are required in every educational 
institution and work. Typing is the most widely used and effective method of human to 
computer connections. That's the reason why typing skills has to be introduced to education at 
early stage, as highly developed typing skills obtained at early age develop overall ability to 
get new information.  This project will provide dynamic personal instruction, placing students in 
lessons based on their current skill level and adjusting their path as their typing improves. 
Time is being saved with typing skills which allows to edit the information created almost all 
together; pointless to say,that preparation for publication in a word processor is greatly easier than on paper.""")

# This is to create the textbox input area for typing
enter = tkinter.Text(root, font=('arial', 13))
enter.configure(background="white")

# This is to initialise the 'Done typing' button so it can be accessed later for manipulation
btn = tkinter.Button()


# This function is to initialise some global variables to be used anywhere in the code
def init():
    global ourWords
    global wrWords
    global errors
    global passage

    # assigning the 'passage' variable to a random selection of a passage from the list at the beginning of the code
    passage = listPSG[random.randint(0, 5)]
    ourWords = passage.split()

    wrWords = []
    errors = 0


# This function is to check for errors in user's typing
def checkAccuracy():
    global errors
    index = 0

    loop = []

    # This conditional statement is used to check the length between user's words and original words so an appropriate
    # list can be chosen for subsequent looping to prevent an 'index out of bound error'
    if (len(userWords) < len(ourWords)):
        loop = userWords
    else:
        loop = ourWords

    # This loop is to go through all words and characters from user's typing input and comparing them with what has
    # been provided for typing so the differences could be recorded as errors for later computations and wrongly
    # typed words would be recorded as well to display to the user later in case there are any
    for word in loop:
        rtUserWord = ourWords[index]
        wrUserWord = userWords[index]
        if ourWords[index] == userWords[index]:
            index += 1
        else:
            wrWords.append(userWords[index])

            index1 = 0
            if len(ourWords[index]) < len(userWords[index]):
                for char in rtUserWord:
                    if rtUserWord[index1] == wrUserWord[index1]:
                        index1 += 1
                    else:
                        index1 += 1
                        errors += 1
                index1 = 0
            elif len(ourWords[index]) > len(userWords[index]):
                for char in wrUserWord:
                    if wrUserWord[index1] == rtUserWord[index1]:
                        index1 += 1
                    else:
                        index1 += 1
                        errors += 1
                index1 = 0
            else:
                for char in rtUserWord:
                    if rtUserWord[index1] == wrUserWord[index1]:
                        index1 += 1
                    else:
                        index1 += 1
                        errors += 1
                index1 = 0
            index += 1


# This function is mainly to take the input from the user textbox to deliver to the checkAccuracy function above
# after which it then displays the result to the user
def checkResult():
    # This is to remove the button that indicates that a person is done typing after it has been clicked.
    btn.pack()
    btn.pack_forget()

    # This is to record the time at which the person ended the typing
    endTime = datetime.datetime.now()

    # This is to get input from the user's textbox
    string = f"{enter.get('1.0', 'end-1c')}"

    # This is to create global variables so the checkAccuracy function can access them later for computations
    global userWords
    global errors

    userWords = string.split()

    # The function is being called to do the accuracy computations
    checkAccuracy()

    # Since errors have been recorded by the checkAccuracy function, further computations are being done to find the
    # percentage accuracy
    if (len(string) == 0):
        accuracy = 100
    else:
        accuracy = (((len(string) - errors) / len(string)) * 100).__round__(2)

    # This is to calculate for the time difference between the time typing started and when it ended so the words per
    # minute can be calculated
    timeElapsed = endTime - startTime

    timeElapsed = (timeElapsed.total_seconds() / 60).__round__(2)

    numOfWords = len(userWords)

    wpm = numOfWords // timeElapsed

    # This is to display a message about the end result of the user's typing input
    message = "Time= " + str(timeElapsed) + ' minutes ' + "\nSpeed= " + str(
        wpm) + ' wpm' + f'\nErrors={errors} ' + f'\nAccuracy= {accuracy}%'
    result = tkinter.Label(root, font=('arial', 30, 'bold'), text=message)
    result.configure(background="green")
    result.place(relx=0.5, rely=0.3, anchor="center")

    # This is to remove the text that was placed on the screen for typing; this is done to make room for the typing
    # result to be displayed
    displayText.pack()
    displayText.pack_forget()

  # This is to remove the textbox area so result can be displayed
    enter.pack()
    enter.pack_forget()

    # This is to figure out whether user typed all words or exceeded and displaying appropriate messages for each
    # condition. The wrong words typed would also be displayed at this stage
    if len(ourWords) > len(userWords):
        info = tkinter.Label(root, font=('arial', 20, 'bold'), text="You did not type all the words")
        info.configure(background="green")
        info.place(relx=0.5, rely=0.6, anchor="center")
    elif len(ourWords) < len(userWords):
        info = tkinter.Label(root, font=('arial', 20, 'bold'), text="You typed in excess")
        info.configure(background="green")
        info.place(relx=0.5, rely=0.65, anchor="center")
    else:
        info = tkinter.Label(root, font=('arial', 20, 'bold'), text="Well done!")
        info.configure(background="green")
        info.place(relx=0.5, rely=0.7, anchor="center")
    if len(wrWords) == 0:
        info = tkinter.Label(root, font=('arial', 20, 'bold'), text="You typed no word wrong")
        info.configure(background="green")
        info.place(relx=0.5, rely=0.75, anchor="center")
    else:
        if len(wrWords) > 1:
            info = tkinter.Label(root, font=('arial', 20, 'bold'), text=f'Your wrong words were,  {wrWords}', wraplength=1300)
            info.configure(background="green")
            info.place(relx=0.5, rely=0.75, anchor="center")
        else:
            info = tkinter.Label(root, font=('arial', 20, 'bold'), text=f'Your wrong words were,  {wrWords}')
            info.configure(background="green")
            info.place(relx=0.5, rely=0.75, anchor="center")


def play():
    # This is to make the start time variable a global one so it can be accessed from other functions and also to
    # record the current time which the typing started

    global startTime
    startTime = datetime.datetime.now()
    enter.place(relx=0.5, rely=0.6, height=300, width=900, anchor="center")
    displayText.place(relx=0.5, rely=0.15, anchor="center")

    # This is to remove the start button after it has been clicked since it wouldn't be needed anymore
    startBtn.pack()
    startBtn.pack_forget()

    # This is to remove the welcome message and caution message after typing has started
    greet.pack()
    greet.pack_forget()
    caution.pack()
    caution.pack_forget()

    # This is to make the done typing button a global variable so it can be accessed in a different function for
    # removal when it is not needed
    global btn

    btn = tkinter.Button(root, text="Done Typing", command=checkResult, bg="blue", fg="white", font=('arial', 15))
    btn.place(relx=0.5, rely=0.85, anchor="center")

    # This is to focus the cursor on the textbox area so typing can start
    enter.focus()


# This is to call the initialisation function for the program to kickstart
init()

# This is to display the text passage for user to see
passage = listPSG[random.randint(0, 5)]
displayText = tkinter.Label(root, font=('arial', 15, 'bold'), text=passage, wraplength=1360, foreground="white")
displayText.configure(background="green")

# This button is to allow user to start when they want to
startBtn = tkinter.Button(root, text=" Start Test", command=play, bg="blue", fg="white", font=('arial', 20))
startBtn.place(relx=0.5, rely=0.5, anchor="center")





# This is to keep the tkinter interface in a running loop so it doesn't end after a single displa
root.mainloop()


