extends CanvasLayer


func _ready():
	# Скрываем виды камер по умолчанию
	office1.visible = true
	view1.visible = false
	view2.visible = false
	view3.visible = false
	view4.visible = false
	view5.visible = false
	view6.visible = false
	view7.visible = false
	
	

func back_to_scheme():
	scheme.visible = true
	view1.visible = false
	view2.visible = false


func _on_city_1_pressed() -> void:
	office1.visible = false
	view1.visible = true
	view2.visible = false
	view3.visible = false
	view4.visible = false
	view5.visible = false
	view6.visible = false
	view7.visible = false


func _on_city_2_pressed() -> void:
	office1.visible = false
	view1.visible = false
	view2.visible = true
	view3.visible = false
	view4.visible = false
	view5.visible = false
	view6.visible = false
	view7.visible = false


func _on_city_3_pressed() -> void:
	office1.visible = false
	view1.visible = false
	view2.visible = false
	view3.visible = true
	view4.visible = false
	view5.visible = false
	view6.visible = false
	view7.visible = false


func _on_city_4_pressed() -> void:
	office1.visible = false
	view1.visible = false
	view2.visible = false
	view3.visible = false
	view4.visible = true
	view5.visible = false
	view6.visible = false
	view7.visible = false


func _on_city_5_pressed() -> void:
	office1.visible = false
	view1.visible = false
	view2.visible = false
	view3.visible = false
	view4.visible = false
	view5.visible = true
	view6.visible = false
	view7.visible = false


func _on_city_6_pressed() -> void:
	office1.visible = false
	view1.visible = false
	view2.visible = false
	view3.visible = false
	view4.visible = false
	view5.visible = false
	view6.visible = true
	view7.visible = false


func _on_city_7_pressed() -> void:
	office1.visible = false
	view1.visible = false
	view2.visible = false
	view3.visible = false
	view4.visible = false
	view5.visible = false
	view6.visible = false
	view7.visible = true
