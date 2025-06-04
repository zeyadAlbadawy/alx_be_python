# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to process priority (optional here, but included per task)
match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Reminder: '{task}' is a low priority task"
    case _:
        base_message = f"Reminder: '{task}' has an unknown priority level"

# Modify message based on time sensitivity
if time_bound == "yes":
    base_message += " that requires immediate attention today!"
else:
    if priority == "low":
        base_message += ". Consider completing it when you have free time."
    else:
        base_message += ". Try to complete it soon."

# Print the final reminder
print(base_message)
