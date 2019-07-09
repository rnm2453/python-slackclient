class OnBoarding:
    """Constructs the onboarding message and stores the state of which tasks were completed."""
    def __init__(self, channel):
        self.channel = channel
        self.username = "pythonbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False


    # Create Blocks You Want To Have In Your OnBoarding Message
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to Slack! This Is A Test Bot"
            ),
        },
    }

    DIVIDER_BLOCK = {"type": "divider"}

    INFO_BLOCK = {
        
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "If You Have A Specific Question, Feel Free To Ask Me. I Am Here For You"
            ),
        },
    }
    #------------------------------------------------------------

    #Retrun The Messagee
    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.INFO_BLOCK,
            ],
        }

