import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

# Filter for Form items with Status 'Open'
open_forms = df[df['Status'] == 'Open']

# Group open forms by Report Form Group and Status Changed, and count the number of items
time_series_data = open_forms.groupby(['Report Forms Group', 'Status Changed']).size().reset_index(name='Count')

# Convert 'Status Changed' to datetime for proper plotting
time_series_data['Status Changed'] = pd.to_datetime(time_series_data['Status Changed'], format='%d/%m/%Y')

# Set 'Status Changed' as index
time_series_data.set_index('Status Changed', inplace=True)

# Resample data to get counts per day
time_series_data = time_series_data.resample('D').sum()

# Create the time series graph
plt.figure(figsize=(10, 6))
for group, data in time_series_data.groupby('Report Forms Group'):
    plt.plot(data.index, data['Count'], label=group)

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Number of Open Form Items')
plt.title('Time Series of Open Form Items by Report Form Group')

# Add legend
plt.legend()

# Show the plot
plt.show()
