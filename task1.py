import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')  # Replace 'your_file.csv' with the actual file path

# Check if the 'Overdue' column exists in the DataFrame
if 'Overdue' in df.columns:
    # Filter the DataFrame to get only the overdue tasks
    overdue_tasks = df[df['Overdue'] == True]

    # Get the total number of overdue tasks
    total_overdue_tasks = len(overdue_tasks)

    print(f'Total number of tasks that are overdue: {total_overdue_tasks}')
else:
    print("The 'Overdue' column is not found in the CSV file.")
