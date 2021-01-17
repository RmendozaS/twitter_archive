import requests
import os
import json
import time
import copy
import datetime

increase_days = 1 #this will include 2 full days

dates = [
    [datetime.datetime(2019,11,26),datetime.datetime(2020,1,17)],
    [datetime.datetime(2020,11,26),datetime.datetime(2021,1,17)]
]

base_url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/{}.json'

accounts = [
    ['@palaciohierro'],
    ['@amazonmex'],
    ['@ML_Mexico','@ML_Ayuda'],
    ['@WalmartMexico'],
    ['@TheHomeDepotMx'],
    ['@liverpoolmexico'],
    ['@claroshop_com','@claroshop_ayuda']
]

base_payload = {
                "query":"",
                "maxResults": "500",
                "fromDate":"", 
                "toDate":  ""
}

def get_project():
    project = os.environ.get("PROJECT")
    if not project:
        raise NameError('Project name must be available'
         ' as an env var before executed')
    return project

def auth():
    token = os.environ.get("BEARER_TOKEN")
    if not token:
        raise NameError('BEARER_TOKEN must be available'
         ' as an env var before executed')
    return token

def create_profile_query(profile):
    return '({})'.format(' OR '.join(profile))

def create_payload(start,end,profile):
    query = create_profile_query(profile)
    payload = copy.deepcopy(base_payload)
    payload['query'] = query
    payload['fromDate'] = start.strftime('%Y%m%d0000')
    payload['toDate'] = end.strftime('%Y%m%d2359')
    return payload

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers, payload):
    response = requests.post(url, headers=headers,json=paylod)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def create_filename(profile,start,end):
    profile = '-'.join(profile).replace('@','')
    return profile+'-'+start+'-'+end+'.json'

def store_json(profile,start,end,json_content):
    f_name = create_filename(profile,start,end)
    with open('data/'+f_name,'w') as f:
        f.write(json.dumps(json_content,indent=1))
    return f_name

def generate_dates(start,end):
    while start < end:
        p_end = start + datetime.timedelta(days=increase_days)
        yield start,p_end
        start = p_end + datetime.timedelta(days=1)

def generate_payloads(start,end):
    for l_start, l_end in generate_dates(start,end):
        for profile in accounts:
            yield create_payload(l_start,l_end,profile)

def main():
    bearer_token = auth()
    project = get_project()
    url = base_url.format(project)
    print(url)
    headers = create_headers(bearer_token)
    counter = 0
    for start,end in dates:
        for payload in generate_payloads(start,end):
            print(payload)
            #json_response = connect_to_endpoint(url, headers, payload)
            #f_path = store_json(profile,payload['fromDate'],
            #                payload['toDate'],json_response)
            counter +=1
            #print(f_path)
            #time.sleep(5)
    print(f'Total queries: {counter}')

if __name__ == "__main__":
    main()