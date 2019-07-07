class Onboarding:
    """Constructs the onboarding message."""
    def __init__(self, channel):
        self.channel = channel
        self.username = "pythonbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False


    #Retrun The Messagee
    def get_message(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Welcome to Slack! :wave: We're so glad you're here. :blush:\n\n*Get started by completing the steps below:*",
                    },
                },
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":white_large_square: *Add an emoji reaction to this message* :thinking_face:\nYou can quickly respond to any message on Slack with an emoji reaction. Reactions can be used for any purpose: voting, checking off to-do items, showing excitement.",
                    },
                },
                
            ],
        }

