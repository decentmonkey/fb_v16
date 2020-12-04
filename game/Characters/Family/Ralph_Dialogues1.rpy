
label ralphDialogue1:
    if cloth_type != "Governess":
        mt "Я не хочу разговаривать с ним в таком виде."
        "Мне надо переодеться!"
        return
    #render+
    #Ральф отвечает Монике в гостиной
    music Groove2_85
    if day_time == "day":
        img 5804
        with fade
#    imgr Dial_Ralph_1
    ralph "Моника, ты что-то хотела?"
#    imgl Dial_begin37_1
    m "Нет, Сэр."
    "Простите."

    return

label ralphDialogue2:
    if act != "t":
        return
    if cloth_type != "Governess":
        return
    if ralphAskedAboutPayment == False:
        $ questHelp("house_2", True)
    $ ralphAskedAboutPayment = True
    #render
    $ store_music()
    #Моника спрашивает у Ральфа про деньги. Гостиная
    music Groove2_85
    img 5805
#    imgl Dial_begin37_13
    with fadelong
    m "Мистер Робертс."
    "Позвольте спросить?"

    img 5806
#    imgr Dial_Ralph_2
    ralph "Да, Моника, спрашивай."
    "Освоилась в доме?"
    img 5807
    m "Еще не до конца, Мистер Робертс."
    img 5808
    ralph "Осваивайся, удачи тебе!"
    img 5809
    m "Спасибо, Мистер Робертс. Можно вопрос?"
    ralph "Да?"
    img 5810
#    imgl Dial_begin37_14
    m "Мистер Робертс. Мне Ваша супруга только что сказала что я слишком дорого для Вас стою."
    "И что у меня зарплата $90 в час..."
    img 5811
    with fadelong
#    imgr Dial_Ralph_3
    ralph "..."
    "Хм..."
    "И что ты хочешь узнать?"
    img 5812
#    imgl Dial_begin37_15
    with fade
    m "Мистер Робертс."
    "Фред сказал мне что я буду работать за бесплатно."
    "И я хотела бы узнать..."
    img 5813
    ralph "Что бы ты хотела узнать, Моника?"
    img 5814
    m "..."
    img 5813
    "..."
    img 5814
    m "..."
    img 5815
#    imgr Dial_Ralph_4
    with fade
    ralph "Ладно."
    "Фред уговорил меня взять тебя."
    "Я не очень-то хотел."
    "Честно говоря, Бетти и сама хорошо справлялась с домом."
    "И нам не нужна была гувернантка."
    img 5816
    "Тем более что почти все наши деньги Бетти тратит на себя."
    "Так что то что она немного работает и приносит пользу - меня устраивало."
    "Фред предложил мне идею..."
    "В общем Бетти я сказал что буду платить тебе $90 в час."
    "Для того чтобы хоть какие-то деньги оставались при мне."
    img 5817
#    imgr Dial_Ralph_5
    ralph "Ну.. Ты понимаешь, Моника?"
    "Бетти такая строгая..."

    music Pyro_Flow
    img 5818
#    imgl Dial_begin37_16
    with hpunch
    mt "О! Я понимаю!"
    "Я понимаю, склизкий червяк!"
    img 5819
    "Что ты будешь забирать мои деньги себе и тратить на шлюх!"
    "Я прекрасно понимаю!"
    music Groove2_85
    img 5820
#    imgl Dial_begin37_17
    m "Да, Сэр. Я понимаю."
    img 5821
#    imgr Dial_Ralph_6
    with fade
    ralph "Если честно, я сам немного побаиваюсь этой авантюры."
    "Так что если ты не хочешь, то можешь не работать."
    "Хочешь я прямо сейчас скажу Бетти что ты уходишь?"
    img 5822
    m "Нет, Сэр."
    "Я буду работать."
    img 5823
    "..."
    "Сэр. Я Вам еще нужна?"
    img 5824
#    imgr Dial_Ralph_7
    ralph "Нет, Моника, можешь идти."
    m "До свидания, Мистер Робертс."
    img 5825
    with fade
    mt "..."
    mt "СВОЛОЧЬ!!!"

    $ remove_objective("ask_ralph")
    $ restore_music()
    $ remove_hook()

    call refresh_scene_fade() from _call_refresh_scene_fade_27

    return False
