
name = input("Search By Name: ").strip()

for user in users:
    if user['Name'] == name:
        print(f"{user['Name']} {user['Number']}")
    else:
        print(f"{name} Not Found.")