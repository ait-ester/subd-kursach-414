extends CanvasLayer

#@onready var scheme = $Scheme
@onready var camera_office = get_parent().get_node("camera_system/office1")
@onready var camera1 = get_parent().get_node("camera_system/Camera1")
@onready var camera2 = get_parent().get_node("camera_system/Camera2")
@onready var camera3 = get_parent().get_node("camera_system/Camera3")
@onready var camera4 = get_parent().get_node("camera_system/Camera4")
@onready var camera5 = get_parent().get_node("camera_system/Camera5")
@onready var camera6 = get_parent().get_node("camera_system/Camera6")
@onready var camera7 = get_parent().get_node("camera_system/Camera7")
@onready var camera8 = get_parent().get_node("camera_system/Camera8")
@onready var camera9 = get_parent().get_node("camera_system/Camera9")
@onready var camera10 = get_parent().get_node("camera_system/Camera10")
@onready var world = get_parent().get_node("camera_system/world")

@onready var animatronic = get_parent().get_node("enemey")  # Путь к аниматронику
@onready var battery_label = $charge 
var flashlight_battery = 100.0  # Заряд батареи (0-100)
var flashlight_drain = 100.0     # Сколько тратится за использование
var flashlight_recharge = 5   # Восстановление за секунду
var flashlight_cooldown = 0   # Время до следующего использования
var max_cooldown = 10          # Максимальный cooldown в секундах

func _ready():
	if camera_office == null:
		print("Ошибка: CameraOffice не найден!")
		return
	camera_office.make_current()

	if animatronic == null:
		print("Ошибка: Animatronic не найден!")
		return
	if battery_label:
		battery_label.text = "Battery: " + str(int(flashlight_battery)) + "%"


func _process(delta: float) -> void:
	if flashlight_battery < 100.0:
		flashlight_battery += flashlight_recharge * delta
		flashlight_battery = min(flashlight_battery, 100.0)
	if flashlight_cooldown > 0.0:
		flashlight_cooldown -= delta

	if battery_label:
		battery_label.text = "Battery: " + str(int(flashlight_battery)) + "%"


func _on_flash_pressed() -> void:
	if flashlight_cooldown <= 0.0 and flashlight_battery >= flashlight_drain:
		flashlight_battery -= flashlight_drain
		flashlight_cooldown = max_cooldown
		animatronic.flash_reset()  # Вызываем сброс
		#print("Вспышка активирована! Заряд: ", flashlight_battery)
	else:
		print("Вспышка не готова! Заряд: ", flashlight_battery, ", Cooldown: ", flashlight_cooldown)

# Обновите функции переключения камер, чтобы передавать правильную строку в аниматроник
func _on_button_city_1_pressed() -> void:
	camera1.make_current()
	animatronic.update_camera("camera1")  # Передаём строку
	#print("camera1")

func _on_button_city_2_pressed() -> void:
	camera2.make_current()
	animatronic.update_camera("camera2")
	#print("camera2")

func _on_button_city_3_pressed() -> void:
	camera3.make_current()
	animatronic.update_camera("camera3")
	#print("camera3")

func _on_button_city_4_pressed() -> void:
	camera4.make_current()
	animatronic.update_camera("camera4")
	#print("camera4")

func _on_button_city_5_pressed() -> void:
	camera5.make_current()
	animatronic.update_camera("camera5")
	#print("camera5")

func _on_button_city_6_pressed() -> void:
	camera6.make_current()
	animatronic.update_camera("camera6")
	#print("camera6")

func _on_button_city_7_pressed() -> void:
	camera7.make_current()
	animatronic.update_camera("camera7")
	#print("camera7")
	
func _on_button_city_8_pressed() -> void:
	camera8.make_current()
	animatronic.update_camera("camera8")
	#print("camera8")

func _on_button_city_9_pressed() -> void:
	camera9.make_current()
	animatronic.update_camera("camera9")
	#print("camera9")

func _on_button_city_10_pressed() -> void:
	camera10.make_current()
	animatronic.update_camera("camera10")
	#print("camera10")

func _on_comp_down_mouse_entered() -> void:
	camera_office.make_current()
	animatronic.update_camera("office")  # Для офиса
	#print("office")

func _on_world_pressed() -> void:
	world.make_current()
	# Для world можно не обновлять, если аниматроник не должен реагировать



#extends CanvasLayer
#
##@onready var scheme = $Scheme  # Схема (если нужно скрывать/показывать)
#@onready var camera_office = get_parent().get_node("camera_system/office1")
#@onready var camera1 = get_parent().get_node("camera_system/Camera1")
#@onready var camera2 = get_parent().get_node("camera_system/Camera2")
#@onready var camera3 = get_parent().get_node("camera_system/Camera3")
#@onready var camera4 = get_parent().get_node("camera_system/Camera4")
#@onready var camera5 = get_parent().get_node("camera_system/Camera5")
#@onready var camera6 = get_parent().get_node("camera_system/Camera6")
#@onready var camera7 = get_parent().get_node("camera_system/Camera7")
#@onready var world = get_parent().get_node("camera_system/world")
## Добавьте остальные камеры: camera3, camera4 и т.д.
#
#@onready var animatronic = get_parent().get_node("enemey")  # Замените на правильный путь к узлу аниматроника
#
## Переменные для вспышки
#var flashlight_battery = 100.0  # Заряд батареи (0-100)
#var flashlight_drain = 100.0     # Сколько тратится за использование
#var flashlight_recharge = 10   # Восстановление за секунду
#var flashlight_cooldown = 0   # Время до следующего использования
#var max_cooldown = 10          # Максимальный cooldown в секундах
#
#func _ready():
	#if camera_office == null:
		#print("Ошибка: CameraOffice не найден!")
		#return
	#camera_office.make_current()
	## Проверка на аниматроника
	#if animatronic == null:
		#print("Ошибка: Animatronic не найден!")
		#return
#func _process(delta: float) -> void:
	## Восстановление батареи и cooldown
	#if flashlight_battery < 100.0:
		#flashlight_battery += flashlight_recharge * delta
		#flashlight_battery = min(flashlight_battery, 100.0)
	#if flashlight_cooldown > 0.0:
		#flashlight_cooldown -= delta
#
## Функция для активации вспышки (вызывайте по сигналу кнопки)
#func _on_flash_pressed() -> void:
	#if flashlight_cooldown <= 0.0 and flashlight_battery >= flashlight_drain:
		#flashlight_battery -= flashlight_drain
		#flashlight_cooldown = max_cooldown
		#animatronic.flash_reset()  # Вызываем сброс аниматроника
		#print("Вспышка активирована! Заряд: ", flashlight_battery)
	#else:
		#print("Вспышка не готова! Заряд: ", flashlight_battery, ", Cooldown: ", flashlight_cooldown)
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
#func _on_comp_down_mouse_entered() -> void:
	#camera_office.make_current()
#func _on_world_pressed() -> void:
	#world.make_current()
