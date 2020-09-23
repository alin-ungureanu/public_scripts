set /P minutes=Enter minutes: 
set /P turret_shutdown=Turret Shutdown? y/n: 
python3 dockOnIdle.py %minutes% %turret_shutdown%