# CSV Parser

This script reads two CSV files, `truck_list.csv` and `kibana_data.csv`, and checks for the presence of a specific list of elements in the `vehicleBusStatus.hasReceivedAfterInstallation` column of the `kibana_data.csv` file. The result is a new CSV file that groups the data by truck and adds a column for each element, indicating whether it exists in the `kibana_data.csv` file.

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. Clone this repository or download the files.
2. Install the `pandas` library if it is not already installed:

    ```bash
    pip install pandas
    ```

## Usage

1. Place the `truck_list.csv` and `kibana_data.csv` files in the same directory as the [csv_parser.py](http://_vscodecontentref_/1) script.
2. Run the script:

    ```bash
    python csv_parser.py
    ```

3. The script will generate a new CSV file named `output.csv` in the same directory.

## CSV File Structure

### truck_list.csv

This file should contain a column named `Truck` that lists the truck identifiers.

### kibana_data.csv

This file should contain a column named `header.manufacturerId` that corresponds to the truck identifiers and a column named `vehicleBusStatus.hasReceivedAfterInstallation` where the presence of the elements will be checked.

## Elements Checked

The script checks for the presence of the following elements:

- bendixFcWarning
- meritorFcWarning
- externalAccelerationDemand
- brakeLight
- ropEngine
- ropBrake
- yawEngine
- yawBrake
- meritorHapticWarning
- distanceForwardVehicle
- secondaryFcWarning
- collisionTime
- primaryFcWarning
- defaultHapticWarning
- defaultFcMitigation

## Output

The generated `output.csv` file will have the same structure as `truck_list.csv`, with additional columns for each checked element, indicating `True` if the element is present and `False` otherwise.
