import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Function to generate bar chart for percentage of overdue tasks by project
def generate_overdue_tasks_percentage_bar_chart():
    total_tasks_by_project = df.groupby('project').size()
    overdue_tasks_by_project = df[df['OverDue'] == True].groupby('project').size()
    
    # Calculate the percentage of overdue tasks
    percentage_overdue = (overdue_tasks_by_project / total_tasks_by_project) * 100
    
    ax = percentage_overdue.plot(kind='bar', xlabel='Project ID', ylabel='Percentage of Overdue Tasks', title='Percentage of Overdue Tasks by Project')
    ax.set_ylim(0, 100)
    plt.show()

# Call the function to generate the bar chart
generate_overdue_tasks_percentage_bar_chart()
