import os
import slack


class Bot():
    def __init__(self, slack_token):
        self.my_token = slack_token
        self.WebClient = slack.WebClient(token=self.my_token)

    def get_myToken(self):
        return self.my_token

    def get_WebClient(self):
        return self.WebClient

    def get_ID(self):
        return self.WebClient.auth_test()["user_id"]

    def get_username(self, user_id):
        request = self.WebClient.api_call("users.list")
        if request['ok']:
            for item in request['members']:
                if item['id'] == user_id:
                   return item['name']


       


