def run(members):
    if not members:
        return "😕 No members found."
    return "🚨 Attention everyone!\n" + "\n".join([f"@{m}" for m in members])
