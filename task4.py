import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Filter for tasks that are overdue
overdue_tasks = df[df['Overdue'] == True]

# Group overdue tasks by Project and count the number of tasks
overdue_counts = overdue_tasks.groupby('Project').size()

# Create a bar chart
ax = overdue_counts.plot(kind='bar', figsize=(10, 6))

# Set labels and title
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.title('Total Number of Overdue Tasks by Project')

# Show the plot
plt.show()
