import pandas as pd
import numpy as np

# Generate data
num_freq = 100
num_adc_values = 100

# Create frequency column
frequency = list(range(1, num_freq + 1))

# Create ADC values for each frequency
adc_data = np.random.rand(num_freq, num_adc_values)

# Create DataFrame
df = pd.DataFrame(adc_data, columns=[f'ADC_{i}' for i in range(1, num_adc_values + 1)])
df.insert(0, 'frequency', frequency)

# Save to CSV
csv_file = 'frequency_adc_data.csv'
df.to_csv(csv_file, index=False)