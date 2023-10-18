import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Function to generate bar chart for overdue tasks by project
def generate_overdue_tasks_bar_chart():
    overdue_tasks_by_project = df[df['OverDue'] == True].groupby('project').size()
    overdue_tasks_by_project.plot(kind='bar', xlabel='Project ID', ylabel='Total Overdue Tasks', title='Overdue Tasks by Project')
    plt.show()

# Call the function to generate the bar chart
generate_overdue_tasks_bar_chart()
