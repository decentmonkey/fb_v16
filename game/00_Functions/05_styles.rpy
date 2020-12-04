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


style questhelp_category_failed_selected:
    color "e80000"
    background "#202020"
    hover_background "#220000"

style questhelp_category_failed_selected_text:
    color "e80000"
    font "fonts/BebasNeue Regular.ttf"

style questhelp_category_failed:
    color "e80000"
#    hover_background "#220000"
    hover_background "#220F11"

style questhelp_category_failed_bold_selected:
    color "e80000"
    background "#202020"
    hover_background "#220000"

style questhelp_category_failed_bold:
    color "e80000"
    hover_background "#220000"

style questhelp_category_failed_bold_text:
    color "e80000"
    font "fonts/BebasNeue Regular.ttf"
    bold True

style questhelp_category_failed_bold_selected_text:
    color "e80000"
    font "fonts/BebasNeue Regular.ttf"
    bold True

style questhelp_category_failed_text:
    color "#720000"
    hover_color "#910000"
    font "fonts/BebasNeue Regular.ttf"
#    bold True


style questhelp_category_completed_selected:
    color "#31e8b1"
    background "#202020"
    hover_background "#12543D"

style questhelp_category_completed_bold_selected:
    color "#31e8b1"
    background "#202020"
    hover_background "#12543D"

style questhelp_category_completed_selected_text:
    color "#31e8b1"
    hover_color "38FFBC"
    font "fonts/BebasNeue Regular.ttf"

style questhelp_category_completed:
#    hover_background "#12543D"
    hover_background "#072117"

style questhelp_category_completed_bold:
    color "#31e8b1"
    hover_background "#12543D"

style questhelp_category_completed_bold_text:
    color "#31e8b1"
    hover_color "38FFBC"
    font "fonts/BebasNeue Regular.ttf"
    bold True

style questhelp_category_completed_bold_selected_text:
    color "#31e8b1"
    hover_color "38FFBC"
    font "fonts/BebasNeue Regular.ttf"
    bold True

style questhelp_category_completed_text:
    color "#197254"
    hover_color "#1E8964"
#    color "#31e8b1"
#    hover_color "38FFBC"
    font "fonts/BebasNeue Regular.ttf"


style questhelp_category_active_selected:
    hover_background "#2D210A"
    background "#202020"

style questhelp_category_active_bold_selected:
    hover_background "#2D210A"
    background "#202020"

style questhelp_category_active_selected_text:
    color "#e8b131"
    hover_color "#FFC038"
    font "fonts/BebasNeue Regular.ttf"

style questhelp_category_active:
    hover_background "#2D210A"

style questhelp_category_active_bold:
#    color "#e8b131"
#    background "#7A5A1A"
    hover_background "#2D210A"

style questhelp_category_active_bold_text:
    color "#e8b131"
    hover_color "#FFC038"
    font "fonts/BebasNeue Regular.ttf"
    bold True

style questhelp_category_active_bold_selected_text:
    color "#e8b131"
    hover_color "#FFC038"
    font "fonts/BebasNeue Regular.ttf"
    bold True

style questhelp_category_active_text:
    color "#E0E0E0"
    hover_color "#F7F7F7"
    font "fonts/BebasNeue Regular.ttf"

style questhelp_category_description:
    color "#E0E0E0"
    size 24


style questhelp_quest_failed:
    hover_background "#220F11"

style questhelp_quest_failed_selected:
    background "#202020"
    hover_background "#220000"

style questhelp_quest_failed_bold_selected:
    background "#220000"
    hover_background "#330000"

style questhelp_quest_failed_bold:
    hover_background "#220000"
#    hover_background "#e80000"

style questhelp_quest_failed_text:
    color "#720000"
    hover_color "#910000"
    size 24
style questhelp_quest_failed_selected_text:
    color "#720000"
    hover_color "#910000"
    size 24

style questhelp_quest_failed_bold_selected_text:
    color "#e80000"
    hover_color "#FF0000"
    size 24

style questhelp_quest_failed_bold_text:
    color "#e80000"
    hover_color "#FF0000"
    size 24
#    bold True
#051610
style questhelp_quest_completed:
    hover_background "#072117"
style questhelp_quest_completed_selected:
    background "#202020"
    hover_background "#0B3325"

style questhelp_quest_completed_bold_selected:
    background "#12543D"
    hover_background "#0B3325"

style questhelp_quest_completed_bold:
    hover_background "#0B3325"

style questhelp_quest_completed_text:
    color "#197254"
    hover_color "#1E8964"
    size 24
style questhelp_quest_completed_selected_text:
    color "#197254"
    hover_color "#1E8964"
    size 24

style questhelp_quest_completed_bold_selected_text:
    color "#31e8b1"
    hover_color "#35F2B6"
    size 24

style questhelp_quest_completed_bold_text:
    size 24
    color "#31e8b1"
    hover_color "#35F2B6"
#    bold True

style questhelp_quest_active:
    hover_background "#2D210A"
style questhelp_quest_active_selected:
    background "#202020"
    hover_background "#2D210A"

style questhelp_quest_active_bold_selected:
    background "#2D210A"
    hover_background "#4C3711"


style questhelp_quest_active_bold:
    hover_background "#2D210A"

style questhelp_quest_active_text:
    size 24
    color "#E0E0E0"
    hover_color "#F7F7F7"
style questhelp_quest_active_selected_text:
    size 24
    color "#E0E0E0"
    hover_color "#F7F7F7"

style questhelp_quest_active_bold_selected_text:
    size 24
    color "#e8b131"
    hover_color "#FFC038"

style questhelp_quest_active_bold_text:
    size 24
    color "#e8b131"
    hover_color "#FFC038"
#    bold True

style questhelp_quest_description_text:
    size 22
    color "#C0C0C0"
    line_spacing 5

style questhelp_disabled_text:
    outlines [(0, "#18181A", 5, 5)]
