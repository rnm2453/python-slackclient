import os
import slack

class Bot():
    """
        This is the 'Bot' class.

        Attributes:
            my_token = a oAuth token provided by slack
            The oAuth Token allows the script to connect to the requested slack app

            WebClient = WebClient class
            This class created by slack allows interaction with the Web API: https://api.slack.com/web

        Methods:
            
            Getters, Setter

            get_ID(): finds bot id
            get_username(): find the username of a user by a given id

    """
    def __init__(self, slack_token):
        self.my_token = slack_token
        self.WebClient = slack.WebClient(token=self.my_token)

    def get_myToken(self):
        return self.my_token

    def get_WebClient(self):
        return self.WebClient

    
    def get_ID(self):
        request = self.WebClient.api_call("auth.test")
        if request['ok']:
            print(request['user_id'])
            return request['user_id']
    
    def get_username(self, user_id):
        request = self.WebClient.api_call("users.list")
        if request['ok']:
            # Loops through all users in group
            for item in request['members']:
                if item['id'] == user_id:
                   return item['name']


       


