import os
import json

directory = "./textcomplexity_mod/datasetcomp"

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as f:
            try:
                file_data = json.load(f)
                if not file_data:
                    os.remove(filepath)
            except json.JSONDecodeError:
                os.remove(filepath)
