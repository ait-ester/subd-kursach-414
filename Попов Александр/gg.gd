extends Node2D
#@onready var sound $sound
@onready var timer = $Timer
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	timer.start()
	#sound.play()


func _on_timer_timeout() -> void:
	get_tree().change_scene_to_file("res://ui.tscn")
