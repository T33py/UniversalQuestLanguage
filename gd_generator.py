import os
import json
from universal_quest_language import turn_folder_to_uql, extract_codegen_info

def generate_quest_datafile(quest_data: list, codegen_info: dict, folder_path: str):
	"""
	Generates a quest data file from the given quest data dictionary.
	"""
	for quest in quest_data:
		if 'TYPE' in quest:
			quest['TYPE'] = codegen_info['event_types'].index(quest['TYPE'])

	code = [
		'class_name UQLRawData\n',
		'\n',
		f'var max_id: int = {str(codegen_info["max_id"])}\n',
		f'var events: Array[Dictionary] = {json.dumps(quest_data, indent=4)}\n',
	]
	with open(os.path.join(folder_path, 'uql_raw_data.gd'), 'w') as file:
		file.writelines(code)
		pass

def generate_event_class_file(quest_data: list, codegen_info: dict, folder_path: str):
	"""
	Generates a quest event class file from the given quest data dictionary.
	"""
	code = [
		'class_name UQLEvent\n',
		'\n',
		'enum EventType {\n',
	]

	for type in codegen_info['event_types']:
		code.append(f'\t{type.upper()},\n')

	code.append('}\n\n')

	for variable in codegen_info['variables']:
		var_type = codegen_info['variable_types'][variable]
		var_default = '""'
		if var_type == 'int':
			var_type = 'int'
			var_default = '0'
		elif var_type == 'bool':
			var_type = 'bool'
			var_default = 'false'
		elif var_type == 'str':
			var_type = 'String'
			var_default = '""'
		elif var_type == 'float':
			var_type = 'float'
			var_default = '0'
		elif var_type == 'array[int]':
			var_type = 'Array[int]'
			var_default = '[]'
		elif var_type == 'array[float]':
			var_type = 'Array[float]'
			var_default = '[]'
		elif var_type == 'array[str]':
			var_type = 'Array[String]'
			var_default = '[]'
		elif var_type == 'enum':
			var_type = 'EventType'
			var_default = '0 as EventType'
		else:
			var_type = 'String'
			var_default = '""'

		var_string = f'var {variable.lower()}: {var_type} = {var_default}\n'
		code.append(var_string)

	with open(os.path.join(folder_path, 'uql_event.gd'), 'w') as file:
		file.writelines(code)
		pass

def generate_event_db(quest_data: list, codegen_info: dict, folder_path: str):
	"""
	Generates a quest event database file from the given quest data dictionary.
	"""
	code = []
	with open(os.path.join('Godot 4.3', 'uql_event_db.gd'), 'r') as file:
		code = file.readlines()

	# fill variables into parse_raw_data function
	for variable in codegen_info['variables']:
		var = variable.lower()
		val = f'event["{variable}"]'
		code.append(f'\t\tif "{variable}" in event:\n')
		if 'array' in codegen_info['variable_types'][variable].lower():
			code.append(f'\t\t\tfor thing in {val}: \n')
			code.append(f'\t\t\t\tuql_event.{var}.append(thing)\n')
			pass
		else:
			code.append(f'\t\t\tuql_event.{var} = {val}\n')

	with open(os.path.join(folder_path, 'uql_event_db.gd'), 'w') as file:
		file.writelines(code)
		pass

if __name__ == '__main__':
	folder_path = "QuestExamples"
	uql_content = turn_folder_to_uql(folder_path)
	codegen_info = extract_codegen_info(uql_content)
	generated_folder = os.path.join(folder_path, 'generated')
	if not os.path.exists(generated_folder):
		os.makedirs(generated_folder)
	generate_quest_datafile(uql_content, codegen_info, generated_folder)
	generate_event_class_file(uql_content, codegen_info, generated_folder)
	generate_event_db(uql_content, codegen_info, generated_folder)
	print(uql_content)