import requests
import json
import hashlib


API_KEY = ''
SECRET_KEY = ''
FROB = ''
TOKEN = ''

#-----------setting(get frob, auth and token)-----------------------------

def get_frob():
    url ='https://api.rememberthemilk.com/services/rest/'

    frob_query = {
            'method': 'rtm.auth.getFrob',
            'api_key': API_KEY,
            'format': 'json'
            }

    frob_query[ "api_sig"] = make_signature(frob_query, SECRET_KEY)

    r = requests.get(url, params=frob_query)

    #print (json.dumps(r.json(),sort_keys=True,  indent=2))
    return (r.json()['rsp']['frob'])



def get_auth_url():
    frob = get_frob()
    url ='https://api.rememberthemilk.com/services/auth/'
    res = ""

    auth_query = {
            'api_key': API_KEY,
            'perms' : 'delete',
            'frob': frob,
            }

    auth_query[ "api_sig"] = make_signature(auth_query, SECRET_KEY)

    res = res + url +"?"
    for key, value in auth_query.items() :
            res= res + key + "=" + value + "&"

            
    return res[:-1]

    #r = requests.get(url, params=auth_query)
    #print (r)
    #print (r.text)

def get_token():
    url ='https://api.rememberthemilk.com/services/rest/'

    auth_query = {
            'method': 'rtm.auth.getToken',
            'api_key': API_KEY,
            'format': 'json',
            'perms' : 'delete',
            'frob': FROB,
            }

    auth_query[ "api_sig"] = make_signature(auth_query, SECRET_KEY)

    r = requests.get(url, params=auth_query)
    print (r)
    print (r.text)

    return

     

def make_signature(query, key):

    res =''
    for e in sorted(query) :
        res = res + e + query[e]

    res = (key + res).encode('utf-8')

    return hashlib.md5(res).hexdigest()

#-----------method-----------------------------
def post(m):

    url ='https://api.rememberthemilk.com/services/rest/'
    timeline = get_timeline()

    query = {
            'method': 'rtm.tasks.add',
            'api_key': API_KEY,
            'format': 'json',
            'perms' : 'delete',
            'name' : m,
            'timeline' : timeline,
            'auth_token' : TOKEN
            }

    query[ "api_sig"] = make_signature(query, SECRET_KEY)

    r = requests.get(url, params=query)
    print (r)
    print (r.text)

    return

def get_list():
    url ='https://api.rememberthemilk.com/services/rest/'

    query = {
            'method': 'rtm.lists.getList',
            'api_key': API_KEY,
            'format': 'json',
            'perms' : 'read',
            'auth_token' : TOKEN
            }

    query[ "api_sig"] = make_signature(query, SECRET_KEY)

    r = requests.get(url, params=query)
    print (r)
    print (r.text)

    return


def get_timeline():
    url ='https://api.rememberthemilk.com/services/rest/'

    query = {
            'method': 'rtm.timelines.create',
            'api_key': API_KEY,
            'format': 'json',
            'perms' : 'delete',
            'auth_token' : TOKEN
            }

    query[ "api_sig"] = make_signature(query, SECRET_KEY)

    r = requests.get(url, params=query)
    #print (r)
    #print (r.text)

    return (r.json()['rsp']['timeline'])

#if __name__ == "__main__":

    #post()
    #get_list()
    #post('test message')

    #print (get_timeline() )
    #print ( make_signature({}, "")  )
    #print ( get_auth_url())
    #print (get_token())
    #print (get_frob())
