import fitbit
consumer_key = 'b785ae87e873133f0baff9bb21dc66ab'
consumer_secret = '28a8fce8b61ac758b1111f1690de151d'
encoded_user_id = '3RVPY5'
#oauth_token = 'adce2ce343bcb360176e233d62a13bee'
#oauth_token_secret = '9983d76c740c6b8d6d4a15d8187984fc'
user_key = 'adce2ce343bcb360176e233d62a13bee'
user_secret = '9983d76c740c6b8d6d4a15d8187984fc'

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
