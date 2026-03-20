# DON'T MODIFY THIS CELL, ONLY RUN IT.

# Importing numpy as np.
import numpy as np

# List of weather in Berlin in Celsius taken from Wikipedia
row_description = ["Record High", "Daily Mean", "Record Low"]
berlin_weather_list = [
    [15.1, 18.0, 25.8, 30.8, 32.7, 35.4, 37.3, 38.0, 32.3, 27.7, 20.4, 15.6], 
    [0.1, 0.9, 43, 9.0, 14.0, 16.8, 19.1, 18.5, 14.2, 9.4, 4.4, 1.0],
    [-25.3, -22.0, -16.0, -7.4, -2.8, 1.3, 4.9, 4.6, -0.9, -7.7, -12.0, -24.0]
]

# Print out the data
for idx, row in enumerate(row_description):
    print(f'{row}:\n{berlin_weather_list[idx]}\n')

# Convert the berlin_weather_list into a NumPy array
berlin_weather=np.array(berlin_weather_list)
# Find the shape of the array
print(berlin_weather)

berlin_weather[1,2]=4.3

berlin_weather_june=berlin_weather[:,5]

berlin_weather_low62=berlin_weather[2:].reshape(6,2).mean(axis=1)

print(berlin_weather>10)

print(np.ones((4,3))+6)

