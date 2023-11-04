from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be in this format: HH:MM:SS AM/PM\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Done... Have a nice sleep.")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if((alarm_time[0] == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9")
       or (alarm_time[3] =="6" or "7" or "8" or "9")
       or (alarm_time[6] == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9")
       or (alert_period != "AM" or "PM")
       or (alert_time[2] or alert_time[5] or alert_time[8] != ":")):
       print("Enter right time as the format suggested!")
       break



    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_seconds == current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break
