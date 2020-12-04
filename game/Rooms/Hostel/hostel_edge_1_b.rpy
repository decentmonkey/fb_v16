label hostel_edge_1_b:
    $ print "enter_hostel_edge_1_b"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_4

    $ sceneIsStreet = True

    $ localDaySuffix = ""
    if day_suffix != "":
        $ localDaySuffix = day_suffix + "2"
    $ scene_image = "scene_hostel_edge_1_b[localDaySuffix]"
    return

label hostel_edge_1_b_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_b_Monica_[cloth][localDaySuffix]", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 15})

    $ add_object_to_scene("Bottle", {"type":2, "base":"hostel_edge_1_b_bottle", "click" : "take_trash_bottle", "actions" : "lh", "zorder" : 12})

    $ add_object_to_scene("Door1", {"type":2, "base":"Hostel_Edge_1_b_Door1", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Door2", {"type":2, "base":"Hostel_Edge_1_b_Door2", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Door3", {"type":2, "base":"Hostel_Edge_1_b_Door3", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Fence", {"type":2, "base":"Hostel_Edge_1_b_Fence", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Trash1", {"type":2, "base":"hostel_edge_1_b_Trash1", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Trash2", {"type":2, "base":"hostel_edge_1_b_Trash2", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Trash3", {"type":2, "base":"hostel_edge_1_b_Trash3", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Trash4", {"type":2, "base":"hostel_edge_1_b_Trash4", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Trash5", {"type":2, "base":"hostel_edge_1_b_Trash5", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Window1", {"type":2, "base":"hostel_edge_1_b_Window1", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Window2", {"type":2, "base":"hostel_edge_1_b_Window2", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Window3", {"type":2, "base":"hostel_edge_1_b_Window3", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Window4", {"type":2, "base":"hostel_edge_1_b_Window4", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
    $ add_object_to_scene("Window5", {"type":2, "base":"hostel_edge_1_b_Window5", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"evnironment"})
#    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"hostel_edge_1_b_Teleport_Hostel_Edge_a", "click" : "hostel_edge_1_b_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8]})

    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":3, "text" : t_("ДРУГАЯ СТОРОНА"), "rarrow" : "arrow_right_2", "base":"Hostel_Edge_1_b_Teleport_Hostel_Edge_A", "click" : "hostel_edge_1_b_teleport", "xpos" : 1670, "ypos" : 910, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Hostel_1_c", {"type":3, "text" : t_("УЛИЦА"), "larrow" : "arrow_left_2", "base":"Hostel_Edge_1_b_Teleport_Hostel_Edge_C", "click" : "hostel_edge_1_b_teleport", "xpos" : 600, "ypos" : 963, "zorder":15, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_edge_1_b_teleport:
    if obj_name == "Teleport_Hostel_1_c":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot") from _call_change_scene_31
            return
        call change_scene("hostel_edge_1_c") from _call_change_scene_32
        return
    if obj_name == "Teleport_Hostel_1_a":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_a", "Fade", "snd_walk_barefoot") from _call_change_scene_33
            return
        call change_scene("hostel_edge_1_a") from _call_change_scene_34
        return
    return
label hostel_edge_1_b_environment:
    if obj_name == "Monica":
        pass

    if obj_name == "Fence":
        mt "Железный забор..."
        "Нет, я преодолею все заборы в моей жизни!!!"
        "Я не сдамся!!!"

    if obj_name == "Door1":
        mt "Какая-то дверь..."
    if obj_name == "Door2":
        mt "Какая-то дверь..."
    if obj_name == "Door3":
        mt "Какая-то дверь..."

    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5":
        mt "Просто мусор..."
    if obj_name == "Window1" or obj_name == "Window2" or obj_name == "Window3" or obj_name == "Window4":
        mt "Заколоченное окно..."
    if obj_name == "Window5":
        mt "Какое-то окно..."

    return
