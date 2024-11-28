#!/usr/bin/env python3
# Group ID: 2

# Importing the functions from member1.py, member2.py, and member3.py
from yalaubadi import login_summary
from rvshah5 import active_users
from pkaur import detect_suspicious_activity, display_suspicious_activity

def main():
    print("=== Assignment 2 ===\n")
    
    # Display active users
    print("1. Active Users:")
    active_users()
    print("\n" + "="*50)
    
    # Display login summary
    print("2. Login Summary:")
    login_summary()
    print("\n" + "="*50)
    
    # Detect and display suspicious activity
    print("3. Suspicious Activity Alerts:")
    suspicious_activity = detect_suspicious_activity()
    display_suspicious_activity(suspicious_activity)

if __name__ == "__main__":
    main()
