import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Function to count the total number of overdue tasks
def count_overdue_tasks():
    overdue_tasks = df[df['OverDue'] == True]
    total_overdue_tasks = len(overdue_tasks)
    print(f"Total number of overdue tasks: {total_overdue_tasks}")

# Call the function to count overdue tasks
count_overdue_tasks()
