from datetime import datetime, timedelta, date

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + datetime.timedelta(days=days)
    print("Future Date: ", future_date.strftime("%Y-%m-%d"))

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
