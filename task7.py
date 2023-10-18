import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

# Filter for Form items with Status 'Open'
open_forms = df[df['Status'] == 'Open']

# Group open forms by Form Type and count the number of items
open_form_counts = open_forms['Type'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
open_form_counts.plot(kind='bar', color='skyblue')

# Set labels and title
plt.xlabel('Form Type')
plt.ylabel('Number of Open Form Items')
plt.title('Number of Open Form Items by Form Type')

# Show the plot
plt.show()
