
label gallery_14821:
    # Бетти сидит напротив учителя, как в прошлый раз. Говорит с улыбкой
    music Groove2_85
    img 14778
    with fadelong
    w
    sound highheels_short_walk
    img 14779
    with diss
    w
    img 14780
    with fade
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    # учитель тоже улыбается
#    img 14813
    img 14815
    with diss
    teacher "Рад вас видеть снова, миссис Робертс. Документы Барди все еще у меня."
    img 14814
    with fade
    betty "Спасибо. Я надеюсь, что мы с вами закроем сегодня этот вопрос?"
    img 14815
    with diss
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    img 14816
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    img 14817
    with diss
    betty_t "Почему мне, порядочной женщине, приходится заниматься подобными вещами из-за какого-то малявки?!"
    betty_t "Мне снова придется работать рукой? Что ж, в прошлый раз это помогло..."
    betty_t "Но только рукой! На большее я не соглашусь, это уже будет изменой! А я замужняя женщина!"
    img 14818
    with diss
    teacher "..."
    img 14819
    with diss
    betty "Мистер Эдвардс?"
    img 14820
    with fade
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди?"
    # Бетти растерянно
    music Hidden_Agenda
    img 14821
    with diss
    betty "???"
    betty "Я... Я думала, что мы просто повторим нашу прошлую встречу..."
    music Loved_Up
    img 14822
    with fade
    teacher "Я просто потрогаю ее и все. У вас такая красивая грудь!"
    img 14823
    with diss
    betty "..."
    img 14824
    with diss
    menu:
        "Не делать этого. Я порядочная замужняя женщина. Я же пришла сюда, чтобы удовлетворить его только рукой...":
            music Groove2_85
            img 14825
            with fade
            betty "Мистер Эдвардс, я порядочная замужняя женщина. Как вы себе это представляете?"
        "Почему нет? Он же просто потрогает мою грудь.":
            img 14826
            with fade
            betty "Мистер Эдвардс, я не против, если вы только потрогаете ее. Не более того!"
    img 14827
    with diss
    teacher "Миссис Робертс, я просто теряю голову от вашей красоты! Позвольте мне прикоснуться к вам. Хотя бы один раз."
    # Бетти встает со стула, приспускает платье и оголяет грудь. Учитель встает, обходит свой стол и подходит к ней
    # Барди подглядывает через приоткрытую дверь, делает фото
    music Sneaky_Snitch
    img 14828
    with fadelong
    bardie_t "!!!"
    bardie_t "Сегодня в моей коллекции прибавятся отличные фотки с Бетти! Жаль, отец пока не может оценить их."
    # учитель берет в ладонь грудь Бетти, приподнимает ее, сжимает
    label gallery_14831:
    music Loved_Up
    img 14829
    with fade
    w
    img 14830
    with diss
    w
    #видео teacher_betty_titsgrooping
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_v.ogg"
    scene black
    image videov_Teacher_Betty_TitsGrooping_1_1 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_1.mkv", fps=30)
    show videov_Teacher_Betty_TitsGrooping_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_2.ogg"
    scene black
    image videov_Teacher_Betty_TitsGrooping_1_2 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_2.mkv", fps=30)
    show videov_Teacher_Betty_TitsGrooping_1_2
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_3.ogg"
        scene black
        image videov_Teacher_Betty_TitsGrooping_1_3 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_3.mkv", fps=30)
        show videov_Teacher_Betty_TitsGrooping_1_3
        wclean
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_4.ogg"
        scene black
        image videov_Teacher_Betty_TitsGrooping_1_4 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_4.mkv", fps=30)
        show videov_Teacher_Betty_TitsGrooping_1_4
        wclean

    img 14831
    with diss
    w
    img 14832
    with diss
    betty "Ох. Мистер Эдвардс. Достаточно." # ахххх
    img 14833
    with diss
    betty_t "Ммм, это так приятно..."
    img 14834
    with fade
    teacher "Миссис Робертс, я хочу поцеловать ее."
    img 14835
    with diss
    betty "Нет, нет. Мы об этом не договаривались." # возмущенно (но ахх)
    # учитель не слушает ее, целует ее соски
    img 14836
    with fade
    betty "Ох! Ооо!"
    #sound поцелуй груди
    sound kiss1
    img 14839
    with diss
    w
    img 14840
    with diss
    w
    #sound поцелуй груди
    label gallery_14856:
    music Loved_Up
    sound kiss1
    img 14838
    with diss
    betty_t "Мне нужно остановить это немедленно. Ммм... Иначе одной рукой я не обойдусь сегодня."
    betty_t "Я порядочная и замужняя женщина! Я не могу себе позволить большего!"
    # Бетти отталкивает препода, неуверенно
    img 14841
    with fade
    betty "Мистер Эдвардс! Давайте, сделаем все, как в прошлый раз и я пойду. У меня мало времени."
    sound snd_zip
    img 14842
    with diss
    teacher "Как скажете. Но вам же это нравится, миссис Робертс. Зачем вы сопротивляетесь?"
    # учитель расстегивает ремень и ширинку, достает член, Бетти смотрит на его стояк
    sound Jump1
    img 14843
    with diss
    teacher "Возьмите его в руку, миссис Робертс."
    img 14844
    with diss
    betty "..."
    # Бетти подходит к преподу ближе и гладит его член
    img 14845
    with fade
    betty_t "Ммм... Какой же он... Ммм..."
    betty_t "Так! Мне надо держать себя в руках и не забывать о том, что я замужем."
    img 14846
    with diss
    teacher "Давайте, миссис Робертс, смелее. Прикоснитесь к нему губами."
    img 14847
    with diss
    betty "Губами?!"
    img 14848
    with diss
    menu:
        "Как он мог предложить мне такое?! Я порядочная женщина!":
            img 14849
            with fade
            betty "Мистер Эдвардс, я не могу на такое согласиться. Я порядочная женщина."
        "Мне совсем неинтересно, какой он на вкус!!!":
            img 14850
            with fade
            betty "Мистер Эдвардс, вам не достаточно нравится, как я делаю это рукой и вы хотите большего?"
    img 14851
    with diss
    teacher "Миссис Робертс, просто поцелуйте его. Неужели он вам не нравится?"
    img 14852
    with diss
    betty_t "Черт!!! Мне неинтересно... Мне неинтересно..."
    img 14853
    with diss
    teacher "Всего один поцелуй..."
    img 14854
    with diss
    betty "Только один!"
    # Бетти опускается на колени перед преподом, смотрит на член
    img 14855
    with fade
    betty_t "Что я творю?"
    betty_t "..."
    betty_t "Я просто прикоснусь к нему губами... и языком. Я делаю это не ради себя!"
    # Бетти прикасается к члену учителя губами, потом проводит языком по головке
    img 14858
    with diss
    w
    img 14856
    with diss
    w
    img 14859
    with diss
    betty_t "Ммм... Ну и что, что он оказался таким вкусным..."
    # и еще раз языком по стволу и по головке
    # видео betty teacher licking
    img black_screen
    with diss
    pause 1.5
    music stop
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_1 = Movie(play="video/v_Teacher_Betty_DickLicking_1_1.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_2 = Movie(play="video/v_Teacher_Betty_DickLicking_1_2.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_3 = Movie(play="video/v_Teacher_Betty_DickLicking_1_3.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_3
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
        scene black
        image videov_Teacher_Betty_DickLicking_1_4 = Movie(play="video/v_Teacher_Betty_DickLicking_1_4.mkv", fps=30)
        show videov_Teacher_Betty_DickLicking_1_4
        wclean
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
        scene black
        image videov_Teacher_Betty_DickLicking_1_5 = Movie(play="video/v_Teacher_Betty_DickLicking_1_5.mkv", fps=30)
        show videov_Teacher_Betty_DickLicking_1_5
        wclean

    img 14860
    with diss
    w
    img 14861
    with diss
    w
    img 14862
    with diss
    betty "Мистер Эдвардс, я... думаю, что... достаточно..."
    # а сама облизывает его
    img 14863
    with diss
    teacher "Еще немного, миссис Робертс. Обхватите его губами."
    # Бетти обхватывает губами головку и насаживается головой на член
    stop music
    music Loved_Up2
    img 14865
    with diss
    w
    sound Jump2
    img 14864
    show screen photoshot_screen()
#    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "Ооо, да!"
    img 14866
    with diss
    betty_t "!!!"
    # Бетти запускает свою руку под платье, в трусики (платье поднимает, трусики красные)
    # audio из видео
    img 14867
    with diss
    betty "Ммммфмммффф..."
    # Бетти старательно делает минет преподу, а Барди делает фото
    img 14868
    with diss
    w
    # видео betty teacher blowjob
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_1 = Movie(play="video/v_Teacher_Betty_Blowjob_1_1.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_1
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
        scene black
        image videov_Teacher_Betty_Blowjob_1_2 = Movie(play="video/v_Teacher_Betty_Blowjob_1_2.mkv", fps=30)
        show videov_Teacher_Betty_Blowjob_1_2
        wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_3 = Movie(play="video/v_Teacher_Betty_Blowjob_1_3.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_4 = Movie(play="video/v_Teacher_Betty_Blowjob_1_4.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_4
    wclean
    music Sneaky_Snitch
    img 14857
    with fadelong
    bardie_t "В прошлый раз подрочила, сегодня отсосала... Как она старается, чтобы меня не отчислили!"
    bardie_t "Аха-ха!"
    bardie_t "!!!"
    # Бетти продолжает работать ртом
    music Loved_Up2
    img 14869
    with fade
    teacher "Ммм... Как же чертовски хорошо! Еще, быстрее!"
    img 14870
    with diss
    betty "Ммммфмммффф..."
    # препод со стоном кончает на ее лицо
    img 14871
    with diss
    w
    img 14872
    with diss
    w
    img 14873
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    img 14874
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "Ооо, дааааааа!"
    sound man_moan18
    # Бетти делает еще несколько движений своей рукой у себя в трусиках и кончает следом за ним
    img 14875
    with diss
    w
    img 14876
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan14
    betty "ООООООООО!!!"
    # препод крайне доволен (уже одет)
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14877
    with fadelong
    teacher "Миссис Робертс, это было великолепно. Думаю, нам с вами нужно будет еще раз встретиться, чтобы закрепить нашу договоренность."
    # смотрит на него снизу вверх, вся в сперме
    img 14878
    with diss
    betty "Еще раз?"
    img 14879
    with fade
    teacher "Именно. Еще раз и я закрою этот вопрос с отчислением Барди."
    # Барди злорадно ухмыляется за дверью
    music Sneaky_Snitch
    img 14880
    with fade
    bardie_t "!!!"
    bardie_t "Отлично!"

    # Барди убегает, Бетти, сидя на полу перед учителем
    sound snd_runaway
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14881
    with fadelong
    betty_t "Еще один визит к преподавателю и этот сопляк у меня в руках! Не могу дождаться, чтобы, наконец, поставить его на место."
    img 14882
    with diss
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И мы закрепим с вами нашу договоренность."
    img 14883
    with fade
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return

label gallery_14638:
    # Барди делает вид, что ничего не знает, спрашивает Бетти
    music Groove2_85
    img 14625
    with fadelong
    bardie "Ну как? Надеюсь, ты все уладила?"
    # Бетти смотрит возмущенно
    img 14638
    with diss
    betty "Ты хоть видел свои оценки?! Ты думаешь так просто решить этот вопрос, если ты вообще не бываешь в колледже?!"
    # Барди строго
    img 14629
    with fade
    bardie "То есть у тебя не получилось договориться с учителем?"
    bardie "..."
    bardie "Я так и знал, что тебе ничего нельзя поручить..."
    # Бетти орет
    music Power_Bots_Loop
    img 14634
    with fade
    betty "Ты как со мной разговариваешь, сопляк!"
    betty "Я не буду решать твои проблемы в колледже!"
    betty "Разбирайся с этим сам!"
    img 14636
    with diss
    betty "А теперь отойди! У меня нет времени на тебя!"
    betty "!!!"
    # Бетти уходит, Барди ей вслед
    img 14640
    with diss
    bardie "Стой! Я с тобой еще не договорил! Ты куда?"
    # кадр меняется на Барди
    music Sneaky_Snitch
    img 14641
    with fade
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return

label gallery_14891:
    # Бетти сидит напротив учителя, как в прошлый раз. Бетти с улыбкой
    music Groove2_85
    img 14884
    with fadelong
    w
    img 14885
    with diss
    w
    sound highheels_short_walk
    img 14886
    with diss
    w
    img 14737
    with fade
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    img 14887
    with diss
    teacher "Рад вас видеть снова, миссис Робертс."
    img 14739
    with fade
    betty "Я надеюсь, что мы с вами закроем сегодня вопрос отчисления Барди с колледжа?"
    img 14888
    with diss
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    img 14816
    with diss
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    img 14817
    with diss
    betty_t "Сегодня нельзя соглашаться на большее! Достаточно было прошлого раза..."
    betty_t "Я не собираюсь изменять своему мужу!"
    img 14818
    with fade
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди, как в прошлый раз?"
    img 14890
    with diss
    betty "???"
    img 14889
    with fade
    betty "Я... Да. Только как в прошлый раз, не более того!"
    img 14758
    with diss
    teacher "Миссис Робертс, ну конечно! Вам не о чем переживать!"
    # Бетти встает, приспускает платье и оголяет грудь. Учитель подходит к ней, берет в ладонь грудь Бетти, целует соски
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14830
    with fadelong
    w
    img 14832
    with diss
    w
    #sound целует грудь Бетти
    sound kiss1
    img 14891
    with diss
    sound ahhh1
    betty_t "Ммм, как же хорошо..."
    img 14892
    with diss
    betty "Ох. Мистер Эдвардс."
    img 14893
    with fade
    teacher "Миссис Робертс, я сниму с вас платье? Оно мешает мне рассмотреть вашу красоту."
    # Бетти растерянно
    img 14894
    betty "Вы хотите снять с меня платье?!"
    img 14895
    with diss
    menu:
        "Это все закончится сексом. Я не должна делать этого! Я порядочная женщина...":
            img 14896
            with fade
            betty "Мистер Эдвардс, вы забыли, что я порядочная женщина? Достаточно моей голой груди."
        "Он хочет приласкать меня. Это же просто ласки, а не измена? Я же порядочная женщина...":
            img 14897
            with fade
            betty "Мистер Эдвардс, вам не достаточно моей голой груди и вы хотите большего?"
    img 14898
    with diss
    teacher "Миссис Робертс, я ничего такого не собираюсь делать. Просто приласкаю вас немного."
    teacher "Вы же в прошлый раз сделали мне приятно, теперь я хочу сделать так, чтобы и вам было хорошо."
    # Бетти возмущенно
    music Power_Bots_Loop
    img 14899
    with hpunch
    betty "Нет, Мистер Эдвардс! Вы - преподаватель. Как вы вообще можете предлагать мне такое?!"
    betty "Мне, замужней женщине!"
    music Groove2_85
    img 14900
    with fade
    teacher "Миссис Робертс, вы такая заботливая мать, так искренне переживаете за вашего сына..."
    teacher "Я предлагаю вам единственный из всех возможных способов окончательно решить вопрос об учебе Барди."
    teacher "Если вы сейчас откажетесь, то я буду вынужден передать документы Барди директору."
    teacher "И тогда ничего нельзя уже будет исправить. Подумайте хорошо, прежде чем отказывать мне."
    # Бетти пристально смотрит на препода, сомневается
    img 14901
    with diss
    betty "..."
    # принимает решение
    img 14902
    with fade
    betty "Ну ладно, мистер Эдвардс... Только быстро!"
    # Бетти раздевается до трусиков, учитель гладит ее рукой через трусики
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 14903
    with fadelong
    sound Jump1
    w
    img 14904
    with diss
    sound chpok3
    w
    #sound ах
    sound ahhh12
    img 14905
    with diss
    betty "Ах!"
    betty_t "О, как же приятно!"
    img 14906
    with diss
    w
    img 14907
    with diss
    sound chpok3
    w
    # учитель подводит ее к столу, нагибает над ним и снимает с нее трусики, второй рукой расстегивает свою ширинку
    label gallery_14919:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 14917
    with fadelong
    sound Jump1
    w
    img 14918
    with diss
    betty "Ммм..."
    # продолжает рукой ласкать ее киску, а потом входит в нее пальцами
    #sound чавк
    sound chmok2
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w


    img 14921
    with diss
    w
    img 14924
    with diss
    sound ahhh12
    betty "Ооо... М-мистер Эд-двардс... Ммм..."
    img 14922
    with diss
    betty_t "Ох, черт! Как же хорошо! Но я должна остановить его!"
    img 14923
    with diss
    betty "М-мистер Эд-двардс, я... дум-маю, что... д-достаточно..."
    # учитель продолжает водить рукой туда-сюда
    img 14925
    with diss
    teacher "Еще немного, миссис Робертс. Раздвиньте ножки пошире."
    # учитель убирает пальцы, берет в руки свой член, нацеливается в киску Бетти и входит в нее
    label gallery_14910:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up2
    img 14910
    with fadelong
    sound chmok2
    w
    #видео teacher betty sex 1
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_1 = Movie(play="video/v_Teacher_Betty_Sex_1_1.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_2 = Movie(play="video/v_Teacher_Betty_Sex_1_2.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_3 = Movie(play="video/v_Teacher_Betty_Sex_1_3.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_4 = Movie(play="video/v_Teacher_Betty_Sex_1_4.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_4
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_5 = Movie(play="video/v_Teacher_Betty_Sex_1_5.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_5
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_6 = Movie(play="video/v_Teacher_Betty_Sex_1_6.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_6
    wclean

    img 14911
    with diss
    w
    img 14912
    with diss
    w
    img 14913
    with diss
    betty "Ааааах!"
    img 14914
    with diss
    w
    img 14915
    with diss
    teacher "Ооооо..."
    img 14916
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_155
    w
    call photoshop_flash() from _rcall_photoshop_flash_156
    w
    # Барди злорадно ухмыляется за дверью и делает несколько кадров
    img 14908
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_157
    w
    bardie_t "!!!"
    bardie_t "Отлично! Теперь она от меня никуда не денется!"
    img 14909
    with fade
    # препод "любит" Бетти на столе, потом они перемещаются на пол, Бетти садится сверху
    w
    label gallery_14931:
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 14926
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_1 = Movie(play="video/v_Teacher_Betty_Sex_2_1.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_2 = Movie(play="video/v_Teacher_Betty_Sex_2_2.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_3 = Movie(play="video/v_Teacher_Betty_Sex_2_3.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_4 = Movie(play="video/v_Teacher_Betty_Sex_2_4.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_4
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_5 = Movie(play="video/v_Teacher_Betty_Sex_2_5.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_5
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_6 = Movie(play="video/v_Teacher_Betty_Sex_2_6.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_6
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_7 = Movie(play="video/v_Teacher_Betty_Sex_2_7.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_7
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_8 = Movie(play="video/v_Teacher_Betty_Sex_2_8.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_8
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_9 = Movie(play="video/v_Teacher_Betty_Sex_2_9.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_9
    wclean
    music Loved_Up2
    img 14927
    with diss
    teacher "Ммммммм..."
    img 14928
    with diss
    betty "Только не кончайте в меня, мистер Эдвардс!"
    # Бетти двигается на учителе и через некоторое время кончает
    img 14929
    with diss
    w
    img 14930
    with diss
    w
    img 14931
    with diss
    w
    img 14932
    #sound бетти кончает
    sound woman_moan14
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "ООООООООО!!!"
    # препод вынимает из нее член и со стоном кончает на ее грудь
    img 14933
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 14934
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    teacher "Ооо, дааааааа!"
    img 14938
    with diss
    w
    # препод крайне доволен, лежит на полу, Бетти сидит на учителе, недоверчиво смотрит на него
    music Groove2_85
    img 14935
    with fade
    teacher "Миссис Робертс, это было великолепно. Считайте, что вопрос с отчислением Барди закрыт."
    # Бетти недоверчиво
    img 14936
    with diss
    betty "Это точно?"
    img 14937
    with fade
    teacher "Да, мы с вами только что закрепили нашу договоренность."
    # Барди делает еще фото и убегает, радостный
    music Sneaky_Snitch
    img 14939
    with fadelong
    w
    call photoshop_flash() from _rcall_photoshop_flash_158
    w
    # Бетти встает и одевается, препод тоже
    music stop
    img black_screen
    with diss
    sound snd_runaway
    pause 2.0
    music Groove2_85
    img 14940
    with fadelong
    sound snd_zip
    teacher "Если вдруг у Барди снова начнутся проблемы с учебой, я вам сразу же позвоню, миссис Робертс."
    img 14941
    with diss
    betty_t "Отлично! Я сделала то, чего хотел этот сопляк. С меня хватит!"
    betty_t "Теперь он не посмеет требовать от меня своих глупостей!"
    img 14942
    with fade
    betty "Хорошо, мистер Эдвардс. Было приятно сотрудничать с вами."
    img 14943
    with diss
    teacher "Всегда к вашим услугам, миссис Робертс."
    return True

label gallery_14962:
    # Моника стоит у дверей, учитель сидит за учительским столом
    music Groove2_85
    img 14944
    with fadelong
    w
    img 14945
    with diss
    w
    sound highheels_short_walk
    img 14946
    with diss
    mt "Это учитель? Надеюсь, разговор с ним не займет у меня много времени."
    img 14947
    with fade
    m "Мистер Эд... Эдвардс?"
    # учитель поворачивается к ней с серьезным лицом
    img 14948
    with diss
    teacher "Да. Миссис Бейкер, я полагаю?"
    img 14949
    with diss
    mt "Точно. Бейкер. Как я могла забыть?"
    img 14950
    with fade
    m "Да, мистер Эдвардс. Я пришла поговорить про моего сына Эрика."
    img 14951
    with diss
    mt "Мелкого озабоченного извращенца..."
    img 14952
    with fade
    teacher "Проходите, миссис Бейкер. Присаживайтесь." #предлагает ей стул сбоку от учительского стола
    # учитель общается очень вежливо, с выражением лица 'солидный учитель', Моника спокойно его слушает
    music stop
    img black_screen
    with diss
    pause 1.5
    sound highheels_short_walk
    music Groove2_85
    img 14953
    with fadelong
    teacher "Эрик - один из лучших студентов в классе и никогда с ним не было проблем. Но вот на днях..."
    teacher "На днях Эрик залез в шкафчик с одеждой тренера по плаванию. И она его застала за тем, что он дро... хм-м, что он мастурбировал, используя ее нижнее белье."
    sound Jump2
    img 14954
    with hpunch
    mt "И почему я не удивлена?.." #Моника продолжает его спокойно слушать с непроницаемым лицом
    img 14956
    with fade
    teacher "Тренер очень возмущена и собирается идти к директору. Она будет требовать у директора наказать Эрика."
    teacher "Но я ее уговорил немного подождать, так как хотел поговорить сначала с вами."
    sound Jump1
    img 14955
    with diss
    teacher "Возможно, мы с вами сможем уладить этот вопрос без вмешательства директора."
    teacher "Я не хотел бы, чтобы у Эрика была плохая характеристика. И чтобы об этом инциденте узнал весь колледж."
    img 14957
    with diss
    mt "Какая-нибудь мама на моем месте, наверное, была бы в шоке."
    mt "Нужно сказать этому мистеру Эдвардсу что-нибудь эмоционально. Как там Барди мне говорил?"
    # Моника делает удивленное лицо
    music Hidden_Agenda
    img 14958
    with fade
    m "Мистер Эдвардс, я просто шокирована поступком Эрика! Я обязательно серьезно поговорю с ним!"
    m "Такого больше не повторится, мистер Эдвардс. И я предпочла бы, чтобы не было никакой огласки."
    # учитель с серьезным лицом
    img 14959
    with diss
    teacher "Я абсолютно с вами согласен, миссис Бейкер."
    img 14960
    with diss
    mt "Отлично!"
    # Моника встает со стула, смотрит на учителя
    sound highheels_short_walk
    img 14961
    with fade
    m "Значит, мы с вами все уладили? Я тогда пойду."
    # учитель отводит взгляд, потом снова смотрит на нее
    music Groove2_85
    img 14962
    with diss
    teacher "Нет, миссис Бейкер. Не торопитесь. Мы не уладили..."
    img 14963
    mt "???"
    # Моника вопросительно смотрит на него, садится обратно
    sound highheels_short_walk
    img 14964
    with fade
    teacher "Видите ли, миссис Бейкер, основная сложность - это успокоить учителя по плаванию."
    teacher "Мисс Мэнсфилд сильно рассержена на Эрика..."
    img 14965
    with diss
    m "..."
    img 14966
    with fade
    teacher "И я даже не знаю, как это сделать."
    teacher "Она очень строгая и так просто с ней не договориться."
    img 14967
    with diss
    teacher "Если у меня получится, тогда с Эриком все будет в порядке. Никто ничего не узнает."
    teacher "Но это будет крайне сложно сделать..."
    img 14968
    with fade
    m "Мистер Эдвардс, есть ли у вас какие-нибудь идеи? Как вы сможете договориться с ней?" #с досадой
    img 14969
    with diss
    teacher "Да, идея есть. Она хочет номинироваться на преподавателя года."
    teacher "Для этого ей нужна не только физическая форма и успехи в педагогике..."
    teacher "Но и солидный объем теоретической работы."
    img 14970
    with diss
    teacher "Она должна предложить какую-нибудь прогрессивную методику преподавания. Таковой у нее нет."
    teacher "А у меня как раз есть кое-какие наработки по современной методике преподавания. И я мог бы передать их мисс Мэнсфилд." #все это с очень важным видом
    teacher "Но, понимаете, миссис Бейкер... Просто так я это сделать не могу. Я потратил немало времени на эту работу."
    img 14971
    with diss
    teacher "Если вы меня поддержите, миссис Бейкер, то я сегодня же поговорю с ней. И предложу помочь мисс Мэнсфилд с этой методикой."
    # Моника удивляется
    music Hidden_Agenda
    img 14972
    with fade
    m "Каким образом я могу вас поддержать, мистер Эдвардс? Что мне нужно сделать?"
    img 14973
    with diss
    mt "Хоть на этот раз обойдется без сомнительных просьб в мой адрес..."
    mt "Это все-таки учитель. Он должен быть высокоморальным человеком и примером для своих учеников."
    # учитель, смущенно улыбаясь
    music Groove2_85
    img 14974
    with fade
    teacher "Мне не совсем удобно, миссис Бейкер..."
    teacher "Но дело уж очень деликатное..."
    teacher "Я вынужден попросить вас о небольшом одолжении. Это все же делается ради вашего сына, миссис Бейкер."
    # Моника с серьезным лицом
    music Hidden_Agenda
    img 14976
    with diss
    m "Каком одолжении, мистер Эдвардс? Я сделаю, что нужно."
    # учитель, смущенно
    music Groove2_85
    img 14975
    with fade
    teacher "Если бы вы, миссис Бейкер, смогли показать мне хотя бы свою грудь..."
    teacher "То я был бы очень рад этому."
    teacher "Это очень поддержало бы меня морально."
    # Моника в шоке
    music Power_Bots_Loop
    img 14977
    with hpunch
    mt "!!!"
    img 14978
    with diss
    menu:
        "Убежать.":
            img 14979
            with fadelong
            m "Я не буду этого делать!!!"
            return
        "Постараться договориться с учителем без этих извращений.":
            music Groove2_85
            img 14980
            with fade
            m "Мистер Эдвардс! Я не ожидала, что вы можете предложить мне подобное!"
            m "Я же мать вашего ученика. Как так можно?"
            # Моника вскакивает со стула, учитель ей, с сожалением
            img 14981
            with diss
            teacher "Тогда у меня, к сожалению, никак не выйдет договориться с мисс Мэнсфилд."
            teacher "И она создаст Эрику большие проблемы."
            img 14982
            with diss
            teacher "..."
        "Если это поможет быстро решить проблему малявки, то, возможно, стоит потерпеть...":
            pass

    # Моника стоит у учителького стола сбоку
    music Hidden_Agenda
    img 14984
    with diss
    mt "Мне нужно всего лишь показать грудь. А она у меня действительно великолепна."
    mt "В принципе, если это все, что от меня требуется..."
    mt "И этим я смогу отделаться от надоедливого Барди... то, возможно, стоит пойти на это."
    img 14985
    with diss
    mt "Он же хочет, чтобы я просто показала грудь. На большее не намекает."
    mt "Хотя мог бы воспользоваться ситуацией."
    mt "Я уже насмотрелась на разных извращенцев и этот мистер Эдвардс не похож на них."
    label gallery_14988:
    music Groove2_85
    img 14986
    with fade
    m "Хорошо, мистер Эдвардс. Я покажу грудь, но только прикасаться ко мне я не позволю."
    m "Можно только посмотреть!" #строго
    # учитель, довольно улыбаясь, встает со своего стула
    img 14987
    with diss
    teacher "Конечно! Я только посмотрю."
    teacher "Это и правда мне очень поможет, миссис Бейкер."
    # Моника с недовольным лицом приспускает блузку и оголяет грудь, учитель пялиться на нее
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 14988
    with fadelong
    m "..."
    img 14989
    with diss
    teacher "Вы потрясающе красивая женщина, миссис Бейкер! Я никогда не видел более красивой груди!"
    img 14990
    with diss
    mt "Еще бы! Я владелица модного журнала и самая красивая женщина в этом городе!"
    mt "Или, вообще, во всей этой стране!"
    img 14991
    with fade
    teacher "Можно я прикоснусь совсем немного?"
    music Groove2_85
    img 14992
    with hpunch
    m "Нет, мы так не договаривались. Вы достаточно посмотрели, мистер Эдвардс?" #строго
    img 14993
    with fade
    teacher "Да, спасибо, миссис Бейкер. Я уверен, что у меня теперь все получится."
    # Моника приводит блузку в порядок
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 14994
    with fadelong
    m "Мистер Эдвардс, как я узнаю, что у вас получилось все уладить с мисс Мэнсфилд?"
    m "Я должна быть уверена в положительном результате."
    img 14995
    with diss
    teacher "Я позвонил бы вам, но так как дело очень деликатное и я боюсь огласки..."
    teacher "Будет лучше, если вы снова придете ко мне. И тогда я вам лично все сообщу, миссис Бейкер." #с улыбочкой
    # Моника недовольна
    music Hidden_Agenda
    img 14998
    with fade
    mt "Черт! Мне снова нужно будет приходить сюда!"
    mt "..."
    img 14999
    with diss
    mt "А если что-то у учителя пойдет не так?"
    mt "То у Эрика будут проблемы. И у меня тогда тоже... с Барди."
    music Groove2_85
    img 14996
    with fade
    m "Договорились, мистер Эдвардс. Буду надеяться на успешное решение этой проблемы."
    m "До встречи."
    img 14997
    with diss
    teacher "До свидания, миссис Бейкер."
    teacher "Приятно было с вами познакомиться."
    # Моника уходит
#    $ log1 = t_("Барди совсем обнаглел и заставляет меня быть мамой для своего одноклассника. Такого же неудачника как он сам!")
    return

label gallery_15029:
    # Моника заходит в кабинет, стоит у дверей, учитель сидит за учительским столом
    music Groove2_85
    img 15000
    with fadelong
    w
    img 15001
    with diss
    mt "Надеюсь, в этот раз мне не придется вдохновлять его своей голой грудью..."
    sound highheels_short_walk
    img 15002
    with fade
    m "Мистер Эдвардс, добрый день."
    # учитель поворачивается к ней, с улыбочкой
    img 15003
    with diss
    teacher "Здавствуйте, миссис Бейкер. Я вас ждал. Присаживайтесь."
    # Моника садится на стул рядом с его столом
    sound highheels_short_walk
    img 15004
    with fade
    m "Удалось ли вам договориться с мисс Мэнсфилд?" #с серьезным выражением лица
    music Hidden_Agenda
    img 15005
    with diss
    teacher "Да, я поговорил с ней, миссис Бейкер."
    teacher "И у меня почти получилось с ней договориться, но..."
    img 15006
    with fade
    m "???"
    m "Но?.."
    img 15007
    with diss
    teacher "Она осталась не совсем довольна тем, что мою методику преподавания ей нужно дорабатывать."
    teacher "Но мисс Мэнсфилд согласна подождать, когда я закончу работу."
    teacher "Только после этого она согласна забыть про случай с Эриком."
    music Groove2_85
    img 15008
    with fade
    m "Когда вы сможете закончить эту работу, мистер Эдвардс?"
    img 15009
    with diss
    teacher "Я уже провел кое-какую работу над своей методикой."
    teacher "Думаю, теперь мисс Мэнсфилд будет ею довольна."
    music Hidden_Agenda
    img 15010
    with fade
    teacher "..."
    teacher "Знаете, миссис Бейкер... Мне очень сложно отдавать свои труды мисс Мэнсфилд..."
    music Groove2_85
    img 15011
    with diss
    m "???"
    img 15012
    with diss
    mt "Сейчас он снова будет просить о поддержке..." #недовольно
    mt "Извращенец..."
    music Hidden_Agenda
    img 15013
    with fade
    teacher "Если бы вы, миссис Бейкер, смогли показать мне снова свою грудь."
    teacher "И дать ее потрогать совсем немного."
    teacher "То я смогу найти в себе силы сделать это." #с улыбочкой
    music Power_Bots_Loop
    img 15014
    with hpunch
    m "..." #недовольно
    img 15015
    with diss
    mt "Мне нужно показать грудь, как в прошлый раз."
    mt "Он ее уже видел. Но вот прикасаться ко мне!.."
    mt "..."
    music Groove2_85
    img 15016
    with diss
    menu:
        "Убежать.":
            music Power_Bots_Loop
            img 15017
            with fade
            m "Я не буду этого делать!!!"
            return
        "Постараться договориться с учителем без этих извращений.":
            music Groove2_85
            img 15018
            with fade
            m "Мистер Эдвардс, я не хочу, чтобы вы трогали меня!"
            m "Показать повторно грудь - это одно дело. Но прикосновения - это уже чересчур!"
            # Моника вскакивает со стула, учитель ей, с сожалением
            img 15019
            with diss
            teacher "Тогда у меня, к сожалению, никак не выйдет договориться с мисс Мэнсфилд."
            # учитель отворачивается и начинает просматривать какие-то бумаги на столе, работать
            sound vjuh3
            img 15020
            with fade
            teacher "..."
#            return 1
        "Если это поможет быстрее решить проблему малявки, то, возможно, стоит потерпеть...":
            pass



    # Моника смотрит на него с раздражением
    music Power_Bots_Loop
    img 15021
    with fade
    mt "Это отвратительно! Почему все вокруг хотят сделать со мной что-то непристойное?!"
    mt "!!!"
    music Groove2_85
    img 15022
    with diss
    mt "С другой стороны, если он просто потрогает немного... А я как-нибудь перетерплю это, то..."
    mt "То, вероятно, вопрос с малявкой будет закрыт совсем скоро."
    mt "И я, наконец, смогу отделаться от надоедливого Барди и его друга."
    img 15023
    with diss
    m "..."
    img 15024
    with diss
    m "Потрогать можно совсем немного, мистер Эдвардс!" #недовольно
    # учитель смотрит на нее и расплывается в улыбке
    music Hidden_Agenda
    img 15025
    with diss
    teacher "Конечно, миссис Бейкер! Это и правда мне очень поможет!"
    # Моника встает, с недовольным лицом приспускает блузку, учитель пялится на нее, потом подходит и трогает ее
    music stop
    img black_screen
    with diss
    pause 2.0
    sound snd_fabric1
    music Loved_Up
    img 15026
    with fade
    w
    img 15027
    with diss
    w
    img 15028
    with fade
    teacher "Я никогда не видел более красивой женщины, чем вы, миссис Бейкер!"
    img 15029
    with diss
    w
    img 15030
    with diss
    m "Я знаю, мистер Эдвардс! Достаточно!" #с раздражением
    # учитель убирает руки и неотрывно смотрит на грудь, пока Моника приводит в порядок блузку
    music Groove2_85
    img 15031
    with fade
    teacher "Спасибо, миссис Бейкер. Вы мне очень помогли. Я отдам свою методику мисс Мэнсфилд в ближайшее время."
    img 15032
    with diss
    m "Как я узнаю, что у вас получилось договориться с ней, мистер Эдвардс?"
    music Hidden_Agenda
    img 15033
    with fade
    teacher "Будет лучше, если вы снова придете ко мне. И тогда я вам лично все сообщу, миссис Бейкер." #с улыбочкой
    # Моника недовольна
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14998
    with fade
    mt "Черт! Мне снова нужно будет приходить сюда!"
    mt "..."
    img 14999
    with diss
    mt "А если что-то у учителя пойдет не так?"
    mt "То у Эрика будут проблемы."
    mt "И у меня тогда тоже... с Барди."
    img 14996
    with fade
    m "Договорились, мистер Эдвардс. Буду надеяться на успешное решение этой проблемы."
    m "До встречи."
    music Hidden_Agenda
    img 14997
    with diss
    teacher "До свидания, миссис Бейкер."
    teacher "Буду рад видеть вас снова."
    return

label gallery_15069:
    # Моника заходит в кабинет, стоит у дверей, учитель сидит за учительским столом
    music Groove2_85
    img 15034
    with fadelong
    w
    img 15035
    with diss
    w
    sound highheels_short_walk
    img 15036
    with fade
    m "Мистер Эдвардс, добрый день."
    img 15037
    with diss
    teacher "Здавствуйте, миссис Бейкер."
    # учитель поворачивается к ней, с улыбочкой
    # Моника садится на стул рядом с его столом
    teacher "Я вас ждал. Присаживайтесь."
    img 15038
    with fade
    m "Удалось ли вам договориться с мисс Мэнсфилд?" #с серьезным выражением лица
    music Hidden_Agenda
    img 15039
    with diss
    teacher "Видите ли, с мисс Мэнсфилд не так просто договориться."
    teacher "Она снова нашла недочеты в моей работе."
    img 15040
    with fade
    m "..."
    img 14740
    with diss
    teacher "Но, благодаря вам, миссис Бейкер, я превзошел сам себя и доделал свою методику." #улыбаясь
    teacher "Теперь она точно будет довольна!"
    music Groove2_85
    img 14954
    with fade
    mt "Наконец-то, проблема решена!"
    # учитель делает задумчивое лицо
    music Hidden_Agenda
    img 14953
    with diss
    teacher "Но теперь я сомневаюсь, стоит ли мне отдавать свою методику ей..."
    music Power_Bots_Loop
    img 15041
    with hpunch
    mt "!!!" #удивленно
    music Groove2_85
    img 15042
    with fade
    m "Я очень рада, что у вас все получилось с вашей работой, мистер Эдвардс, но..."
    m "Надеюсь, что я не зря прихожу к вам уже третий раз."
    m "Я ожидаю, что вы все-таки договоритесь с мисс Мэнсфилд."
    # вопросительно смотрит на него, учитель серьезно
    img 15043
    with diss
    teacher "Мне будет очень непросто это сделать, миссис Бейкер."
    teacher "Ведь я сам могу стать номинантом! Я считаю, что моя работа достойна этого."
    teacher "Все зависит от того, насколько вы, миссис Бейкер, готовы поддержать меня..." #улыбочка
    # Моника  в шоке, возмущается
    music Power_Bots_Loop
    sound Jump1
    img 15044
    with fade
    m "Вы в своем уме?! Как вы можете мне такое предлагать?!"
    m "Если бы я знала, что в итоге вы потребуете от меня ТАКОГО. Я бы отказалась вообще от вашей помощи!"
    m "!!!"

    music Hidden_Agenda
    img 15045
    with diss
    teacher "Вы не совсем так меня поняли, миссис Бейкер."
    teacher "Я хочу, чтобы вы просто потрогали меня рукой. Не более того."
    img 15046
    with diss
    teacher "А без моей помощи вы бы вовсе не смогли уладить эту ситуацию, миссис Бейкер."
    # Моника зло на него смотрит
    music Power_Bots_Loop
    img 15047
    with fade
    m "!!!"
    # учитель продолжает говорить спокойно
    music Hidden_Agenda
    img 15048
    with diss
    teacher "После этого я сразу же отдам свою работу мисс Мэнсфилд."
    teacher "И вопрос будет закрыт."
    # он при этом встает и расстегивает штаны, Моника зло на него смотрит, сидя на стуле
    music Groove2_85
    img 15050
    with fade
    mt "Он снова пытается склонить меня к сексуальным действиям!"
    mt "Я не собираюсь этого делать!!!"
    mt "Пусть этот учитель катится к черту! С меня хватит!"
    img 15049
    with diss
    mt "Пусть идет и рассказывает хоть всему колледжу об этом придурке Эрике!"
    mt "!!!"
    mt "Только что я скажу потом Барди?"
    img 15051
    with diss
    mt "..."
    mt "Черт! Ненавижу эту малявку!"
    mt "Он же устроит мне массу проблем посерьезнее, чем потрогать член учителя."
    # Моника возмущается
    music Power_Bots_Loop
    img 15052
    with fade
    m "Я пожалуюсь на вас вашему руководству!"
    m "Или в полицию!"
    music Hidden_Agenda
    img 15053
    with diss
    teacher "Я уважаемый педагог с хорошей репутацией. Вам будет крайне сложно меня обвинить в подобном."
    teacher "Вам просто не поверят, миссис Бейкер."
    img 15054
    with diss
    teacher "Тем более, что на меня пожалуется мать студента, который сам замечен в аморальном поведении."
    teacher "Вам должно быть стыдно, миссис Бейкер."
    teacher "..."
    # Моника возмущенно смотрит на него, но молчит, сидит на стуле
    music Groove2_85
    img 15055
    with fade
    mt "Сомневаюсь, что руководство колледжа мне поверит..."
    mt "В полицию мне нельзя..."
    mt "Что же мне делать?"
    mt "..."
    img 15056
    with diss
    menu:
        "Убежать.":
            music Power_Bots_Loop
            img 15017
            with fade
            m "Я не буду этого делать!!!"
            return
        "Постараться договориться с учителем без этих извращений.":
            music Groove2_85
            img 15018
            with fade
            m "Я не занимаюсь такими вещами, мистер Эдвардс!"
            img 15019
            with diss
            teacher "Я сделал все зависящее от меня, миссис Бейкер. Я пошел на такие жертвы." #спокойно и уверенно
            teacher "И все ради вас..."
            teacher "В таком случае, у меня не получится решить проблему вашего сына, миссис Бейкер."
            # учитель отворачивается и начинает просматривать какие-то бумаги на столе, работать
            img 15020
            with diss
            teacher "..."
        "Если это поможет быстрее решить проблему малявки, то, возможно, стоит потерпеть...":
            pass


    music Groove2_85
    img 15057
    with fade
    mt "Если все что нужно этому извращенцу - это потрогать его член... И ничего более..."
    mt "Возможно, мне стоит потерпеть и это все закончится, наконец-то?"
    # учитель подходит к ней, достает свой стояк и выжидательно смотрит на нее
    img 15058
    with diss
    w
    img 15060
    with diss
    w
    img 15059
    with diss
    teacher "Просто приласкайте его, миссис Бейкер..."
    sound snd_zip
    img 15061
    with fade
    m "..." #зло
    img 15062
    with diss
    # Моника с отвращением протягивает руку, прикасается к нему пальцами
    w
    music Loved_Up
    sound Jump1
    img 15063
    with fade
    w
    img 15064
    with diss
    teacher "Обхватите его рукой, миссис Бейкер..."
    # Моника делает, как он просит, учитель кладет свою руку поверх ее и начинает двигать вверх-вниз
    img 15065
    with fade
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float(rand(1,7))*1.0) + " loop 0.0>Sounds/v_Monica_Teacher_HandJob1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_HandJob1_1 = Movie(play="video/v_Monica_Teacher_HandJob1_1.mkv", fps=30)
    show videov_Monica_Teacher_HandJob1_1
    with fadelong
    wclean
    music Loved_Up
    img 15067
    with diss
    teacher "Ммм... Да-а-а, как же хорошо..."

    music stop
    stop music
    play music "<from " + str(float(rand(1,7))*1.0) + " loop 0.0>Sounds/v_Monica_Teacher_HandJob1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_HandJob1_2 = Movie(play="video/v_Monica_Teacher_HandJob1_2.mkv", fps=30)
    show videov_Monica_Teacher_HandJob1_2
    with fadelong
    wclean

    music Loved_Up
    sound drkanje5
    img 15068
    with fade
    mt "Какой кошмар! Что я делаю?! Как это все мерзко!!!"
    sound drkanje5
    img 15069
    with diss
    teacher "Ммммммм..."
    music stop
    stop music
    play music "<from " + str(float(rand(1,7))*1.0) + " loop 0.0>Sounds/v_Monica_Teacher_HandJob1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_HandJob1_3 = Movie(play="video/v_Monica_Teacher_HandJob1_3.mkv", fps=30)
    show videov_Monica_Teacher_HandJob1_3
    with fadelong
    wclean
    music Loved_Up2
    # учитель ускоряет движения и со стоном кончает на блузку Моники
    img 15066
    with diss
    w
    sound drkanje5
    img 15070
    with diss
    w
#######################################




#######################################
    music stop
    music Loved_Up2
    sound bulk1
    img 14800
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "ОООООО!!!"
    w
    sound man_moan18
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    img 15071
    with diss
    w
    sound hlup2
    music Groove2_85
    img 15383
    with fade
    mt "Фуууу!!! Какая гадость!"
    mt "Какого черта?! Он меня испачкал!"
    # Моника оттирает блузку и зло смотрит на учителя, он застегивает штаны, садится за свой стол, улыбается
    img 15384
    with diss
    teacher "Я весьма рад, миссис Бейкер... Мы с вами весьма успешно закрыли проблему с Эриком."
    music Power_Bots_Loop
    img 15311
    with fade
    mt "Он такой же извращенец, как и все."
    mt "Только притворяется благородным и высокоморальным."
    mt "А сам готов меня склонить к сексу!"
    img 15385
    with diss
    mt "!!!" #смотрит на него зло
    music Groove2_85
    img 14994
    with fade
    m "Проблема с Эриком точно решена, мистер Эдвардс?"
    m "Мне не придется приходить сюда снова, чтобы удостовериться в этом?"
    img 14995
    with diss
    teacher "Абсолютно точно, миссис Бейкер. Можете не переживать."
    teacher "Я прямо сейчас отнесу методику мисс Мэнсфилд."
    img 14996
    with fade
    m "Хорошо. До свидания, мистер Эдвардс." #недовольно
    img 14997
    with diss
    teacher "Всегда к вашим услугам, миссис Бейкер."
    # Моника уходит
    return

label gallery_15340:
    # Моника заходит в кабинет, стоит у дверей, учитель сидит за учительским столом
    music Groove2_85
    img 15301
    with fadelong
    w
    img 15302
    with diss
    w
    sound highheels_short_walk
    img 14947
    with fade
    m "Мистер Эдвардс, добрый день."
    # учитель поворачивается к ней, с улыбочкой
    music Hidden_Agenda
    img 15303
    with diss
    teacher "Здавствуйте, миссис Бейкер. Я вас ждал."
    teacher "Присаживайтесь."
    # Моника садится на стул рядом с его столом
    music Groove2_85
    img 14965
    with fade
    m "Что натворил Эрик в этот раз, мистер Эдвардс?!" #с серьезным выражением лица
    img 14964
    with diss
    teacher "Вы не поверите, миссис Бейкер..."
    teacher "Он снова залез в шкафчик к тренеру по плаванью..."
    teacher "И сделал то же самое."
    music Power_Bots_Loop
    img 15304
    with vpunch
    m "ЧТО?!" #офигевает
    m "!!!"
    music Groove2_85
    img 14956
    with fade
    teacher "Да. Мисс Мэнсфилд это снова увидела." #с сожалением
    teacher "У меня есть подозрения, что Эрик делает это постоянно."
    teacher "Просто Мисс Мэнсфилд это не всегда замечает."
    # Моника в шоке
    img 15305
    with diss
    m "..."
    img 14959
    with fade
    teacher "В любом случае, Мисс Мэнсфилд была очень злая на него..."
    img 15306
    with diss
    m "Была?.."
    img 14770
    with fade
    teacher "Да, она очень злилась. И я с ней уже договорился."
    teacher "Мне пришлось составить для нее несколько педагогических отчетов, но..."
    music Hidden_Agenda
    img 14955
    with diss
    teacher "Как вы понимаете, миссис Бейкер, мне пришлось проделать огромную работу."
    teacher "Поэтому я надеюсь на особую благодарность с вашей стороны, миссис Бейкер."
    music Groove2_85
    img 15307
    with fade
    mt "Ну вот, опять он начинает..." #раздраженно
    mt "!!!"
    mt "С другой стороны, вопрос с мисс Мэнсфилд уже улажен..."
    img 15038
    with diss
    m "И что я должна сделать, мистер Эдвардс?" #с подозрением
    img 15308
    with diss
    mt "Учитель на этот раз все очень быстро решил."
    mt "И в итоге поставил меня перед фактом, что я ему должна."
    mt "Высокоморальная сволочь!"
    # учитель с улыбочкой, поднимается со стула и встает напротив Моники
    music Hidden_Agenda
    img 15309
    with fade
    teacher "Я уже видел вашу прекрасную грудь, миссис Бейкер."
    teacher "Теперь я хочу посмотреть на вашу попку..."
    teacher "И потрогать ее."
    # Моника в шоке
    music Power_Bots_Loop
    img 15310
    with diss
    m "Мистер Эдвардс, вам не кажется, что это уже слишком?!"
    m "Я не собираюсь показывать вам то, что у меня под шортами!"
    music Groove2_85
    img 15311
    with fade
    mt "Ведь проблема уже решена. Зачем мне соглашаться на это?"
    img 15312
    with diss
    menu:
        "Отказаться и уйти!":
            # Моника встает со своего стула
            label gallery_15317:
            music Groove2_85
            sound Jump1
            img 15313
            with fade
            m "Мистер Эдвардс, я не буду вам ничего показывать!"
            m "На этот раз вы зашли слишком далеко!"
            img 15053
            with diss
            teacher "Миссис Бейкер, я же только посмотрю..."
            # учитель подходит к Монике и кладет руки ей на ягодицы
            sound vjuh3
            img 15314
            with diss
            teacher "И совсем немного потрогаю..."
            # Моника в шоке
            music Power_Bots_Loop
            img 15315
            with diss
            w
            img 15316
            with diss
            m "Не смей прикасаться ко мне, извращенец!!!"
            # ударяет учителя коленом между ног, тот скрючивается и орет
            sound anger2
            img 15317
            w
            sound snd_kick_fred1
            img 15318
            with diss
            w
            sound snd_fred_argh
            img 15319
            with diss
            teacher "АААААА!"
            img 15320
            with fade
            m "И только попробуй предложить мне еще раз подобное!"
            m "Весь колледж узнает о том, какая ты озабоченная сволочь!"
            # Моника уходит
            return
        "Постараться договориться с учителем без этих извращений.":
            music Groove2_85
            img 15321
            with fade
            m "Я не занимаюсь такими вещами, мистер Эдвардс!"
            img 15322
            with diss
            teacher "Мисс Мэнсфилд может и передумать..." #говорит многозначительно
            teacher "..."
            # учитель отворачивается и начинает просматривать какие-то бумаги на столе, работать
#            return 1
        "Если это поможет быстрее решить проблему малявки, то, возможно, стоит потерпеть...":
            pass

    # Моника злится
    music Groove2_85
    img 15323
    with fade
    mt "!!!"
    img 15324
    with diss
    m "Я не собираюсь этого делать!!!"
    music Hidden_Agenda
    img 15325
    with fade
    teacher "Я сделал все зависящее от меня..." #с укором
    teacher "Пошел на такие жертвы..."
    img 15326
    with diss
    teacher "И очень быстро все уладил."
    teacher "И все ради вас, миссис Бейкер!"
    music Groove2_85
    img 15327
    with fade
    m "..." #зло смотрит
    img 15307
    with diss
    mt "Учитель может сделать так, что о дебильном поступке Эрика узнают все."
    mt "Тогда Барди точно разозлится и устроит мне массу проблем."
    img 15328
    with diss
    mt "Если потрогать мою изумительную попу - это все о чем он просит..."
    mt "Возможно, после этого он отстанет от меня..."
    # Моника возмущенно смотрит на него, но молчит, затем встает со стула, учитель подходит к ней ближе, она поворачивается к нему спиной и снимает шорты, она в трусиках Юлии
    img 15329
    with fade
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 15331
    with fade
    w
    sound highheels_short_walk
    img 15330
    with diss
    w
    img 15332
    with diss
    w
    img 15333
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15334
    with fadelong
    w
    img 15335
    with fade
    mt "Я, Моника Бакфетт, стою с голым задом перед учителем в колледже!"
    mt "Какой кошмар!!!"
    # учитель смотрит на ее зад
    img 15336
    with diss
    teacher "Миссис Бейкер, я не видел ничего красивее в своей жизни!"
    img 15337
    with diss
    mt "Еще бы! Об этой попе мечтают миллионы мужчин!"
    mt "Знал бы он, кто я такая на самом деле..."
    # учитель кладет ладони на ее ягодицы, гладит, потом снимает с нее трусики
    sound grabbing3
    img 15338
    with fade
    w
    img 15339
    with diss
    w
    img 15340
    with diss
    w
    img 15341
    with diss
    m "Этого можно было и не делать, мистер Эдвардс!"
    #m "В них и так все прекрасно видно было!" # возмущенно
    # учитель ее не слушает и начинает целовать ее ягодицы, присев за ней
    sound vjuh3
    img 15342
    with fade
    w
    sound lick13
    img 15344
    with diss
    w
    img 15343
    with diss
    m "Ай, что вы делаете?!" # удивленно
    # учитель продолжает, потом встает, кладет ей руку на спину и наклоняет ее на свой стол, затем снова тянется к ее попе и целует ягодицы, потом начинает лизать ее киску
    music Groove2_85
    img 15345
    with fade
    w
    music Groove2_85
    img 15346
    with diss
    m "Ч-что вы д-делаете?! Нет-нет!!!"
    m "Остановитесь, м-мы договаривались не так!"
    sound Jump2
    img 15347
    with fade
    mt "Что этот извращенец творит?! Как он смеет так поступать со мной?!"
    # учитель, не слушая ее продолжает лизать и раздвигает ее ноги шире
    label gallery_15363:
    music Loved_Up
    sound vjuh3
    img 15348
    with diss
    w
    sound lick13
    music Groove2_85
    img 15349
    with diss
    m "!!!"
    m "Прекратите это немедленно!"
    m "Мистер Эдвардс!!!"
    # но сама продолжает стоять в этой позе, оперевшись об стол
    music Loved_Up
    img 15350
    with fade
    w
    sound lick13
    img 15351
    with diss
    w
    img 15352
    with diss
    w
    img 15353
    with fade
    mt "!!!"
    mt "Фу, неужели ему приятно делать такие мерзкие вещи?!"
    sound ahhh11
    img 15354
    with diss
    mt "Это так... Так щекотно..."
    mt "..."
    # учитель прекращает лизать, проводит по киске пальцем и погружает его в Монику
    img 15355
    with fade
    sound chpok3
    w
    img 15356
    with diss
    m "Ай! Нет!"
    m "Прекратите!!!"
    m "Уберите сейчас же!"
    w
    music stop
    img 15357
    with diss
    sound chmok2
    w
    sound chmok2
    img 15358
    with diss
    w
    music Loved_Up
    sound ahhh11
    img 15359
    with fade
    mt "Боже, что же мне делать?"
    mt "Мне надо остановить его!"
    # учитель начинает двигать пальцем туда-сюда, он уже расстегнул брюки себе, член в полной готовности
    img 15360
    with diss
    sound chmok2
    mt "Надо... Остановить."

######################################
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float(rand(1,7))*1.0) + " loop 0.0>Sounds/v_Monica_Teacher_Fingering1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_Fingering1_1 = Movie(play="video/v_Monica_Teacher_Fingering1_1.mkv", fps=30)
    show videov_Monica_Teacher_Fingering1_1
    with fadelong
    wclean

    if game.extra == True:
        music stop
        stop music
        play music "<from " + str(float(rand(1,7))*1.0) + " loop 0.0>Sounds/v_Monica_Teacher_Fingering1_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
        scene black
        image videov_Monica_Teacher_Fingering1_2 = Movie(play="video/v_Monica_Teacher_Fingering1_2.mkv", fps=30)
        show videov_Monica_Teacher_Fingering1_2
        with fadelong
        wclean
######################################

    music Loved_Up
    sound snd_zip
    img 15361
    with fade
    mt "Сейчас же..."
    mt "Почему такое чувство, как-будто... Как-будто..."
    # учитель продолжает ласкать ее рукой, встает, приближает свой член к киске, уже почти прикоснулся
    sound Jump1
    img 15362
    with diss
    w
    img 15363
    with diss
    sound chmok2
    mt "Что за странное ощущение?"
    mt "Не понимаю, что со мной... Надо прекратить это немедленно..."
    img 15364
    with diss
    w
    label gallery_15382:
    music Groove2_85
    img 15365
    with fade
    m "Мне это совсем не нравится! Не смейте этого делать!"
    m "Прекратите!!!"
    music Hidden_Agenda
    img 15366
    with diss
    teacher "Да, конечно, миссис Бейкер... Еще несколько минут и я прекращу..."
    # и вводит головку в нее
    # Моника в панике
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up2
    sound2 Jump2
    img 15367
    with hpunch
    sound chmok2
    m "АААА!"
    m "НЕЕЕЕТ!"
    # но вырваться не пытается, ноги послушно раздвинуты, учитель входит в нее полностью
    w

    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float(rand(1,5))*1.16666667) + " loop 0.0>Sounds/v_Monica_Teacher_Sex1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_Sex1_1 = Movie(play="video/v_Monica_Teacher_Sex1_1.mkv", fps=30)
    show videov_Monica_Teacher_Sex1_1
    with fadelong
    wclean
    music Loved_Up2
    img 15382
    with diss
    w
    img 15368
    with fade
    mt "Черт! Черт!"
    if game.extra == True:
        music stop
        stop music
        play music "<from " + str(float(rand(1,5))*1.16666667) + " loop 0.0>Sounds/v_Monica_Teacher_Sex1_3.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
        scene black
        image videov_Monica_Teacher_Sex1_3 = Movie(play="video/v_Monica_Teacher_Sex1_3.mkv", fps=30)
        show videov_Monica_Teacher_Sex1_3
        with fadelong
        wclean
    music stop
    stop music
    play music "<from " + str(float(rand(1,5))*1.16666667) + " loop 0.0>Sounds/v_Monica_Teacher_Sex1_5.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_Sex1_5 = Movie(play="video/v_Monica_Teacher_Sex1_5.mkv", fps=30)
    show videov_Monica_Teacher_Sex1_5
    with fadelong
    wclean

    music Loved_Up2
    img 15369
    with diss
    m "Ах!"
    img 15370
    with diss
    mt "Я чувствую ЭТО в себе!!!"
    mt "Черт! Нет!"
    m "!!!"
    # учитель подается назад, почти выходит из нее, но не до конца, потом снова входит
    img 15371
    with fade
    m "Ох!"

    music stop
    stop music
    play music "<from " + str(float(rand(1,5))*1.16666667) + " loop 0.0>Sounds/v_Monica_Teacher_Sex1_4.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_Sex1_4 = Movie(play="video/v_Monica_Teacher_Sex1_4.mkv", fps=30)
    show videov_Monica_Teacher_Sex1_4
    with fadelong
    wclean
    music Loved_Up2
    img 15372
    with diss
    sound ahhh11
    mt "Какое непонятное чувство... Что-то внизу живота и... ТАМ!"
    mt "Что он со мной делает?!"
    mt "Я хочу, чтобы он... Ах! ...чтобы он остановился!"
    music stop
    stop music
    play music "<from " + str(float(rand(1,5))*1.16666667) + " loop 0.0>Sounds/v_Monica_Teacher_Sex1_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
    scene black
    image videov_Monica_Teacher_Sex1_2 = Movie(play="video/v_Monica_Teacher_Sex1_2.mkv", fps=30)
    show videov_Monica_Teacher_Sex1_2
    with fadelong
    wclean
    if game.extra == True:
        music stop
        stop music
        play music "<from " + str(float(rand(1,5))*1.16666667) + " loop 0.0>Sounds/v_Monica_Teacher_Sex1_6.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
        scene black
        image videov_Monica_Teacher_Sex1_6 = Movie(play="video/v_Monica_Teacher_Sex1_6.mkv", fps=30)
        show videov_Monica_Teacher_Sex1_6
        with fadelong
        wclean
    # учитель ускоряется, Моника удивлена и испугана новыми ощущениями
    # в итоге сцены секса Моника не кончает, учитель кончит ей на ягодицы
    # Моника спешит одеться, ее бомбит, паника еще не прекратилась

####################################



#####################################

    music Loved_Up2
    img 15373
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    mt "!!!"
    img 15374
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    img 15375
    with fade
    mt "Фуууу!!! Он испачкал меня!"
    mt "Долбанный высокоморальный извращенец!!! Что он натворил?!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15376
    with fadelong
    mt "!!!"
    mt "..."
    mt "Чувствую себя также непонятно, как после вылизываний Барди и его друга..."
    img 15377
    with fade
    mt "..."
    mt "Похоже это нервный срыв из-за всего за последнее время...!"
    # учитель застегивает штаны и садится за свой стол, довольный собой
    music Hidden_Agenda
    img 15378
    with diss
    teacher "Я весьма рад такой благодарности от вас, миссис Бейкер!"
    teacher "Я давно хотел это сделать."
    # Моника убивает его взглядом
    music Power_Bots_Loop
    img 15379
    with fade
    mt "Он занялся со мной сексом (!!!) в классе, где сидят студенты!"
    mt "Я не хочу больше видеть этого учителя! Никогда! Ненавижу его!"
    mt "Ненавижу их всех! Больше никому не позволю прикасаться ко мне!!!"
    mt "!!!"
    music Hidden_Agenda
    img 15380
    with diss
    teacher "Надеюсь, мы с вами еще увидимся, миссис Бейкер?" #широко улыбаясь
    # Моника еще раз убивает его взглядом
    music Power_Bots_Loop
    img 15381
    with fade
    mt "!!!"
    # Моника молча уходит
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    return

label gallery_22574:
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("ТЕМ ВРЕМЕНЕМ...")) from _rcall_textonblack_23
    scene black_screen
    with Dissolve(1)
    # в кабинет к Эдвардсу заходит мисс Мэнсфилд, в руках нагайка, учитель вскакивает со своего стула, широко улыбается
    music Groove2_85
    img 22558
    with fadelong
    w
    sound highheels_short_walk
    img 22559
    with diss
    w
    img 22560
    with fade
    teacher "Вы сегодня восхитительно выглядите, мисс Мэнсфилд."
    teacher "Рад вас видеть! Присаживайтесь."
    # училка делает несколько шагов по кабинету, останавливается, стоит в уверенной позе с надменным выраженем лица
    img 22561
    with fade
    mansfield "Давайте, ближе к делу, мистер Эдвардс!"
    # Эдвардс, посерьезнев
    music Hidden_Agenda
    img 22562
    with diss
    teacher "Да, конечно. Я доработал методику для вас. Осталось внести всего несколько поправок."
    img 22563
    with fade
    mansfield "..."
    img 22564
    with diss
    teacher "Завтра утром я ее вам отдам, мисс Мэнсфилд."
    music Groove2_85
    sound highheels_short_walk
    img 22565
    with fade
    mansfield "В таком случае до завтра, мистер Эдвардс!" #строго
    # училка поворачивается, чтобы уйти, Эдвардс ей вслед
    img 22566
    with diss
    teacher "Мисс Мэнсфилд?!"
    # она поворачивается, вопросительно смотрит на него
    img 22567
    with diss
    mansfield "???"
    img 22568
    with fade
    teacher "Я... для вас..."
    teacher "Я очень старался для вас, мисс Мэнсфилд." #волнуясь
    teacher "Это лучшая прогрессивная методика преподавания."
    teacher "Я проделал огромную работу..."
    music Hidden_Agenda
    img 22569
    with diss
    teacher "Я был бы очень рад угостить вас ужином, мисс Мэнсфилд."
    teacher "Для меня это будет лучшая благодарность с вашей стороны."
    # училка подходит к нему, тыкает своей нагайкой ему в грудь и со строгим фейсом
    music Groove2_85
    sound Jump2
    img 22570
    with vpunch
    mansfield "Мистер Эдвардс! Сколько раз можно заводить этот разговор про ужин?"
    mansfield "Ответ тот же..."
#    music Groove2_85
    img 22571
#    with diss
    mansfield "НЕТ!"
    img 22572
    with fade
    mansfield "Уясните, меня это НЕ ИНТЕРЕСУЕТ!"
    mansfield "Меня ВЫ не интересуете!"
    music Hidden_Agenda
    img 22573
    with diss
    teacher "Тогда, можеть быть... Кофе?" #растерянно
    teacher "Составите мне компанию, мисс Мэнсфилд?"
    music Groove2_85
    sound Jump2
    img 22574
    with vpunch
    mansfield "Ответ НЕТ."
    # убирает нагайку с его груди, он держится за это место, она ему с насмешкой
#    music Groove2_85
    img 22575
    with diss
    mansfield "И о какой благодарности с моей стороны может быть речь?!"
    mansfield "Вообще-то, это Я вам сделала одолжение, мистер Эдвардс!"
    img 22576
    with fade
    teacher "???" #удивленно
    img 22577
    with diss
    mansfield "Я не рассказала про вашего студента директору..."
    mansfield "По вашей просьбе."
    img 22578
    with fade
    teacher "..."
    img 22579
    with diss
    mansfield "Не знаю, зачем вы так за него заступаетесь..."
    teacher "Он... Я..." #растерянно
    music Groove2_85
    sound vjuh3
    img 22580
    with fade
    mansfield "Надеюсь, вас за это хорошо отблагодарили, мистер Эдвардс."
    sound highheels_short_walk
    img 22581
    with diss
    teacher "!!!" #он офигел
    # училка поворачивается и уходя, тыча в его сторону нагайкой, строго
    img 22582
    with fade
    mansfield "Жду мою методику завтра!"
    # хлопает дверью, Эдвардс стоит расстроенный
    music stop
    img black_screen
    with diss
    pause 2.0
    return

############ Julia 1############

label gallery_20231:

# ЧТО?! Юлия?!
# julia "Миссис Бакфетт?"
# m "Что ты делаешь здесь?"
# julia "Я... Я здесь работаю, Миссис Бакфетт..."
    # в движке

    music Groove2_85
    img 20231
    with fadelong
    julia "Миссис Бакфетт?" # ошарашена
    img 20230
    m "Что ты делаешь здесь?"
    img 20232
    with diss
    julia "Я... Я здесь работаю, Миссис Бакфетт..."

    if juliaFirePlanned == True and juliaFireCancelled == False: # Моника уволила Юлию
# Если Моника уволила Юлию
        music Pyro_Flow
        img 20233
        with fade
        m "Я уже уволила тебя, нерадивая гувернантка!"
        m "Значит тебя в дверь, а ты в окно?!"
        img 20234
        with diss
        w
        sound highheels_short_walk
        img 20235
        with diss
        w
        music stop
        img black_screen
        with diss
        pause 1.0
        music Pyro_Flow
        # Моника садится
        img 20236
        with fadelong
        m "Встать сюда!"
        sound highheels_short_walk
        img 20237
        with diss
        w
        img 20238
        with fade
        m "После увольнения из моего дома, ты решила устроиться ко мне в офис?!"
        img 20239
        with diss
        m "Ты за кого меня принимаешь, Юлия?"
        img 20240
        with fade
        julia "Миссис Бакфетт... Я... Я не знала что это Ваш офис..."
        julia "Меня сюда устроил Мистер Фред..."
        img 20241
        with diss
        m "Фред? Этот мерзавец! Он все-время ведет игру за моей спиной!"
        m "Сначала он подсунул нерадивую гувернантку ко мне в дом!"
        m "А теперь привел ее в мой офис!"
        img 20242
        with diss
        m "С какой стати он делает тебе такие одолжения, Юлия?!"
        m "Ты что, спишь с ним?!"
        # если Юлия имела секс
        if juliaHasSexInPool == True:
            music Hidden_Agenda
            img 20243
            with fadelong
            julia "..." # (напряженно смотрит)
        else:
            # если не имела секс
            music Power_Bots_Loop
            img 20244
            with fadelong
            julia "Я не сплю с ним, Миссис Бакфетт!"

    else:
        # Если Моника не увольняла Юлию
        music stop
        img black_screen
        with diss
        sound highheels_short_walk
        pause 1.0
        music Groove2_85
        img 20245
        with fadelong
        m "Как ты здесь оказалась?"
        img 20246
        with fade
        julia "Миссис Бакфетт, Мистер Фред сказал мне что Вы надолго уехали и у меня теперь нет работы в доме."
        julia "Мне было долго не найти другую работу, но, в конце концов, Мистер Фред помог мне устроиться сюда."

    # продолжение после разветвления
    music Groove2_85
    img 20247
    with fade
    m "Ладно, опустим детали."
    m "Итак, ты теперь работаешь здесь и снова подчиняешься мне."
    m "Я буду работать в этом же кабинете."
    img 20248
    with diss
    julia "Миссис Бакфетт, я думала что у меня самая низкая должность здесь."
    julia "Для меня удивительно что я буду работать рядом с Вами..."
    img 20249
    with fade
    m "В моей компании не бывает незначительно работы, Юлия."
    m "Обработка этих отчетов очень важна для нас."
    m "Я буду присутствовать здесь, чтобы проследить тщательность, с которой ты будешь выполнять эту ответственную работу."
    img 20252
    with fade
    julia "Да, Миссис Бакфетт. Как скажете..." #(боится)
    img 20250
    with diss
    mt "Эти никчемные отчеты никому не нужны!"
    mt "Биф просто решил почесать свое эго, проявив власть надо мной."
    mt "Что-ж, мне стоит подыграть ему."
    img 20251
    with diss
    mt "Он даже не догадывается, что рядом с ним настоящая Моника Бакфетт!"
    mt "Умная, расчетливая и хладнокровная!"
    mt "И я верну назад мою компанию и все остальное!"
    img 20253
    with diss
    mt "Даже если мне придется переступить через себя и рыться в этом бумажном хламе..."
    mt "Временно..."

    return

label gallery_20286:
    # Если обратиться к Юлии
    music Groove2_85
    img 20278
    with fadelong
    m "Юлия, подойди ко мне!"
    sound highheels_run2
    img 20279
    with fade
    julia "Да, Миссис Бакфетт?"
    img 20280
    with diss
    m "Юлия, что там с отчетами, которые надо обработать сегодня?"
    img 20281
    julia "Их очень много, Миссис Бакфетт."
    julia "У меня впечатление, что это объем для обработки двумя сотрудниками."
    img 20282
    with diss
    julia "Я не представляю как справлюсь с этим!"
    julia "Мне придется работать с этим до ночи!"
    menu:
        "Заставить Юлию работать допоздна.":
            pass
        "Пожалеть Юлию.":
            music Stealth_Groover
            img 20287
            with fade
            m "Юлия, да, отчетов дейтвительно много."
            m "Однако, это не повод задерживаться допоздна."
            m "Сделай сколько успеешь до конца рабочего дня и можешь быть свободна."
            img 20288
            with diss
            julia "Миссис Бакфетт, большое спасибо Вам!"
            return
    img 20284
    with fade
    m "Юлия, ты здесь новый сотрудник."
    m "И ты должна проявить себя."
    m "Я здесь для того, чтобы приглядывать за тобой."
    img 20285
    with diss
    m "Ты ведь не намекаешь на то, что я должна помогать тебе в этой работе?"
    if juliaOfficeOffended1 == False:
        $ juliaOfficeOffended1 = True
        $ juliaOfficeOffendedDay = day
    img 20286
    julia "Нет, Миссис Бакфетт. Что Вы?"
    img 20283
    with diss
    julia "Я сделаю все сама."
    julia "Пожалуйста. Извините меня!"
    # скип до вечера с событиями
    return

label gallery_20836:
# Начало после того как Моника отдаст первый отчет Бифу
# После нажатия начать работу появляется Фред.
# Фред говорит Монике какая встреча, Миссис Бакфетт.
# Рад видеть Вас в кресле Босса.
# Юлия смотрит с удивлением.
    music Hidden_Agenda
    img 20797
    with fadelong
    w
    music stop
    sound plastinka2
    img 20798
    with hpunch
    mt "ФРЕД?!"
    music Groove2_85
    img 20799
    with fade
    fred "О, какая встреча, Миссис Бакфетт."
    fred "Рад видеть Вас в кресле Босса."
    music Hidden_Agenda
    img 20800
    with diss
    julia "???"

# Моника говорит Фреду что он делает здесь?!
# Фред отвечает что он работает в этой компании, поэтому это странный вопрос. И непрофессиональный.
# Моника говорит что его профессионализм не должен выходить за пределы рулевого колеса.
# Моника строго спрашивает у Юлии не пришел-ли Фред к ней?
# Юля смущается.
    music Pyro_Flow
    img 20801
    with fade
    m "Фред, что ты делаешь здесь?!"
    img 20802
    with diss
    fred "Миссис Бакфетт, я работаю в этой компании, поэтому Ваш вопрос звучит странно."
    fred "И непрофессионально."
    img 20803
    with fade
    m "Твой профессионализм не должен выходить за пределы рулевого колеса, Фред!"
    m "Что ты здесь делаешь, спрашиваю еще раз!"
    img 20804
    with diss
    m "Юлия, он что, пришел к тебе?!"
    img 20805
    with diss
    julia "..."
# Фред говорит что, если говорить о сферах профессионализма, то, возможно, кое-кому стоит ограничиться обязанностями гувернантки.
# А работа Боссом может выходить за профессиональные рамки основной профессии.
# Юлия смотрит на Фреда
# Фред смотрит на Монику улыбаясь
# Моника смотрит напряженно на Фреда и на Юлию
# Моника говорит Юлии, чтобы она вышла из кабинета, быстро.
    music Groove2_85
    img 20806
    with fade
    fred "Миссис Бакфетт."
    fred "Если говорить о сферах профессионализма, то, возможно, кое-кому стоит ограничиться обязанностями гувернантки."
    fred "А работа Боссом при этом - это выход за профессиональные рамки основной профессии."
# Юлия смотрит на Фреда
    music Master_Disorder
    img 20807
    with diss
    julia "???"
# Фред смотрит на Монику улыбаясь
    img 20808
    with diss
    m "!!!"
    img 20809
    with diss
    fred "..."
# Моника смотрит напряженно на Фреда и на Юлию
    img 20810
    with diss
    m "..."
# Моника говорит Юлии, чтобы она вышла из кабинета, быстро.
    music Power_Bots_Loop
    img 20811
    with fadelong
    m "Юлия, выйди из кабинета."
    m "Быстро!"

# Юлия выходит
    img 20812
    with diss
    julia "..."

    # затемнение

# Моника говорит Фреду не слишком-ли тот зарывается
# Добавляет (если ударила его рукой или ногой) мало-ли ему показалось в прошлый раз?
# Фред отвечает, что усвоил то, что Монику лучше не трогать и не принуждать к чему-то силой.
# Это опасно
# Моника отвечает что рада что Фред это понимает.
    sound highheels_run2
    music stop
    img black_screen
    with diss
    pause 1.5
    sound snd_door_close1
    music Pyro_Flow
    img 20813
    with fadelong
    m "Фред, не слишком-ли ты нарываешься?!"
    # если била его рукой или ногой
    if fredKickedByMonicaToBalls == True or fredKickedByMonicaToFace == True:
        m "Тебе что, в прошлый раз показалось мало?!"
    #
    music Groove2_85
    img 20814
    with diss
    fred "Миссис Бакфетт, я усвоил то, что Вас лучше не трогать и не принуждать к чему-либо силой."
    fred "В вашем случае это опасно."
    img 20815
    with diss
    m "Я рада что ты, Фред, это понимаешь."

# Фред отвечает, что гораздо безопаснее, если Моника сделает это сама.
# Моника злится и спрашивает что Фред имеет ввиду?
# И говорит что не собирается спать с Фредом ни за что!
# Фред говорит что насчет попки Миссис Бакфетт у него отдельные планы.
# Они связана с попками Стефани и Ребекки, если Моника помнит...
    img 20816
    with fade
    fred "Гораздо безопаснее, Миссис Бакфетт, если Вы сделаете это сами..."
    music Power_Bots_Loop
    img 20817
    with hpunch
    m "!!!"
    img 20818
    with diss
    m "Что ты имеешь ввиду, Фред?!"
    m "Если ты рассчитываешь на то, чтобы я спала с тобой, то можешь даже не надеяться!"
    m "Я не пойду на это ни за что!"
    music Groove2_85
    img 20819
    with fade
    fred "О, Миссис Бакфетт, насчет Вашей попки у меня отдельные планы."
    img 20820
    with diss
    fred "Они также связаны с попками Стефани и Ребекки, если Вы помните..."
# Моника зло отвечает Фред...
# Фред говорит что Миссис Бакфетт хороший Босс.
# А у хорошего Босса не должно быть секретов от своих подчиненных.
# Это непрофессионально.
# Моника спрашивает на что Фред намекает
    music Master_Disorder
    img 20821
    with diss
    mt "!!!"
    m "Фред..." # Шипит убийственно
    music Groove2_85
    img 20822
    with fade
    fred "Миссис Бакфетт, Вы хороший Босс."
    fred "А у хорошего Босса не должно быть секретов от своих подчиненных."
    fred "Это непрофессионально."
    img 20823
    with diss
    m "На что это ты намекаешь, Фред?!"
# Фред отвечает что считает профессиональным долгом рассказать всему коллективу о том, что их Босс имеет основную работу.
# Гувернантки.
# Моника злится
    img 20824
    with diss
    fred "Миссис Бакфетт, я считаю профессиональным долгом рассказать всему коллективу о том, что их Босс имеет основную работу..."
#    music stop
    img 20825
    fred "Гувернанткой." # вблизи улыбается
    music Master_Disorder
    img 20826
    with hpunch
    m "!!!" # Моника в ярости
# Если уровень Барди низкий, то говорит что гувернантки, которая носит трусики Юлии, потому что у нее нет других.
# (если уровень не выше далее) И она теперь трет пятно на ковре в своем доме, сверкая Юлиными трусиками каждый день.
# Если уровень Барди выше (?), то говорит что гувернантки, которая носит трусики своей новой хозяйки, которые та носила за день до этого
# (если уровень не выше далее) И она теперь трет пятно на ковре в своем доме, сверкая разными трусиками каждый день.
# Если уровень Барди выше (?), то говорит, но которой, в конце концов, вообще запретили носить трусики
# И она теперь трет пятно на ковре без трусиков, сверкая своей очаровательной попой.

    if char_info["Bardie"]["level"] < 3:
        img 20827
        with diss
        fred "Гувернанткой, которой приходится носить трусики Юлии, потому что у нее нет других."
        img 20828
        with diss
        fred "Или, может быть, ей нравится это..."
        img 20830
        with diss
        fred "И она теперь трет пятно на ковре в своем доме, сверкая Юлиными трусиками каждый день."
    else:
        if char_info["Bardie"]["level"] < 5:
            img 20827
            with diss
            fred "Гувернанткой, которая носит трусики Юлии, а также трусики своей новой хозяйки."
            img 20828
            with diss
            fred "Которые та носила за день до этого."
            img 20830
            with diss
            fred "И она теперь трет пятно на ковре в своем доме, сверкая то Юлиными трусиками, то трусиками хозяйки каждый день."
        else:
            img 20827
            with diss
            fred "Гувернанткой, которая носила трусики Юлии, а затем трусики новой хозяйки дома."
            img 20828
            with diss
            fred "Которые та носила за день до этого."
            fred "И она терла пятно на ковре в своем доме, сверкая то Юлиными трусиками, то трусиками хозяйки каждый день."
            img 20829
            with diss
            m "!!!"
            fred "А затем ей вообще запретили носить трусики."
            img 20830
            with diss
            fred "И она теперь трет пятно на ковре без трусиков, сверкая своей очаровательной попой."

# Я люблю смотреть на Вашу попу, Миссис Бакфетт, когда Вы трете пятно...
    music Groove2_85
    img 20831
    with fade
    fred "Я люблю смотреть на Вашу попу, Миссис Бакфетт."
    fred "Когда Вы трете то пятно..."
# Моника !!!
# Ты не расскажешь этого никому!
# Почему-же? Ваше фото и видео того, как Вы трете пятно, понравится всем в этом отделе.
# Моника отвечает у тебя не фото и видео этого, ты лжешь!
# Фред отвечает что нет, но он может сделать их в любое время, например завтра.
# Или послезавтра. Ведь Моника не будет уклоняться от обязанностей по дому, правда?
# Моника злится!
    music Power_Bots_Loop
    img 20832
    with hpunch
    m "!!!" # Моника в ярости
    img 20833
    with fade
    m "Ты не расскажешь этого никому!" # шипит
    fred "Почему-же?"
    fred "Ваше фото и видео того, как Вы трете пятно, понравится всем в этом отделе."
    img 20834
    with vpunch
    m "У тебя нет ни фото, ни видео этого!"
    m "Ты лжешь!"
    img 20835
    with diss
    fred "Вы правы, у меня этого нет."
    fred "Но я могу сделать их в любое время."
    fred "Например, завтра."
    fred "Или послезавтра."
    img 20836
    with diss
    fred "Ведь Вы стараетесь быть хорошей гувернанткой и не будете уклоняться от обязанностей по дому, правда?"
    fred "В конце концов, я за Вас поручился перед Мистером Робертсом."
    img 20837
    with diss
    m "!!!"

# Особенно это видео понравится Юлии.
# Я, пожалуй, покажу его ей первой.
# Моника отвечает: Фред, мерзавец. Ты всегда пользуешься ситуацией в свою пользу.
# ...
# Ты говорил что у тебя другие планы... насчет меня...
# Что ты хочешь сейчас? Ведь ты меня просто шантажируешь, я знаю.
# Ты не станешь никому рассказывать про то что я делаю в своем доме.
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20838
    with fadelong
    fred "Особенно это видео понравится Юлии."
    m "!!!"
    img 20839
    with diss
    fred "Я, пожалуй, покажу ей эти видео-материалы первой."
    sound snd_door_open1
    img 20840
    with fadelong
    sound highheels_run2
    w1 "Миссис Бакфетт, можно войти?"
    music Power_Bots_Loop
    img 20841
    with vpunch
    m "Вон отсюда!"
    # убегает темнота
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 1.5
    music Groove2_85
    img 20842
    with fadelong
    m "..."
    m "Фред, мерзавец..."
    m "Ты всегда пользуешься ситуацией в свою пользу."
    img 20843
    with diss
    fred "..." # Улыбается
    music Hidden_Agenda
    img 20844
    with fade
    m "..."
    m "Ты говорил что у тебя другие планы... насчет меня..."
    m "Что ты хочешь сейчас?"
    m "Ведь ты меня просто шантажируешь, я знаю."
    m "Ты не станешь никому рассказывать про то что я делаю в своем доме."

# Фред отвечает что это сущая мелочь.
# Фред уважает Миссис Бакфетт как Босса и как профессионала и хочет, чтобы та просто вела себя более вежливо по отношению к Юлии.
# Моника отвечает что и так ведет себя по отношению к Юлии как того требует профессиональная этика.
# Фред отвечает что Юлия хрупкая и ранимая девушка и ей не помешало бы побольше нежности от такого строгого Босса как Моника.
# Скажите Юлии в следующий раз, что она хорошо выглядит сегодня.
    img 20845
    with diss
    fred "О, Миссис Бакфетт, мне нужна сущая мелочь."
    fred "Я уважаю Вас как Босса и как профессионала."
    fred "И я хочу, чтобы Вы просто вели себя более вежливо по отношению к Юлии."
    img 20846
    with fade
    m "Я и так веду себя по отношению к Юлии так, как того требует профессиональная этика."
    img 20847
    with diss
    fred "Да, но Юлия хрупкая и ранимая девушка."
    fred "И ей бы не помешало побольше нежности от такого строгого Босса как Вы, Миссис Бакфетт."
    img 20848
    m "???"
    img 20849
    with diss
    fred "Скажите Юлии, что она хорошо выглядит сегодня."

# Моника отвечает что не понимает зачем?
# Фред отвечает что Вы скажете это, иначе Ваше профессиональные тайны станут достоянием общественности.
# Моника злится и спрашивает когда она должна это сделать?
# Фред отвечает что завтра или в ближайшее время.
# Моника спрашивает и как ты узнаешь что я это сделала.
# Фред говорит что общается с Юлей и что Юля расскажет об этом непременно.
    music Groove2_85
    img 20850
    with fade
    m "Я не понимаю, зачем мне это говорить?"
    m "Она всего-лишь работник, а я ее Босс!"
    fred "Вам придется это сказать, Миссис Бакфетт."
    fred "Иначе Ваши профессиональные тайны станут достоянием общественности."
    img 20851
    with diss
    m "!!!"
    img 20852
    with diss
    fred "..." # Улыбается
    img 20853
    with fade
    m "Ладно..."
    m "Когда я должна это сделать?"
    fred "Сделайте это завтра или в ближайшие дни."
    m "И как ты узнаешь что я это сделала?"

    img 20854
    with diss
    if juliaHasSexInPool == True:
        # Если Юлия спала с фредом
        fred "Юлия иногда доверяется моему... профессиональному мнению."
    else:
        # Юлия не имела секса с Фредом
        fred "Юлия немного стесняется меня, но иногда спрашивает моего совета."
        fred "Дополнительное доверие ко мне поможет ей расслабиться в будущем."
    #

# Выбор
# Я подумаю над этим.
# Моника отвечает что подумает над этим.
# Фред уходит, говоря что подумайте, Миссис Бакфетт.
    img 20851
    with diss
    menu:
        "Я подумаю над этим.":
            pass
        "Прогнать Фреда (пропуск событий с Юлией).":
# Либо:
# Прогнать Фреда
# Моника говорит Фреду чтобы он убирался со своими мелкими шантажами!
# И, если хоть что-то просочится сюда про нее, то она оторвет ему яйца.
# Жаль что не сделал этого в прошлый раз!
# Фред говорит что мы еще обсудим это, Миссис Бакфетт и уходит.
# В таком случае квест скипается
            music Power_Bots_Loop
            img 20855
            with fade
            m "Фред, лучше убирайся со своими мелкими шантажами!"
            m "Предупреждаю!"
            img 20856
            with diss
            m "Если хоть что-то просочится в эти стены про то, что я делаю в своем доме..."
            m "Я оторву тебе яйца, клянусь!" # злая близко
            # Если Моника била Фреда в фитнес зале
            if fredKickedByMonicaToBalls == True or fredKickedByMonicaToFace == True:
                m "Жаль что я не сделала этого в прошлый раз в раздевалке фитнес зала!"
            return

# Проходит рабочий день.
    m "Я подумаю над этим."
    img 20852
    with diss
    fred "Я буду держаться в курсе, Миссис Бакфетт..."
    return

label gallery_20879:
# Появляется пункт сказать Юлии что Монике нравится ее прическа
# Моника говорит Юлии что она красивая девушка и Моника нравится ее прическа.
# Юлия странно смотрит на Монику с удивлением.
# И говорит спасибо, Миссис Бакфетт. У Вас тоже очень красивые волосы.
# Моника отвечает надменно что она знает об этом.
# Это действие добавляет уровень у Юлии
    music Hidden_Agenda
    sound highheels_short_walk
    img 20875
    with fade
    w
    img 20876
    with diss
    w
    img 20877
    with fade
    m "Юлия, ты..."
    img 20878
    with diss
    julia "Да, Миссис Бакфетт?"
    img 20879
    with fade
    m "Юлия... Ты... Ты красивая девушка."
    sound Jump2
    img 20880
    with vpunch
    julia "..."
    img 20881
    with fade
    m "И... И мне нравится твоя прическа."
    sound Jump1
    img 20882
    with diss
    julia "..." # ошарашена и странно смотрит
    music Groove2_85
    img 20883
    with fade
    m "..." # надменно
    img 20884
    with diss
    julia "Спасибо, Миссис Бакфетт."
    julia "У Вас тоже очень красивые волосы."
    img 20885
    with diss
    m "Спасибо, но я и так знаю это!" # Надменно отвечает и уходит
    sound highheels_short_walk
# Это действие добавляет уровень 1 у Юлии
    return

label gallery_20899:
# Появляется выбор сказать Юлии комплимент по поводу тела.
# Моника сидит за креслом и зовет Юлию, чтобы та подошла к Монике
# Юлия подходит
# Моника напрягается и смотрит на Юлию
# Юлия вопросительно смотрит на Монику
# Моника говорит Юлии что у нее красивая фигура и Монике нравится ее грудь.
# Юлия очень удивленно смотрит на Монику и молчит
# Моника говорит Юлии, чтобы та повернулась спиной к ней
    music Groove2_85
    img 20886
    with fadelong
    w
    img 20887
    with diss
    m "Юлия, подойди ко мне!"
# Юлия подходит
    sound highheels_short_walk
    img 20888
    with fadelong
    julia "Да, Миссис Бакфетт?" # немного испуганно
    img 20889
    with diss
    m "..."
    img 20890
    with diss
    julia "..." # вопросительно
    music Hidden_Agenda
    img 20891
    with fade
    m "Юлия..."
    img 20892
    with diss
    m "Юлия, у тебя красивая фигура и мне нравится твоя грудь."
    sound Jump1
    img 20893
    with vpunch
    julia "..." # Юлия очень удивленно смотрит на Монику и молчит
    music Groove2_85
    img 20894
    with fade
    m "А теперь повернись ко мне спиной!" # жестко

# Юлия поворачивается
# Моника говорит что у Юлии также красивая попа и что она нравится МОнике
# Юлия ошарашенно смотрит на Монику
# Моника зло смотрит на Юлию
# Юлия отвечает Сссспасибо, Миссис Бакфетт.
# Для меня это неожиданно. Я могу идти на свое рабочее место?
# Моника говорит что да, она может идти
# Это действие добавляет уровень у Юлии
    img 20895
    with diss
    julia "???"
    img 20896
    with diss
    m "!!!"
    music Hidden_Agenda
    img 20897
    with fade
    w
    img 20898
    with diss
    w
    img 20899
    with diss
    w
    img 20900
    with fade
    m "У тебя также красивая попа и она также нравится мне."
    sound Jump2
    img 20901
    with vpunch
    julia "!!!" # Юлия ошарашенно смотрит на Монику
    music Groove2_85
    img 20902
    with fade
    m "!!!" # Моника зло смотрит на Юлию
    img 20903
    with fade
    julia "Ссссс... Сссспасибо, Миссис Бакфетт..."
    julia "Для меня это неожиданно..."
    img 20904
    with diss
    julia "Я могу идти на свое рабочее место?"
    img 20905
    with diss
    m "Да, Юлия, ты можешь идти!"
# Это действие добавляет уровень 1 у Юлии
    return

label gallery_20923:
# Появляется вариант поцеловать Юлию
# Моника подходит к Юлии
# Юлия встает и говорит чем она может помочь?
# Моника говорит сядь и сиди работай, я просто хочу проверить как ты работаешь
# Юлия отвечает да, конечно и садится
# Моника встает сзади и смотрит
    music Groove2_85
    sound highheels_short_walk
    img 20906
    with fadelong
    w
    sound desk_open
    img 20907
    with diss
    julia "Миссис Бакфетт, чем я могу помочь Вам?"
    music Hidden_Agenda
    sound highheels_short_walk
    img 20908
    with fade
    m "Юлия, сядь и сиди работай."
    m "Я просто хочу проверить как ты работаешь."
    img 20909
    with diss
    julia "Да, конечно, Миссис Бакфетт."
    julia "Как скажете."
    sound desk_open
    img 20910
    with fade
    m "..."
# Выбор:
# Поцеловать Юлию
# Не целовать.
# Нет, я не могу зайти настолько далеко. Все-таки, я Босс!
    img 20911
    with diss
    menu:
        "Поцеловать Юлию.":
            pass
        "Не целовать.": #corruption
            music Groove2_85
            img 20912
            with fade
            mt "Нет, я не могу зайти настолько далеко."
            mt "Все-таки, я Босс!"
            return

# Если поцеловать:
# Моника нагибается и пытается поцеловать Юлию
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 20913
    with fadelong
    w
    img 20914
    with diss
    w
    img 20915
    with diss
    w
    img 20916
    with diss
    w
    img 20917
    with diss
    w
    img 20918
    with diss
    w
# Если уровень не 2, то Юлия уворачивается и говорит: Миссис Бакфетт, что Вы собираетесь сделать?!


# Если уровень 2, то Моника быстро целует Юлию в щечку
# Юлия в шоке
# Спрашивает Миссис Бакфетт, что это было?
# Моника отвечает что ничего.
    sound snd_kiss2
    img 20922
    with diss
    m "(чмок)" #звук
    img 20924
    with diss
    w
    sound snd_kiss3
    img 20923 #чмок звук снова
    with hpunch
    julia "!!!"
    music Groove2_85
    img 20925
    with fade
    m "..."
    julia "Миссис Бакфетт, что это было?"
    img 20926
    with diss
    m "Ничего..." # уходит в кресло

# Моника садится в кресло.
# Моника сидит и смотрит в сторону гордо и надменно (думает гребаный фред)
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    img 20921
    with fadelong
    mt "Гребаный Фред!"
    mt "Я чувствую себя полной дурой!"
# Юлия ошарашенно продолжает сидеть и смотреть на Монику

# Это добавляет прогресс к ур.2
    return

label gallery_20944:
# Появляется вариант Ущипнуть Юлию за зад.
# Моника подходит к Юлии и просит ее встать и подойти к ней.
# Моника подходит к окну, Юлия следует за ней
    music stop
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    music Groove2_85
    img 20927
    with fadelong
    w
    sound desk_open
    img 20928
    with diss
    julia "Миссис Бакфетт?"
    sound highheels_short_walk
    img 20929
    with fadelong
    m "Юлия."
    m "Пожалуйста, встань и подойди ко мне."
# Моника встает чуть сзади Юлии и говорит ей посмотреть в окно.
# Спрашивает у Юлии что она там видит?
# Юлия смущается и говорит Монике что видит там город.
    sound highheels_short_walk
    img 20930
    with diss
    julia "..."
    music Loved_Up
    img 20931
    with diss
    m "Юлия, посмотри, пожалуйста, в окно."
    img 20932
    with fade
    julia "..."
    img 20933
    with diss
    w
    img 20934
    with diss
    m "Юлия, что ты там видишь?"
    img 20935
    with fade
    julia "Миссис Бакфетт, я вижу там город..."

# Выбор:
# Ущипнуть Юлию
# Не делать этого.
# # Если не делать: Моника говорит Юлии что хватит смотреть в окно, пора возвращаться к работе.
# Юлия подозрительно смотрит на Монику
    img 20936
    with diss
    menu:
        "Ущипнуть Юлию.": #corruption
            pass
        "Не делать этого.":
            music Groove2_85
            mt "Нет, я не могу сделать это..."
            # моника уходит к столу
            sound highheels_run2
            img 20937
            with fadelong
            m "Юлия, хватит смотреть в окно!"
            m "Пора возвращаться к работе!"
            julia "..." # удивленно смотрит
            return

    img 20938
    with fade
    w
    img 20939
    with diss
    m "Да, там город..."
# Если ущипуть:


# Если ур. больше или равен 3
# Моника щипает Юлию за попу.
# Юлия вскрикивает от неожиданности, она ошарашена.
# Спрашивает у Моники: Миссис Бакфетт, что Вы делаете?
# Вы ущипнули меня... за мою попу!
# Моника отвечает что это ей показалось и пусть она идет заниматься работой, а не смотреть в окно.
# Потому что, если она будет плохо работать, то ее ждет увольнение!
# Юлия в шоке отвечает да, конечно и идет работать
    # щипает
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    sound Jump1
    img 20940
    with diss
    w
    sound Jump2
    img 20944
    with diss #jump
    w
    music Power_Bots_Loop
    img 20946
    with hpunch
    julia "Ай!"
    img 20945
    with diss
    w
    sound Jump1
    img 20947
    with vpunch
    julia "!!!"
    img 20948
    with fade
    julia "Миссис Бакфетт, что Вы сделали?!"
    m "..."
    music Groove2_85
    img 20949
    with diss
    julia "Вы... Вы ущипнули меня за мою попу!"
    img 20950
    with fade
    m "Нет!"
    m "Видимо тебе что-то показалось, Юлия."
    m "Иди занимайся работой."
    m "Хватит смотреть в окно!"
    img 20951
    with diss
    julia "..."
    img 20952
    with fade
    m "Если ты будешь плохо работать, то тебя ждет увольнение!"
    julia "Да, Миссис Бакфетт..."
    julia "Конечно..."

# Это добавляет прогресс к ур.3
# Затем сообщение что дальнейший прогресс с Юлией будет доступен в следующем обновлении.
#    help "Дальнейший прогресс с Юлией будет доступен в следующем обновлении."
    return

label gallery_21930:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    music Groove2_85
    img 21911
    with fadelong
    mt "Какой же этот Фред мерзавец!"
    mt "Скорее бы вернуть себе все, что у меня отняли!"
    mt "Первым делом я уволю этого 'профессионала'!"
    music Hidden_Agenda
    img 21912
    with fade
    mt "!!!"
    mt "Как мне узнать цвет трусиков Юлии?"
    mt "Не могу же я у нее просто взять и спросить! Что она обо мне подумает?"
    mt "Как тогда мне это сделать?"
    mt "И чтобы Юлия ничего не заподозрила..."
    img 21913
    with diss
    mt "Хм..." # с улыбочкой
    # Моника подходит к своему столу, незаметно кладет на свой стол флешку. куда-нибудь за монитор. Потом тоном босса подзывает Юлию.
    sound highheels_short_walk
    img 21914
    with fadelong
    w
    music Groove2_85
    img 21915
    with fade
    m "Юлия! Подойди ко мне!"
    # Юлия подходит к Монике
    sound highheels_short_walk
    img 21916
    with diss
    julia "Да, Миссис Бакфетт?"
    img 21917
    with fade
    m "Юлия! Я потеряла свою флешку. А она мне срочно нужна!"
    m "Найди ее! Я ее, наверное, выронила где-то в кабинете."
    img 21918
    with diss
    julia "Хорошо, Миссис Бакфетт... Только... Где ее искать?"
    img 21919
    with fade
    m "Откуда я знаю?! Поищи под столом!" # раздраженно
    img 21920
    with diss
    julia "Да, Миссис Бакфетт. Сейчас посмотрю."
    # Юлия наклоняется и заглядывает под стол Моники
    img 21921
    with diss
    m "..."
    music Hidden_Agenda
    img 21922
    with diss
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            music Groove2_85
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return
    # Моника в это время пытается заглянуть ей под платье, но ей ничего не видно
    music Loved_Up
    img 21923
    with diss
    w
    img 21924
    with diss
    mt "Черт! Еще немного!"
    # Юлия выпрямляется, Моника делает вид, что тоже ищет флешку
    music Groove2_85
    img 21925
    with fade
    julia "Миссис Бакфетт, под вашим столом нет флешки..."
    m "..."
    mt "Конечно, ее там нет!.."
    img 21926
    with diss
    m "Юлия, ты уверена, что внимательно посмотрела?" # строго
    # Юлия неуверенно
    img 21927
    with diss
    julia "М-м-миссис Бакфетт, я сейчас посмотрю еще раз..."
    # Юлия встает на колени и заглядывает под стол, Моника в это время пытается посмотреть ей под платье
    music Loved_Up
    img 21928
    with fadelong
    w
    img 21929
    with diss
    w
    img 21930
    with diss
    w
    img 21931
    with diss
    mt "Все равно мне ничего не видно!"
    img 21932
    with diss
    w
    sound Jump1
    img 21933
    with diss
    mt "!!!"
    # Юлия выпрямляется, но все еще стоит на коленях и тут замечает на столе флешку
    img 21934
    with diss
    julia "???" # удивленно
    img 21935
    with diss
    w
    # Юлия поворачивается к Монике и замечает, что та пристально смотрит на ее зад
    img 21936
    with diss
    w
    #sound Юлия увидела флешку на полке
    sound vjuh3
    img 21937
    with fade
    w
    img 21938
    with diss
    w
    music Groove2_85
    img 21939
    with fade
    julia "Миссис Бакфетт... Что в-в-вы д-делаете?"  # вопросительно смотрит на Монику
    img 21940
    with diss
    m "..." # растерянно
    img 21941
    m "Ничего!"
    m "..."
    m "Ты нашла флешку?!" # строго
    # Юлия встает, с непонимающим видом
    img 21942
    with fade
    julia "Да, Миссис Бакфетт... Она лежит у вас на столе." # на полке
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 21943
    with fadelong
    m "..."
    img 21944
    with diss
    julia "..."
    # Моника с покер-фейсом протягивает руку
    img 21945
    with fade
    m "Давай ее мне!"
    # Юлия подходит, отдает флешку, смотрит на Монику вопросительно
    img 21946
    with diss
    julia "???"
    # Моника делает вид, что ничего не произошло
    img 21947
    with fade
    m "А теперь иди работай! Не отвлекайся!"
    # садится за свой стол и прячется за монитором
    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 21948
    with fade
    mt "Вот черт! Ничего не получилось!"
    mt "Более того, мне кажется, что она заметила, как я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    mt "!!!"
    mt "Мне нужно будет придумать еще что-нибудь..."
    return

label gallery_21978:
### На полках документов нет. Моника говорит достань. Юлия отвечает что там нет документов на тех полках. +
### Моника говорит они там есть (ей надо чтобы она туда полезла) +
### В итоге, Юлия ничего не находит +
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    music Groove2_85
    img 21949
    with fadelong
    mt "Не могу поверить! Мне приходится выяснять, какие трусики носит моя секретарша!!!"
    mt "И все из-за этого мерзавца Фреда!"
    mt "Как-будто без этого у меня мало забот!"
    mt "Я здесь начальник! Мне нужно думать о работе целого отдела и о том, как вернуть назад мою компанию, а не о трусиках секретарши!"
    music Hidden_Agenda
    img 21950
    with diss
    mt "..."
    mt "Как мне посмотреть на трусики Юлии?"
    mt "И чтобы она ничего не заподозрила..."
    img 21951
    with diss
    w
    img 21952
    with diss
    mt "Хм..." # с улыбочкой
    # Моника садится за свой стол. Потом тоном босса подзывает Юлию.
    music Groove2_85
    img 21953
    with fadelong
    m "Юлия! Подойди ко мне!"
    # Юлия подходит к Монике
    sound highheels_run2
    img 21954
    with diss
    julia "Да, Миссис Бакфетт?"
    img 21955
    with fade
    m "Юлия! Мне срочно для работы нужна папка с отчетами за прошлый год!"
    m "Достань мне ее!" # строго
    img 21956
    with diss
    julia "Хорошо, Миссис Бакфетт. А где эта папка?"
    img 21957
    with fade
    m "Эта папка стоит в шкафу на верхней полке."
    # Юлия смотрит на шкаф, никаких документов там нет, смотрит на Монику
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 21958
    with fadelong
    julia "М-м-Миссис Бакфетт... Там на полках... Там нет никаких папок и документов..."
    img 21959
    with diss
    mt "..."
    img 21960
    with fade
    m "Юлия! Я тебе говорю, что эта папка там есть! Достань мне ее!" # раздраженно
    m "Срочно!!!"
    # Юлия растерянно
    sound highheels_run2
    img 21961
    with diss
    julia "Да, Миссис Бакфетт... Я сейчас принесу стул..."
    # Юлия ставит стул, встает на него и тянется к верхней полке, где нет документов. Ее платье немного приподнимается
    sound highheels_run2
    img 21962
    with fade
    w
    sound Jump1
    img 21963
    with diss
    w
    music Hidden_Agenda
    img 21964
    with diss
    m "..."
    img 21965
    with diss
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            music Groove2_85
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return
    # Моника пытается заглянуть ей под платье, но ей ничего не видно
    img 21966
    with diss
    mt "Черт! Еще чуть-чуть и я увижу ее трусики!"
    music Groove2_85
    img 21967
    with fade
    julia "Миссис Бакфетт, здесь нет никаких документов..."
    img 21968
    with diss
    w
    music Hidden_Agenda
    img 21969
    with fade
    m "..."
    img 21970
    with diss
    m "Посмотри внимательнее, Юлия!" # строго
    # Юлия пытается найти папку, а Моника пытается заглянуть ей под платье
    img 21971
    with diss
    w
    img 21972
    with diss
    w
    img 21973
    with diss
    julia "Все равно мне ничего не видно!"
    img 21974
    with fade
    julia "???"
    music Loved_Up
    img 21975
    with diss
    w
    img 21976
    with diss
    w

    # Юлия поворачивает голову и видит, что Моника заглядывает ей под платье
    img 21977
    with fade
    julia "!!!" # удивленно
    img 21978
    with diss
    m "Ну же!"
    music Groove2_85
    sound Jump1
    img 21979
    with diss
    julia "Миссис Бакфетт... Что в-в-вы д-делаете?"  # вопросительно смотрит на Монику
    # Моника делает вид, что ничего не произошло
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 21980
    with fade
    m "..." # растерянно
    m "Ничего!"
    img 21981
    with diss
    julia "???"
    music Power_Bots_Loop
    img 21982
    with fade
    m "..."
    m "Ты нашла папку с отчетами, Юлия?!" # строго
    # Юлия с непонимающим видом спускается со стула
    music Groove2_85
    img 21983
    with fade
    julia "Нет, Миссис Бакфетт... На полке нет ничего."
    julia "..."
    img 21984
    with diss
    m "..."
    # Моника с серьезной миной
    m "Ты плохо искала, Юлия! Тебе ничего нельзя доверить!"
    img 21985
    julia "???"
    julia "Н-но..."
    img 21986
    with diss
    m "А теперь иди работай! И не отвлекайся!"
    # Юлия возвращается за свой стол, Моника прячется за монитором
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21987
    with fadelong
    mt "Вот черт! Ничего не получилось!"
    img 21988
    with diss
    mt "Более того, она увидела, как я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    img 21989
    with diss
    mt "!!!"
    mt "Мне нужно будет придумать еще что-нибудь..."
    mt "Иначе мерзавец Фред не оставит меня в покое..."
    return

label gallery_22003:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    music Groove2_85
    img 21990
    with fadelong
    mt "Не могу поверить! Мне приходится выяснять, какие трусики носит моя секретарша!!!"
    mt "Я здесь начальник! Мне нужно думать о работе целого отдела, а не о трусиках секретарши!"
    music Hidden_Agenda
    img 21991
    with diss
    mt "..."
    mt "Как мне посмотреть на трусики Юлии?"
    mt "И чтобы она ничего не заподозрила..."
    music Groove2_85
    img 21992
    with fade
    mt "Хм..." # с улыбочкой
    mt "Собственно, какая мне разница, что она подумает?"
    mt "Она же просто секретарша!"
    mt "А мне надо скорее заканчивать с этими дурацкими заданиями Фреда!"
    img 21993
    with diss
    mt "..."
    menu:
        "Заглянуть под стол Юлии.": #corruption
            pass
        "Не заглядывать.":
            music Groove2_85
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return
    # Моника лезет под стол Юлии, Юлия удивленно и испуганно смотрит вниз
    music Hidden_Agenda
    img 21994
    with fade
    sound Jump1
    w
    img 21995
    with diss
    w
    img 21996
    with diss
    w
    img 21997
    with diss
    w
    music Groove2_85
    img 21998
    julia "Миссис Бакфетт! Что вы делаете?!"
    img 21999
    m "Ничего!"
    m "Сиди и работай!"
    m "И не отвлекайся!"
    img 22000
    with fade
    julia "М-м-Миссис Бакфетт... Вы что-то потеряли? Вам помочь?" # растерянно
    img 22001
    with diss
    mt "Да!!! Раздвинь ноги и покажи свои трусики!"
    img 22002
    m "Нет!!! Я сама! Сиди и работай!"
    # Моника все это время пытается посмотреть, в каких трусиках Юлия, но ей ничего не видно
    music Loved_Up
    img 22003
    with diss
    mt "Еще чуть-чуть и я увижу ее трусики!"
    mt "!!!"
    sound Jump1
    img 22004
    with diss
    m "Отодвинь ногу, Юлия! Она мне мешает!"
    # Юлия вскакивает со своего стула
    music Groove2_85
    sound plastinka1b
    img 22005
    with vpunch
    julia "Миссис Бакфетт! Мне кажется или вы пытаетесь... Вы..."
    img 22006
    with diss
    m "!!!"
    # Юлия смущается, Моника поднимается с пола
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22007
    with fadelong
    m "Тебе кажется, Юлия!!!" # строго
    m "Я..."
    m "Я просто потеряла кое-что! Иди работай!"
    # Юлия возвращается за свой стол, Моника садится за свой стол и прячется за монитором
    music Hidden_Agenda
    img 22008
    with fadelong
    mt "Вот черт! Снова ничего не получилось!"
    mt "Более того, эта Юлия поняла, что я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    img 22009
    with diss
    mt "!!!"
    mt "Что же мне еще придумать?.."
    mt "Пора уже заканчивать с этим! Сколько можно заниматься этими глупостями?!"
    return

label gallery_22035:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    music Groove2_85
    img 22009
    with fadelong
    mt "Не могу поверить!"
    mt "Я собираюсь показывать своей секретарше, в каких я трусиках!!!"
    img 22010
    with diss
    mt "А вдруг она узнает свои трусики?!"
    mt "Не могу же я признаться ей в том, что я ношу ЕЕ трусики!"
    mt "Я, Моника Бакфетт, ношу трусики своей бывшей гувернантки!"
    img 22011
    with diss
    mt "Хотя... Я сама в это с трудом верю, а Юлия тем более не поверит..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22012
    with fadelong
    mt "..."
    m "Юлия!"
    sound highheels_short_walk
    img 22013
    with diss
    julia "Да, Миссис Бакфетт?" # вопросительно
    img 22014
    with diss
    m "..."
    menu:
        "Ты очень хорошо работала гувернанткой, поэтому я...": #corruption
            pass
        "Ничего! Сиди и работай! Не отвлекайся!":
            music Groove2_85
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return
    # Моника обращается к Юлии неуверенно
    music Hidden_Agenda
    img 22015
    with fade
    m "Хм... Юлия, ты знаешь..."
    m "..."
    m "Несмотря на то, что я иногда была немного строга с тобой..."
    m "Мне нравилось, как ты работала у меня гувернанткой."
    # Юлия крайне удивлена, смотрит на Монику
    music Loved_Up
    img 22016
    with diss
    julia "Это правда, Миссис Бакфетт?.."
    music Hidden_Agenda
    img 22017
    with fade
    m "Да, Юлия..."
    img 22018
    with diss
    julia "А я думала, что... Вы... В общем..."
    m "Мне правда все нравилось. Думаю, весьма непросто найти гувернантку лучше, чем ты."
    music Groove2_85
    img 22019
    with fade
    mt "Черт!!! Я не могу этого сказать!"
    music Hidden_Agenda
    img 22020
    with diss
    m "После того, как ты перестала работать, я увидела в твоей комнате твои трусики..." # выдавливает из себя
    m "И мне они очень понравились..."
    img 22021
    with diss
    m "..."
    m "И я себе купила такие же..."
    music Groove2_85
    img 22022
    with vpunch
    julia "!!!"
    img 22023
    with diss
    mt "Я не верю, что я говорю это! Я говорю это своей секретарше!!!"
    # Юлия смотрит с недоверием
    img 22024
    with diss
    julia "Купили себе трусики, как у меня?!"
    img 22025
    with fade
    m "Да, Юлия. Ты мне не веришь?"
    # Юлия, смутившись
    img 22026
    with diss
    julia "Если быть честной, Миссис Бакфетт, то я... Я сомневаюсь, что Вы говорите правду..."
    img 22027
    with diss
    m "..."
    menu:
        "Поднять платье и показать Юлии трусики.": #corruption
            pass
        "Я не собираюсь ставить себя в такую глупую ситуацию!":
            music Groove2_85
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return
    # Моника задирает свое платье
    sound snd_fabric1
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 22028
    with fadelong
    m "Вот смотри! Они сейчас на мне!"
    # Юлия смотрит на трусики, она в шоке
    img 22029
    with diss
    w
    music Groove2_85
    img 22030
    with fade
    julia "Это не такие же трусики как у меня... Это..."
    img 22031
    with diss
    julia "Миссис Бакфетт... Это мои трусики..."
    img 22032
    with diss
    julia "Я узнаю их!"
    # Моника стыдится
    img 22033
    with fade
    mt "Боже! Какая глупая ситуация!"
    mt "И как мне теперь выкрутиться из нее?"
    music Hidden_Agenda
    img 22034
    with diss
    m "..."
    m "Но ведь правда они красивые?" # сквозь зубы
    music Groove2_85
    img 22035
    with fade
    julia "Вообще-то, Миссис Бакфетт, они ужасные. Я ненавидела носить их."
    # Моника молча смотрит на нее, опускает платье
    music Power_Bots_Loop
    img 22036
    with diss
    mt "!!!"
    sound snd_fabric1
    img 22037
    with diss
    mt "Пора заканчивать весь этот цирк!"
    sound highheels_short_walk
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    sound Jump1
    img 22038
    with fadelong
    m "Юлия, я тебе показала свои трусики. Теперь я хочу увидеть твои!"
    # Юлия офигевает
    img 22039
    with vpunch
    julia "Что???"
    julia "Нет! Я не буду вам ничего показывать, Миссис Бакфетт!"
    # Моника требовательно

    music Turbo_Tornado
    img black_screen
    with diss
    pause 1.0
    img 22040 # падает стул
    with fadelong
    sound down9
    w
    img 22041
    with diss
    m "Юлия, просто покажи мне их и все. Я просто хочу посмотреть."
    julia "Нет, Миссис Бакфетт! Я вам ничего не покажу!"

    img black_screen
    with diss
    #sound беготня, что-то падает и тд
    sound run2
    pause 3.0 # время беготни

    music stop
    img black_screen
    with diss
    pause 2.5
    music Groove2_85
    img 22042
    with fadelong
    julia "Нет!"
    julia "Извините, но нет!"
    sound highheels_run2
    img 22043
    with diss
    julia "Мне надо идти работать..."
    # Юлия продолжила работу, сидит за своим столом и косо посматривает на Монику
    # Моника садится за свой стол и прячется за монитором
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 22044
    with fadelong
    mt "Вот черт! Это было так ужасно!"
    mt "Такая глупая ситуация!!!"
    mt "!!!"
    img 22045
    with diss
    mt "И снова ничего не получилось!"
    mt "Эта Юлия теперь думает, что я пристаю к ней!"
    mt "Я, Моника Бакфетт, пристаю к какой-то секретарше!!!"
    img 22046
    with diss
    mt "!!!"
    mt "Пусть что хочет, то и думает! Какое мне дело до этого?!"
    mt "Только что я теперь скажу этому мерзавцу Фреду?"
    mt "???"
    return

label gallery_22318:
    # Моника стоит у себя в кабинете, Юлия работает за своим столом
    music Groove2_85
    img 22287
    with fadelong
    mt "Как мне узнать цвет трусиков Юлии?"
    mt "Я уже не знаю, что придумать..."
    mt "..."
    music Hidden_Agenda
    img 22288
    with fade
    # садится за свой рабочий стол, смотрит на свой неработающий комп
    mt "Хм..." #с улыбочкой
    img 22289
    with diss
    m "Юлия! Подойди ко мне!"
    # Юлия смотрит на Монику с подозрением
    sound highheels_run2
    img 22290
    with fadelong
    julia "???"
    # Юлия подходит и встает перед столом Моники
    music Groove2_85
    img 22291
    with diss
    julia "Да, Миссис Бакфетт..."
    # Моника тоном босса
    img 22292
    with fade
    m "Юлия! У меня не работает компьютер!"
    m "Посмотри, что с ним не так!"
    # Юлия удивленно смотрит на Монику
    img 22293
    with diss
    julia "Миссис Бакфетт, но я совсем не разбираюсь в компьютерах."
    julia "У нас есть программист. Я могу позвать его. Он поможет Вам."
    # Моника смотрит на Юлию строго
    img 22294
    with fade
    mt "!!!"
    mt "Черт! Я совсем забыла про него..."
    img 22295
    with diss
    m "Юлия!" # тоном Я ТУТ БОСС
    m "..."
    julia "Да, Миссис Бакфетт..."
    music Groove2_85
    img 22296
    with fade
    m "Хм..."
    m "Юлия! Ты забываешь, что работаешь в серьезной компании!"
    m "О работе в такой организации мечтают сотни девушек!"
    m "И мне не составит труда найти тебе замену, Юлия!"
    img 22297
    with diss
    julia "!!!" # Юлия осознает, что ничего хорошего этот разговор не предвещает
    # Моника продолжает вещать тоном БОССА
    img 22298
    with fade
    m "Поэтому ты, как и любой другой сотрудник здесь, должна..."
    m "..."
    m "Должна выполнять не только свои прямые обязанности!"
    m "Ты должна справляться с любыми поставленными задачами, если это потребуется!"
    m "Ты понимаешь, о чем я говорю, Юлия?!"
    julia "Да, Миссис Бакфетт..." # испуганно
    music Power_Bots_Loop
    img 22299
    with diss
    m "Тогда почему я дважды должна повторять, что ты должна посмотреть, что с моим компьютером?!" # переходит на крик
    #sound Юлия бежит к компьютеру
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22300
    with fadelong
    julia "Д-д-да, М-м-миссис Бакфетт. Я сейчас посмотрю." # растерянно
    mt "Никчемная помощница!!!"
    sound highheels_short_walk
    img 22301
    with diss
    m "Я жду!"
    m "И быстрее! У меня много работы!"
    # Юлия подходит справа, смотрит на монитор
    img 22302
    with fade
    julia "М-м-миссис Бакфетт, Ваш компьютер... Он не работает..." # растерянно
    music Hidden_Agenda
    img 22303
    with diss
    m "О чем я тебе и говорю!" # смотрит на зад Юлии
    m "!!!"
    m "Заставь его работать!!!"
    img 22304
    with fade
    julia "..."
    julia "Но как я это сделаю?.."
    img 22305
    with diss
    m "Откуда я знаю?! Там есть какие-то кнопки..."
    m "Понажимай на них."
    # Юлия нагибается, чтобы нажать кнопки
    music Groove2_85
    img 22306
    with fade
    w
    sound keyboard
    img 22307
    with diss
    #sound Юлия нажимает на кнопки
    w
    sound keyboard
    img 22308
    with diss
    m "..."
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            music Groove2_85
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return
    label gallery_22323:
    music Loved_Up
    img 22309
    with fade
    w
    img 22310
    with diss
    w
    img 22311
    with diss
    w
    img 22312
    with diss
    w
    img 22313
    with diss
    w
    img 22314
    with diss
    w
    sound vjuh3
    img 22315
    w
    img 22316
    with diss
    w
    img 22317
    with diss
    w
    img 22318
    with diss
    # Моника тоже нагибается, пытаясь подсмотреть Юлии под платье, но ей ничего не видно
    mt "Черт! Еще немного!"
    # Юлия поворачивает голову и видит, что Моника подглядывает
    sound Jump1
    img 22319
    with vpunch
    julia "Миссис Бакфетт! Что Вы делаете?!"
    # Юлия резко выпрямляется, Моника растерянно
    music Hidden_Agenda
    img 22320
    with diss
    m "..."
    img 22321
    with diss
    w
    img 22322
    with diss
    m "!!!"

    #sound Моника делает рывок, чтобы подсмотреть
    sound vjuh3
    img 22323
    with diss
    w
    sound Jump1
    img 22324
    with hpunch
    julia "Миссис Бакфетт!!!"
    # потом Моника делает вид, что ничего не произошло
    music Groove2_85
    img 22325
#    with diss
    w
    img 22326
#    with diss
    m "!!!"
    img 22327
    with fade
    m "Я, как твой начальник, Юлия, должна контролировать, насколько ты хорошо исполняешь свою работу!"
    m "И я не понимаю, чему ты так удивляешься!"
    m "!!!"
    # Юлия смутилась
    img 22328
    with diss
    w
    img 22329
    with diss
    m "Ты уже починила мой компьютер, Юлия?!" # строго
    mt "Я снова ничего не успела рассмотреть..."
    img 22330
    with fade
    julia "Миссис Бакфетт, я нажала на кнопки..."
    julia "Компьютер все равно не работает..." # растерянно
    img 22331
    with diss
    m "Юлия, ты уверена, что нажала на все кнопки?"
    sound Jump1
    img 22332
    with fade
    julia "Да, Миссис Бакфетт..."
    julia "Я не знаю, что еще можно нажать..."
    julia "Я могу спросить у программиста, Миссис Бакфетт..."
    # Моника рассержена
    img 22333
    with diss
    m "!!!"
    img 22334
    with fade
    m "У программиста я и сама могу спросить, Юлия!"
    m "А тебе ничего нельзя поручить!"
    music Power_Bots_Loop
    img 22335
    with diss
    m "!!!"
    img 22336
    with diss
    m "А теперь иди работай! Не отвлекайся!"
    # Юлия расстроенная уходит и садится за свой стол
    music Hidden_Agenda
    sound highheels_short_walk
    img 22337
    with fade
    #sound Юлия уходит
    w
    img 22338
    with diss
    mt "Вот черт! У меня снова ничего не получилось!"
    mt "По-моему, она поняла, что я пыталась заглянуть ей под платье!!!"
    img 22339
    with diss
    mt "!!!"
    mt "Нужно придумать какой-нибудь другой способ подсмотреть, какие у нее трусики."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 22340
    with fade
    mt "Такой способ, чтобы точно сработало."
    img 22341
    with diss
    mt "Мне надоело уже заниматься этими глупыми играми этого профессионального мерзавца Фреда!"
    mt "Пора заканчивать с этим!"
    return

label gallery_22358:
    # Моника стоит у себя в кабинете, Юлия работает за своим столом
    # Принести горячий кофе
    music Groove2_85
    img 22342
    with fadelong
    mt "Итак, рабочий день снова начинается с вопроса: как мне узнать цвет трусиков Юлии?"
    mt "У меня скоро это войдет в привычку..."
    mt "Хотя, мой рабочий день должен начинаться не с этого."
    mt "А с чашечки горячего кофе, например."
    music Hidden_Agenda
    img 22343
    with fade
    mt "..."
    mt "Горячий кофе..."
    mt "Хм..." #с улыбочкой
    music Groove2_85
    img 22344
    with diss
    m "Юлия!" # тоном босса
    # Юлия смотрит на Монику с подозрением
    julia "???"
    sound Jump1
    img 22345
    with fade
    julia "Да, Миссис Бакфетт?"
    img 22346
    with diss
    m "Юлия, я хочу выпить кофе! Принеси мне его!"
    # Юлия удивленно
    img 22347
    with fade
    julia "Кофе?"
    img 22348
    with diss
    m "Да!"
    img 22349
    with fade
    julia "Хорошо, Миссис Бакфетт. Но где мне его взять?"
    music Power_Bots_Loop
    img 22350
    with diss
    m "Юлия! Ты в прошлый раз себя проявила как некомпетентный сотрудник!" # строго
    m "Ты не смогла включить мой компьютер!!!"
    m "И это после разговора о том, что на твое место найдется масса желающих?!"
    m "!!!"
    # Юлия смотрит испуганно
    img 22351
    with fade
    julia "!!!"
    music Groove2_85
    img 22352
    with diss
    m "Принести мне горячего кофе - это тоже сложная задача для тебя?!" # также строго
    m "Создается впечатление, что ты совсем не дорожишь своей работой, Юлия..."
    img 22353
    with diss
    julia "М-м-миссис Бакфетт, это не так..." # растерянно
    julia "Я сейчас принесу Вам кофе, Миссис Бакфетт!"
    img 22354
    with fade
    m "Горячего кофе, Юлия!"
    img 22355
    with diss
    julia "Да, Миссис Бакфетт, я поняла."
    # Юлия уходит за кофе, Моника с довольной ухмылкой садится на диванчик в зоне отдыха
    sound highheels_run2
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 22356
    with fadelong
    mt "И как я раньше не могла додуматься до этого?"
    mt "Это же самый простой способ заставить ее нагнуться: ей нужно будет поставить горячий кофе на стол."
    mt "А я в это время смогу заглянуть ей под платье..."
    img 22357
    with fade
    mt "И в этот раз она не сможет отпрыгнуть от меня. Ведь у нее в руке будет горячий кофе."
    mt "Главное, не упустить момент..."
    # Моника сидит на диванчике расслабленно, улыбается
    img 22358
    with diss
    mt "..."
    mt "Наконец-то, я смогу узнать цвет трусиков Юлии."
    mt "Да еще и совместить это с чашечкой ароматного кофе."
    mt "Чувствую, что сегодня меня ожидает просто отличный день!"
    img 22359
    with diss
    mt "Сегодня закончится эта дурацкая ситуация, когда мне надо узнавать какие-то глупости у никчемных работников..."
    mt "..."
    mt "И больше я не буду слушать Фреда! С меня хватит!"
    # в кабинет заходит Джон-подхалим, следом за ним идет Юлия. У подхалима кофе в руке
    # они подходят к Монике, у нее шок
    # подхалим доволен собой, ставит кофе на столик. Юлия стоит рядом с ним. Моника смотрит на чашку кофе, потом на Юлию, потом на подхалима
    # затемнение
    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound snd_door_close1
    music Sneaky_Snitch
    img 22360
    with fadelong
    w
#    sound vjuh3
    sound Jump1
    img 22361
    with fade
    w
    img 22362
    with hpunch
    sound Jump2
    mt "!!!"
    mt "Какого черта?!"
    img 22363
    with fade
    w5 "Миссис Бакфетт! Вы сегодня прекрасно выглядите!" # решил выслужиться, как обычно
    img 22364
    with diss
    mt "..."
    img 22365
    with fade
    w5 "Я узнал от Вашей помощницы, что Вам нужен кофе, и сразу принес его Вам!"
    img 22366
    with diss
    mt "..."
    music Groove2_85
    menu:
        "Послушать, что он скажет дальше.":
            music Sneaky_Snitch
            img 22367
            with fade
            w5 "Миссис Бакфет, Вы всегда можете на меня рассчитывать."
            mt "!!!" # начинает сердиться, но молчит
            mt "О, Боже! Когда он уйдет отсюда?!"
            img 22368
            with diss
            w5 "Ведь я могу не только качественно и быстро выполнять свои прямые обязанности..."
            w5 "Я также могу помогать Вам, ведь Вам приходится очень много работать."
            music Groove2_85
            mt "!!!"
            mt "Какой же он мерзкий тип этот Джон!"
            mt "Какого черта ОН притащил мне этот кофе!!!"
            mt "!!!" # уже очень злая
            music Sneaky_Snitch
            img 22369
            with fade
            w5 "И такой помощник, как Я, будет Вам как раз кстати, Миссис Бакфетт."
            w5 "В отличии от толстухи Греты, Я могу делать любую работу в этом отделе."
            w5 "Даже самую сложную и ответственную..."
            music Groove2_85
            img 22370
            with diss
            mt "!!!" # очень-очень злая
            mt "Когда этот сукин сын уже замолчит?!"
            music Sneaky_Snitch
            img 22371
            with fade
            w5 "Помимо этого, я всегда внимателен к желаниям начальства..."
            w5 "Я могу приносить Вам горячий кофе каждое утро, Миссис Бакфетт!"
            w5 "Я..."
            music Power_Bots_Loop
            img 22372
            with hpunch
            m "ТАК, ХВАТИТ!"
            m "!!!"
            m "Ты слишком много разговариваешь! Иди работай!!!"
            # подхалим, ничуть не смутившись
            music Sneaky_Snitch
            img 22373
            with fade
            w5 "Да, конечно, Миссис Бакфетт. Я понимаю, что Вам некогда."
            w5 "Помните, что всегда можете на меня рассчитывать, Миссис Бакфетт."
            img 22374
            with diss
            w5 "Надеюсь, Вам понравится кофе. Если захотите еще, я с радостью его Вам принесу..."
            music Power_Bots_Loop
            img 22375
            with hpunch
            m "Вон из моего кабинета!!!"
            mt "!!!"

        "Не слушать его болтовню, прогнать этого подхалима из кабинета.":
            music Power_Bots_Loop
            img 22376
            with fade
            m "Я не знала, что в ваши обязанности входит работать моей помощницей!"
            m "Выйди и закрой за собой дверь!!!"
            music Sneaky_Snitch
            img 22377
            with diss
            w5 "Хорошо, Миссис Бакфетт. Понимаю, Вы очень заняты."
            w5 "Помните, что Вы всегда можете на меня рассчитывать, Миссис Бакфетт." # уходит

    # подхалим уходит, Юлия стоит на том же месте. Моника зло смотрит на нее
    # sound переход, подхалим уходит
    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound snd_door_close1
    music Hidden_Agenda
    img 22378
    with fadelong
    w
    img 22379
    with fade
    julia "???"
    menu:
        "Отчитать Юлию и выгнать из комнаты отдыха.":
            music Groove2_85
            img 22380
            with diss
            m "Юлия!!!" # строго
            m "Я в очередной раз убедилась, что самостоятельно ты не можешь справиться с поставленными задачами!!!"
            img 22381
            with fade
            julia "Но, Миссис Бакфетт..." # растерянно
            music Power_Bots_Loop
            img 22382
            with diss
            m "Никаких 'но'!!! Я не желаю слушать твои жалкие оправдания!"
            m "Иди работай!!!"
            # Юлия расстроенная уходит
            sound highheels_run2

        "Не отчитывать Юлию.":
            music Groove2_85
            img 22383
            with diss
            m "Юлия, ты можешь заняться своей работой." # сдержанно
            m "Я хочу побыть одна."
            julia "Хорошо, Миссис Бакфетт..."
            img 22384
            with diss
            #sound Юлия уходит на рабочее место, Моника смотрит вслед
            m "..."
            # Юлия уходит
            sound highheels_short_walk
    # Моника кипит от злости
    music Power_Bots_Loop
    img 22385
    with fadelong
    mt "!!!"
    mt "Это был просто отличный план, чтобы закончить эту историю с трусиками Юлии!!!"
    mt "Какого черта ОН притащил мне этот долбанный кофе!!!"
    img 22386
    with fade
    mt "ААААААААРРРГХХХХХ!!!"
    mt "Как меня достал этот мерзкий тип!!!"
    mt "!!!"
    music Groove2_85
    img 22387
    with diss
    mt "Никчемные сотрудники!!! Все они никчемные!!! Бесполезные!!!"
    mt "Когда верну себе свое место босса, вышвырну отсюда всех этих бездельников!!!"
    mt "!!!"
    img 22388
    with fade
    mt "Теперь мне снова нужно придумывать какой-нибудь способ заглянуть Юлии под платье!"
    mt "..."
    return
