import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Filter for tasks with Status 'Open' or 'Closed'
filtered_df = df[df['Status'].isin(['Open', 'Closed'])]

# Group tasks by Task Group and Status, and count the number of tasks
task_counts = filtered_df.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)

# Print the result
print("Total Number of Open and Closed Tasks by Task Group:")
print(task_counts)
