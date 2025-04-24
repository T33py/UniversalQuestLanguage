import os
import json

vocabiulary_types = {
	'ID': 'int',
    'TYPE': 'enum',
    'REQUIRES': 'array[str]',
    'PRICE': 'array[str]',
    'REWARDS': 'array[str]',
    'RELATED_QUESTS': 'array[int]',
    'ACTIVATES': 'array[int]',
}

def export_uql_to_json(folder_path):
    """
    Exports all UQL files in a folder to a single JSON file.
    """
    uql_content = turn_folder_to_uql(folder_path)
    json_output = json.dumps(uql_content, indent=4)
    with open(os.path.join(folder_path, 'quests.json'), 'w') as json_file:
        json_file.write(json_output)
    return uql_content

def turn_folder_to_uql(folder_path) -> list:
    """
    Converts all text files in a folder into a single UQL file.
    """
    uql_content = []
    for thing in os.listdir(folder_path):
        path = os.path.join(folder_path, thing)
        if os.path.isfile(path):
            if path.endswith(".uql"):
                uql_content.append(parse_uql_to_dict(path))
        elif os.path.isdir(path):
            uql_content.extend(turn_folder_to_uql(path))
    return uql_content

def parse_uql_to_dict(file_path) -> dict:
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
        if line.startswith("__") and line.endswith("__"):
            if current_key:
                data[current_key] = "\n".join(current_value).strip()
            current_key = line.strip("_")
            current_value = []
        elif line.startswith("#"):  # Ignore comments
            pass
        elif current_key:
            current_value.append(line)

    if current_key:  # Save the last section
        data[current_key] = "\n".join(current_value).strip()

    post_process_raw_uql(data)
    return data

def post_process_raw_uql(data: dict):
    """
    Post-processes the UQL data. Converting the data into more sofisticated structures.
    """
    for key, value in data.items():
        match key:
            case 'ID':
                data[key] = format_id(value)
            case 'TYPE':
                data[key] = value.strip().split('\n')[0].strip()
            case 'REQUIRES':
                data[key] = [requirement.strip() for requirement in value.split("\n") if len(requirement.strip()) > 0]
            case 'PRICE':
                data[key] = [price.strip() for price in value.split("\n") if len(price.strip()) > 0]
            case 'REWARDS':
                data[key] = [reward.strip() for reward in value.split("\n") if len(reward.strip()) > 0]
            case 'RELATED_QUESTS':
                data[key] = [ int(related_quest) for related_quest in value.split("\n") if related_quest.isdigit() ]
            case 'ACTIVATES':
                data[key] = [ int(activates) for activates in value.split("\n") if activates.isdigit() ]
            
    return

def extract_codegen_info(data: list) -> dict:
    """
    Extracts code concepts from the UQL data.
    """
    codegen_info = {
        'max_id': 0,
        'variables': [],
        'variable_types': {},
        'event_types': [],
    }
    for quest in data:
        if quest['ID'] > codegen_info['max_id']:
            codegen_info['max_id'] = quest['ID']
        for key, value in quest.items():
            if key not in codegen_info['variables']:
                codegen_info['variables'].append(key)
            if key not in codegen_info['variable_types']:
                codegen_info['variable_types'][key] = 'str'
                if key in vocabiulary_types:
                    codegen_info['variable_types'][key] = vocabiulary_types[key]
            if key == 'TYPE':
                if value not in codegen_info['event_types']:
                    codegen_info['event_types'].append(value)

    return codegen_info

def format_id(id: str) -> int:
    return int(id)

# Example usage
if __name__ == "__main__":
    uql_file_path = "quest_template.uql"
    json_output = export_uql_to_json('QuestExamples')
    print(json_output)