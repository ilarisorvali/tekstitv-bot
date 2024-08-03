import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

app_token = os.getenv("SLACK_APP_TOKEN")
bot_token = os.getenv("SLACK_BOT_TOKEN")

print(app_token)
print(bot_token)


# Initializes your app with your bot token and socket mode handler
app = App(token=bot_token)

@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()