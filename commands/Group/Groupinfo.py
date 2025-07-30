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
