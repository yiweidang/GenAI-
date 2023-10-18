import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Function to group tasks by task group and count status
def count_open_and_closed_tasks():
    # Filter the DataFrame for Open and Closed statuses
    filtered_df = df[df['Status'].isin(['Open', 'Closed'])]
    
    grouped_data = filtered_df.groupby(['Task Group', 'Status']).size().unstack().fillna(0)
    print("\nTask Count by Task Group and Status:")
    print(grouped_data)

# Call the function to perform the counts
count_open_and_closed_tasks()
