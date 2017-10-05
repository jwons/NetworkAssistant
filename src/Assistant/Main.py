'''
Created on Aug 20, 2017

@author: Wonsil
'''
from appJar import gui
from Assistant import ScheduleReader
from Assistant import DailyLogResource


def press(self):
    logChooser = gui("Log Chooser", "200x200")
    logChooser.addLabelEntry("Employee:")
    logChooser.addButton(schedule.getSurveyOfDay()[0],addEntry(schedule.getSurveyOfDay()[0], logChooser.getEntry("Employee:")))
    logChooser.addButton(schedule.getSurveyOfDay()[1],addEntry(schedule.getSurveyOfDay()[1], logChooser.getEntry("Employee:")))
    logChooser.go()
    
def addEntry(building, name):
    dailyLog.addEntry(name, building)
    

if __name__ == '__main__':
    #Create a ScheduleReader object that will read in the closet and survey schedules so that
    #we can get them from it later
    schedule = ScheduleReader.ScheduleReader()
    
    with DailyLogResource.DailyLogResource() as dailyLog:
    
        #Pull information from corresponding areas to give to the network support assistant 
        surveyInfo = "Network Support should survey " + schedule.getSurveyOfDay()[0] + " and " + schedule.getSurveyOfDay()[1] + " today."
        closetInfo = "The " + schedule.getClosetOfDay() + " closet needs to be checked today"
        
        dailyInfo = gui("Network Helper", "500x300")
        dailyInfo.setBg("grey")
        dailyInfo.addLabel("Title", "Welcome Network Support Employee")
        dailyInfo.setLabelBg("Title", "grey")
             
        dailyInfo.addLabel("surveyInfo", surveyInfo)
        dailyInfo.setLabelBg("surveyInfo", "grey")
        
        dailyInfo.addButton("Click to log survey", press)
             
        dailyInfo.addLabel("closetInfo", closetInfo)
        dailyInfo.setLabelBg("closetInfo", "grey")
    
        dailyInfo.go()