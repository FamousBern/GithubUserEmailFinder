import requests
import json
# re module provides support 
# for regular expressions 
import re 

username = input('Please type in github user username: ')
base_url = 'https://api.github.com/users/{}/events/public'
url = base_url.format(username)

# Make a regular expression 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' # Define a function for 
# for validating an Email 
def check(email):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        print("Valid Email", email)  
          
    else:  
        print("Invalid Email")



res = requests.get(url)
r = json.loads(res.text)
# for each dict in the list
for event in r:
    # using .get() means you can chain .get()s for nested dicts 
    # and they won't fail even if the key doesn't exist
    commits = event.get('payload', dict()).get('commits', list())
    # also using .get() with an empty list default means
    # you can always iterate over commits
    for commit in commits:
        # email = commit.get('author', dict()).get('email', None)
        # is also an option if you're not sure if those keys will exist
        email = commit['author']['email']
        # print(email)
        check(email)