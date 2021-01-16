import requests
import os
import json
import time
import urllib.parse
import datetime

#Parameters
#https://developer.twitter.com/en/docs/twitter-api/tweets/full-archive-search/api-reference/get-tweets-search-all

increase_days = 1 #this will include 2 full days

dates = [
    [datetime.datetime(2019,11,26),datetime.datetime(2020,1,17)],
    [datetime.datetime(2020,11,26),datetime.datetime(2021,1,17)]
]

accounts = [
    ['@palaciohierro'],
    ['@amazonmex'],
    ['@ML_Mexico','@ML_Ayuda'],
    ['@WalmartMexico'],
    ['@TheHomeDepotMx'],
    ['@liverpoolmexico'],
    ['@claroshop_com','@claroshop_ayuda']
]

def auth():
    token = os.environ.get("BEARER_TOKEN")
    if not token:
        raise NameError('BEARER_TOKEN must be available'
         ' as an env var before executed')
    return token

def create_profile_query(profile):
    return '({})'.format(' OR '.join(profile)) if len(profile) > 1 \
                else profile[0]


def create_url(start,end,profile):
    start_time=urllib.parse.quote(start.strftime('%Y-%m-%dT00:00:00Z'))
    end_time=urllib.parse.quote(end.strftime('%Y-%m-%dT23:59:59Z'))
    profile= create_profile_query(profile)
    query=urllib.parse.quote(f'({profile} AND (@AtencionProfeco OR @Profeco))')
    base = 'https://api.twitter.com/2/tweets/search/all?query='
    q = f"{query}&max_results=500&start_time={start_time}&end_time={end_time}"
    return base + q

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.get(url, headers=headers)
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
    return profile+'-'+str(start).split()[0]+'-'+str(end).split()[0]+'.json'

def store_json(profile,start,end,json_content):
    f_name = create_filename(profile,start,end)
    with open(f_name,'w') as f:
        f.write(json.dumps(json_content,indent=1))
    return r_name


def generate_dates(start,end):
    while start < end:
        p_end = start + datetime.timedelta(days=increase_days)
        yield start,p_end
        start = p_end + datetime.timedelta(days=1)

def generate_urls(start,end):
    for l_start, l_end in generate_dates(start,end):
        for profile in accounts:
            url = create_url(l_start,l_end,profile)
            yield profile,l_start,l_end,url

def main():
    bearer_token = auth()
    headers = create_headers(bearer_token)
    counter = 0
    for start,end in dates:
        for profile,l_start,l_end,url in generate_urls(start,end):
            #json_response = connect_to_endpoint(url, headers)
            #f_path = store_json(profile,l_start,l_end,json_response)
            counter +=1
            #print(f_path)
            #print(counter)
            #print()
            #time.sleep(5)
    print(f'Total queries: {counter}')
    #test_url = 'https://api.twitter.com/2/tweets/search/all?query=%28%40palaciohierro%20AND%20%28%40AtencionProfeco%20OR%20%40Profeco%29%29&max_results=500&start_time=2021-01-13T00%3A00%3A00Z&end_time=2021-01-14T23%3A59%3A59Z'
    #json_response = connect_to_endpoint(test_url, headers)
    #print(json_response)


if __name__ == "__main__":
    main()