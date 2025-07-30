from commands import ping, help
from config import BOT_NAME, PREFIX

def handle_message(message):
    msg = message.lower().strip()

    if msg == f"{PREFIX}ping":
        return ping.run()
    elif msg == f"{PREFIX}help":
        return help.run()
    else:
        return f"❓ Unknown command. Try `{PREFIX}help`"

# For testing
if __name__ == "__main__":
    print(f"{BOT_NAME} is running!")
    while True:
        msg = input("You: ")
        print("Bot:", handle_message(msg))
