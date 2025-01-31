import pandas as pd
import os

# Get the script directory
script_dir = os.path.dirname(__file__)

# Load the truck_list.csv file, ignoring the first line
truck_list_path = os.path.join(script_dir, 'truck_list.csv')
truck_list_df = pd.read_csv(
    truck_list_path, header=None, names=['Truck'], skiprows=1)

# 'kibana data' directory
kibana_data_dir = os.path.join(script_dir, 'kibana data')

# Iterate over all CSV files in the 'kibana data' directory
for file_name in os.listdir(kibana_data_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(kibana_data_dir, file_name)
        rop_engine_df = pd.read_csv(file_path)

        # Name of the column to be added
        column_name = file_name.replace('.csv', '')

        # Check the existence of each cell in the 'Truck' column in the 'header.manufacturerId' column
        truck_list_df[column_name] = truck_list_df['Truck'].apply(
            lambda x: 'Yes' if x in rop_engine_df['header.manufacturerId'].values else 'No')

# Manually add the header row
truck_list_df.loc[-1] = ['Truck'] + [file_name.replace(
    '.csv', '') for file_name in os.listdir(kibana_data_dir) if file_name.endswith('.csv')]
truck_list_df.index = truck_list_df.index + 1  # shifting index
truck_list_df = truck_list_df.sort_index()  # sorting by index

# Desired order of columns
desired_order = [
    'Truck', 'Wheel Speed', 'Rop Brake', 'Rop Engine', 'Yaw Engine', 'Yaw Brake',
    'Default FCM', 'Meritor FCM', 'Bendix FCM', 'Default Haptic', 'Primary FCW',
    'Secondary FCW', 'Brake Light', 'XBR', 'Forward Vehicle Distance', 'Collision Time'
]

# Reorder the columns of the DataFrame
truck_list_df = truck_list_df[desired_order]

# Save the result to a new CSV file
output_path = os.path.join(script_dir, 'data_availability.csv')
truck_list_df.to_csv(output_path, index=False, header=False)
