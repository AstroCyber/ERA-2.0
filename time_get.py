from datetime import datetime

#getting current time
now = datetime.now()

#getting time in Hr:Min:Sec format
current_time = now.strftime("%H:%M:%S")
#spliting Hour-Minute-Seconds into diffrent variables
current_timeH, current_timeM, current_timeS = current_time.split(":")

#making time name function
def time_name(x):
    #checking if statments
    if (x > 4) and (x <= 8):
        return 'Early in the Morning'
    elif (x > 8) and (x <= 12):
        return 'in the Morning'
    elif (x > 12) and (x <= 16):
        return 'in the Noon'
    elif (x > 16) and (x <= 20):
        return 'in the Evening'
    elif (x > 20) and (x <= 24):
        return 'in the Night'
    elif (x <= 4):
        return 'in Late Night'

#making time function
def time(x):
    #checking if statements
    if (x => 12) and (x <= 20):
        return 'Evening'
    elif (x > 4) and (x < 12):
        return 'Morning'
    elif (x > 20) or (x <= 4):
        return 'Night'

#getting time in format H:M
int_time = int(current_timeH)
#checking if its am or pm
ampm = time_name(int_time)
#if the Hour is more than 12 Hour = Hour - 12 so we get clock time not digital time
if int_time > 12:
    int_time = int(current_timeH)
    current_timeH = int_time - 12
    
mn = time(int_time)
