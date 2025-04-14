#!/usr/bin/python3
# Given a dictionary of usernames and passwords,
# write a script that asks for a username and prints the stored password.

def get_password(user):
    # Ask for a username
    username = input("Enter your username: ")

    # Check if the username exists in the dictionary
    if username in user_credentials:
        print(f"The stored password for '{username}' is: {user_credentials[username]}")
    else:
        print("Username not found.")


user_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

get_password(user_credentials)
