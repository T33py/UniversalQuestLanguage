class_name UQLEventDB

var all_events: Array[UQLEvent] = []
var raw_data: UQLRawData = UQLRawData.new()

func _init():
	all_events.resize(raw_data.max_id)
	parse_raw_data()
	return

func parse_raw_data():
	for event in raw_data.events:
		var uql_event = UQLEvent.new()
