# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case to determine base message
match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Note: '{task}' is a low priority task"
    case _:
        base_message = f"Note: '{task}' has an unknown priority level"

# Add time sensitivity note
if time_bound == "yes":
    base_message += " that requires immediate attention today!"
else:
    if priority == "low":
        base_message += ". Consider completing it when you have free time."
    else:
        base_message += ". Try to complete it soon."

# Final output
print(base_message)
