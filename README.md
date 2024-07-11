**Frequency ADC Graph Dashboard**

This dashboard application, built using Python, Plotly, and the Dash framework, visualizes frequency vs. ADC values for EMI detection. The application allows users to interactively filter and view ADC data across different frequencies.
Features

    Interactive Dropdowns: Select minimum and maximum frequency limits to filter the data displayed on the graph.
    Dynamic Graphs: View median, low, and high ADC values across the selected frequency range.
    Single Frequency Data: Examine detailed ADC values for individual frequency points.

Installation

    Clone the repository:

    git clone https://github.com/yourusername/frequency-adc-dashboard.git

    cd frequency-adc-dashboard

Install required packages:

    pip install -r requirements.txt

Run the application:

    python3 freq_adc.py

Dependencies

    Dash
    Plotly
    Pandas
    Dash Bootstrap Components

You can install these dependencies using the provided requirements.txt file.
File Structure

    frequency-adc-dashboard/
    │
    ├── freq_adc.py                # Main application file
    ├── requirements.txt      # List of dependencies
    ├── frequency_adc_data.csv # CSV file with frequency and ADC data

Data

    Ensure the frequency_adc_data.csv file is in the same directory as app.py. This CSV file should contain your frequency and ADC data with the following structure:

    frequency,adc_value_1,adc_value_2,...,adc_value_n

Usage

    Run the application:

        python3 freq_adc.py

    Access the dashboard:
        Open a web browser and navigate to http://127.0.0.1:8050/.

    Interact with the dashboard:
        Use the dropdowns to select minimum and maximum frequency limits.
        View the graph displaying the median, low, and high ADC values within the selected range.
        Select a specific frequency to view detailed ADC values over sampling points.

E
