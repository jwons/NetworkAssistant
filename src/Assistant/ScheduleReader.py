'''
Created on Aug 20, 2017

@author: Wonsil
'''
import csv 
import datetime

class ScheduleReader(object):
    
    def __init__(self):
        #This variable will hold the survey schedule that will be read in from a file each time
        #the program is run. It is a dict object where the day of the month is the key to
        #the building that is to be surveyed
        self.surveySchedule = {}
        
        #This variable will hold the closet schedule that will be read in from a file each time
        #the program is run.It is a dict object where the day of the month is the key to
        #the closet that is to be checked
        self.closetSchedule = {}
        
        #Use a csvreader to then loop through the csv and then add each
        #row to the schedule so that the day of the month is the key to the building
        with open('schedule.csv','rU') as surveyFile:
            surveyReader = csv.reader(surveyFile)
            for row in surveyReader:
                self.surveySchedule[row[0]] = [row[1], row[2]]
        
        with open('closets.csv','rU') as closetFile:
            closetReader = csv.reader(closetFile)
            for row in closetReader:
                self.closetSchedule[row[0]] = row[1]
        
        #This variable holds a string of the day of the month to be a key to the closet or survey that needs
        #to be checked
        self.dayOfTheMonth = str(datetime.datetime.today().day)

    def getSurveyOfDay(self):
        return self.surveySchedule[self.dayOfTheMonth]
    
    def getClosetOfDay(self):
        return self.closetSchedule[self.dayOfTheMonth]