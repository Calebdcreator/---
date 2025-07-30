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
from commands.group import tagall, promote, demote, kick, welcome

# Example fake group members
members = ['calebdcreator', 'toyin360', 'itz_emeka']

if msg == f"{PREFIX}tagall":
    return tagall.run(members)
elif msg.startswith(f"{PREFIX}promote"):
    user = msg.split()[-1]
    return promote.run(user)
elif msg.startswith(f"{PREFIX}demote"):
    user = msg.split()[-1]
    return demote.run(user)
elif msg.startswith(f"{PREFIX}kick"):
    user = msg.split()[-1]
    return kick.run(user)
elif msg.startswith(f"{PREFIX}welcome"):
    user = msg.split()[-1]
    return welcome.run(user)
# commands/group/groupinfo.py

def run(group_data):
    name = group_data.get("name", "Unknown Group")
    members = group_data.get("members", [])
    admins = group_data.get("admins", [])
    description = group_data.get("description", "No description available.")

    return f"""📍 *Group Info*
🏷️ Name: {name}
👥 Members: {len(members)}
🛡️ Admins: {len(admins)}
📝 Description: {description}"""
