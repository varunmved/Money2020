import fitbit
#I NEED TO STOP PUTTING KEYS IN PLAINTEXT

'''
z = fitbit.Fitbit()
auth_url, auth_token = z.GetRequestToken()
#access_token = z.GetAccessToken('132', auth_token, oauth_verifier)
#response = z.ApiCall(access_token, apiCall='/1/user/-/activities/log/steps/date/today/7d.json')
'''
unauth_client = fitbit.Fitbit(consumer_key, consumer_secret)
# certain methods do not require user keys
#a=unauth_client.food_units()
#print(a)

# You'll have to gather the user keys on your own, or try
# ./gather_keys_cli.py <consumer_key> <consumer_secret> for development
authd_client = fitbit.Fitbit(consumer_key, consumer_key, resource_owner_key=user_key, resource_owner_secret=user_secret)
authd_client.sleep()
