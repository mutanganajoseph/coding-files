def chat():
    print("Chat function started")  # Add this for debugging
    message = input("> ")
    words = message.split(' ')
    emojis = {
        "::smile": "😊",
        "::sad": "😔",
        "::happy": "🙂",
        "::laugh": "🤣",
        "::heart": "❤️",
        "::like": "👍",
        "::hello": "👋",
    }
    
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    
    print(output)

chat()
