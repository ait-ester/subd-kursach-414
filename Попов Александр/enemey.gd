extends Node2D

var movement_oprtunity = {
	"start1": ["room9", "room8"],
	"room9": ["room7", "room6", "room8"],
	"room8": ["room6", "room5", "room9"],
	"room7": ["room4", "room6", "room9"],  
	"room6": ["room4", "room3", "room7", "room5", "room9", "room8"],  
	"room5": ["room3", "room6", "room8"],  
	"room4": ["office", "room3", "room6", "room7"],
	"room3": ["office", "room4", "room6", "room5"],
	"room2": ["room1", "room3"], # НЕ ИСПОЛЬЗУЕТСЯ 
	"room1": ["office", "room7"], # НЕ ИСПОЛЬЗУЕТСЯ
	"office": []  # Конец пути, нет дальнейших комнат
}
var positions = {
	"office": Vector2(555, 383),
	"room1": Vector2(674, -424),
	"room2": Vector2(1413, -553),
	"room3": Vector2(2928, -473),
	"room4": Vector2(4231, -439),
	"room5": Vector2(5526, -481),
	"room6": Vector2(2185, 393),
	"room7": Vector2(2991, 251),
	"room8": Vector2(3691, 290),
	"room9": Vector2(4756, 269),
	"start1": Vector2(5562, 285),
}

var current_room = "start1"
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
	"camera7": "room7",
	"camera8": "room8",
	"camera9": "room9",
	"camera10": "start1",
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
	timer.start()

func _on_timer_timeout():
	# Получаем список возможных следующих комнат для текущей
	var possible_next = movement_oprtunity.get(current_room, [])
	#print(possible_next)
	if possible_next.size() > 0:
		var next_room
		if current_room == "start1":
			var cam8 = possible_next[0]
			var cam9 = possible_next[1]
			
			var weighted_choices = [cam8, cam9] 
			print(weighted_choices)
			next_room = weighted_choices[randi() % weighted_choices.size()]
		elif possible_next.size() == 2: # используется для start1

			var forward_room = possible_next[0] #первая комната в масссиве 
			var back_room = possible_next[1] #вторая комната

			var weighted_choices = [forward_room, forward_room, forward_room, back_room] # зависит от числа значений а этом показателе, тоесть тут шансы 
			print(weighted_choices)
			next_room = weighted_choices[randi() % weighted_choices.size()]

		elif possible_next.size() == 3: # используется для комнат 9, 8, 7, 5

			var forward_room = possible_next[0] #первая комната
			var middle_room = possible_next[1] #вторая комната
			var back_room = possible_next[2] #третья комната

			var weighted_choices = [forward_room, forward_room, middle_room, middle_room, back_room]
			print(weighted_choices)
			next_room = weighted_choices[randi() % weighted_choices.size()]

		elif possible_next.size() == 4: #используется для комнат 4, 3
			var office_room = possible_next[0] #первая комната
			var middle_room = possible_next[1] #вторая комната
			var main_room = possible_next[2] #третья комната (центральная)
			var back_room = possible_next[3] #четвёртая комната

			var weighted_choices = [office_room, office_room, office_room, office_room, office_room, middle_room, middle_room, middle_room, main_room, main_room, back_room] #надо будет вычислить проценты передвижения
			print(weighted_choices)
			next_room = weighted_choices[randi() % weighted_choices.size()]

		elif possible_next.size() == 5: #ПУСТЬ БУДЕТ НА ВСЯКИЙ СЛУЧАЙ (НЕ ИСПОЛЬЗУЕТСЯ)
			var forward_room = possible_next[0] #первая комната
			var neighbor_room = possible_next[1] #вторая комната
			var middle_room = possible_next[2] #третья комната
			var main_room = possible_next[3] #четвёртая комната
			var back_room = possible_next[4] #пятая комната

			var weighted_choices = [forward_room, neighbor_room, middle_room, main_room, back_room]#надо будет вычислить проценты передвижения
			print(weighted_choices)
			next_room = weighted_choices[randi() % weighted_choices.size()]

		elif possible_next.size() == 6: #используется для центральной комнаты 6
			var forward_room = possible_next[0] #первая комната
			var foforward_room = possible_next[1] #вторая комната
			var neighbor_room = possible_next[2] #третья комната
			var middle_room = possible_next[3] #четвёртая комната
			var main_room = possible_next[4] #пятая комната
			var back_room = possible_next[5] #шестая комната

			var weighted_choices = [forward_room, forward_room, forward_room, forward_room, forward_room, forward_room, foforward_room, foforward_room, foforward_room, foforward_room, foforward_room, foforward_room, neighbor_room, neighbor_room, middle_room, middle_room, main_room, back_room]#надо будет вычислить проценты передвижения
			print(weighted_choices)
			next_room = weighted_choices[randi() % weighted_choices.size()]
		else:
			# Если нет развилок
			next_room = possible_next[0]
		
		if current_room != current_camera:  # Это условие можно оставить или убрать, в зависимости от логики
			current_room = next_room
			position = positions[current_room]
		print("Аниматроник в ", current_room)
		if current_room == "office":
			print("Аниматроник в офисе!")
			game.visible = true
			get_tree().change_scene_to_file("res://gg.tscn")


func update_camera(new_camera: String):
	current_camera = new_camera

# сброс аниматроника при вспышке	## Проверяем, можно ли отпугнуть (например, если аниматроник в room1 или office)
func flash_reset():
	# комната, соответствующая текущей камере
	var camera_room = camera_to_room.get(current_camera, "")
	# Сброс, если аниматроник в той же комнате, что и камера
	if current_room == camera_room and current_room != "office":
		if current_room == "room9":
			$roar1.play()
		elif current_room == "room8":
			$roar1.play()
		elif current_room == "room7":
			$roar5.play()
		elif current_room == "room6":
			$roar5.play()
		elif current_room == "room5":
			$roar5.play()
		elif current_room == "room4":
			$roar7.play()
		elif current_room == "room3":
			$roar7.play()
		elif current_room == "room2": #ЭТИ ДВЕ КОМНАТЫ НЕ ИСПОЛЬЗУЮТСЯ (ROOM1 И ROOM2)
			$roar6.play()
		elif current_room == "room1": #ЭТИ ДВЕ КОМНАТЫ НЕ ИСПОЛЬЗУЮТСЯ (ROOM1 И ROOM2)
			$roar7.play()
		elif current_room == "office": #ЭТИ ДВЕ КОМНАТЫ НЕ ИСПОЛЬЗУЮТСЯ (ROOM1 И ROOM2)
			$roar1.play()
			
		current_room = "start1"
		position = positions[current_room]
		timer.stop()
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
## функция для сброса аниматроника при вспышке
#func flash_reset():
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
