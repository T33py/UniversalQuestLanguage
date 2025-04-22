import os
import json

def export_uql_to_json(folder_path):
    """
    Exports all UQL files in a folder to a single JSON file.
    """
    uql_content = turn_folder_to_uql(folder_path)
    json_output = json.dumps(uql_content, indent=4)
    with open(os.path.join(folder_path, 'quests.json'), 'w') as json_file:
        json_file.write(json_output)
    return uql_content

def turn_folder_to_uql(folder_path):
	"""
	Converts all text files in a folder into a single UQL file.
	"""
	uql_content = []
	for filename in os.listdir(folder_path):
		if filename.endswith(".uql"):
			uql_content.append(parse_uql_to_dict(os.path.join(folder_path, filename)))
	return uql_content

def parse_uql_to_dict(file_path):
    """
    Parses a UQL file and converts it into a JSON object.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {}
    current_key = None
    current_value = []

    for line in lines:
        line = line.strip()
        if line.startswith("__") and line.endswith("__"):  # Detect section headers
            if current_key:  # Save the previous section
                data[current_key] = "\n".join(current_value).strip()
            current_key = line.strip("_")  # Remove underscores for the key
            current_value = []
        elif line.startswith("#"):  # Ignore comments
            pass
        elif current_key:  # Collect content for the current section
            current_value.append(line)

    if current_key:  # Save the last section
        data[current_key] = "\n".join(current_value).strip()

    return data

# Example usage
if __name__ == "__main__":
    uql_file_path = "quest_template.uql"
    json_output = export_uql_to_json('./')
    print(json_output)