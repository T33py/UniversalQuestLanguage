class_name UQLEventDB

var all_events: Array[UQLEvent] = []
var quests: Array[UQLEvent] = []
var raw_data: UQLRawData = UQLRawData.new()

func _init():
	all_events.resize(raw_data.max_id + 1)
	parse_raw_data()
	return

func parse_raw_data():
	for event in raw_data.events:
		var uql_event = UQLEvent.new()
		all_events[event["ID"]] = uql_event
		if event["TYPE"] == UQLEvent.EventType.QUEST:
			quests.append(uql_event)
