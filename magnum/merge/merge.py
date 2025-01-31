import pandas as pd
import os

# Get the script directory path
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the paths for the CSV files
truck_list_path = os.path.join(script_dir, 'truck_list.csv')
magnum_express_path = os.path.join(
    script_dir, 'Magnum Express - 8133 - DVR Health Status.csv')
asset_list_path = os.path.join(
    script_dir, 'Magnum Express - 8133 - Asset List.csv')
installation_progress_path = os.path.join(
    script_dir, 'Magnum Truck Installation Progress - Sheet1.csv')

# Load the CSV files
magnum_express_df = pd.read_csv(magnum_express_path)
truck_list_df = pd.read_csv(truck_list_path)
asset_list_df = pd.read_csv(asset_list_path)
installation_progress_df = pd.read_csv(installation_progress_path)

# Rename the column to facilitate the merge
magnum_express_df.rename(columns={'Serial Number': 'Truck'}, inplace=True)
asset_list_df.rename(columns={'DVR SN': 'Truck'}, inplace=True)
installation_progress_df.rename(
    columns={'DVR Serial Number': 'Truck'}, inplace=True)

# Merge the dataframes
merged_df = pd.merge(truck_list_df, magnum_express_df[[
                     'Truck', 'Vehicle Number']], on='Truck', how='left')
merged_df = pd.merge(merged_df, asset_list_df[[
                     'Truck', 'Year', 'Make', 'Model']], on='Truck', how='left')
merged_df = pd.merge(merged_df, installation_progress_df[[
                     'Truck', 'Gateway (OBC) Serial Number']], on='Truck', how='left')

# Save the result to a new CSV file
output_path = os.path.join(script_dir, 'merged_truck_list.csv')
merged_df.to_csv(output_path, index=False)
