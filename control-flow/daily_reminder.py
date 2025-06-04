# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case to handle priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority"

# Add urgency if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority in ["high", "medium"]:
        reminder += ". Try to complete it soon."
    else:
        reminder += ". Consider completing it when you have free time."

# Output the final reminder
print(reminder)
