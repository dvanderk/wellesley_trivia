# Dee van der Knaap and Molly Hoch
# CS 111 Final Project
# Wellesley Trivia Adventure

import Tkinter as tk
import os
import random
import animation

WIDTH, HEIGHT = 1200,800
SPEED = 4

# makes it possible for the character to stop at all
TOLERANCE = 5000
# list of places
places = ["ScienceCenter", "StoneDavis", "HoughtonChapel", "AcademicQuad", "ClappLib", "Davis Museum", "LuluWang", "LastPosition"]  
# list of coordinates
# these are for laptops
coords = [(395, 150), (395, 285), (290, 175), (230, 125), (245, 265), (115, 170), (215, 85), (0,0)]
# these are for desktops
coords2 = [(790, 300), (790, 570), (580, 350), (460, 250), (495, 530), (230, 340), (430, 170), (0,0)]


class OpeningScreen(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self)
        self.awaitingToClick = True
        self.root=root
        root.title('The Wellesley Trivia Adventure')
        self.grid()
        self.createWidgets()


    def createWidgets(self): 
        # set the opening photo on the screen
        titleLabel = tk.Label(self, text = 'Welcome to the Wellesley Trivia Adventure!',
        fg = 'red', font = 'Helvetica 16 bold italic')
        titleLabel.grid(row = 0, columnspan = 2)
        pic = tk.PhotoImage(file = "WellesleyOpeningPic.gif")
        imageLabel = tk.Label(self, image=pic, borderwidth = 0)
        imageLabel.pic = pic
        imageLabel.grid(row = 1, columnspan = 2)
        titleLabel = tk.Label(self, text='Wellesley Trivia!', bg='white', font='Helvetica 24')

        # create a button to move into the game from the opening screen
        # sets the game up for a laptop user
        # with proportions roughly half that of the desktop user
        self.enterButton = tk.Button(self, text = 'Enter the Game Laptop Version', command=self.onEnterButtonClick)
        self.enterButton.grid(row = 1, column = 1, sticky = tk.S + tk.W)
        
        # creates a button to move into the game from the opening screen
        # sets the game up for a desktop user
        self.enterButton2 = tk.Button(self, text = 'Enter the Game Desktop Version', command = self.onEnter2ButtonClick)
        self.enterButton2.grid(row=1,column=2, sticky=tk.S+tk.W)
        
        self.quitButton = tk.Button(self, text = 'Quit', command = self.onQuitButtonClick)
        self.quitButton.grid(row=1, column =3, sticky=tk.S+ tk.E)
    
    # creates a frame with the pick your character screen, set up for a laptop
    def onEnterButtonClick(self):
        newThing = PickYourCharacter(self.root,'laptop')
        newThing.pack()
        self.destroy()
    
    # creates a frame with the pick your character screen, set up for a desktop
    def onEnter2ButtonClick(self):
        newThing = PickYourCharacter(self.root,'desktop')
        newThing.pack()
        self.destroy()
        
    def onQuitButtonClick(self):
        root.destroy()
        
        
