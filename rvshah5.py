#!/usr/bin/env python3
# Student ID: rvshah5

import os
from datetime import datetime

def active_users():
    """Displays currently logged-in users in a formatted table."""
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
    
    # Print the table header
    print(f"{'Username':<15}{'TTY':<10}{'Login Time':<25}")
    print("=" * 50)
    
    # Print each user's information
    for user in users:
        login_time = user[2] if isinstance(user[2], str) else user[2].strftime("%Y-%m-%d %H:%M")
        print(f"{user[0]:<15}{user[1]:<10}{login_time:<25}")

if __name__ == "__main__":
    print("Active Users:")
    active_users()
