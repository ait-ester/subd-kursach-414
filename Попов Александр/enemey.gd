extends Node2D

var movement_oprtunity = {
	"room7": ["room6"],  # Из room7 только в room6
	"room6": ["room5", "room7"],  # Развилка: из room6 в room5 или обратно в room7\
	"room5": ["room4", "room6"],  # Из room5 только в room4 (можно добавить развилку, если нужно)
	"room4": ["room3", "room5"],
	"room3": ["room2", "room4"],
	"room2": ["room1", "room3"],
	"room1": ["office", "room7"],
	"office": []  # Конец пути, нет дальнейших комнат
}
var positions = {
	"office": Vector2(555, 383),
	"room1": Vector2(1929, -521),
	"room2": Vector2(2695, -336),
	"room3": Vector2(4266, -428),
	"room4": Vector2(2088, 227),
	"room5": Vector2(3096, 329),
	"room6": Vector2(3998, 146),
	"room7": Vector2(3379, 868)
}

var current_room = "room7"
var current_camera = "office"

# сопоставление камер и комнат
var camera_to_room = {
	"office": "office",
	"camera1": "room1",
	"camera2": "room2",
	"camera3": "room3",
	"camera4": "room4",
	"camera5": "room5",
	"camera6": "room6",
	"camera7": "room7"
}

@onready var game = $Gameover
#@onready var sprite = $Sprite2D
@onready var timer = $Timer

@onready var flash_sounds = [

	$roar1,  # Для room1 (индекс 0)
	$roar2,  # Для room2 (индекс 1)
	$roar3,  # Для room3 (индекс 2)
	$roar4,  # Для room4 (индекс 3)
	$roar5,  # Для room5 (индекс 4)
	$roar6,  # Для room6 (индекс 5)
	$roar7   # Для room7 (индекс 6)
]

func _ready():
	position = positions[current_room]
	timer.wait_time = randf_range(5, 5)
	timer.start()
	timer.connect("timeout", Callable(self, "_on_timer_timeout"))

func _on_timer_timeout():
	# Получаем список возможных следующих комнат для текущей
	var possible_next = movement_oprtunity.get(current_room, [])

	if possible_next.size() > 0:
		# Случайно выбираем одну из возможных комнат
		var next_room = possible_next[randi() % possible_next.size()]
		if current_room != current_camera:  # Это условие можно оставить или убрать, в зависимости от логики
			current_room = next_room
			position = positions[current_room]
		print("Аниматроник в ", current_room)
		if current_room == "office":
			print("Аниматроник в офисе!")
			game.visible = true
	timer.wait_time = randf_range(5, 5)
	timer.start()

func update_camera(new_camera: String):
	current_camera = new_camera
	if current_room == "office":
		print("Аниматроник в офисе!")

# сброс аниматроника при вспышке
func flash_reset():
	# комната, соответствующая текущей камере
	var camera_room = camera_to_room.get(current_camera, "")
	# Сброс, если аниматроник в той же комнате, что и камера
	if current_room == camera_room and current_room != "office":
		if current_room == "room7":
			$roar1.play()
		elif current_room == "room6":
			$roar2.play()
		elif current_room == "room5":
			$roar3.play()
		elif current_room == "room4":
			$roar4.play()
		elif current_room == "room3":
			$roar5.play()
		elif current_room == "room2":
			$roar6.play()
		elif current_room == "room1":
			$roar7.play()

			
		current_room = "room7"
		position = positions[current_room]
		timer.stop()
		timer.wait_time = randf_range(15, 15)  # Сброс таймера
		timer.start()
		print("успех вспышки")
	else:
		print("мимо!")







#extends Node2D
#
#var room_order = ["room7", "room6", "room5", "room4", "room3", "room2", "room1", "office"]
#var positions = {
	#"office": Vector2(555, 383),
	#"room1": Vector2(1929, -521),
	#"room2": Vector2(2695, -336),
	#"room3": Vector2(4266, -428),
	#"room4": Vector2(2088, 227),
	#"room5": Vector2(3096, 329),
	#"room6": Vector2(3998, 146),
	#"room7": Vector2(3379, 868)
#}
#
#var current_room = "room7"
#var current_camera = "office"
#
#@onready var game = $Gameover
#@onready var sprite = $Sprite2D
#@onready var timer = $Timer
#
#func _ready():
	#position = positions[current_room]
	#timer.wait_time = randf_range(8, 8)
	#timer.start()
	#timer.connect("timeout", Callable(self, "_on_timer_timeout"))
#
#func _on_timer_timeout():
	#var current_index = room_order.find(current_room)
	#if current_index < room_order.size() - 1:
		#var next_index = current_index + 1
		#var next_room = room_order[next_index]
		#if current_room != current_camera:
			#current_room = next_room
			#position = positions[current_room]
		#print("Аниматроник телепортировался в ", current_room)
		#if current_room == "office":
			#print("Аниматроник в офисе! Игра окончена.")
			#game.visible = true
	#timer.wait_time = randf_range(8, 8)
	#timer.start()
#
#func update_camera(new_camera: String):
	#current_camera = new_camera
	#if current_room == "office":
		#print("Аниматроник в офисе! Игра окончена.")
#
## Новая функция для сброса аниматроника при вспышке
#func flash_reset():
	## Проверяем, можно ли отпугнуть (например, если аниматроник в room1 или office)
	#current_room = "room7"
	#position = positions[current_room]
	#timer.stop()
	#timer.wait_time = randf_range(1, 1)  # Сброс таймера
	#timer.start()
	#print("Аниматроник отпугнут вспышкой и сброшен в room7!")
	#

#func flash_retreat():
	#var current_index = room_order.find(current_room)
	#var retreat_index = max(0, current_index - 2)  # Отойти на 2 комнаты назад, но не меньше 0
	#var retreat_room = room_order[retreat_index]
	#current_room = retreat_room
	#position = positions[current_room]
	#print("Аниматроник отступил в ", current_room)
	## Опционально: задержка перед следующим движением
	#timer.stop()
	#await get_tree().create_timer(5.0).timeout  # Задержка 5 секунд
	#timer.start()
	#
