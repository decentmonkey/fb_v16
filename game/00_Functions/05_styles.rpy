init:
    style c_gray:
        color "#808080"
    style c_darkgray:
        color "#303030"
    style c_green:
        color "#31e8b1"
    style c_blue:
        color "#31b1e8"
    style c_pink:
        color "#e831b1"
    style c_orange:
        color "#e8b131"
    style c_red:
        color "#e80000"
    style c_white:
        color "#ffffff"

    define c_gray = "#808080"
    define c_darkgray = "#303030"
    define c_green = "#31e8b1"
    define c_blue = "#31b1e8"
    define c_pink = "#e831b1"
    define c_orange = "#e8b131"
    define c_red = "#e80000"
    define c_white = "#ffffff"

    style sprite_test1:
        xpadding 15
        ypadding 15

    style sprite_textbutton is button:
#        background "#18181a"
        xpadding 15
        ypadding 15

#            outlines [(0, "#000000", 1, 1)]
#    outlines [(0, "#000000", 0, 0)]
#    outlines [(0, "#696935", 1, 1)]


    transform imagebutton_hover_type1(idle_num):
        on idle:
            linear idle_num alpha 0.0

        on show, start:
            alpha 0.0
#            pause 0.01
#            alpha 0.0

        on hover:
#            alpha 0.0
#            linear 0.2 alpha 1.0
            pause 0.02
            alpha 1.0
#        function init_idle_transform



    transform hover_text_sprite_transform():
#        zoom zoom_factor
        on show, start, idle:
#            alpha 0.0
#            linear 0.2 alpha 1.0
            alpha 1.0

        on hide:
            alpha 1.0
            linear 0.4 alpha 0.0

    style action_menu_screen_actions_buttons is button:
        background "#303030"

        hover_background "#808080"

    transform dialogue_image_left():
#        zoom zoom_factor
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5

    transform dialogue_image_right():
#        zoom zoom_factor
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5

    transform dialogue_image_center():
#        zoom zoom_factor
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5

    style dialogue_image_left_style:
        xmaximum 100

    transform dialogue_down_arrow_transform():
        xalign 0.5
        yalign 1.0
        alpha 0
        pause 0.6
        alpha 1
        pause 0.6
        repeat

    transform map_icon_button_transform():
        on idle:
            alpha 0.0

        on hover:
            alpha 0.0
            linear 0.5 alpha 1.0

    transform mega_test_image_anim:
#        on idle:
#            "icons/map_icon2_idle.png" with Dissolve(0.5, alpha=True)
        on hover:
            "icons/map_icon2_hover.png" with Dissolve(0.5, alpha=True)

    image mega_test_image:
        "icons/map_icon2_idle.png"
#        with None
        "icons/map_icon2_hover.png" with Dissolve(0.5, alpha=True)
        repeat


    transform bitchmeter_style_transform():
        rotate_pad False
        rotate -90.0
    transform corruption_style_transform():
        rotate_pad False
        rotate 90.0

    transform convert_resolution_transform():
#        zoom zoom_factor

transform photoshoot_transform(idle_num):
    alpha 0.8
    linear 0.7 alpha 0.0

transform photoshoot_transform2(idle_num):
    alpha 0.3
    linear 0.4 alpha 0.0

style menu_choice_empty_background_button:
    background None

default objectivesFont = "fonts/OpenSans-Regular.ttf"

style choice_button_disabled_text:
    color "#666666"
    xalign 0.5

style choice_button_disabled_text_chinese:
    color "#666666"
    xalign 0.5
    font gui.text_font_chinese

style choice_button_text_chinese:
    xalign 0.5
    font gui.text_font_chinese

style text_chinese:
    font gui.text_font_chinese

transform credits_black_overlay:
    alpha 0.0
    linear 5.0 alpha 0.8

transform quest_log_transform:
    alpha 1.0
    linear 0.5 alpha 0.3
    linear 0.5 alpha 1.0
    repeat

transform camera_record_icon_transform:
    "images/Icons2/Rec_Icon1.png"
    pause 0.4
    "images/Icons2/Rec_Icon2.png"
    pause 0.4
    repeat

transform pole_dance_shake:
    anchor (0.5,0.5)
    pos (0.5, 0.5)
    ease 1.0 zoom 1.1 xpos 0.51 ypos 0.53 zoom 1.06
    ease 1.0 zoom 1.0 xpos 0.49 ypos 0.48 zoom 1.1
    ease 1.0 zoom 1.1 xpos 0.51 ypos 0.53 zoom 1.06
    ease 1.0 zoom 1.0 xpos 0.49 ypos 0.47 zoom 1.13
    ease 1.0 zoom 1.1 xpos 0.52 ypos 0.53 zoom 1.06
    ease 1.0 zoom 1.0 xpos 0.49 ypos 0.48 zoom 1.1
    ease 1.0 zoom 1.1 xpos 0.52 ypos 0.47 zoom 1.06
    ease 1.0 zoom 1.0 xpos 0.49 ypos 0.49 zoom 1.1
    ease 1.0 zoom 1.0 xpos 0.5 ypos 0.5 zoom 1.1
    repeat

transform blur(child):
    contains:
        child
        alpha 1.0
    contains:
        child
        alpha 0.2 xoffset -30
    contains:
        child
        alpha 0.2 xoffset 30
    contains:
        child
        alpha 0.2 yoffset -30
    contains:
        child
        alpha 0.2 yoffset 30
#translate german python:
#    objectivesFont = "fonts/OpenSans-Regular.ttf"
