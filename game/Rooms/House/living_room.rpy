default livingRoomRalphIsHere = False
default livingRoomRalphSuffix = ""
default livingRoomBettySuffix = 1

label living_room:
    $ print "enter_living_room"
    $ miniMapData = []
    call miniMapHouseGenerate() from _call_miniMapHouseGenerate_2

    $ scene_image = "scene_House_LivingRoom[day_suffix]"

    $ livingRoomRalphIsHere = True if get_active_objects("Ralph") != False else False
    music houseMusic
    return

label living_room_init:

    $ monica_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "House_LivingRoom_Monica_[cloth][day_suffix]", "click" : "living_room_environment", "actions" : "l", "zorder":11, "tint": monica_tint}, {"monicaCleaningInProgress":{"v":True, "base":"House_LivingRoom_Monica_[cloth]_Cleaning_[monicaCleaningObject]", "stop":True}, "livingRoomRalphIsHere":{"v":True, "base" : "House_LivingRoom_Ralph_Monica_[cloth][day_suffix]"}})

#        $ scene_image = "scene_House_LivingRoom_Ralph_Monica_" + cloth + day_suffix
#        $ add_object_to_scene("Monica", {"type" : 2, "base" : "House_LivingRoom_Ralph_Monica_" + cloth + day_suffix, "click" : "living_room_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
    $ add_object_to_scene("Ralph", {"type" : 2, "base" : "House_LivingRoom_Ralph[livingRoomRalphSuffix][day_suffix]", "click" : "ralphInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})


#    $ add_object_to_scene("Chair1", {"type":2, "base":"House_LivingRoom_Chair1", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chair2", {"type":2, "base":"House_LivingRoom_Chair2", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Chair3", {"type":2, "base":"House_LivingRoom_Chair3", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_LivingRoom_Chair3_Dust"}})
    $ add_object_to_scene("Chair4", {"type":2, "base":"House_LivingRoom_Chair4", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_LivingRoom_Chair4_Dust"}})
    $ add_object_to_scene("Chandelier", {"type":2, "base":"House_LivingRoom_Chandelier", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("DinnerTable", {"type":2, "base":"House_LivingRoom_DinnerTable", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Sofa", {"type":2, "base":"House_LivingRoom_Sofa", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_LivingRoom_Sofa_Dust"}})
    $ add_object_to_scene("TableLamp1", {"type":2, "base":"House_LivingRoom_TableLamp1", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"House_LivingRoom_TableLamp1_Dust"}})
    $ add_object_to_scene("TableLamp2", {"type":2, "base":"House_LivingRoom_TableLamp2", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("TV", {"type":2, "base":"House_LivingRoom_TV", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Wine1", {"type":2, "base":"House_LivingRoom_Wine1", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Wine2", {"type":2, "base":"House_LivingRoom_Wine2", "click" : "living_room_environment", "actions" : "l", "zorder" : 0, "group":"environment"})

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ХОЛЛ"), "larrow" : "arrow_left_2", "base":"House_LivingRoom_Teleport_Floor1", "click" : "living_room_teleport", "xpos" : 460, "ypos" : 956, "zorder":20, "teleport":True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label living_room_init_additional1:
    $ add_object_to_scene("Ralph", {"type" : 2, "base" : "House_LivingRoom_Ralph[livingRoomRalphSuffix][day_suffix]", "click" : "ralphInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"}, scene="living_room")
    return

label living_room_teleport:
    if obj_name == "Teleport_Floor1":
        call change_scene("floor1") from _call_change_scene_40
        return
    return

label living_room_environment:
    if obj_name == "Monica":
        mt "Не помню когда я здесь была в последний раз."
        "Кажется когда запретила мужу приводить гостей."
        return
    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4":
        mt "Здесь много стульев, но я не разрешала мужу приводить сюда гостей."
        "Эта новые хозяева любят принимать гостей, хвастаются моим домом."
        "Когда я верну дом себе, то выкину эту мебель и вообще переделаю весь дизайн дома."
        "Чтобы ничего не напоминало мне об этом кошмаре, в который я, по-прежнему, не могу поверить!"
    if obj_name == "Chandelier":
        mt "Эта люстра особенно опасна!!!"
    if obj_name == "DinnerTable":
        mt "Это обеденный стол."
        "Я предпочитала обедать на кухне, как в детстве..."
        "Эххх...."
    if obj_name == "Sofa":
        mt "Удобный диван..."
        "МОЙ!!!"
    if obj_name == "TableLamp1" or obj_name == "TableLamp2":
        mt "Хоть у меня и отобрали дом... пока..."
        "Но эти лампочки светят только для меня!"
    if obj_name == "TV":
        mt "Дурацкий телевизор..."
        "Может быть мне что-то украсть отсюда, чтобы продать?"
        if monicaKitchenForbidden == True:
            mt "Хотя эта Бетти, кажется, переписала все вещи в доме и она следит за мной..."
    if obj_name == "Wine1" or obj_name == "Wine2":
        mt "Похоже это вино Бетти специально оставила здесь."
        "Как ловушку для меня..."
        "Они только ищет повод выгнать меня отсюда!"
        "Мне надо быть осторожной..."
    return
