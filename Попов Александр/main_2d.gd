#extends Node2D
#
#@onready var scheme = $Scheme  # Схема (если нужно скрывать/показывать)
#@onready var camera_office = get_parent().find_node("office1")
#@onready var camera1 = get_parent().find_node("Camera1")
#@onready var camera2 = get_parent().find_node("Camera2")
#@onready var camera3 = get_parent().find_node("Camera3")
#@onready var camera4 = get_parent().find_node("Camera4")
#@onready var camera5 = get_parent().find_node("Camera5")
#@onready var camera6 = get_parent().find_node("Camera6")
#@onready var camera7 = get_parent().find_node("Camera7")
## Добавьте остальные камеры: camera3, camera4 и т.д.
#
#func _ready():
	## Проверки на null (для отладки)
	#if camera_office == null:
		#print("Ошибка: CameraOffice не найден!")
		#return
	## Аналогично для других
	#
	## По умолчанию активна камера офиса
	#camera_office.make_current()
	#
#func _on_button_city_1_pressed() -> void:
	#camera1.make_current()
#func _on_button_city_2_pressed() -> void:
	#camera2.make_current()
#func _on_button_city_3_pressed() -> void:
	#camera3.make_current()
#func _on_button_city_4_pressed() -> void:
	#camera4.make_current()
#func _on_button_city_5_pressed() -> void:
	#camera5.make_current()
#func _on_button_city_6_pressed() -> void:
	#camera6.make_current()
#func _on_button_city_7_pressed() -> void:
	#camera7.make_current()
#
#func back_to_office():
	#camera_office.make_current()
	#scheme.visible = true 
