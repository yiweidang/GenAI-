import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Function to generate bar chart for Open and Closed tasks by task group
def generate_open_closed_tasks_bar_chart():
    # Filter the DataFrame for Open and Closed statuses
    filtered_df = df[df['Status'].isin(['Open', 'Closed'])]
    
    grouped_data = filtered_df.groupby(['Task Group', 'Status']).size().unstack().fillna(0)
    ax = grouped_data.plot(kind='bar', stacked=True)
    ax.set_xlabel('Task Group')
    ax.set_ylabel('Total Tasks')
    ax.set_title('Open and Closed Tasks by Task Group')
    plt.show()

# Call the function to generate the bar chart
generate_open_closed_tasks_bar_chart()
