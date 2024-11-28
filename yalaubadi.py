#!/usr/bin/env python3

import os
from datetime import datetime

# Function to get the active users (currently logged in)
def active_users():
    """Displays currently logged-in users and their login time."""
    # Get the output of the `who` command
    who_output = os.popen("who").read().strip()
    
    if not who_output:
        print("No active users found.")
        return

    # Parse the output of `who`
    users = []
    for line in who_output.splitlines():
        parts = line.split()
        if len(parts) >= 3:
            username = parts[0]
            tty = parts[1]
            login_time_str = " ".join(parts[2:4])
            
            # Convert login time to datetime object for better formatting
            try:
                login_time = datetime.strptime(login_time_str, "%Y-%m-%d %H:%M")
            except ValueError:
                login_time = "Invalid Time Format"
            
            users.append((username, tty, login_time))
    
    return users

# Function to get login and logout sessions
def login_summary():
    """Tracks the login and logout activities and calculates session duration."""
    users = active_users()

    if not users: # Here if no active users found it will exit
        return

    sessions = []
    # Get current time to calculate session durations
    current_time = datetime.now()

    for user in users:
        username, tty, login_time = user
        if isinstance(login_time, datetime):
            # Calculate session duration
            session_duration = current_time - login_time
            sessions.append((username, login_time.strftime("%Y-%m-%d %H:%M"), session_duration))

    # Display the session summary
    print(f"\n{'Username':<15}{'Login Time':<20}{'Session Duration':<20}")
    print("=" * 60)
    for session in sessions:
        print(f"{session[0]:<15}{session[1]:<20}{str(session[2]):<20}")

if __name__ == "__main__":
    print("Login Summary:")
    login_summary()