class PickYourCharacter(tk.Frame):
    '''Creates a GUI where a player can select a character'''
    def __init__(self, root,compType):
        tk.Frame.__init__(self)
        self.root=root
        self.compType =compType
        root.title('You\'re ready to pick your character!')
        self.grid()
        
        # a list of pictures corresponding to each potential character
        self.pictures = ['','rhys.gif','wanda.gif','wendy.gif']
        
        # a list of pictures corresponding to each potential character, made smaller for laptops
        self.smallPictures=['','rhys_small.gif','wanda_small.gif','wendy_small.gif']
        
        # a list of captions corresponding to each potential character
        self.captions = ['welcome','Rhys!','Wanda!','Wendy!']
        
        # variable that will be used to get the player's choice 
        self.picChoice = tk.IntVar()
     
        self.createWidgets()
        
    def createWidgets(self):
             
        # Image and Title
        pic = tk.PhotoImage(file='') # left blacnk until character is selected
        
        self.iLabel = tk.Label(self,image=pic,borderwidth=3)
        self.iLabel.pic = pic
        self.iLabel.grid(row=1,column=1,columnspan=3,rowspan=3,sticky=tk.N+tk.E+tk.S+tk.W)
        
        titleLabel = tk.Label(self, text='Pick your character:', fg='red',bg='white', font='Helvetica 26 bold italic')
        titleLabel.grid(row=0,column=2,sticky=tk.N+tk.E+tk.S+tk.W)
 
        leftLabel = tk.Label(self, text=' ', bg='white')# adding some space on left side
        leftLabel.grid(row=0,column=0,sticky=tk.N+tk.E+tk.S+tk.W)
        
        # Status Label
        # left blank until character is picked, then appears below the photo
        self.results = tk.StringVar()
        self.resultsLabel = tk.Label(self, fg='blue', font='Verdana 14 italic', textvariable=self.results)
        self.resultsLabel.grid(row=4,column=2)
        self.results.set('')
        
        # Choose Again
        # left blank until character is picked
        self.chooseAgain = tk.StringVar()
        self.chooseAgainLabel = tk.Label(self, fg='blue', font='Helvetica 14', textvariable=self.chooseAgain)
        self.chooseAgainLabel.grid(row=5,column=2)
        self.chooseAgain.set('')
        
        # Radio buttons
        # player uses these to select a character
        
        rhys = tk.Radiobutton(self, text='Rhys',value=1, variable=self.picChoice)
        rhys.grid(row=6,column=1)
        
        wanda = tk.Radiobutton(self,text='Wanda',value=2, variable=self.picChoice)
        wanda.grid(row=6,column=2)
        
        wendy = tk.Radiobutton(self, text='Wendy',value=3, variable=self.picChoice)
        wendy.grid(row=6,column=3)       
        
        # Change picture button
        
        changeButton = tk.Button(self, text = 'Pick Character',command=self.onChangeButtonClick)
        changeButton.grid(row=7,column=2)
         
        # Quit Button        
        quitButton = tk.Button(self, text='Quit', command=self.onQuitButtonClick)
	quitButton.grid(row=7,column=5)
	
	
     
     # Add any more functions that you need here
     
    def onQuitButtonClick(self):
        root.destroy()
    
    def onChangeButtonClick(self):
        self.choice = self.picChoice.get()
        if self.compType == 'desktop':
            self.character = self.pictures[self.choice]
        else:
            self.character = self.smallPictures[self.choice]
        
        newpic=tk.PhotoImage(file=self.character)
        
        # Create Move On Button
        moveOnButton = tk.Button(self, text='Start Game', command=self.onMoveButtonClick)
        moveOnButton.grid(row=7, column=3)
        
        self.iLabel.configure(image=newpic)
        self.iLabel.image = newpic
        self.results.set('You chose ' + self.captions[self.choice])
        self.chooseAgain.set('Pick another character or press "Start Game".')
    
    def onMoveButtonClick(self):
        if self.compType == 'laptop':
            newThing2 = WellesleyGameApp(self.root,self.character,'laptop')
        else:
            newThing2 = WellesleyGameApp(self.root,self.character,'desktop')
        newThing2.pack()
        self.destroy()

class QuestionsAndChoices:

    def __init__(self, filename):
        self.questionsAndChoices = []
        in_file = open(filename, 'r')
        lines = in_file.readlines()
        for line in lines:
            newLine = line.strip('\n').split('\t')
            answerList=[]
            for i in range(2,5):
                answerList.append(newLine[i]) # remove trailing newline
            self.questionsAndChoices.append((newLine[0],newLine[1],answerList))
        in_file.close()
        
        
    def getTitle(self,questionNumber):
        return self.questionsAndChoices[questionNumber-1][0]
    
    def getQuestion(self, questionNumber):
        return self.questionsAndChoices[questionNumber-1][1]
    
    def getChoices(self, questionNumber):
        return self.questionsAndChoices[questionNumber-1][2]
    
