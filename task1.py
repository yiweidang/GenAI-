import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Filter tasks that are overdue
overdue_tasks = df[df['Overdue'] == True]

# Get the total number of overdue tasks
total_overdue_tasks = len(overdue_tasks)

# Print the total number of overdue tasks
print(f"Total number of tasks that are overdue: {total_overdue_tasks}")
