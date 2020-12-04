default hostel_edge_1_a_visited = False

default monicaHostelEdge1ASuffix = ""
default monicaHostelEdge1ASuffixOneTime = False

default hostel_edge_1_a_ep24_inited = False

label hostel_edge_1_a:
    $ print "enter_hostel_edge_1_a"
    $ miniMapData = []
    call miniMapHostelGenerate() from _call_miniMapHostelGenerate_2

    $ sceneIsStreet = True

    if hostel_edge_1_a_ep24_inited == False:
        call hostel_edge_1_a_init_additional1() from _call_hostel_edge_1_a_init_additional1
        $ hostel_edge_1_a_ep24_inited = True

    $ localDaySuffix = ""
    if day_suffix != "":
        $ localDaySuffix = day_suffix + "2"
    $ scene_image = "scene_hostel_edge_1_a[localDaySuffix]"

    $ monicaHostelEdge1ASuffix = ""
    if monicaHostelEdge1ASuffixOneTime != False:
        $ monicaHostelEdge1ASuffix = monicaHostelEdge1ASuffixOneTime
        $ monicaHostelEdge1ASuffixOneTime = False

    $ hostel_edge_1_a_visited = True
    return

label hostel_edge_1_a_init:

    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_a_Monica_[cloth][monicaHostelEdge1ASuffix][localDaySuffix]", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 15})

    $ add_object_to_scene("Bar24", {"type":2, "base":"Hostel_Edge_1_a_Bar24", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Boxes", {"type":2, "base":"Hostel_Edge_1_a_Boxes", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Door1", {"type":2, "base":"Hostel_Edge_1_a_Door1", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Door2", {"type":2, "base":"Hostel_Edge_1_a_Door2", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Letters", {"type":2, "base":"Hostel_Edge_1_a_Letters", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Poster", {"type":2, "base":"Hostel_Edge_1_a_Poster", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 12, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Pylon", {"type":2, "base":"Hostel_Edge_1_a_Pylon", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Hostel_Edge_1_a_Trash1", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Hostel_Edge_1_a_Trash2", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Hostel_Edge_1_a_Trash3", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Hostel_Edge_1_a_Trash4", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Hostel_Edge_1_a_Trash5", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Window1", {"type":2, "base":"Hostel_Edge_1_a_Window1", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Window2", {"type":2, "base":"Hostel_Edge_1_a_Window2", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
    $ add_object_to_scene("Window3", {"type":2, "base":"Hostel_Edge_1_a_Window3", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 11, "b":0.13, "group":"environment"})
#    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"hostel_edge_1_a_Teleport_Hostel_Edge_a", "click" : "hostel_edge_1_a_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8]})

    $ add_object_to_scene("Teleport_Hostel_1_c", {"type":3, "text" : t_("УЛИЦА"), "rarrow" : "arrow_right_2", "base":"Hostel_Edge_1_a_Teleport_Hostel_Edge_C", "click" : "hostel_edge_1_a_teleport", "xpos" : 1800, "ypos" : 780, "zorder":15, "teleport":True})
    $ add_object_to_scene("Teleport_Hostel_1_b", {"type":3, "text" : t_("ДРУГАЯ СТОРОНА"), "larrow" : "arrow_down_2", "base":"Hostel_Edge_1_a_Teleport_Hostel_Edge_B", "click" : "hostel_edge_1_a_teleport", "xpos" : 550, "ypos" : 933, "zorder":15, "teleport":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_edge_1_a_init_additional1:
    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_a_Monica_[cloth][monicaHostelEdge1ASuffix][localDaySuffix]", "click" : "hostel_edge_1_a_environment", "actions" : "l", "zorder" : 15})
    return
label hostel_edge_1_a_teleport:
    if obj_name == "Teleport_Hostel_1_c":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot") from _call_change_scene_10
            return
        call change_scene("hostel_edge_1_c") from _call_change_scene_11
        return
    if obj_name == "Teleport_Hostel_1_b":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_b", "Fade", "snd_walk_barefoot") from _call_change_scene_12
            return
        call change_scene("hostel_edge_1_b") from _call_change_scene_13
        return
    return
label hostel_edge_1_a_environment:
    if obj_name == "Monica":
        pass

    if obj_name == "Bar24":
        mt "Бар24?"
        "Это вывеска от какого-то бара."
        "Выброшенная..."
    if obj_name == "Boxes":
        mt "Какие-то коробки..."
        "Пустые..."
    if obj_name == "Door1":
        mt "Какая-то дверь..."
    if obj_name == "Door2":
        mt "Дверь? Там???"
    if obj_name == "Letters":
        mt "Выброшенные буквы от вывесок..."
    if obj_name == "Poster":
        mt "Старый выброшенный постер..."
    if obj_name == "Pylon":
        mt "ЭТО ЧТО???"
        "ПИЛОН???"
        "ЗДЕСЬ???"
    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5":
        mt "Просто мусор..."
    if obj_name == "Window1" or obj_name == "Window2" or obj_name == "Window3":
        mt "Заколоченное окно..."

    return
