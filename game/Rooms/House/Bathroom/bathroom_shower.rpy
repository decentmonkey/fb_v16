label bathroom_shower:
    $ print "enter_bathroom_shower"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_16

    $ scene_image = "scene_Bathroom_Shower"
    return

label bathroom_shower_init:
    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Shower_Monica_[cloth]", "click" : "bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Shower", {"type":2, "base":"Bathroom_Shower_Shower", "click" : "bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "bathroom_teleport", "xpos" : 990, "ypos" : 956, "zorder":11, "high_sprite_hover": True, "teleport":True})
    $ add_object_to_scene("Teleport_Bathroom_Bath", {"type":3, "text" : t_("ВАННА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "bathroom_teleport", "xpos" : 240, "ypos" : 520, "zorder":11, "teleport":True})

    return
