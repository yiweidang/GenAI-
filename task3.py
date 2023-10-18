import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Filter for tasks with Status 'Open' or 'Closed'
filtered_df = df[df['Status'].isin(['Open', 'Closed'])]

# Group tasks by Task Group and Status, and count the number of tasks
task_counts = filtered_df.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)

# Create a bar chart
ax = task_counts.plot(kind='bar', stacked=True, figsize=(10, 6))

# Set labels and title
plt.xlabel('Task Group')
plt.ylabel('Number of Tasks')
plt.title('Total Number of Open and Closed Tasks by Task Group')

# Show the legend
plt.legend(title='Status', loc='upper right')

# Show the plot
plt.show()
