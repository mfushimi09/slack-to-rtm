from slacker import Slacker
import urllib.parse
import time
from datetime import datetime as dt


def init():
    slack = Slacker("YOUR-TOKEN")

    return slack

def update_executed_date():

    #write present date to setting.ini
    f=open('setting.ini', 'w')
    f.write( str(dt.now().strftime('%Y-%m-%d %H:%M:%S')) )
    f.close()
    return

def get_executed_date():
    str =""
    f=open('setting.ini', 'r')
    for row in f:
        str = str + row
    f.close()

    return  dt.strptime(str, '%Y-%m-%d %H:%M:%S')


def get_channel_id(channel_name) :
    slack = init()
    raw_data = slack.channels.list().body

    for data in raw_data["channels"]:
        if data["name"] == channel_name:
            return data["id"]


def get_message(channel_name):

    #get raw_data
    slack = init()
    channel_id = get_channel_id(channel_name)
    raw_data = slack.channels.history(channel_id).body

    res= []
    posted = []
    is_executed=False

    f=open('setting.ini', 'r')
    for row in f:
        posted.append(row[0:-1])
    f.close()

    for mes in raw_data["messages"]:
        
        #starred?
        if  "is_starred" in mes and mes["is_starred"] == True : 
            
            m = mes["text"].replace("\n", "")
            if m not in posted : 
                res.append( m )
                f = open('setting.ini', 'a')
                f.write(m + "\n" )
                f.close()

    #for e in res:
    #    print(e) 

    return res
    

#print(get_channel_id("general"))

if __name__ == "__main__":

    
    #get_message("general")
    #print(update_executed_date())
    print(get_message("general"))


