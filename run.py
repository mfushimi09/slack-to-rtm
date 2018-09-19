import schedule
import time
import slack_to_rtm

def job():
    #print("I'm working...")
    slack_to_rtm.run()
    

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
