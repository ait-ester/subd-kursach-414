extends Control

# Глобальная переменная для сложности (можно использовать Autoload для доступа из других сцен)
var selected_difficulty = "Normal"  # По умолчанию

@onready var button_easy = $CanvasLayer/easy
@onready var button_normal = $CanvasLayer/normal
@onready var button_brutal = $CanvasLayer/brutal


func _on_easy_pressed():
	selected_difficulty = "Easy"
	_start_game()

func _on_normal_pressed():
	selected_difficulty = "Normal"
	_start_game()

func _on_brutal_pressed():
	selected_difficulty = "Hard"
	_start_game()

func _start_game():
	# Загружаем основную сцену
	get_tree().change_scene_to_file("res://main_2d.tscn")
