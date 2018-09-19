import get_slack as slack
import post_rtm as rtm

def run():
   mes = slack.get_message("general") 
   for m in mes:
       print ( 'Updated :' + m )
       rtm.post(m)

if __name__ == "__main__":
    run()