class Icon(animation.AnimatedObject):
    # create the animated object over the map
    
     def __init__(self,canvas,character,currentIndex,isMoving,compType):
         self.CurrentIndex = currentIndex
         self.character = character
         self.compType = compType
         if self.compType=='laptop':
             self.coords=coords
         else:
             self.coords=coords2
         self.NextPosition = self.coords[self.CurrentIndex+1]
         self.CurrentPosition = self.coords[self.CurrentIndex]
         self.x = self.CurrentPosition[0]
         self.y = self.CurrentPosition[1]
         self.canvas = canvas
         self.character = tk.PhotoImage(file = self.character) # image variable is newpic from pickYourCharacter file
         self.displayCharacter = self.character.subsample(2,2)
         self.id = self.canvas.create_image(self.CurrentPosition[0], self.CurrentPosition[1], image = self.displayCharacter)
         #self.moving = True
         self.moving = isMoving
         
    
     def move(self):
         #print str((self.x - self.NextPosition[0])*(self.x - self.NextPosition[0])+(self.y - self.NextPosition[1])*(self.y - self.NextPosition[1]))
         if (self.x - self.NextPosition[0])*(self.x - self.NextPosition[0])+(self.y - self.NextPosition[1])*(self.y - self.NextPosition[1]) < TOLERANCE:
             self.moving = False
             
         if self.moving:
             self.canvas.move(self.id, ((self.NextPosition[0] - self.CurrentPosition[0])/100), ((self.NextPosition[1] - self.CurrentPosition[1])/100))
             self.x +=((self.NextPosition[0] - self.CurrentPosition[0])/100)
             self.y += ((self.NextPosition[1] - self.CurrentPosition[1])/100)

         if self.CurrentIndex >= len(self.coords):
             return "The Game is Over"
         else:
             self.CurrentIndex += 1 # update index of the list
             
        
#         
        

class WellesleyGameApp(tk.Frame):

    def __init__(self, root,character, compType):
        tk.Frame.__init__(self, root)            
        self.root = root       
        self.character = character 
        self.root.title("Are You A True Wendy Wellesley?")
        self.QA = QuestionsAndChoices('questions.txt')
        self.pack()
        self.compType = compType
        if self.compType == 'laptop':
            self.width=WIDTH/2
            self.height=HEIGHT/2
            self.photo = 'wesleyan.gif'
        else:
            self.width =WIDTH
            self.height=HEIGHT
            self.photo='wellesley_map.gif'
        self.totalNumberOfQuestions = 7 
        
        self.numberOfAnswers = 3
        
        self.currentQuestionNumber = 1 
        
        self.numberAnsweredCorrectly = 0
        
        #self.indexOfCurrentQuestion = self.currentQuestionNumber-1
        
        self.awaitingUserToSubmitAnswer = True
        
        self.createWidgets()
        
    def createWidgets(self):
        self.canvas = animation.AnimationCanvas(self,width=self.width,height=self.height)
        
        self.im = tk.PhotoImage(file=self.photo)
        
        self.canvas.create_image(self.width/2,self.height/2,image=self.im) #this is the center

        self.canvas.pack()
        
        self.iconOne = Icon(self.canvas,self.character,self.currentQuestionNumber-1,False,self.compType)
        self.canvas.addItem(self.iconOne)
        self.canvas.start()
        
        # Question
        self.question = tk.StringVar()
        questionLabel = tk.Label(self, fg='blue', font='Times 14', textvariable=self.question)
        questionLabel.pack()
        self.setQuestion()  # Set text of question
        
        # Answers
        self.answerIndex = tk.IntVar()  # Index of selected radiobutton
        # List of StringVars, one for each radiobutton. 
        # Each list element allows getting/setting the text of a radiobutton.
        self.answerTexts = []  
        for i in range(0,3):
            self.answerTexts.append(tk.StringVar())
        self.rbs = []  
        for i in range(len(self.answerTexts)):  # Create radiobuttons
            rb = tk.Radiobutton(self, fg='red', textvariable=self.answerTexts[i],\
            variable=self.answerIndex,value=i)
            rb.pack()
            self.rbs.append(rb)
        self.setAnswers()  # Set text of radiobuttons
        
        # Status Label
        self.results = tk.StringVar()
        self.resultsLabel = tk.Label(self, fg='brown', font='Times 14 italic', \
        textvariable=self.results)
        self.resultsLabel.pack()
        
        # Submit Button
        self.submitButton = tk.Button(self, text='Submit', command=self.onSubmitButtonClick)
        self.submitButton.pack()

        # Quit Button        
        quitButton = tk.Button(self, text='Quit', command=self.onQuitButtonClick)
        quitButton.pack()
        
        self.canvas.start()
    
    def setQuestion(self):
        self.question.set('Stop ' + str(self.currentQuestionNumber) + ' out of ' \
        + str(self.totalNumberOfQuestions) +'--'+\
        str(self.QA.getTitle(self.currentQuestionNumber))+ '.\n' + \
        self.QA.getQuestion(self.currentQuestionNumber)) 
    
    def setAnswers(self):
        '''Populates the answer radiobuttons in a random order 
        with the correct answer as well as random answers.'''
        answers = []  # List of possible answers
        choices = self.QA.getChoices(self.currentQuestionNumber)
        answers.append(choices[0])  # Add correct answer to list
        answers.append(choices[1])
        answers.append(choices[2])
        random.shuffle(answers)  # Randomly shuffle answer list
        for i in range(0, len(answers)):  # Populate text of radiobuttons
            self.answerTexts[i].set(answers[i])
            self.rbs[i].deselect()      # deselect the radiobuttons
    def onSubmitButtonClick(self):
        
        '''dictates what is executed when player clicks the submit button'''
        # Invariant: self.awaitingUserToSubmitAnswer is True when button has 
        #   label 'Submit' and is False when button has label 'Next'
        
        if self.awaitingUserToSubmitAnswer:
            
            # the correct answer is always the first in the list
            correctAnswer = self.QA.getChoices(self.currentQuestionNumber)[0]
            
            # this gets which answer the player picked
            userAnswer = self.answerTexts[self.answerIndex.get()].get()
            
            # if the answer is correct, gives player positive feedback
            if correctAnswer == userAnswer:
                self.results.set("Correct!")
                self.numberAnsweredCorrectly += 1 # Increment correct score
                
            # if incorrect, provides player with the correct answer
            else:
                self.results.set("Incorrect: the correct answer is " + correctAnswer)
                
            # if there are more questions, changes 'Submit' to 'Next'
            if self.currentQuestionNumber<self.totalNumberOfQuestions:
                self.submitButton.config(text="Next") # Change "Submit" button to "Next"
                
            # if there are no more questions, changes 'Submit' to 'Finish Game'
            else:
                self.submitButton.config(text='Finish Game')
            self.awaitingUserToSubmitAnswer = False
            
        elif self.currentQuestionNumber < self.totalNumberOfQuestions: 
            # User has pressed Next button when game not over
            
            # removes previous icon if possible
            try:
                self.canvas.removeItem(self.iconTwo)
            except AttributeError:
                pass
            
            # adds a moving icon so character can go from place to place
            self.iconTwo = Icon(self.canvas,self.character,self.currentQuestionNumber-1,True,self.compType)
            self.canvas.addItem(self.iconTwo)
            
            self.currentQuestionNumber += 1 # Increment question number
            self.setQuestion() # Populate text of question
            self.setAnswers() # Populate text of answer radiobuttons
            self.results.set('') # Clear status label
            self.submitButton.config(text="Submit") # Change "Next" button to "Submit"
            self.awaitingUserToSubmitAnswer = True
            
        else:
            
            # if the user did well, they will see a picture of ice cream!
            if self.numberAnsweredCorrectly>3:
                finalScreen = Screen(self.root,True,self.width,self.height)
                finalScreen.pack()
                self.destroy()
                
            # if the user did poorly, they go in the lake :(
            else:
                finalScreen = Screen(self.root, False,self.width,self.height)
                finalScreen.pack()
                self.destroy()
                 
    def onQuitButtonClick(self):
        root.destroy()

