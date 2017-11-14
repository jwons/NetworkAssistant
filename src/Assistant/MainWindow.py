'''
Created on Oct 20, 2017

@author: Wonsil
'''

from Tkinter import *
import ScheduleReader
import DailyLogResource

class MainWindow(object):

    def __init__(self, master, dailyLog):
        '''
        Constructor
        '''
        #create an instance to read and write logs as well as hold the surveys of the day
        self.dailyLog = dailyLog
        surveys = ScheduleReader.ScheduleReader().getSurveyOfDay()
        self.academicSurvey = surveys[0]
        self.residenceSurvey = surveys[1]
        
        #this is the main from for the GUI of the program 
        #Populate it with greeting text
        frame = Frame(master)
        frame.pack()
        
        self.greeting = Label(frame, text="Welcome Network Support Employee!")
        self.greeting.pack()
        
        #Show the user the necessary surveys and closets based off what day it is 
        academicText = "The academic building scheduled to be surveyed today is: " + self.academicSurvey
        residenceText = "The residence hall scheduled to be surveyed today is: " + self.residenceSurvey 
        
        self.academicLabel = Label(frame, text=academicText)
        self.academicLabel.pack()
        
        #button will allow the user to log a survey they conducted
        self.academicButton = Button(frame, text="Log Academic Survey", command=self.academicEntry)
        self.academicButton.pack()
        
        self.residenceLabel = Label(frame, text=residenceText)
        self.residenceLabel.pack()

        #button will allow the user to log a closet they checked
        self.residenceButton = Button(frame, text="Log Residence Hall Survey", command=self.residenceEntry)
        self.residenceButton.pack()
        
        self.reminderLabel = Label(frame, text="Always be checking RT!!")
        self.reminderLabel.pack()
        
    def academicEntry(self):
        self.userEntryWindow = Tk()
        self.userEntryWindow.bind('<Return>', self.submitAcademicEntry)
        
        instructionsLabel = Label(self.userEntryWindow, text="Who conducted this survey?")
        instructionsLabel.pack()
        
        self.userAcademicEntry = Entry(self.userEntryWindow)
        self.userAcademicEntry.pack()
        
        entryButton = Button(self.userEntryWindow, text="Submit")
        entryButton.bind('<Button-1>', self.submitAcademicEntry)
        entryButton.pack()
        
        self.userEntryWindow.mainloop()   
          
    def residenceEntry(self):
        self.residenceLabel.destroy()
        self.residenceButton.destroy()
    
    def submitAcademicEntry(self, event):
        self.dailyLog.addEntry(self.userAcademicEntry.get(), self.academicSurvey)
        self.academicLabel.destroy()
        self.academicButton.destroy()   
        self.userEntryWindow.destroy()
        