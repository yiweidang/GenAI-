import pandas as pd
from datetime import datetime

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

# Function to calculate average days from creation to present
def calculate_average_days():
    # Convert 'Created' column to datetime format
    df['Created'] = pd.to_datetime(df['Created'])
    
    # Calculate the difference between today and the 'Created' date
    df['Days_Ago'] = (datetime.now() - df['Created']).dt.days
    
    # Calculate the average
    average_days = df['Days_Ago'].mean()
    print(f"The average number of days from creation to present is: {average_days:.2f} days")

# Call the function to calculate average days
calculate_average_days()
