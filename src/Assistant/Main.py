'''
Created on Aug 20, 2017

@author: Wonsil
'''
from appJar import gui

import scheduleReader

if __name__ == '__main__':
    #Create a scheduleReader object that will read in the closet and survey schedules so that
    #we can get them from it later
    schedule = scheduleReader.scheduleReader()
    
    #Pull information from corresponding areas to give to the network support assistant 
    surveyInfo = "Network Support should survey " + schedule.getSurveyOfDay() + " today."
    closetInfo = "The " + schedule.getClosetOfDay() + " closet needs to be checked today"
    
    dailyInfo = gui("Network Helper", "400x200")
    dailyInfo.setBg("grey")
    dailyInfo.addLabel("Title", "Welcome Network Support Employee")
    dailyInfo.setLabelBg("Title", "grey")
         
    dailyInfo.addLabel("surveyInfo", surveyInfo)
    dailyInfo.setLabelBg("surveyInfo", "grey")
         
    dailyInfo.addLabel("closetInfo", closetInfo)
    dailyInfo.setLabelBg("closetInfo", "grey")

    dailyInfo.go()
    
    

