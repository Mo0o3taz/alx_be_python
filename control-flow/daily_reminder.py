task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ") 
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task. Consider completing it as soon as possible.")
            
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium proirity that requires attention immediatly after you finish high priority tasks.")
        else:
            print(f"Note: {task} is a mediem priority task. Consider completing it when you finish high priority tasks.")
                
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low proirity that requires attention after you finish high and medium priority tasks.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")


