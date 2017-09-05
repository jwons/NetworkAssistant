'''
Created on Aug 20, 2017

@author: Wonsil
'''
from appJar import gui
from rtkit.resource import RTResource
from rtkit.authenticators import CookieAuthenticator
from rtkit.errors import RTResourceError

from rtkit import set_logging
import logging

import scheduleReader

if __name__ == '__main__':
    
    def showInfo(ticketNum):
        #Pull information from corresponding areas to give to the network support assistant 
        surveyInfo = "Network Support should survey " + schedule.getSurveyOfDay() + " today."
        closetInfo = "The " + schedule.getClosetOfDay() + " closet needs to be checked today"
        ticketInfo = "The number of new or open tickets owned by nsa is: " + str(ticketNum)
        
        window = gui("Network Helper", "400x200")
        window.setBg("grey")
        window.addLabel("Title", "Welcome Network Support Employee")
        window.setLabelBg("Title", "grey")
         
        window.addLabel("surveyInfo", surveyInfo)
        window.setLabelBg("surveyInfo", "grey")
         
        window.addLabel("closetInfo", closetInfo)
        window.setLabelBg("closetInfo", "grey")
        
        window.addLabel("ticketInfo", ticketInfo)
        window.setLabelBg("ticketInfo", "grey")
         
        window.go()
        
    def attemptLogin(u,p):
        set_logging('debug')
        logger = logging.getLogger('rtkit')
        resource = RTResource('https://help.carthage.edu/rt/REST/1.0/', u, p, CookieAuthenticator)
        
        #attempt to verify the validity of the login by trying to pull down ticket 1, this doesnt not exist so should return a 404 error
        response = resource.get(path="ticket/1")
        
        #if it does not work, display a message warning the user of their incorrect login
        if response.status_int != 404:
            badLogin = gui("Bad Login Window", "400x200")
            badLogin.setBg("grey")
            badLogin.setFont(20)
            badLogin.addLabel("message", "Incorrect Credentials")
            badLogin.go()
        else:
            response = resource.get(path="search/ticket?query=Owner='nsa'AND(Status='open'ORStatus='new')")
            if response.parsed.__len__() > 0:
                ticketNum = response.parsed[0].__len__()
            else:
                ticketNum = 0
            showInfo(ticketNum)
            
    #This function executes when the user presses submit on the program 
    def press(button):
        if button == "Cancel":
            login.stop()
        else:
            user = login.getEntry("Username")
            pasw = login.getEntry("Password ")
            login.stop()
            attemptLogin(user,pasw)
                        
    #Create a scheduleReader object that will read in the closet and survey schedules so that
    #we can get them from it later
    schedule = scheduleReader.scheduleReader()
    
    #create the gui that will login so we can authenticate into RT 
    login = gui("Login Window", "400x200")
    login.setBg("grey")
    login.setFont(16)

    login.addLabel("title", "Please enter your network credentials")
    login.setLabelBg("title", "grey")
    
    login.addLabelEntry("Username")
    login.addLabelSecretEntry("Password ")
    
    login.addButtons(["Submit", "Cancel"], press)
    
    login.setFocus("Username")

    login.go()
    
    

