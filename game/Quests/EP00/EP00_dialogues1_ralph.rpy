default ep00_dialogues_ralph1_flag = False
default ep00_dialogues_ralph2_flag = False

label ep00_dialogues_ralph1:
    if ep00_dialogues_ralph1_flag == True:
        return
    $ ep00_dialogues_ralph1_flag = True
    # не рендерить
    # Моника думает о том, что можно было бы соблазнить Ральфа
    m "можно было бы соблазнить Ральфа"
    return

label ep00_dialogues_ralph2:
    if ep00_dialogues_ralph2_flag == True:
        return
    $ ep00_dialogues_ralph2_flag = True
    # не рендерить
    # Моника рассуждает о том, что можно взять одежду Бетти и притвориться ей (происходит на фитнесе)
    m "переодеться в бетти"
    return
