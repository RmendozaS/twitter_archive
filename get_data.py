import requests
import os
import json
import urllib.parse


#Parameters
#https://developer.twitter.com/en/docs/twitter-api/tweets/full-archive-search/api-reference/get-tweets-search-all

accounts = [
    '@palaciohierro',
    '@amazonmex',
    '@ML_Mexico',
    '@ML_Ayuda',
    '@WalmartMexico',
    '@TheHomeDepotMx',
    '@liverpoolmexico',
    '@claroshop_com',
    '@claroshop_ayuda'
]

start_time=urllib.parse.quote('2019-12-01T00:00:00Z')
end_time=urllib.parse.quote('2019-12-31T23:59:59Z')
query=urllib.parse.quote(f'({accounts[0]} AND (@AtencionProfeco OR @Profeco))')

url = f"https://api.twitter.com/2/tweets/search/all?query={query}&start_time={start_time}&end_time={end_time}" #-H "Authorization: Bearer $BEARER_TOKEN"

breakpoint()

def auth():
    token = os.environ.get("BEARER_TOKEN")
    if not token:
        raise NameError(('BEARER_TOKEN must be available')
         (' as an env var before executed'))
    return token


def create_url():
    # Replace with user ID below
    return "https://api.twitter.com/2/search/all".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    params = get_params()
    breakpoint()
    json_response = connect_to_endpoint(url, headers, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()