class Screen(tk.Frame):
    '''Creates the final game screen'''
    
    def __init__(self, root, win,width,height):
        
        tk.Frame.__init__(self, root)
        
        # sets whether or not user won
        self.win=win
        
        # gets the width and height depending on user's screen size
        self.width = width
        self.height= height
        self.root = root
        root.title('Game Over')
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        
        # the user gets ice cream if she wins - Yay!
        if self.win:
            self.picName = 'dinoCrunch.gif'
            self.titleLabel = tk.Label(self, text = 'You did very well! You get '+\
            'a big scoop of ice cream in Lulu!',
            fg = 'red', font = 'Helvetica 16 bold italic')

        # the user has to go for a swim in the chemically-infested Lake Waban
        # if she loses--not yay
        else:
            self.picName = 'lakeWaban.gif'
            self.titleLabel = tk.Label(self, text = 'This did not go well for you.' +\
            ' You must take a dip in Lake Waban.',
            fg = 'red', font = 'Helvetica 16 bold italic')
    
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.im = tk.PhotoImage(file = self.picName)
        self.canvas.create_image(self.width/2,self.height/2, image = self.im)
        self.canvas.pack()
        self.titleLabel.pack()
     
        

root = tk.Tk()
app = OpeningScreen(root)
# For Macs only: Bring root window to the front
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

app.mainloop()