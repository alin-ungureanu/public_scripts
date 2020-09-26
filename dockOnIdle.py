import time
import sys
from ctypes import *
#import win32api
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

#   PREREQUISITES
# make sure you have set a destination beforehand
	
class LASTINPUTINFO(Structure):
	_fields_ = [
		('cbSize', c_uint),
		('dwTime', c_int),
	]
		
def getIdleTime():
	lastInputInfo = LASTINPUTINFO()
	lastInputInfo.cbSize = sizeof(lastInputInfo)
	if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
		millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
		return millis / 1000.0
	else:
		return 0

#def getIdleTime():
#	return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0

def getWindowFocus():
	print("Getting the focus of the full screen window on the first display")
	mouse = MouseController()

	mouse.position = (400, 200)
	mouse.press(Button.left)
	time.sleep(0.2)
	mouse.release(Button.left)
	time.sleep(0.5)


def retrieveDrones():

	print("Retrieving drones to drone bay")
	keyboard = KeyboardController()
	with keyboard.pressed(Key.shift_l):
		keyboard.press('r')
		time.sleep(0.3)
		keyboard.release('r')
		#waiting 1 min for drones to come back
		time.sleep(60)

def stopTurretActivity():
	print("Stopping miner activity")
	keyboard = KeyboardController()
	keyboard.press(Key.f1)
	time.sleep(0.3)
	keyboard.release(Key.f1)
	time.sleep(0.5)
	keyboard.press(Key.f2)
	time.sleep(0.3)
	keyboard.release(Key.f2)
	time.sleep(0.5)
	keyboard.press(Key.f3)
	time.sleep(0.3)
	keyboard.release(Key.f3)
	time.sleep(0.5)
	keyboard.press(Key.f4)
	time.sleep(0.3)
	keyboard.release(Key.f4)
	time.sleep(0.5)
	keyboard.press(Key.f5)
	time.sleep(0.3)
	keyboard.release(Key.f5)
	time.sleep(0.5)
	keyboard.press(Key.f6)
	time.sleep(0.3)
	keyboard.release(Key.f6)
	time.sleep(0.5)
	keyboard.press(Key.f7)
	time.sleep(0.3)
	keyboard.release(Key.f7)
	time.sleep(0.5)
	keyboard.press(Key.f8)
	time.sleep(0.3)
	keyboard.release(Key.f8)
	time.sleep(0.5)

def activateAutoPilot():
	
	print("Activating Auto-Pilot")
	keyboard = KeyboardController()

	with keyboard.pressed(Key.ctrl_l):
		keyboard.press('s')
		time.sleep(0.2)
		keyboard.release('s')

timeoutValue = 15 * 60.0#15 minutes
turretShutdown = False
if (len(sys.argv) > 1):
	timeoutValue = int(sys.argv[1]) * 60.0#X minutes
if (len(sys.argv) > 2):
	if (sys.argv[2] == 'y'):
		turretShutdown = True

		
while(True):
	idleTime = getIdleTime()
	print("running, idle for " + str(idleTime) + "s, less than " + str(timeoutValue - idleTime) + "s remaining")
	if (idleTime > timeoutValue):
        #getWindowFocus()
		retrieveDrones()
		if (turretShutdown):
			stopTurretActivity()
		#industrial command ship agression timer will expire because autopilot warps within 10km of the station
		activateAutoPilot()
		break
	time.sleep(5)
	
print("Exiting")
