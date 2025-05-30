task = input("Enter your task: ")
priority = input("Enter the priority (high, medium, low): ")
time = input("Is it time inbound? (yes/no): ")
match priority:
    case "high":
        if time == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention")
        else:
            print(f"Reminder: '{task}' is a high priority task, should be done soon.")
    case "medium":
        if time == "yes":
            print(f"Reminder: '{task}' is a medium priority task, should be done soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task, can be done later.")
    case "low":
        if time == "yes":
            print(f"Reminder: '{task}' is a low priority task, can be done later.")
        else:
            print(f"Reminder: '{task}' is a low priority task, can be done whenever you have time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")