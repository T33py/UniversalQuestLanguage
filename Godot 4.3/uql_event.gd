class_name UQLEvent
enum Types {
	QUEST,
	BREADCRUMB,
	ITEM,
}

var id: int = 0
var name: String = ""
var type: Types = Types.QUEST
var requires: Array[String] = []
var description: String = ""
var tooltip: String = ""
var rewards: Array[String] = []
var activates: Array[int] = []
var related_quests: Array[int] = []

var data: Dictionary = {}

@warning_ignore("shadowed_variable")
func setup(data: Dict):
	self.data = data
	id = data.get("id", 0)
	name = data.get("name", "")
	type = Types[data.get("type", "QUEST").upper()]
	requires = data.get("requires", [])
	description = data.get("description", "")
	tooltip = data.get("tooltip", "")
	rewards = data.get("rewards", [])
	activates = data.get("activates", [])
	related_quests = data.get("related_quests", [])
	pass