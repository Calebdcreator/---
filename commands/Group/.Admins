# commands/group/admins.py

def run(group_data):
    admins = group_data.get("admins", [])
    if not admins:
        return "No admins found 👀"

    admin_list = "\n".join([f"👑 @{admin}" for admin in admins])
    return f"""👑 *Group Admins:*\n{admin_list}"""
