from commands import ping

def handle_message(message):
    if message == "ping":
        return ping.run()
    else:
        return "Unknown command. Try 'ping' 😎"

# For testing (remove in production)
if __name__ == "__main__":
    while True:
        msg = input("You: ")
        print("Bot:", handle_message(msg))
