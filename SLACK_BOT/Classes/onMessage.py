class OnMessage:
    """Constructs A Message ."""
    def __init__(self, channel, msg):
        self.channel = channel
        self.username = "pythonbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False
        self.TEXT_BLOCK = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    msg
                 ),
            },
         }      
       

 
    #Retrun The Messagee
    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.TEXT_BLOCK
            ],
        }

