#!user/bin/env python3 

import os
from datetime import datetime, timedelta

# Thresholds for suspicious activity
MAX_LOGIN_ATTEMPTS = 3  # Max allowed logins in the time window
LOGIN_WINDOW = timedelta(minutes=10)  # Time window for detecting multiple logins (e.g., 10 minutes)

# Function to get the active users and their login times
def get_login_attempts():
    """Get login attempts from the `who` command and check for suspicious activities."""
    # Get the output of the `who` command
    who_output = os.popen("who").read().strip()
    
    if not who_output:
        print("No login attempts found.")
        return []

    login_attempts = []
    
    # Parse the output of `who`
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
            
            login_attempts.append((username, tty, login_time))

    # Debug output to check the login attempts
    print(f"Login Attempts: {login_attempts}")
    
    return login_attempts

# Function to detect suspicious activities (e.g., too many logins in a short time)
def detect_suspicious_activity():
    """Detect and alert for suspicious activity based on login attempts."""
    login_attempts = get_login_attempts()

    if not login_attempts:
        return []

    suspicious_activity = []

    # Dictionary to track login attempts for each user
    user_logins = {}

    for username, tty, login_time in login_attempts:
        if username not in user_logins:
            user_logins[username] = []
        
        # Add the current login attempt to the user's list
        user_logins[username].append(login_time)

    # Debug output to check the user logins
    print(f"User Logins: {user_logins}")
    
    # Check for multiple logins within a short time window
    for username, login_times in user_logins.items():
        login_times.sort()  # Sort login times for the user
        for i in range(len(login_times) - 1):
            # Compare each login with the next one to see if it is within the login window
            if login_times[i + 1] - login_times[i] <= LOGIN_WINDOW:
                suspicious_activity.append((username, login_times[i], login_times[i + 1]))

    return suspicious_activity

# Function to display suspicious activity alerts
def display_suspicious_activity(suspicious_activity):
    """Display alerts for suspicious login activity."""
    if not suspicious_activity:
        print("No suspicious activity detected.")
    else:
        print("\nSuspicious Activity Alerts:")
        for username, login_time1, login_time2 in suspicious_activity:
            print(f"ALERT: {username} logged in multiple times within {LOGIN_WINDOW} minutes: "
                  f"{login_time1.strftime('%Y-%m-%d %H:%M')} and {login_time2.strftime('%Y-%m-%d %H:%M')}")

if __name__ == "__main__":
    print("Monitoring for Suspicious Activity...\n")
    
    # Detect suspicious activity
    suspicious_activity = detect_suspicious_activity()
    
    # Display any suspicious activity detected
    display_suspicious_activity(suspicious_activity)
