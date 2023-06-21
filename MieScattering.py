
import pandas as pd
import matplotlib.pyplot as plt

# Read the two text files into separate pandas dataframes
df1 = pd.read_csv('Biophotonics/6_micron_cell.txt', delim_whitespace=True, header=None, usecols=[0,1])
df2 = pd.read_csv('Biophotonics/8_micron_cell.txt', delim_whitespace=True, header=None, usecols=[0,1])

# Merge the two dataframes on the first column (which is the same)
merged_df = pd.merge(df1, df2, on=0)

merged_df.columns = ['theta', 'col2_x', 'col2_y']

# Plot the merged data with theta on the x-axis and the y-axis on a log scale
plt.plot(merged_df['theta'], merged_df['col2_x'], label='Non-cancerous')
plt.plot(merged_df['theta'], merged_df['col2_y'], label='Cancerous')

plt.yscale('log')
plt.xlabel('Theta')
plt.ylabel('Log Intensity')
plt.legend()
plt.show()


