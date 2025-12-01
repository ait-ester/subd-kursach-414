extends Node2D

@onready var hour = $hour
@onready var label_hours = $CanvasLayer/hours 
var AM = 0

func _ready() -> void:
	hour.start()
	label_hours.text = str(int(AM)) + "AM"
	
	

func _process(_delta: float) -> void:
	label_hours.text = str(int(AM)) + "AM"
	
func _on_hour_timeout() -> void:
	print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
	if AM < 5:
		AM += 1
	else:
		AM = 6
		victory()
func victory():
	get_tree().change_scene_to_file("res://victory.tscn")
