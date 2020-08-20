import pyautogui
import time
from time import gmtime, strftime
import string
#1920 X 1080 screen
#corporation tab in the top right corner
#place bid
#pay button is at (x=1800,y=630)
#increment (x=1630, y=630)
#edit as you wish for other screen sizes

#enter time of bid
#lay back and relax

_SCREEN_WIDTH_ = 1920
_SCREEN_HEIGHT_ = 1080

_100K_ = 100000

_H_ = 0
_M_ = 1
_S_ = 2



def getTime():
	gmtTime = strftime("%H:%M:%S", gmtime())
	gmtList = string.split(gmtTime, ':')
	h = (int(gmtList[_H_]) + 2) % 24
	m = int(gmtList[_M_])
	s = int(gmtList[_S_])
	return [h, m, s]


def click(wt=0.1):
	pyautogui.mouseDown()
	time.sleep(wt)
	pyautogui.mouseUp()
	return


def removeInactivityScreen():
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2, 710)
	click(0.5)
	time.sleep(0.5)
	return

def enterCorporationTab():
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 15, 990)
	click(0.5)
	time.sleep(0.5)
	return

def enterWorkerTab():
	enterCorporationTab()
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 175, 360)
	click(0.5)
	time.sleep(0.5)
	return

def increaseWorkerBid(sum):
	bid = 0;
	enterWorkerTab()
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 175, 760)
	
	while(bid < sum):
			click(0.05)
			if (bid < _100K_):
				bid = bid + 1000
			elif (bid < 250000):
				bid = bid + 5000
	time.sleep(0.01)
	return

def placeWorkerBid():
	enterWorkerTab()
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 320, 760)
	click(0.5)
	time.sleep(0.5)
	return


	
def threeAM_Worker():
	bid = False
	while(bid != True):
		time.sleep(2)
		
		currentTime = getTime()
		print currentTime
		if (currentTime[_M_] == 59 and currentTime[_S_] > 50):
			removeInactivityScreen()
			placeWorkerBid()
			bid = True
		

	return

threeAM_Worker()

