import pandas as pd
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the CSV files
truck_list_df = pd.read_csv(os.path.join(current_dir, 'truck_list.csv'))
kibana_df = pd.read_csv(os.path.join(current_dir, 'kibana_data.csv'))

# List of elements to be searched
elements = [
    "bendixFcWarning",
    "meritorFcWarning",
    "externalAccelerationDemand",
    "brakeLight",
    "ropEngine",
    "ropBrake",
    "yawEngine",
    "yawBrake",
    "meritorHapticWarning",
    "distanceForwardVehicle",
    "secondaryFcWarning",
    "collisionTime",
    "primaryFcWarning",
    "defaultHapticWarning",
    "defaultFcMitigation"
]

# Initialize the output DataFrame
output_df = truck_list_df.copy()

# Add columns for each element
for element in elements:
    output_df[element] = False

# Check for the presence of each element for each truck
for truck in truck_list_df['Truck']:
    truck_data = kibana_df[kibana_df['header.manufacturerId'] == truck]
    for element in elements:
        if truck_data['vehicleBusStatus.hasReceivedAfterInstallation'].str.contains(element).any():
            output_df.loc[output_df['Truck'] == truck, element] = True

# Save the new CSV
output_df.to_csv(os.path.join(current_dir, 'output.csv'), index=False)