import json
import os
import numpy as np

# Specify the directory containing the JSON files
directory = "./textcomplexity_mod/datasetcomp"

# Initialize empty lists to store values for calculations
dependents_per_word_values = []
longest_shortest_path_stdev_values = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):  # Ensure we're reading a JSON file
        with open(os.path.join(directory, filename), 'r') as f:
            file_data = json.load(f)

            # Extract values for 'dependents per word' and 'longest shortest path' with their respective standard deviations
            dependents_per_word = file_data.get("dependents per word", {}).get("value")
            longest_shortest_path_stdev = file_data.get("longest shortest path", {}).get("stdev")

            # Check if values are present before appending
            if dependents_per_word is not None:
                dependents_per_word_values.append(dependents_per_word)
            if longest_shortest_path_stdev is not None:
                longest_shortest_path_stdev_values.append(longest_shortest_path_stdev)

# Compute averages and standard deviations
dependents_per_word_avg = np.mean(dependents_per_word_values)
longest_shortest_path_stdev_avg = np.mean(longest_shortest_path_stdev_values)

dependents_per_word_stdev = np.std(dependents_per_word_values)
longest_shortest_path_stdev_stdev = np.std(longest_shortest_path_stdev_values)

# Print results
print("Average Dependents per Word:", dependents_per_word_avg)
print("Standard Deviation of Longest Shortest Path:", longest_shortest_path_stdev_avg)
print("Standard Deviation of Dependents per Word:", dependents_per_word_stdev)
print("Standard Deviation of Standard Deviation of Longest Shortest Path:", longest_shortest_path_stdev_stdev)