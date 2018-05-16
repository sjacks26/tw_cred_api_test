# tw_cred_api_test

This code tests Twitter API credentials to make sure they are still active. Given a list of multiple sets of credentials, it iterates through that list for a specified number of times, makes a call to the Twitter API each time using the verify_credentials function from tweepy, and prints the number of times remaining calls using this function that are available for each set of credentials.

**To use the code**
1)  In [creds.txt](creds.txt), insert information about your Twitter apps. If you do not want to provide the Twitter account or password, you can leave those fields as is. The "available" and "use note" fields for each app are also optional.
2) In [main.py](main.py), specify the number of times you want to make a call to the API with each set of credentials. By default, this number is three. This allows you to be confident that none of your apps have been deactivated by Twitter, even after each app has made at least one API call.
3) Run [main.py](main.py).

Prerequisites:
* Python 3
* tweepy
