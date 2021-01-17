# Twitter full archive search 

This code is meant to allow the usage of a Twitter full archive 
premium subscription using [v1.1 API](https://developer.twitter.com/en/docs/twitter-api/premium/search-api/quick-start/premium-full-archive).

## Requirements
___

### Environment variables

It is coded in Python3 and requires to have as an environment variable:
- BEARER_TOKEN
- ENVIRONMENT

### How to get this parameters?

After you have granted access from Twitter, you will need to create a project that
will contain an app. For completing this 
part follow this [link](https://developer.twitter.com/en/docs/projects/overview#:~:text=To%20create%20a%20Project%2C%20click,%2C%20description%2C%20and%20use%20case). From the registered app, you will need to get 
the BEARER_TOKEN.

Finally, to link the app to the subscription, create an envionment following
https://developer.twitter.com/en/account/environments. 


### Dependencies

Install requirements.txt using pip by running.

```bash
pip install -r requirements.txt
``` 
 
