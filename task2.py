import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')  # Replace 'your_file.csv' with the actual file path

# Check if the 'Status' and 'Task Group' columns exist in the DataFrame
if 'Status' in df.columns and 'Task Group' in df.columns:
    # Group the data by 'Task Group' and 'Status' and count the number of tasks in each group
    task_group_counts = df.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)

    print(task_group_counts)
else:
    print("Either 'Status' or 'Task Group' columns are not found in the CSV file.")
