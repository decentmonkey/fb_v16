### исправлено
label gallery_10416:
# Теперь, когда Бетти находится в спальне, там периодически находится Барди, который проверяет ее трусики.
# Моника может подойти к Бетти в спальне и проверить ее трусики.
# Также Моника может подойти к Бетти у зеркала на floor2 и проверить трусики тоже.


    # Бетти в спальне, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10402
    with fadelong
    w
    img 10403
    w
    img 10404
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"
    img 10420
    with fade
    sound Jump2


    #nude
    img 10415
    with fade
    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
        #random
    call showRandomImagesDiss([10416, 10417, 10418, 10419], 2) from _rcall_showRandomImagesDiss
#        w
#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"

    betty "!!!"

    $ restore_music()
    music Sneaky_Snitch
    return

### исправлено
label gallery_10432:
    # Бетти у зеркала, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10421
    with fadelong
    w
    img 10422
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"

    #betty

    img 10431
    with diss
    sound Jump2
    w
    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    img 10432
    with diss
    w


#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    img 10439
    betty "!!!"

    $ restore_music()

    return

### исправлено
label gallery_10435:
    # Бетти у зеркала, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10421
    with fadelong
    w
    img 10422
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"

    img 10433
    with diss
    sound Jump2
    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    #random
    img 10434
    with diss
    w
    call showRandomImagesDiss([10435, 10436, 10437, 10438], 2) from _rcall_showRandomImagesDiss_1

#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    img 10439
    betty "!!!"

    $ restore_music()

    return

## исправлено
label gallery_10452:
    # Моника у зеркала проверяет трусики Бетти
    $ store_music()
    music Hidden_Agenda high
    img 10440
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10441
    betty "!!!"

    img 10442
    with fade
    m "..."
    #betty
    sound snd_fabric1
    img 10451
    with fade
    betty "На, гувернантка, смотри."
    img 10452
    with fade
    w
    betty "И не вздумай одеть другие!"

#    betty "На, гувернантка, смотри. И не вздумай одеть другие!"
    $ restore_music()
    return

label gallery_10459:
    # Моника проверяет без трусиков Бетти у зеркала
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False



    $ store_music()
    music Hidden_Agenda high
    img 10453
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10454
    betty "..."

    w
    # Бетти показывает попу
    sound snd_fabric1
    img 10455
    with fade
    w
    #random
    call showRandomImagesDiss([10456, 10457, 10458], 1) from _rcall_showRandomImagesDiss_2
#    img 10456
#    img 10457
#    img 10458
#    w

    img 10459
    with diss
    w
    betty "Я соблюдаю правила этого дома..."
    img 10460
    with fade
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."

    # Моника показывает попу
    sound snd_fabric1
    img 10461
    with fade
    w
    img 10462
    with diss
    w
    #random
    call showRandomImagesDiss([10463, 10464, 10465, 10466, 10467, 10468], 3) from _rcall_showRandomImagesDiss_3
#    img 10463
#    img 10464
#    img 10465
#    img 10466
#    img 10467
#    img 10468


    img 10462
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()

    return

label gallery_10463:
    # Моника проверяет без трусиков Бетти у зеркала
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики

    #

    $ store_music()
    music Hidden_Agenda high
    img 10453
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10454
    betty "..."

    w
    # Бетти показывает попу
    sound snd_fabric1
    img 10455
    with fade
    w
    #random
    call showRandomImagesDiss([10456, 10457, 10458], 1) from _rcall_showRandomImagesDiss_4
#    img 10456
#    img 10457
#    img 10458
#    w

    img 10459
    with diss
    w
    betty "Я соблюдаю правила этого дома..."
    img 10460
    with fade
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."

    # Моника показывает попу
    sound snd_fabric1
    img 10461
    with fade
    w
    img 10462
    with diss
    w
    #random
    call showRandomImagesDiss([10463, 10464, 10465, 10466, 10467, 10468], 3) from _rcall_showRandomImagesDiss_5
#    img 10463
#    img 10464
#    img 10465
#    img 10466
#    img 10467
#    img 10468


    img 10462
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()

    return

label gallery_10482:
    # Моника в спальне проверяет трусики Бетти
    $ store_music()
    music Hidden_Agenda high
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False
    img 10469
    with fade
    w
    img 10470
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10471
    betty "!!!"

    img 10472
    with diss
    m "..."
    img 10473
    with fade
    betty "Ладно..."
    sound snd_fabric1
    img 10474
    with fade
    w

    #betty


    img 10482
    with fade
    w
    img 10483
    with diss
    betty "На, гувернантка, смотри."
    w
    img 10477 #общий
    with diss
    w
    img 10484
    with diss
    w


    betty "И не вздумай одеть другие!"

#    betty "На, гувернантка, смотри. И не вздумай надеть другие!"
    img 10491
    with fade
    mt "..."

    $ restore_music()
    return

label gallery_10498:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики

    #

    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"



    #обычный
    # Бетти показывает попу
    img 10495
    with fade
    w

    img 10496
    with fade
    w
    sound snd_fabric1
    img 10497
    with fade
    w

    #random
    call showRandomImagesDiss([10498, 10499, 10500, 10501, 10502, 10503, 10504, 10505], rand(3,4)) from _rcall_showRandomImagesDiss_6
    #

    img 10506
    with diss
    betty "Я соблюдаю правила этого дома..."
    img 10507
    with fade
    betty "Покажи, что ты тоже!"
    img 10508
    w
    img 10509
    with fade
    m "Да, Миссис Робертс, конечно..."

    sound snd_fabric1
    img 10510
    with fade
    w
    img 10511
    with diss
    w
    img 10512
    with diss
    w
    img 10513
    with diss
    w

    #random
    call showRandomImagesDiss([10514, 10515, 10516, 10517, 10518, 10519, 10520, 10521], rand(3,4)) from _rcall_showRandomImagesDiss_7
#        img 10514
#        img 10515
#        img 10516
#        img 10517
#        img 10518
#        img 10519
#        img 10520
#        img 10521
    #
    img 10522
    with diss
    w
    img 10523
    with diss
    w
    img 10524
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()
    return


label gallery_10515:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики


    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"

    #обычный
    # Бетти показывает попу
    img 10495
    with fade
    w

    img 10496
    with fade
    w
    sound snd_fabric1
    img 10497
    with fade
    w

    #random
    call showRandomImagesDiss([10498, 10499, 10500, 10501, 10502, 10503, 10504, 10505], rand(3,4)) from _rcall_showRandomImagesDiss_8
    #

    img 10506
    with diss
    betty "Я соблюдаю правила этого дома..."
    img 10507
    with fade
    betty "Покажи, что ты тоже!"
    img 10508
    w
    img 10509
    with fade
    m "Да, Миссис Робертс, конечно..."

    sound snd_fabric1
    img 10510
    with fade
    w
    img 10511
    with diss
    w
    img 10512
    with diss
    w
    img 10513
    with diss
    w

    #random
    call showRandomImagesDiss([10514, 10515, 10516, 10517, 10518, 10519, 10520, 10521], rand(3,4)) from _rcall_showRandomImagesDiss_9
#        img 10514
#        img 10515
#        img 10516
#        img 10517
#        img 10518
#        img 10519
#        img 10520
#        img 10521
    #
    img 10522
    with diss
    w
    img 10523
    with diss
    w
    img 10524
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()
    return



label gallery_10539:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False



    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"

    #бонус
    music Loved_Up high
    sound snd_fabric1
    img 10525
    with fade
    w
    img 10526
    with fade
    w
    img 10527
    with diss
    w
    img 10528
    with diss
    w
    img 10529
    with diss
    w
    #random
    call showRandomImagesDiss([10530, 10531, 10532, 10533, 10534, 10535], 3) from _rcall_showRandomImagesDiss_10
#        img 10530
#        img 10531
#        img 10532
#        img 10533
#        img 10534
#        img 10535
    #

    img 10536
    with fade
    betty "Я соблюдаю правила этого дома..."
    betty "Покажи, что ты тоже!"

    img 10537
    with fade
    m "Да, Миссис Робертс, конечно..."
    sound snd_fabric1
    img 10538
    with fade
    w
    img 10539
    with diss
    w
    #random
    call showRandomImagesDiss([10540, 10541, 10542, 10543, 10544, 10545], 3) from _rcall_showRandomImagesDiss_11
#        img 10540
#        img 10541
#        img 10542
#        img 10543
#        img 10544
#        img 10545
    #
    img 10546
    with diss
    w
    img 10547
    with diss
    w
    img 10548
    with diss
    w
    img 10549
    with diss
    w
    img 10550
    with diss
    w
    img 10551
    with diss
    w
    img 10552
    with diss
    w
    img 10553
    with fade
    m "Я тоже соблюдаю правила этого дома..."

    $ restore_music()
    return

label gallery_12962:
    # Моника случайно заходит к Барди (первый раз)

    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up
    # Сцена Барди с журналом
    # Старт, пара кадров
    #video
    img 12959
    with fadelong
    bardie "Аххх! Ахххх!!!"
    bardie "Моника Бакфетт..."
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_1 = Movie(play="video/v_Bardie_Masturbation_1_1.mkv", fps=30)
    show videov_Bardie_Masturbation_1_1
    with fade
    wclean
    img 12960
    with fade
    bardie "Аххх! Ахххх!!!"
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_2 = Movie(play="video/v_Bardie_Masturbation_1_2.mkv", fps=30)
    show videov_Bardie_Masturbation_1_2
    with fade
    wclean
    img 12961
    with fade
    bardie "Моя гувернантка..."
    bardie "Аххх!"
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_3 = Movie(play="video/v_Bardie_Masturbation_1_3.mkv", fps=30)
    show videov_Bardie_Masturbation_1_3
    with fade
    wclean
    img 12962
    with fade
    bardie "Я молодец!"
    bardie "Я хороший хозяин, Аххх!"
    # video end
    # Барди кончает
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_4 = Movie(play="video/v_Bardie_Masturbation_1_4.mkv", fps=30)
    show videov_Bardie_Masturbation_1_4
    with fade
    wclean
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    sound hlup10
    img 12963
    with diss
    bardie "АХХХХХХ!!!"
    bardie "..."
    sound hlup10
    img 12965
    with diss
    bardie "Ее сиськи..."
    sound hlup10
    img 12964
    with diss
    w
    music stop
    sound hlup19
    img 13183
    with diss
    w
    music Sneaky_Snitch
    img 12966
    with fadelong
    bardie "Интересно, они настоящие или нет..."
    bardie "Как это я упустил их из виду..."
    img 12967
    bardie "У меня все еще недостаточный контроль над ней..."
    bardie "Мне нужно увидеть ее сиськи... И даже больше..."
    img 12968
    with diss
    bardie "И мне нужна еще фотография, чтобы дрочить на нее."
    bardie "Этот журнал уже надоел мне..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    # хитро прищуриваясь
    music Sneaky_Snitch
    img 12969
    with fadelong
    bardie "Может быть есть еще выпуски?"
    bardie "Надо будет спросить у гувернантки..."
    img 12970
    bardie "И, было бы неплохо не только дрочить на нее, но и делать нечто более..."
    bardie "Хотя я ее, пока, немного побаиваюсь..."
    img 12971
    with diss
    bardie "Все-таки она Моника Бакфетт, но, почему-то боится штрафа..."
    bardie "Может быть она не настоящая Моника Бакфетт, потому и боится?"
    bardie "И Бетти..."
    img 12972
    with fade
    bardie "Эта мачеха, хоть и соблюдает правила дома, но, все-же, действует мне на нервы."
    bardie "Я мечтаю не только смотреть ей под юбку, но и, когда-нибудь, трахнуть ее!"
    img 12973
    with diss
    bardie "Вокруг ходит столько целей, а я все еще девственник!"
    bardie "Это ненормально! Я что, какой-то нудачник?!"


    # Моника заходит. Журнал весь в сперме
    music Power_Bots_Loop
    sound highheels_run2
    img 12974
    with fadelong
    m "Что... Что ты делаешь??"
    img 13183
    with diss
    w
    img 13184
    with diss
    m "Это... Это Я?!"
    img 12975
    with diss
    m "Это мой журнал! Мой!"
    m "Что ты делаешь с ним?!"
    music Groove2_85
    img 12976
    bardie "Я дрочу на него, я же говорил тебе."
    img 12977
    with fade
    m "Я... Не смей делать этого!"
    m "Верни его мне!"
    img 12978
    bardie "Я верну тебе его только если ты принесешь мне другой!"
    bardie "Новый выпуск!"
    img 12979
    with diss
    m "Нет новых выпусков, я не работаю там!"
    m "Я торчу здесь! И меня это бесит!"
    img 12980
    with fade
    bardie "Ты здесь работаешь! И я твой хозяин!"
    music Power_Bots_Loop
    img 12981
    m "!!!"
    # Моника уходит
    sound highheels_short_walk
    img 12982
    with fadelong
    w
    return

label gallery_13001:
    # Моника прходит к Барди спросить о еде в доме (второй приход)
# Моника приходит к Барди и говорит что, учитывая то, что она ведет себя хорошо, может быть
# Барди скажет Бетти, чтобы та кормила прислугу в доме.
# Барди спрашивает хорошая-ли Моника гувернантка, что просит о таком?
# Моника отвечает что хорошая (либо не отвечает)
# Барди просит продемострировать что Моника соблюдает правила дома.
    music Hidden_Agenda
    img 12983
    with fadelong
    m "Барди..."
    img 12984
    bardie "Да, гувернантка?"
    img 12985
    with diss
    m "У меня разговор к тебе..."
    sound snd_cardboard2
    img 12986
    with fade
    bardie "Я тебя слушаю."
    img 12987
    with diss
    m "Барди, я ведь хорошо себя веду, так ведь?"
    img 12988
    bardie "Да, гувернантка... Обычно ты соблюдаешь правила дома..."
    img 12989
    with diss
    m "Барди, если ты доволен мной, то..."
    m "То, может быть, Я заслуживаю того, чтобы меня кормили в этом доме."
    m "Может быть ты скажешь Бетти об этом?"
    # Щурится
    img 12990
    with diss
    m "Ты ведь тут самый главный? Правда?"
    music Groove2_85
    img 12991
    with fade
    bardie "О таком может просить только хорошая гувернантка."
    bardie "Ты хорошая гувернантка, Моника?"
    img 12992
    with diss
    menu:
        "Да, я хорошая гувернантка...":
            pass
        "Уйти.":
            sound highheels_run2
            img 12982
            with fade
            w
            return
    img 12993
    with fade
    m "Да, я хорошая гувернантка..."
    img 12994
    with diss
    bardie "Хорошо, покажи, что ты соблюдаешь правила дома!"

# Моника соглашается либо нет.
# Если соглашается и у нее надеты трусики, то Барди злится и устраивает порку.

    music Groove2_85
    img 13078
    with fade
    menu:
        "Задрать юбку.":
            pass
        "Попросить выйти.":
            music Hidden_Agenda
            img 12996
            with fade
            m "Барди, конечно я соблюдаю правила."
            m "Я вспомнила об одном важном деле!"
            img 12997
            with diss
            m "Мне надо отлучиться и я вернусь сюда!"
            sound highheels_run2
            img 12982
            with fade
            w
            return

    # Моника показывает
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 13185
    with fadelong
    w

    img 13001
    with diss
    w



# Тогда Барди говорит чтобы та показала свою грудь.
# Моника может это делать, либо нет. Если нет, то Барди злится и устраивает порку, но грудь Моника не показывает.
#    img 13007
    img 12999
    with fade
    bardie "Хорошо."
    bardie "Теперь покажи свои сиськи!"
    music Power_Bots_Loop
    img 13008
    with diss
    m "Мы так не договаривались!"
    m "Я не собираюсь этого делать!"
    img 13009
    bardie "Ты моя игрушка и принадлежишь мне!"
    img 13010
    with diss
    m "Ах ты мелюзга!"
    m "Я не буду показывать тебе свою грудь!"
    music Groove2_85
    img 13011
    with fade
    bardie "Ты решила не подчиняться приказам хозяина дома? Я правильно понял?"
    img 13012
    with diss
    menu:
        "Подчиниться и показать грудь.":
            pass
        "Не показывать грудь!":
            music Power_Bots_Loop
            img 13013
            with fade
            m "Я и так хожу с голой задницей по дому целыми днями!"
            m "Разве тебе этого мало?!"
            music Groove2_85
            img 12998
            with diss
            bardie "Нерадивая гувернантка!"
            bardie "Ты не слушаешься хозяина дома!"
            bardie "Следуй к себе в подвал для прохождения наказания!"
            return

    # Моника показывает грудь
    label gallery_13051:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 13014
    with fadelong
    w
    img 13049
    with diss
    w
    img 13050
    with diss
    w
    # Барди берет журнал и держит его рядом, сравнивая грудь
    sound snd_take_paper
    img 13051
    with diss
    w
    img 13052
    with diss
    bardie "Да, у тебя такая же грудь."
    bardie "Ты действительно похожа не нее."
    music Power_Bots_Loop
    img 13053
    with fade
    m "ЭТО И ЕСТЬ Я!"
    music Loved_Up
    img 13054
    with diss
    mt "Черт! Зачем я это сказала?!"

# Барди задумывается, улыбается и говорит что хозяин дома подумает, пусть Моника приходит завтра.

    img 13055
    with fade
    w
    img 13056
    with diss
    w
    music Groove2_85
    img 13057
    with fade
    bardie "Хорошо, хозяин дома подумает." # разглядывая грудь
    bardie "Гувернантка, приходи завтра."
    bardie "Хозяин скажет тебе о своем решении."
    # Моника закрывает грудь
    sound snd_fabric1
    img 13058
    with fadelong
    m "!!!"

#    bardie "Да, и еще!"
    return

label gallery_13045:
# На след. день Моника приходит к Барди и спрашивает подумал-ли он?
# Барди отвечает что готов сделать величественный жест ради хорошей гувернантки, которая хорошо себя ведет.
# И сказать Бетти, чтобы она кормила Монику
# Переспрашивает хорошая-ли гувернантка Моника?
    music Hidden_Agenda
    img 13015
    with fadelong
    m "Барди, ты подумал насчет того, чтобы я получала заслуженную еду в этом доме?!"
#    music Groove2_85
    img 13016
    with diss
    bardie "Да, гувернантка."
    bardie "Я подумал и решил что готов сделать величественный жест ради хорошей гувернантки."
    bardie "Которая хорошо себя ведет..."
    img 13017
    mt "!!!"
    img 13018
    with diss
    bardie "И я скажу Бетти, чтобы она кормила гувернантку."
    bardie "Но только хорошую гувернантку!"
    bardie "Ты ведь хорошая гувернантка, Моника?"
    img 13019
    menu:
        "Да...":
            pass
        "Я... Подумаю о том какая Я...":
            music Groove2_85
            img 13020
            with fade
            m "Я еще не решила..."
            img 13021
            with diss
            bardie "Когда будешь уверена, приходи!"
            return

# Моника отвечает что да.
    m "Да..."
#    img 13021
# Барди говорит чтобы та сделала titjob. Моника в шоке и спрашивает не рановато-ли Барди думать о таких вещах.
# Барди отвечает что он уже достаточно большой. (мне уже 18, либо можно поменять число)
    img 13023
    with fade
    bardie "Хорошо, я много раз кончал на твои сиськи на журнале."
    bardie "Теперь я хочу сделать это прямо на них."
    music Groove2_85
    img 13024
    with diss
    m "ЧТО?!"
    m "Барди, я понимаю, что ты уже интересуешься девушками."
    m "Придумываешь разные глупые игры. У тебя играют гормоны."
    img 13025
    with diss
    m "Но тебе не кажется, что тебе рановато думать о чем-то большем?!"
    m "Тем более в отношении меня!"
    img 13026
    with fadelong
    bardie "Я не маленький! Я большой!"
    bardie "Мне уже 21!"
#    help "Внося изменения в игру, Вы берете на себя ответственность."
#    help "Вы уверены в этом?"


# Барди ложится на кровать и достает член.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 13027
    with fadelong
    bardie "..."
# Моника в шоке смотрит на это.
    sound Jump2
    img 13186
    w
    img 13028
    with diss
    m "!!!"
# Барди спрашивает чего гувернантка ждет? Она должна выполнять обязанности по дому, в число которых входит
# то, чтобы хозяин дома оставался доволен.
    img 13029
    with fade
    bardie "Ну?!"
    bardie "И чего же гувернантка ждет?"
    bardie "Хорошая гувернантка должна выполнять обязанности по дому."
    bardie "Соблюдать везде чистоту."
    img 13030
    bardie "Это место надо протереть от пыли."
    bardie "И оно слишком чувствительное, поэтому это надо сделать твоими сиськами!"
    music Groove2_85
    img 13031
    m "!!!"

# Моника злая, смотрит и думает.
    img 13032
    with diss
    m "Я уверена в том, что это место протирается регулярно и без меня!"
# Барди говорит что если гувернантка будет хорошей, то ее в этом доме будут кормить.
    img 13033
    with fade
    bardie "Хорошая гувернантка должна выполнять эту работу."
    bardie "И, если гувернантка будет хорошей, то ее в этом доме будут кормить."

# Моника принимает решение
    music Hidden_Agenda
    img 13034
    with fade
    mt "Что же мне делать?!"
    mt "Ведь я не буду трогать своей изысканной грудью член этого Барди?"
    img 13035
    with diss
    mt "С другой стороны, я в шаге от того, чтобы нормально питаться."
    mt "В своем же доме!"
    music Groove2_85
    img 13036
    with fade
    bardie "А плохую гувернантку может ждать наказание..."
    img 13037
    with diss
    mt "Что же мне делать?!"
    img 13038
    with diss
    menu:
        "Сделать это...":
            pass
        "Я... Пока не готова для этого...":
            # Говорит что она пока не готова для этого (corruption)
            music Hidden_Agenda
            img 13039
            with fade
            m "Я... Пока не готова для этого..."
            music Groove2_85
            img 13040
            with diss
            bardie "Тогда иди и готовься!"
            bardie "Иначе ты станешь плохой гувернанткой!"
            return
# Либо соглашается и делает titjob
    music Hidden_Agenda
    img 13041
    with fadelong
    m "Я не умею делать это..."
    music Groove2_85
    img 13042
    bardie "Я тоже не умею делать это. Но не думаю что это сложно!"
    bardie "Вынь свои сиськи и положи их на мой член!"

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 13043
    with fadelong
    m "..."
    img 13044
    with diss
    bardie "Вот так. А теперь начинай двигать ими вверх и вниз!"
# Барди говорит хорошая гувернантка и тд
    # video
    music stop
    img black_screen
    with diss
    pause 1.5
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_1 = Movie(play="video/v_Monica_Bardie_Titjob_1_1.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_2 = Movie(play="video/v_Monica_Bardie_Titjob_1_2.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_2
    with fadelong
    wclean
    music Loved_Up
    img 13045
    with fade
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_3 = Movie(play="video/v_Monica_Bardie_Titjob_1_3.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_4 = Movie(play="video/v_Monica_Bardie_Titjob_1_4.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_4
    with fadelong
    wclean
    music Loved_Up
    img 13046
    with fade
    bardie "Хорошая гувернантка..."
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_5 = Movie(play="video/v_Monica_Bardie_Titjob_1_5.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_5
    with fadelong
    wclean
    music Loved_Up
    img 13047
    with fade
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_6 = Movie(play="video/v_Monica_Bardie_Titjob_1_6.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_6
    with fadelong
    wclean
    music Loved_Up
    img 13048
    with fade
    bardie "Хорошая..."
    bardie "Протирай как следует, это твоя работа..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_7 = Movie(play="video/v_Monica_Bardie_Titjob_1_7.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_8 = Movie(play="video/v_Monica_Bardie_Titjob_1_8.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_8
    with fadelong
    wclean
# Когда заканчивают, Барди говорит Монике придти завтра, когда он уладит обязанности хозяина дома и
# выдаст необходимые распоряжения Бетти
    # end video

    # Барди кончает на грудь Монике
    music stop
    stop music
    img black_screen
    with diss
    bardie "Оооооох!!!"
    sound bulk1
    img 13123
    with fade
    w
    img 13125
    with diss
    w
    sound bulk1
    img 13124
    with fade
    bardie "Оооооох!!!"
    sound hlup19
    img 13126
    with diss
    w
    music Groove2_85
    img 13127
    with fade
    mt "!!!"
    img 13128
    with diss
    w
    img 13129
    bardie "Хорошая гувернантка!"
    bardie "Приходи завтра."
    bardie "Я улажу обязанности хозяина дома и выдам необходимые распоряжения Бетти!"
    sound snd_fabric1
    img 13130
    with fadelong
    m "!!!"
    img black_screen
    with diss

# Моника уходит
    return

label gallery_13115:
    # Если в течении этого дня Моника заглядывает в комнату Барди

    # Идет сцена наказания Бетти
# Бетти стоит в углу.
# Барди говорит что поняла-ли она что хозяина дома надо слушаться.
# Бетти отвечает что да.
    # кадр смотрит
    # обращается
    music Hidden_Agenda
    img 13109
    with fadelong
    w
    img 13110
    with diss
    m "Мистер Робертс, от меня еще что-нибудь требуется?"
    # Бетти смотрит на Монику
    img 13111
    with diss
    # Моника смотрит на Бетти
    m "..."
    img 13112
    with diss
    betty "!!!"
    # Барди отвечает
    img 13113
    with fade
    bardie "Нет, гувернантка. Ты можешь отдыхать."
    # поворачивается в Бетти
    music stop
    img black_screen
    with diss
    sound snd_cardboard2
    pause 1.5
    music Groove2_85
    img 13114
    with fade
    bardie "Поняла что хозяина дома надо слушаться?!"
    img 13115
    with diss
    betty "Да!"
    img 13116
    with fade
    bardie "Поняла что бывает с непослушными девочками?"
    img 13117
    with diss
    betty "Да, поняла. Их ставят в угол..."
    img 13118
    with fade
    bardie "Будешь еще нарушать правила дома?!"
    img 13119
    with diss
    betty "Нет! Не буду!"
    if bettyCollegeDay1JobFinished == False and bettyCollegeTeacherRefused == True:
        img 13118
        bardie "И ты еще не закончила решать мои проблемы в колледже..."
        bardie "Ты не забыла про них?"
        menu:
            "Я завтра пойду в колледж...":
                img 13117
                betty "Я завтра пойду в колледж..."
                return
            "Промолчать...":
                betty "..."
    else:
        img 13120
        with fade
        bardie "И не только в угол! Есть еще другие наказания, хе-хе!"
        bardie "А теперь можешь идти! Заниматься делами по дому!"
        bardie "Завтра на обед я хочу вкусный бургер!"
    img 13121
    with diss
    betty "!!!" # зло смотрит, тянется к платью
    sound snd_fabric1
    img 13122
    with diss
    mt "..." # язвительно улыбается

    # Бетти стоит с красным задом и зло смотрит на Монику
    return

label gallery_13155:
    # Моника заходит на кухню первый раз (либо любой раз, пока Моника еще не показывала грудь)

# Если Моника заходит так, то прибегает Бетти и говорит Монике чтобы та убиралась с кухни!
# Что ей вообще не нужны проститутки в доме и что ей уже надоело присматривать за дурной гувернанткой
# Которая так и норовит нарушить дисциплину!
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 13131
    with fadelong
    betty "Моника, гувернантка!"
    betty "Что ты делаешь здесь!"
    img 13132
    betty "Я запретила тебе заходить на кухню!"
    betty "Быстро убирайся отсюда!"
    img 13133
    with diss
    betty "И вообще... Мне не нужны проститутки в доме!"
    betty "И мне надоело присматривать за дурной гувернанткой, которая так и норовит нарушить дисциплину!"
# Моника спрашивает: есть-ли правила, которые позволяют ей питаться здесь?
# Бетти смущается и говорит что есть кое-какое правило и гувернантка сама про него знает. (злится)
# Говорит Монике чтобы та выметалась с кухни
    music Hidden_Agenda
    img 13134
    with fade
    m "Миссис Робертс..."
    m "Есть-ли правила, которые позволяют мне питаться здесь?"
    img 13135
    with diss
    betty "..."
    img 13136
    m "???"
    img 13137
    betty "!!!"
    music Groove2_85
    img 13138
    with fade
    betty "Есть кое-какое правило... И ты, гувернантка, сама знаешь про него..."
    betty "А сейчас, выметайся с кухни!"
# Моника делает выбор:
# Уйти или Оголить грудь (corruption)
    img 13139
    with diss
    menu:
        "Оголить грудь...":
            pass
        "Уйти...":
            sound highheels_run2
            img 13140
            with fade
            w
            return
# Если оголяет: А так?
# Если оголяет первый раз, то Моника про себя думает о том что же она творит, но, с другой стороны.
# Никто кроме Бетти этого не видит и это лучше, чем разносить флаеры за еду или что-то еще похуже.
    music Hidden_Agenda
    img 13142
    with fade
    mt "Моника, что ты творишь?"
    mt "Неужели ты пойдешь на это?"
    img 13141
    with diss
    mt "С другой стороны... Никто кроме Бетти этого не видит"
    mt "И это лучше, чем разносить флаеры за еду или делать что-то еще похуже..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    #fade
    music Loved_Up
    img 13143
    with fadelong
    m "А так?"

# Бетти злится и говорит что у гувернантки нет никакого стыда.
# И чтобы та убиралась отсюда.
    img 13144
    with diss
    betty "!!!"
    img 13145
    with diss
    m "..." # Моника стервозно улыбается
    music Groove2_85
    img 13146
    with fade
    betty "Гувернантка, у тебя нет никакого стыда!"
    betty "Немедленно убирайся отсюда!"
# Моника спрашивает: Вы уверены, Миссис Робертс? Что я должна выйти отсюда?
# Бетти злится и говорит чтобы та садилась за стол.
    music Loved_Up
    img 13147
    with fade
    m "Вы уверены, Миссис Робертс!"
    m "Вы уверены что я должна выйти отсюда?"
    img 13148
    with diss
    betty "!!!"
    music Groove2_85
    img 13149
    with fade
    betty "Садись за стол, сейчас подам тебе..."
# Моника садится.
# Бетти подает еду и говорит что если Ральф увидит ее в таком виде, то ей уже ничего не поможет.
# Даже мелкий засранец, с которым Моника спелась.
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13150
    with fadelong
    betty "И не вздумай в таком виде шляться по дому!"
    betty "Если Ральф увидит тебя в таком виде, то я вышвырну тебя!"
    img 13151
    betty "И тебе никто не поможет!"
    betty "Даже мелкий засранец Барди, с которым ты спелась!"

    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5

    $ rnd = rand(1,3)

    #
    music RnB3_65
    if rnd == 1:
        img 13167
        with fadelong
        mt "Мммм... Наконец-то я ем вкусную еду..."
        img 13168
        with diss
        mt "В своем доме..."

    if rnd == 2:
        img 13167
        with fadelong
        mt "Мой дом... Моя любимая кухня..."
        mt "Все не так уж плохо..."
        img 13168
        with diss
        mt "Это только первые шаги..."
        mt "Скоро дом будет снова мой..."

    if rnd == 3:
        #
        img 13169
        with fadelong
        mt "Ммм... Я кушаю на своей любимой кухне."
        img 13170
        with diss
        mt "А Бетти прислуживает мне..."
        mt "Так мне нравится намного больше..."

    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_plates
    music RnB3_65

#    $ images = random.sample(set(images_set1, images_set2, images_set3), 1)

    $ rnd = rand(1,3)
    if rnd == 1:
        img 13152
        with fadelong
        w
        $ images_set1 = [13153, 13154, 13155, 13156]
        $ images = random.sample(set(images_set1), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда1
        music Groove2_85
        img 13174
        with fade
        m "Миссис Робертс. Пожалуйста, подайте мне другие приборы."
        m "Эти недостаточно хорошо вымыты."
        img 13177
        betty "!!!"

    if rnd == 2:
        img 13157
        with fadelong
        w
        $ images_set2 = [13158, 13159, 13160, 13161]
        $ images = random.sample(set(images_set2), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда2
        music Groove2_85
        img 13176
        with fade
        m "Миссис Робертс. Пожалуйста, подогрейте еду."
        m "Она недостаточно горячая."
        img 13177
        betty "!!!"

    if rnd == 3:
        img 13162
        with fadelong
        w
        $ images_set3 = [13163, 13164, 13165, 13166]
        $ images = random.sample(set(images_set3), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда3
        music Groove2_85
        img 13175
        with fade
        m "Миссис Робертс. Вы вкусно готовите."
        m "Это похвально."
        img 13177
        betty "!!!"




    # Моника поела
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13171
    with fadelong
    m "Благодарю Вас, Миссис Робертс."
    m "Я поела."
    img 13172
    betty "!!!"
    return

label gallery_14600:
    # Бетти стоит в комнате Барди и недовольно
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("Вечер...")) from _rcall_textonblack_24
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 14566
    with fadelong
    betty "Чего тебе надо? Зачем ты меня звал?"
    # Барди лежит на кровати и смотрит на Бетти с улыбочкой
    music Sneaky_Snitch
    img 14567
    with diss
    bardie "Мне нужно проверить, соблюдаешь ли ты правила этого дома..."
    img 14568
    with fade
    betty_t "Как же меня этот сопляк достал со своими глупостями! Пусть проверяет... и отстанет уже от меня."
    # подходит к Бетти и задирает ей юбку, заглядывает под нее. Бетти без трусиков. Барди довольно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14569
    with fadelong
    w
    img 14570
    with diss
    w
    img 14571
    with diss
    w
    music Sneaky_Snitch
    img 14572
    with fade
    bardie "Хорошо. Я вижу, что ты соблюдаешь правила. Позови гувернантку. Я давно не проверял ее."
    # Бетти недовольно
    music Power_Bots_Loop
    img 14573
    with diss
    betty "Тебе надо - ты и зови. Мне нет дела до твоих глупостей."
    img 14574
    with fade
    bardie "Я сказал тебе, чтобы ты позвала гувернантку..."
    bardie "Или ты решила, что меня не надо слушаться? Ты забыла, что у меня есть парочка очень интересных фото с тобой и тренером?"
    # Бетти поворачивается к Барди, зло смотрит на него
    music Groove2_85
    img 14575
    with diss
    betty_t "Когда же ты уже отстанешь от меня?!"
    betty_t "!!!"
    # Барди с серьезной миной
    img 14576
    with fade
    bardie "Ну? Я жду!"
    img 14577
    with diss
    betty "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    img 14578
    with fadelong
    with hpunch
    betty "Гувернантка! Гувернантка!!!"
    # спустя несколько минут появляется Моника, Барди возле Моники
    # с лица
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Power_Bots_Loop
    img 14579
    with fadelong
    mt "Эта деревенщина не знает, что так орать на весь дом - неприлично..."
    mt "Что на этот раз?.. Эта Бетти с этим малявкой. Я уже даже не знаю, чего ожидать от них."
    mt "Когда же они все уже исчезнут из моего дома?.."
    # со спины
    music Hidden_Agenda
    img 14580
    with fade
    m "Да, миссис Робертс..."
    # Бетти, не поворачиваясь к Монике
    # Барди идет к кровата
    music Groove2_85
    img 14582
    with diss
    betty "Гувернантка, я тебя позвала, чтобы..."
    img 14583
    with diss
    betty "..."
    # Барди прыгает на кровать
    sound Jump1
    img 14581
    with diss
    w
    img 14584
    with fade
    betty "Хм. Барди, что ты там хотел? Давай, быстрее.!"
    music Sneaky_Snitch
    img 14585
    with diss
    bardie "Мне нужно проверить, насколько хорошо вы соблюдаете правила этого дома и..."
    img 14586
    with diss
    betty "И?"
    img 14587
    with diss
    bardie "... и запечатлеть это на свой телефон!"
    # Барди поворачивается к Монике и говорит
    img 14588
    with fade
    bardie "Начнем с тебя. Ты же хорошая гувернантка? Ты соблюдаешь правила?"
    # Моника в шоке, смотрит на него, как на больного
    music Power_Bots_Loop
    img 14589
    mt "Он совсем обнаглел!!!"
    mt "Эта малявка требует от меня, Моники Бакфетт, чтобы я согласилась задрать юбку!"
    mt "Задрать юбку перед каким-то малявкой, который будет снимать это на телефон! Который поселился в МОЕМ доме!!!"
    mt "!!!"
    img 14590
    with fade
    m "Я не буду делать этого! Да как ты смеешь?! В обязанности гувернантки не входит позировать в голом виде перед камерой!"
    music Groove2_85
    img 14591
    with diss
    bardie "А в обязанности хорошей гувернантки - входит. Ты же хорошая гувернантка?"
    # Моника смотрит зло
    img 14592
    m "!!!"
    img 14593
    with fade
    bardie "Или ты не соблюдаешь правила этого дома и хочешь получить штраф?"
    bardie "???"
    # Моника думает

    img 14594
    with diss
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            # Моника убегает
            sound highheels_run2
            music Groove2_85
            img 14595
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return
    img 14596
    with diss
    m "!!!"
    # Моника, срипя зубами соглашается, поднимает юбку, Барди фото не делает и смотрит на Бетти
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 14597
    with fadelong
    w
    img 14598
    with diss
    w
    img 14599
    with fade
    bardie "Бетти, а ты чего ждешь? Я хочу запечатлеть на фото вас вдвоем. Поднимай юбку!"
    # Бетти офигевает и начинает ор-р-р-рать
    music Power_Bots_Loop
    img 14600
    with hpunch
    betty "Если эта шлюха готова поднять юбку перед любым, даже перед моим приемным сыном..."
    betty "То я на такое никогда не соглашусь!"
    music Groove2_85
    img 14601
    with diss
    betty "!!!"
    # Бетти уходит, Моника продолжает держать юбку и смотрит ей вслед
    sound highheels_run2
    img 14602
    with fade
    betty "Я порядочная замужняя женщина и ты не смеешь требовать от меня такого!" #высокомерно
    bardie "Стой! Я с тобой еще не договорил! Ты куда?" # в этом же арте
    # кадр меняется на Барди
    music Sneaky_Snitch
    img 14603
    with diss
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return

label gallery_14612:
    # Барди разговаривает нагло, отдает приказ
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("Утро...")) from _rcall_textonblack_25
    scene black_screen
    with Dissolve(1)
    music Sneaky_Snitch
    img 14604
    with fadelong
    w
    img 14605
    with diss
    bardie "Сегодня мой преподаватель вызывает к себе родителей..."
    # Бетти вопросительно
    img 14606
    with diss
    betty "???"
    # Поворачивается
    music Groove2_85
    img 14607
    with fade
    betty "А я здесь причем?"
    betty "Иди к Ральфу, скажи ему об этом."
    img 14608
    with diss
    bardie "Ты же моя приемная мать. Ты и сходишь в колледж. Отцу не обязательно об этом знать."
    bardie "У меня там небольшие проблемы: меня могут отчислить. Я хочу, чтобы ты уладила этот вопрос."
    img 14609
    with fade
    betty "В смысле, 'ты хочешь'?! Почему я должна идти в колледж и вообще тратить свое время на это?"
    img 14610
    with diss
    bardie "Потому что отцу не обязательно знать не только о том, что у меня проблемы в колледже, но и еще кое о чем..."
    bardie "О чем мы оба с тобой знаем."
    # Бетти зло смотрит
    img 14611
    betty "!!!"
    img 14612
    with fade
    bardie "Вот поэтому сегодня именно ТЫ пойдешь в колледж и сделаешь так, чтобы меня не отчислили!"
    # Бетти раздражена назойливостью Барди
    img 14613
    with diss
    betty_t "Чего эта малявка пристала ко мне?! Как бы поскорее отвязаться от него?"
    img 14614
    with diss
    betty "Это твои проблемы, разбирайся с этим сам!"
    img 14615
    with fade
    bardie "Это наша общая проблема! Так же, как и проблема того, что ты трахаешься со всеми подряд!"
    # Бетти, кипя от злости
    img 14616
    betty "!!!"
    img 14617
    with diss
    betty "Вообще-то, я верная жена! Не смей говорить обо мне такое!"
    # Барди в ответ смеется
    img 14618
    with fade
    bardie "Если хочешь, чтобы отец и дальше думал, что ты верная жена, делай, что я тебе говорю."
    bardie "И только попробуй не уладить вопрос моего отчисления. Тебе же хуже будет!"
    # Бетти убийственным взглядом смотрит на него и уходит
    img 14619
    betty "!!!"
    img 14620
    with fade
    bardie_t "Мне нужно будет убедиться, что она все сделает правильно. Надо за ней проследить!"
    return

label gallery_15076:
    # Барди стоит возле своего стола и улыбается, Бетти заходит к нему в комнату, возмущается
    music Groove2_85
    img 15072
    with fadelong
    betty "Ты, наверное, не понял, о чем я тебе говорила! Ты почему со мной так разговариваешь?!"
    betty "!!!"
    # Барди с улыбочкой указывает рукой на свой ноут
    music Sneaky_Snitch
    img 15073
    with fade
    bardie "Я позвал тебя, чтобы ты посмотрела мою коллекцию фотографий. За последние дни я сделал несколько очень интересных фоток."
    img 15074
    with diss
    betty "???"
    betty "Что за глупости?! Какое мне дело до твоих дурацких коллекций?"
    img 15075
    with fade
    bardie "Я уверен, что тебе понравится... Посмотри."
    # Бетти подходит к его столу и заглядывает в ноут, видит на фото себя с учителем и офигевает
    #sound звук клавиши
    sound keyboard
    img 15076
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15077
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15078
    with diss
    betty "!!!"
    #sound звук клавиши
    sound keyboard
    img 15079
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15114
    with diss
    betty "ЧТО! ЭТО! ТАКОЕ?!"
    # Бетти бомбит
    music Power_Bots_Loop
    img 15080
    with fade
    betty "Ты что делаешь, сволочь!!!"
    betty "Я порядочная женщина! Что это за фотографии?!"
    betty "Как ты смеешь, мерзкий сопляк?! Я это сделала для тебя, а ты!.. Ты!!!"
    # Барди спокойно отвечает
    music Groove2_85
    img 15081
    with diss
    bardie "Я не просил тебя трахаться с ним. Ты даже в моем колледже нашла член, за который можно подержаться."
    bardie "На этих фото доказательство очередной измены моему отцу. Попробуй только сделать что-нибудь не так..."
    img 15082
    with diss
    bardie "..."
    bardie "Нууу, например, не слушаться меня... Эти фото сразу же увидит твой муж. И с того момента он станет уже твоим 'бывшем мужем'."
    # Бетти кипит от злости
    music Power_Bots_Loop
    img 15083
    betty_t "!!!"
    betty_t "Ненавижу! Да как он смеет?!"
    # Бетти смотрит на Барди убийственным взглядом
    img 15084
    with diss
    betty_t "Этот сопляк шпионил за мной! Он это все специально подстроил!"
    betty_t "!!!"
    music Hidden_Agenda
    img 15085
    with fade
    betty_t "Но я не могу позволить, чтобы Ральф увидел эти фотографии! Даже несмотря на то, что я это делала для его сына!"
    betty_t "..."
    # Бетти, злая, складывает руки на груди и спрашивает Барди
    music Groove2_85
    img 15086
    with diss
    betty "Чего тебе надо от меня?"
    img 15087
    with diss
    betty_t "Ненавижу этого сопляка!"
    img 15088
    with fade
    bardie "Так-то лучше."
    bardie "Помнишь, я хотел тебя сфотографировать с задранной юбкой? Ты мне отказала тогда..."
    bardie "Так вот..."
    # Бетти снова начинает орать
    music Power_Bots_Loop
    img 15089
    with fade
    betty "Да ты совсем охренел!"
    betty "НЕТ!"
    img 15090
    with diss
    betty "Ни за что!!! Я не буду фотографироваться так!"
    betty "!!!"
    # Барди с мерзкой улыбочкой
    music Groove2_85
    img 15091
    bardie "???"
    img 15092
    with diss
    bardie "Ты хорошо подумала?"
    img  15093
    with fade
    betty "..."
    # Барди показывает свой смартфон
    img 15094
    with diss
    bardie "Копии твоих фотографий с учителем есть у меня в телефоне. Отправить их отцу - вопрос нескольких секунд."
    img 15095
    betty "Ты не сделаешь этого!"
#    img 15096
    img 15097
    with diss
    bardie "Я уже делаю это."
    betty "!!!"
    # делает вид, что отправляет фотки, Бетти не выдерживает
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15098
    with fade
    betty "Хорошо, твоя взяла... Я согласна... Но только одно фото и ты обещаешь, что никому его не покажешь!"
    betty "..."
    img 15099
    bardie "Естественно, не покажу. Это только для меня..."
    img 15100
    with diss
    bardie_t "... и моего одноклассника."
    bardie_t "Теперь он мне точно поверит!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку, она в трусиках
    img 15101
    betty "Давай, быстрее!"
    # Барди ничего не делает и смотрит на нее вопросительно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15102
    with fadelong
    w
    img 15103
    with diss
    bardie "..."
    music Groove2_85
    img 15104
    with fade
    bardie "Во-первых, почему ты в трусах?"
    # Бетти опускает юбку, смотрит возмущенно и зло, но молчит
    img 15105
    with diss
    bardie "Ты забыла, что должна соблюдать правила этого дома? Снимай их, быстро!"
    bardie "Во-вторых, позови гувернантку. Я хочу сфотографировать вас вдвоем."
    # Бетти опять бомбит
    music Power_Bots_Loop
    img 15106
    betty "Я не собираюсь фотографироваться с этой шлюхой!"
    betty "!!!"
    music Groove2_85
    img 15107
    with diss
    bardie "Ты сейчас снимешь свои трусы и позовешь гувернантку! Я жду!"
    # Барди садится на свою кровать и демонстративно показывает Бетти свой телефон. Бетти кипит от злости, но подчиняется
    img 15108
    with diss
    w
    sound Jump1
    img 14581
    with diss
    w
    img 15109
    with diss
    w
    img 15110
    with fade
    betty_t "Ненавижу этого сопляка!"
    # Бетти отворачивается от Барди, со злостью снимает трусики
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 15111
    with fadelong
    w
    img 15112
    with diss
    betty "!!!"
    # Бетти с напряженным лицом зовет Монику
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 15113
    with hpunch
    betty "Гувернантка!!! Иди сюда!"
    # Барди самодовольно ухмыляется
    return

label gallery_15130:
    # Барди с телефоном в руках сидит на своей кровати, Бетти стоит в комнате Барди и недовольно кричит
    music Power_Bots_Loop
    img 15113
    with hpunch
    betty "Гувернантка!!!"
    # спустя несколько минут появляется Моникаg
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Groove2_85
    img 14579
    with fade
    mt "Она опять орет на весь дом..."
    mt "Что этой деревенщине снова от меня нужно?"
    img 14582
    with diss
    m "Да, миссис Робертс..."
    # Бетти и Моника стоят перед Барди, он сидит на кровати
    img 15115
    with fade
    betty "Гувернантка, я..."
    img 15116
    with diss
    betty "..."
    img 15117
    with fade
    bardie "Мне нужно проверить, насколько хорошо ты соблюдаешь правила этого дома и..."
    bardie "...сделать фото!"
    img 14589
    with diss
    mt "Он опять хочет фото?! Когда он уже отстанет от меня?!"
    img 15118
    with fade
    bardie "Давай, без лишних разговоров. Поднимай юбку!"
    # Моника зло смотрит на него
    music Power_Bots_Loop
    img 14592
    with diss
    m "Я не собираюсь фотографироваться с задранной юбкой!"
    m "Достаточно того, что ты при каждом удобном случае заглядываешь мне под юбку!"
    img 15119
    with diss
    mt "Мелкий озабоченный извращенец!"
    music Groove2_85
    img 15120
    with fade
    bardie "Гувернантка слишком много разговаривает!"
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    img 14592
    with diss
    m "..."
    # Барди с угрозой
    img 15121
    with fade
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    img 14594
    with diss
    mt "!!!"
    mt "Ненавижу эту малявку! И эту чокнутую деревенщину Бетти!"
    mt "Когда этот дом снова станет моим, я возьму ее к себе гувернанткой. Будет работать у меня за еду."
    mt "!!!"
    # Моника смотрит зло, Бетти все это время стоит с каменным лицом
    img 14588
    with fade
    m "Зачем тебе нужна эта фотография?"
    img 15122
    with diss
    bardie "Гувернантку это не касается! Поднимай юбку!"
    # Барди поднимает руку с телефоном, чтобы сделать фото
    mt "..."

    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            sound highheels_run2
            img 14595
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return
    # Моника, срипя зубами соглашается, поднимает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14598
    with fadelong
    w
    img 15123
    with diss
    w
    music Groove2_85
    img 15124
    with fade
    bardie "Хорошая гувернантка."
    # Барди фото не делает и смотрит на Бетти
    img 15125
    with diss
    bardie "Бетти?.."
    img 15126
    betty "!!!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15127
    with fadelong
    w
    img 15128
    with diss
    w
    img 15129
    with diss
    betty "Давай, быстрее!"
    betty "Только одно фото!"
    w
    call photoshop_flash() from _rcall_photoshop_flash_159
    w
    # Барди с довольным видом делает фотку
    img 15130
    with diss
    betty "Все?"
    bardie "Подождите, что-то не получилось фото. Ну-ка еще раз."
    w
    call photoshop_flash() from _rcall_photoshop_flash_160
    w
    # Барди делет еще несколько кадров
    img 15131
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_161
    w
    img 15132
    with diss
    w
    call photoshop_flash() from _rcall_photoshop_flash_162
    w
    img 15133
    with diss
    betty "Все! Хватит!"
    w
    call photoshop_flash() from _rcall_photoshop_flash_163
    w
    # Бетти опускает юбку, Моника следом за ней
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 14584
    with fadelong
    betty "Надеюсь, ты доволен?"
    img 14585
    with diss
    bardie "Очень! Вы обе доказали мне, что соблюдаете правила этого дома."
    bardie "..."
    img 14587
    with diss
    bardie "Моему однокласснику точно понравится!"
    # Бетти с Моникой офигевают
    music Power_Bots_Loop
    img 15134
    with hpunch
    mt "!!!"
    betty "!!!"
    # Бетти начинает орать, Моника зло смотрит
    img 15135
    with fade
    betty "ЧТООООО?!!"
    betty "Какому еще однокласснику?!"
    # Барди нагло
    music Groove2_85
    img 15136
    with diss
#    if ep28_monica_eric_meeting_completed == False:
    bardie "Ах да... Вы же еще не знакомы... Я скоро приглашу его в гости."
#    else:
#        bardie "Ах да... Ты еще с ним не знакома... В отличие от гувернантки."
    img 15119
    with diss
    mt "Он совсем обнаглел! Ненавижу эту малявку!"
    mt "И почему у этой деревенщины не хватает мозгов, чтобы приструнить его?!"
    music Power_Bots_Loop
    img 15137
    with fade
    betty "Нет!!! Не смей! Ты говорил, что это фото никто не увидит!"
    betty "!!!"
    music Groove2_85
    img 14587
    with diss
    bardie "Я так сказал?! Хм... Никто, кроме моего одноклассника."
    bardie "Аха-ха!"
    music Power_Bots_Loop
    img 15138
    with fade
    betty "Да как ты смеешь так обращаться со мной, порядочной женщиной?! Сопляк!"
    betty "Я - жена твоего отца! А ты собираешься показываеть фото, где я голая, да еще и с этой шлюхой, своему однокласснику!!!"
    img 15139
    with diss
    mt "Ненавижу эту семейку! Когда она будет моей гувернанткой, я ее уволю!"
    mt "!!!"
    music Groove2_85
    img 15140
    with fade
    bardie "Если ты и дальше будешь со мной так разговаривать, то женой моего отца ты будешь недолго..."
    bardie "Ты забыла, что у меня есть много фото, интересных фото...?"
    img 15141
    with diss
    bardie "И в интересной компании..."
    bardie "???"
    # Бетти смотрит испепеляющим взглядом, но молчит
    img 15142
    betty "!!!"
    img 15143
    with diss
    mt "Хм. Кто из нас после этого шлюха?"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15144
    with fade
    bardie "Вы на сегодня свободны. Можете идти."
    return

label gallery_15147: # если ушла от учителя
    # Моника заходит в комнату Барди, тот сидит на кровати, залипнув в телефон
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 15145
    with fadelong
    w
    img 15146
    with diss
    mt "Ненавижу эту малявку! Он меня достал уже со своими глупостями!"
    # Барди вопросительно смотрит на нее
    img 15147
    with fade
    bardie "Ну как сходила, гувернантка? Надеюсь, у тебя все получилось уладить?"
    # Моника недовольно
    img 15148
    with diss
    m "Если бы твой друг включил мозг, когда надумал залезть в шкафчик мисс Мэнсфилд. То проблем бы никаких не было."
    # Барди смотрит на Монику
    img 15149
    with fade
    bardie "И? Проблема решена?"
    # Моника орет
    music Power_Bots_Loop
    img 15150
    m "Нет! И я не собираюсь заниматься этими глупостями!"
    m "Я не пойду больше в этот твой чертов колледж! Разбирайтесь сами!"
    # Барди угрожающе
    music Groove2_85
    img 15151
    with fade
    bardie "Гувернантка забыла, что Эрик делает хозяину домашку?"
    music Power_Bots_Loop
    img 15152
    m "Да какое мне дело до этого?!" #возмущенно
    m "Пусть сам решает свои проблемы!!!"
    music Groove2_85
    img 15153
    with fade
    bardie "Гувернантка плохая! Ее надо наказать!"

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("5 минут спустя...")) from _rcall_textonblack_26
    img black_screen
    with Dissolve(2.0)
    music Groove2_85

    if monicaUnder != "Nude":
        sound snd_fabric1
        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                img 10272
        else:
            if monicaBettyPantiesId == 1:
                #betty
                img 10273
            if monicaBettyPantiesId == 2:
                img 10274
            if monicaBettyPantiesId == 3:
                img 10275
            if monicaBettyPantiesId == 4:
                img 10276
            if monicaBettyPantiesId == 5:
                img 10277
        with fadelong
        bardie "Покажи мне, как хорошо ты соблюдаешь правила этого дома!"
        sound snd_fabric1
        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                #governess
                img 10292
                with diss
                w
                img 10293
                with diss
                w
        else:
            if monicaBettyPantiesId == 1:
                #betty
                img 10295
                with diss
                w
                img 10294
                with diss
                w
                img 10305
                with diss
                w
        #
            if monicaBettyPantiesId == 2:
                img 10296
                with diss
                w
                img 10297
                with diss
                w
                img 10306
                with diss
                w
        #
            if monicaBettyPantiesId == 3:
                img 10299
                with diss
                w
                img 10298
                with diss
                w
                img 10307
                with diss
                w
        #
            if monicaBettyPantiesId == 4:
                img 10300
                with diss
                w
                img 10301
                with diss
                w
                img 10308
                with diss
                w
        #
            if monicaBettyPantiesId == 5:
                img 10303
                with diss
                w
                img 10302
                with diss
                w
                img 10304
                with diss
                w
    else:
        img 10281
        with fadelong
        bardie "Покажи мне, как хорошо ты соблюдаешь правила этого дома!"
    img 10309
    with fade
    w
    img 10310
    with fade
    w
    img 10311
    with fade
    mt "Ненавижу его!"
    img 10312
    with fade
    w
    img 10313
    with fade
    mt "Он меня этим не напугает и не заставит идти к учителю!"
    img 10314
    with fade
    w
    img 10315
    with fade
    mt "Он все равно не добьется своего!"
    img 10316
    with fade
    w
    img 10317
    with fade
    mt "Я не пойду в этот чертов колледж! Я не хочу!!!"
    img 10318
    with fade
    w
    img 10319
    with fade
    w


label gallery_15147_1:
    # Барди шлепает Монику

    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_1 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_1.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_1
    wclean
    stop music

    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_2 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_2.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_2
    bardie "Гувернантка ослушалась приказа хозяина!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_3 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_3.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_3

    bardie "Получай!"
    bardie "Плохая гувернантка!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_4 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_4.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_5 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_5.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_5
    bardie "Гувернантка поняла, что вела себя плохо?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_6 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_6.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_6
    bardie "Гувернантка больше не будет так делать и выполнит все, что скажет хозяин?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_7 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_7.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_7
    bardie "Гувернантка должна пойти в колледж и решить проблему Эрика!"
    wclean
    stop music

    music Power_Bots_Loop
    mt "Черт! Как больно! Когда он уже остановится?!"
    menu:
        "Отпусти меня немедленно, малявка!":
            img 10320
            with fade
#            m "!!!"
            m "Я хорошая гувернантка!"
            m "Но я не пойду в колледж!"
            m "Отпусти меня немедленно, малявка!"
#            mt "Нет! Я не пойду туда больше!"
            jump gallery_15147_1
        "Я поняла! Я буду слушаться хозяина!":
            pass


    music Groove2_85
    img 10321
    with fade
    m "Я поняла! Я буду слушаться хозяина!"
    img 10322
    with fade
    m "Я хорошая гувернантка! Я поговорю с учителем еще раз!"
    img 10323
    with fade
    bardie "Так-то лучше!"
    img 10324
    with diss
    bardie "Если будешь себя снова плохо вести, получишь еще!"
    img 10325
    with fade
    bardie "Гувернантка, можешь продолжать работать..."
    bardie "Ты мне пока не нужна."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Pyro_Flow
    img 10326
    with fadelong
    mt "Не могу поверить!"
    mt "Этот малявка отшлепал меня словно я маленький ребенок!"

    #Если повтор
    if bardieMonicaPunishmentCount > 1:
        img 10327
        with fade
        mt "И уже не первый раз!!!"
        #
        img 10327
        mt "В моем же доме!"
        mt "Отшлепали! Меня!!!"
        mt "Монику Бакфетт!!!"
        #

    img 10328
    with fade
    mt "У меня попа горит!"
    img 10329
    with diss
    mt "Что этот Барди себе позволяет?!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 10330
    with fadelong
    mt "Как унизительно!"
    mt "Мне надо как-то избавиться от него!"


#    img 14596
#    m "!!!" # зло смотрит на него
#    img 15154
#    mt "Надеюсь, после этого он, наконец, отстанет от меня."
    # поднимает юбку БАРДИ НАКАЗЫВАЕТ МОНИКУ - ШЛЕПАЕТ ПО ПОПЕ
#    bardie "Гувернантка ослушалась приказа хозяина!"
#    bardie "Плохая гувернантка!"
#    bardie "Гувернантка поняла, что вела себя плохо?"
#    bardie "Гувернантка больше не будет так делать и выполнит все, что скажет хозяин?"
#    bardie "Гувернантка должна пойти в колледж и решить проблему Эрика!"


    return

label gallery_22069:
    music stop
    img black_screen
    with diss
    pause 2.0
    # через несколько минут Моника заходит к нему в комнату, смотрит на Эрика, тот заинтересованно смотрит на нее
    music Groove2_85
    img 15254
    with fadelong
    mt "Этот малявка привел в дом еще одного такого же озабоченного мелкого извращенца, как он сам."
    # переводит взгляд на Барди
    img 15255
    with diss
    m "Да? Ты звал меня?"
    # Барди с серьезным лицом говорит Монике
    img 15256
    bardie "Гувернантка, мне надо проверить, соблюдаешь ли ты правила этого дома!"
    music Power_Bots_Loop
    img 15257
    with hpunch
    m "Что, прямо сейчас? При твоем друге?!" # удивленно
    m "???"
    # Барди все с такой же серьезной миной
    music Groove2_85
    img 15258
    with fade
    bardie "Да, мне нужно проверить прямо сейчас, гувернантка."
    # Моника зло
    img 15259
    with diss
    m "В мои обязанности это не входит! Я не собираюсь проходить эту проверку при твоем друге!"
    m "!!!"
    # Барди с угрозой
    img 15260
    with fade
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    img 15261
    with diss
    m "..."
    img 15262
    with fade
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    # Моника злится, но молчит
    img 15263
    with diss
    mt "!!!"
    mt "Ненавижу эту малявку!"
    img 15264
    with fade
    bardie "Ну? Я долго должен ждать?"

    img 15267
    with diss
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            img 15266
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 2.0
            return
    # Моника с недовольным лицом задирает юбку, Эрик сидит офигевший и пялится на нее, Барди самодовольно ему говорит
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15268
    with fadelong
    w
    img 15270
    with diss
    bardie "Ну что? Теперь ты убедился, что я не врал?"
    img 15269
    with diss
    eric "..."
    music Groove2_85
    img 15271
    with fade
    bardie "Я выиграл спор! С тебя домашка на месяц вперед!"
    # Моника опускает юбку, недовольно смотрит на Барди
    img 15272
    with diss
    mt "Они спорили на домашку? Детский сад!"
    mt "Теперь он, наконец, отвяжется от меня?"
    # Эрик продолжает пялиться на Монику
    img 15273
    with fade
    eric "Н-нет..."
    # Барди и Моника вопросительно смотрят на Эрика
    img 15274
    with diss
    bardie "Что 'нет'? Мы с тобой договаривались!"
    img 15275
    with fade
    eric "Я... Хм... Спор не выигран."
    eric "Потому что я... Я не рассмотрел..."
    img 15276
    with diss
    m "Что значит 'не рассмотрел'?! Я все сделала, как сказал Барди."
    # Эрик смотрит на юбку Моники, но обращается к Барди
    img 15277
    with fade
    eric "Если твоя гувернантка задерет юбку еще раз и... даст посмотреть поближе, тогда я буду делать тебе домашку 2 месяца."
    # Моника офигевает
    music Power_Bots_Loop
    img 15278
    with hpunch
    mt "!!!"
    mt "Эти две малявки спорят на какую-то глупость! А я должна тут стоять перед ними полуголая!!!"
    # Барди поворачивается к Монике и смотрит вопросительно, Моника смотрит на него зло, но ничего не делает
    music Groove2_85
    img 15279
    with fade
    bardie "Чего ты ждешь, гувернантка? Ты не слышала что-ли? Подойди поближе к нам и подними юбку еще раз!"
    img 15272
    with diss
    mt "Ненавижу эту малявку! И его озабоченного друга!"
    mt "Если я этого не сделаю, он не отвяжется от меня."
    img 15280
    with fade
    bardie "Я жду."
    # Моника подходит ближе к  Эрику, и снова задирает юбку, Эрик с тупым выражением лица пялится на ее киску
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15281
    with fadelong
    w
    img 15282
    with diss
    w
    img 15283
    with diss
    eric "Я... Я вообще ничего не могу рассмотреть."
    # Барди смотрит на Монику, Моника взглядом готова убить Эрика
    img 15284
    with fade
    bardie "Гувернантка, расставь ноги шире!"
    # Моника зло смотрит на него, но подчиняется и ставит ноги шире
    img 15285
    mt "!!!"
    # Моника снова испепеляет взглядом Эрика, а он пристально разглядывает
    img 15286
    with fade
    w
    img 15287
    with diss
    w
    img 15288
    with diss
    w
    music Groove2_85
    img 15289
    with fade
    eric "Я хочу увидеть еще ближе. Пусть твоя гувернантка сядет на кровать. Тогда я смогу все рассмотреть."
    # Моника злится
    img 15291
    m "!!!"
    img 15290
    with diss
    menu:
        "Сесть на кровать.":
            pass
        "Отказаться. Эти малявки совсем обнаглели!":
            music Power_Bots_Loop
            img 15292
            with fade
            m "Я не буду этого делать! Все итак слишком далеко зашло!!!"
            # Барди угрожающе
            img 15293
            with diss
            bardie "Гувернантка не хочет быть хорошей? Она забыла, что может сделать хозяин, если она не будет слушаться его?"
            img 15272
            with diss
            mt "Черт!"
            img 15294
            with diss
            m "..."
            music Groove2_85
#            return 1
    # Моника садится на край кровати, а Барди и Эрик смотрят на нее
#    img 15295
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22048
    with fadelong
    w
    img 22049
    with diss
#    img 15296
    bardie "Подними юбку."
    # Моника слушается
#    img 15297
    img 22050
    with diss
    m "!!!"
#    img 15298
    sound snd_fabric1
    img 22051
    with diss
    w
    img 22052
    with diss
    w
    img 22053
    with diss
    bardie "Раздвинь ноги."
    img 22054
    w
    # Моника раздвигает их, совсем немного
    img 22055
    with fade
    w
    img 22056
    with diss
    w
    img 22057
    with diss
    w
    img 22058
    with fade
    w
    img 22059
    with diss
    bardie "Eще шире! Ему же ничего не видно так."
    # Барди с Эриком внимательно смотрят, Моника подчиняется
    img 22060
    mt "Я когда-нибудь задушу эту мерзкую малявку! И почему он прицепился именно ко мне, а не к Бетти?!"
    img 22061
    with diss
    mt "!!!"
    img 22062
    with fade
    w
    img 22063
    with diss
    w
    # Эрик наклоняется над кроватью близко от киски Моники и разглядывает ее в упор
    sound Jump1
    img 22064
    with diss
    w
    img 22065
    with diss
    w
    m "!!!"
    music Loved_Up
    img 22066
    with fade
    eric "Чувак, я видел в порно, как лижут киски и всегда хотел попробовать. Ты же не против?"
    # Барди удивленно смотрит на него
    img 22067
    with diss
    bardie "???"
    music Groove2_85
    img 22068
    with fade
    bardie "Окей."
    # Моника возмущается
    img 22069
    with diss
    m "Какого черта?! А меня ты не хочешь спросить? Я не хочу, чтобы ты ко мне прикасался!"
    # Барди, смотря не на нее, а на киску
    img 22070
    with fade
    bardie "Он только потрогает языком и не будет больше ничего делать."
    bardie "Зато за хозяина будут делать домашние задания целых два месяца."
    img 22071
    with diss
    bardie "Хорошая гувернантка должна быть рада пойти на такие маленькие жертвы ради своего хозяина."
    img 22072
    with fade
    mt "Какой ужас! Мне что, приходится раздвигать ноги перед кем-то ради домашних заданий этого сопляка?"
    mt "Мне?! Монике Бакфетт! Самой богатой и влиятельной женщине этого города!"

    # Моника негодует, но продолжает сидеть с развинутыми ногами
    label gallery_22079:
    music Power_Bots_Loop
    img 22073
    with hpunch
    m "Только попробуй коснуться меня там пальцами или чем-либо еще!"
    m "!!!"
    music Groove2_85
    img 22074
    with fade
    bardie "Да, Эрик! Не трогай ее там пальцами или чем-то еще. Это МОЯ гувернантка."
    bardie "Не забывай это!"
    # Эрик все это время глаз не отводит от ее киски
    music Loved_Up
    img 22075
    with diss
    eric "..."
    # лицо Эрика все ближе к киске Моники, на лице Моники отвращение
    music Groove2_85
    img 22076
    with fade
    mt "Фу, как это мерзко! Но если я не послушаюсь Барди..."
    mt "Я тогда остановила его прямо в полиции. Еще несколько минут и он был бы у Маркуса."
    mt "Боже! Даже боюсь думать о последствиях."
    mt "У меня сейчас нет другого выхода, кроме того, как перетерпеть эту мерзость."
    # Эрик высовывает свой язык и касается им киски Моники
#    music Loved_Up
    #видео erick licking monica
    music v_Monica_Eric_Licking_1_1
    img 22079
    with diss
    w
    img 22077
    with diss
    w
    img 22078
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Licking_1_1 = Movie(play="video/v_Monica_Eric_Licking_1_1.mkv", fps=30)
    show videov_Monica_Eric_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Licking_1_2 = Movie(play="video/v_Monica_Eric_Licking_1_2.mkv", fps=30)
    show videov_Monica_Eric_Licking_1_2
    with fadelong
    wclean
#    music v_Monica_Eric_Licking_1_1
    img 22080
    with diss
    w
    img 22082
    with diss
    w
    img 22081
    with diss
    mt "По крайней мере, это не так неприятно как я думала."
    mt "Но это все-равно отвратительно!"
    mt "Когда же он уже закончит все это?!"
    music Groove2_85
    img 22083
    with fade
    bardie "Эй, чувак! У нас точно все в силе? Ты мне будешь делать домашку?"
    music Turbo_Tornado
    img 22084
    with diss
    eric "Да буду, буду!"
    # тут Эрик присасывается к Монике, Барди в шоке смотрит на это
    sound Jump2
    #sound звук эрик присосался к Монике
    img 22085 # присосался
    with hpunch
    w
    img 22086
    with diss
    m "!!!"
    img 22087
    with diss
    bardie "Эй-эй, чувак. Полегче..."
    # Эрик делает еще несколько движений языком и поворачивается к Барди
    img 22088
    with fade
    eric "Лизать самому намного прикольнее, чем просто смотреть на это!"
    eric "А ты пробовал?"
    img 22089
    with diss
    bardie "Не, даже не думал об этом."
    img 22090
    with fade
    eric "Давай, чувак, попробуй."
    img 22091
    with diss
    bardie "Прямо сейчас?"
    eric "Ага. Это правда прикольно."
    # Барди смотрит на Монику, та на него смотрит испепеляющим взглядом, но молчит
    img 22092
    with diss
    bardie "..."
    img 22093
    with diss
    m "!!!"
    img 22095
    with diss
    w
    sound plastinka1b
    music stop
    img 22094
    with diss
    m "!!!"
    # Эрик отстраняется от Моники, Барди наклоняется к ней
    music Sneaky_Snitch
    img 22096
    with fade
    bardie_t "Хм. Надо хотя бы разочек попробовать, каково это лизать киску."
    img 22097
    with diss
    bardie_t "..."
    # наклоняется еще ближе и проводит языком, лицо Эрика совсем близко и когда Барди останавливается и поднимает голову, то тоже проводит языком
    label gallery_22113:
    music Groove2_85
    img 22098
    with fade
    bardie "Хорошая гувернантка поднимает юбку!"
    sound Jump1
    img 22099
    with diss
    w
    img 22100
    with diss
    w
    img 22101
    m "!!!"
    img 22102
    with fade
    bardie "Плохая гувернантка будет наказана штрафом..."
    menu:
        "Сделать что говорит Барди.":
            pass
    img 22103
    with diss
    mt "Какой кошмар! Что эти озабоченные малявки творят?!"
    sound snd_fabric1
    img 22104
    with fade
    mt "Что вообще у них в голове творится? Как можно было до такого додуматься?"
    img 22105
    with diss
    w
    mt "!!!"
    img 22106
    with diss
    w
    mt "Почему я должна это терпеть?!"
    music stop
    img black_screen
    with diss
    pause 1.5
#    music Loved_Up
    music v_Monica_Eric_Bardie_Licking_1_1
    img 22107
    with fadelong
    w
    #видео monica eric bardie licking
    img 22108
    with diss
    mt "Черт! Как же щекотно..."
    img 22109
    with diss
    w
    img 22110
    with diss
    w
    img 22111
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Bardie_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Bardie_Licking_1_1 = Movie(play="video/v_Monica_Eric_Bardie_Licking_1_1.mkv", fps=30)
    show videov_Monica_Eric_Bardie_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Bardie_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Bardie_Licking_1_2 = Movie(play="video/v_Monica_Eric_Bardie_Licking_1_2.mkv", fps=30)
    show videov_Monica_Eric_Bardie_Licking_1_2
    with fadelong
    wclean
    music v_Monica_Eric_Bardie_Licking_1_1
    img 22112
    with diss
    mt "..."
    img 22113
    with diss
    w
    img 22114
    with diss
    sound ahhh11
    mt "Странные ощущения какие-то..."
    img 22115
    with diss
    w

    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 22116
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    eric "Ааааааа..."

    sound bulk1
    img 22117
    sound man_moan6
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    eric "Ааааааахххх!!!"
    # парни в это время продолжают лизать, сначала один, потом его сменяет другой. Эрик достает свой член из штанов
    # Эрик смотрит, как лижет Барди, проводит по своему члену рукой пару раз и кончает
    # Барди видит это и делает то же самое со своим членом, и кончает на живот Моники
    img 22118
    with diss
    m "Эй, что ты делаешь?! Фуууу!!!"
    img 22120
    with diss
    m "Не смей!"
    sound bulk1
    img 22119 # звук кончания
    sound man_moan1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    #sound звук спермы на живот
    sound hlup2
    img 22121 # прилетает сперма Монике на живот
    with diss
    w
    img 22122
    with diss
    mt "!!!"
    # Моника сдвигает ноги и опускает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 22123
    with fadelong
    mt "Наконец-то, это закончилось!"
    # вопросительно смотрит на Барди, тот расслаблен и доволен
    img 22124
    with diss
    bardie "Гувернантка хорошая. Гувернантка помогла хозяину выиграть спор."
    img 22125
    mt "!!!"
    # смотрит на Эрика
    img 22126
    with fade
    bardie "Эй, чувак, что там с домашкой?"
    # Эрик тоже расслаблен и доволен
    eric "Окей. Ты выиграл два месяца домашки."
    # Барди радостный, поворачивается к Монике
    sound highheels_run2
    img 22127
    with diss
    bardie "Можешь идти, гувернантка. На сегодня ты свободна."
    music stop
    img black_screen
    with diss
    pause 1.5
    return

label gallery_22180:
    # Барди на кровати, Бетти стоит напротив него и недовольно на него смотрит
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 22128
    with fadelong
    betty "Зачем ты меня звал? У меня нет времени на твои глупости!"
    img 22129
    with diss
    betty "Давай быстрее!"
    # Барди с мерзкой улыбочкой
    img 22130
    with fade
    bardie "Зови гувернантку. Я хочу проверить, как вы соблюдаете правила этого дома."
    img 22131
    betty "!!!"
    img 22132
    with diss
    betty "А сам проверить не можешь?!"
    betty "Я не хочу звать ее! А тем более при ней показывать, что я соблюдаю правила!"
    # Барди с фейсом а-ля хозяин дома
    img 22133
    with fade
    bardie "Ты, наверное, забыла, что я тут хозяин?!"
    bardie "Ты должна меня слушаться! Зови гувернантку!!!"
    # Бетти с недовольным лицом орет
    img 22131
    betty "!!!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 22134
    with hpunch
    betty "Гувернантка! Иди сюда!"
    # через несколько минут в комнату заходит Моника, они вдвоем стоят перед кроватью Барди
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Hidden_Agenda
    img 22135
    with fadelong
    m "Да, миссис Робертс?" #недовольно
    music Power_Bots_Loop
    img 22136
    with diss
    mt "Эта деревенщина с малявкой уже меня достали!"
    mt "Что бы такого придумать, чтобы они от меня отстали?"
    music Hidden_Agenda
    img 22137
    with fade
    mt "???"
    # Бетти смотрит на Монику высокомерно
    betty "Гувернантка, я тебя позвала, чтобы..."
    betty "Чтобы..."
    # поворачивается к Барди
    img 22138
    with diss
    betty "..."
    music Groove2_85
    img 22139
    with fade
    bardie "Гувернантка, я хочу проверить, насколько хорошо вы соблюдаете правила этого дома."
    img 22140
    with diss
    bardie "И как хорошо слушаетесь хозяина."
    # Моника зло смотрит на Бетти
    img 22141
    with diss
    mt "Эта провинциальная шлюха могла бы поставить сопляка на место..."
    mt "Если бы была в состоянии говорить 'нет' мужчинам..."
    # Моника поворачивается к Барди
    img 22142
    with fade
    m "Что мне надо сделать? Задрать юбку?"
    img 22143
    with diss
    bardie "Ага. Но не прямо сейчас. Сначала я хочу проверить Бетти."
    img 22144
    with diss
    mt "???"
    betty "!!!"
    # Барди встает с кровати, улыбаясь многозначительно, говорит Бетти
    music stop
    img black_screen
    with diss
    pause 1.5
    sound Jump1
    music Groove2_85
    img 22145
    with diss
    bardie "Сядь на мою кровать."
    # Бетти офигевает
    music Power_Bots_Loop
    img 22146
    with fade
    betty "А это еще зачем?! Что ты еще придумал, сопляк?"
    img 22147
    with diss
    # Барди угрожающе
    bardie "Ты не хочешь слушать то, что говорю тебе я?"
    # Бетти психует, злится
    music Groove2_85
    img 22148
    with fade
    betty "..."
    betty_t "Ненавижу этого сопляка!!!"
    # но выполняет его приказ и садится на край его кровати
    img 22149 # садится
    with diss
    w
    img 22150
    betty "!!!"
    img 22151
    with fade
    bardie "А теперь я проверю, как ты соблюдаешь правила. Покажи мне. Разведи ноги в стороны и подними юбку."
    # Бетти зло на него смотрит
    img 22152
    with diss
    w
    music Power_Bots_Loop
    img 22153
    betty "Я не хочу делать этого при гувернантке! Вообще-то, на мне нет трусиков!"
    img 22154
    with diss
    betty "!!!"
    img 22155
    with diss
    betty "Я не собираюсь сидеть тут перед вами с раздвинутыми ногами!"
    # Барди ей показывает рукой на свой ноут
    music Groove2_85
    sound Jump1
    img 22156
    with fade
    bardie "Давай, еще раз посмотрим на твои фото?"
    img 22157
    with diss
    bardie "Возможно, ты забыла, что там отлично видно, как ты мастерски ведешь переговоры, с раздвинутыми ногами?"
    music Power_Bots_Loop
    img 22158
    with hpunch
    betty "Не смей такое говорить про меня! Я порядочная женщина!"
    music Groove2_85
    img 22159
    with fade
    bardie "Тогда делай, как я говорю! Порядочные женщины должны слушаться хозяина дома!"
    img 22160
    with diss
    bardie "Я жду!"
    # Бетти зло смотрит, но подчиняется, поднимает юбку, раздвигает ноги (далее она их раздвинет еще шире, см.ниже)
    img 22161
    with diss
    betty "!!!"
    # Барди смотрит на нее
    music stop
    img black_screen
    with diss
    pause 1.5
    sound snd_fabric1
    music Groove2_85
    img 22162
    with fade
    w
    img 22163
    with diss
    w
    img 22164
    with fade
    bardie "Хорошо. Так и сиди, не опускай юбку."
    img 22165
    with hpunch
    bardie "Сейчас я буду проверять гувернантку."
    # Барди поворачивается к Монике
    img 22166
    with fade
    bardie "Гувернантка, встань на пол на колени между ног Бетти!"
    # Моника офигевает
    music Power_Bots_Loop
    img 22167
    with diss
    m "ЧТО?!"
    m "Я не буду этого делать!!!"
    m "Проверяй как обычно!"
    # Барди недовольно
    music Groove2_85
    img 22168
    with fade
#    bardie "Ты плохая гувернантка. Ты отказалась принять благодарность моего друга."
    bardie "Ты плохая гувернантка."
    bardie "Плохую гувернантку хозяин должен наказать!"
    # Барди угрожающе
    img 22169
    with diss
    bardie "Если не сделаешь, как я говорю, то тебе будет только хуже!"
    # Моника зло на него смотрит
    music Power_Bots_Loop
    img 22170
    with fade
    mt "Он снова угрожает мне Маркусом..."
    mt "Ему же ничего не стоит пойти в полицию и сказать, что я живу здесь!"
    img 22171
    with diss
    mt "..."
    mt "Он расскажет..."
    mt "Полицейские будут здесь в тот же день..."
    mt "Возможно, даже завтра..."
    img 22172
    with diss
    mt "Нет! Я не должна допустить этого!!!"
    music Groove2_85
    img 22173
    with fade
    mt "!!!"
    # Моника с недовольным видом встает на колени перед Бетти
    # Барди самодовольно улыбается
    sound Jump1
    img 22174
    with diss
    w
    img 22175
    with diss
    w
    img 22176
    with diss
    w
    img 22177
    with fade
    bardie "Бетти, откинься назад, на кровать."
    img 22178
    with diss
    bardie "Гувернантка, наклонись и дотронься языком до киски Бетти."
    # Моника смотрит на него уничтожающим взглядом, а Бетти возмущается
    music Power_Bots_Loop
    img 22179
    with hpunch
    betty "Я не хочу, чтобы эта шлюха прикасалась своими губами ко мне!" #говорит она Барди
    img 22180
    with diss
    betty "Гувернантка, не смей прикасаться ко мне!" #говорит Монике
    # Моника зло
    img 22181
    with fade
    mt "Они издеваются?! Меня тошнит от того, что он просит сделать!"
    mt "И кому?! Этой деревенщине! Я, Моника Бакфетт!"
    img 22182
    with diss
    w
    img 22183
    with diss
    w
    music Groove2_85
    img 22184
    with fade
    w
    img 22185
    with diss
    w
    # Моника с ненавистью смотрит на Бетти, потом с отвращением приближается к ее киске и проводит языком
    img 22186
    with diss
    w
    img 22187
    with diss
    w
    img 22188
    with diss
    w
    img 22189
    with diss
    w
    img 22190
    with diss
    w
    img 22191
    with diss
    w
    img 22192
    with diss
    w
    #sound Моника прикасается языком к киске Бетти
    sound lick3
    img 22193
    with diss
    w
    img 22194
    with diss
    betty "Фууу!"
    # Моника отстраняется все с тем же отвращением, смотрит на Барди
    sound Jump1
    music Power_Bots_Loop
    img 22195
    with fade
    m "!!!"
    img 22196
    with diss
    m "Надеюсь, это все?! Я могу идти?"
    bardie "Нет, гувернантка! Я тобой очень недоволен!"
    bardie "Сделай так еще несколько раз, а я подумаю, достаточно или нет."
    # Моника снова с отвращением прикасается к Бетти и лижет ей там, Бетти злится, смотрит на Барди
    label gallery_22199:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22197
    with fadelong
    w
    img 22198
    with diss
    w
    #sound Моника прикасается языком к киске Бетти
    sound lick3
    img 22199
    with diss
    w
    img 22200
    with diss
    betty "Когда весь этот цирк прекратится?!"
    img 22201
    with diss
    betty_t "Фу! Эта шлюха согласилась лизать меня ТАМ!"
    betty_t "Как же это противно, что она ко мне прикасается!"
    img 22202
    with fade
    bardie "Гувернантка, еще не все."
    bardie "Продолжай. Я еще думаю, простить тебя или нет..."
    #sound Моника прикасается языком к киске Бетти
    sound lick3
    img 22203
    with diss
    w
    music Loved_Up
    img 22204
    with diss
    betty_t "Как же это противно... М-м-м-мне совсем это не нравится... Мммм..."
    #sound Бетти произносит Аааааааххх
    sound ahhh1
    img 22205
    with diss
    betty "Ааааааххх..."
    # Бетти раздвигает ноги еще шире, сама смотрит на Барди
    img 22206
    with diss
    betty "Все, хватит, достаточно! Мне неприятно, что она трогает меня там-м-м..."
    #sound Моника лижет киску Бетти обычно
    sound lick10
    img 22207
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.66666667)) + " loop 0.0>Sounds/v_Monica_Betty_Licking_1_1.ogg"
    scene black
    image videov_Monica_Betty_Licking_1_1 = Movie(play="video/v_Monica_Betty_Licking_1_1.mkv", fps=30)
    show videov_Monica_Betty_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.66666667)) + " loop 0.0>Sounds/v_Monica_Betty_Licking_1_1.ogg"
    scene black
    image videov_Monica_Betty_Licking_1_2 = Movie(play="video/v_Monica_Betty_Licking_1_2.mkv", fps=30)
    show videov_Monica_Betty_Licking_1_2
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.66666667)) + " loop 0.0>Sounds/v_Monica_Betty_Licking_1_1.ogg"
    scene black
    image videov_Monica_Betty_Licking_1_3 = Movie(play="video/v_Monica_Betty_Licking_1_3.mkv", fps=30)
    show videov_Monica_Betty_Licking_1_3
    with fadelong
    wclean

    #sound Бетти произносит ММмммммм...
    sound woman_moan8a
    music Loved_Up
    img 22208
    with diss
    betty "Мммм..."
    # Бетти закрывает глаза и приподнимает свои ноги, раскрываясь полностью (см. позу)
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    #sound падает мяч
    img 22209 # падает мяч
    with fadelong
    sound ball3
    w
    #sound Бетти произносит Ммммммм в экстазе
    sound woman_moan6
    #sound Моника лижет сильно
    sound lick13
    img 22210
    with diss
    betty "Мммм..."
    img 22211
    with diss
    w
    img 22212
    with diss
    w
    img 22213
    with diss
    betty "Сколько я могу терпеть эту мерзость..."
    img 22214
    with diss
    betty "Мммм..."
    img 22215
    with diss
    w
    img 22216
    with diss
    betty "Я... Порядочная женщина..."
    img 22217
    with diss
    w
    img 22218
    with diss
    w
    img 22219
    with diss
    betty "Аааах, прикажи ей остановится... Оооо..."
    # в итоге Бетти кончает со стонами
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan7a
    img 22220
    with diss
    w
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan12
    img 22221
    with diss
    w
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan11
    img 22222
    with diss
    w
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan12
    img 22223
    with diss
    betty "Ты... Ты!... Ты...."
    #sound Бетти кончает
    sound woman_moan14
    img 22224
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "АААААААА!!!"
    #sound Бетти кончает
    sound woman_moan15
    img 22225
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "ААААА!!! АААААА!!!"
    # Моника отстраняется от нее, смотрит с отвращением на нее, потом на Барди вопросительно и зло
    # Барди с довольной ухмылкой
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    sound snd_bodyfall
    img 22226 #Бетти кончила
    with fadelong
    w
    img 22227
    with diss
    w
    img 22228
    with diss
    w
    img 22229
    with fade
    bardie "Достаточно, гувернантка."
    sound highheels_short_walk
    img 22230
    with diss
    bardie "Теперь хозяин доволен своей гувернанткой и она может идти."
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    # Барди поворачивается к Бетти, та после оргазма лежит на кровати
    music Groove2_85
    img 22231
    with fadelong
    bardie "Я вижу, что ты соблюдаешь правила этого дома. Ты тоже свободна на сегодня."
    img 22232
    with Dissolve(2.0)
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    music Mandeville
    return

############ College 1############

label gallery_14747:
    # Бетти садится напротив учителя, который сидит за учительским столом. Бетти с улыбкой
    music Groove2_85
    img 14735
    with fadelong
    w
    img 14741
    with diss
    w
    img 14742
    with fade
    w
    img 14736
    with diss
    w
    sound highheels_short_walk
    img 14743
    with fade
    w

    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14737
    with fadelong
    betty "Добрый день, мистер..."
    # учитель с серьезным лицом
    img 14738
    with diss
    teacher "...Эдвардс. Добрый день. Я так понимаю, вы - мать Барди?"
    img 14739
    with fade
    betty "Да, мистер Эдвардс. Барди сказал, что у него какие-то проблемы..."
    img 14740
    with diss
    teacher "У Барди серьезные проблемы с успеваемостью. У него много прогулов и много не сданных зачетов."
    teacher "Я неоднократно пытался проводить с ним разъяснительные беседы, но безуспешно."
    teacher "К сожалению, я вынужден вам сообщить, что я сейчас готовлю документы на отчисление Барди для передачи директору."
    img 14744
    with fade
    betty "Мистер Эдвардс, документы еще находятся у вас? Я могу их посмотреть?"
    img 14745
    with diss
    teacher "Да, конечно. Я вас пригласил сегодня именно для этого. Вот личный файл Барди, можете ознакомиться."
    # Учитель дает Бетти папку с документами, та их просматривает, сосредоточенно думая. Учитель в это время пялится на ее грудь
    img 14746
    with vpunch
    betty_t "Этот мелкий сопляк совсем не бывает в колледже!"
    betty_t "Если мне удастся уговорить учителя притормозить это дело, у меня появится отличная возможность приструнить его..."
    img 14747
    with diss
    w
    img 14748
    with diss
    betty_t "В противном случае, Барди мне вообще никакой жизни не даст. Я итак его уже видеть не могу."
    betty_t "Интересно, как мне уговорить этого мистера Эдвардса? Может, попросить денег у Ральфа? Скажу, что для колледжа..."
    # Бетти поднимает взгляд на учителя, тот продолжает пялиться на нее. Бетти уже без улыбки, с серьезным выражением лица
    img 14749
    with fade
    betty "Мистер Эдвардс, я вижу, что у Барди совсем все плохо с учебой. Этот сорванец и правда в последнее время совсем отбился от рук."
    betty "Возможно, мы с вами как-то сможем уладить этот вопрос? Я могла бы оказать спонсорскую помощь колледжу. Купить мел для доски, например."
    betty "Я обещаю, что поговорю с Барди. Этот сопл... Барди больше не будет прогуливать занятия и сдаст все зачеты."
    sound Jump2
    img 14750
    teacher "..."
    img 14751
    with fade
    betty "Мистер Эдвардс?"
    # учитель, наконец, отрывает взгляд от ее груди.
    img 14752
    with diss
    teacher "А? Что?"
    img 14753
    with fade
    betty "Я говорю, что готова поговорить с Барди и он будет себя хорошо вести..."
    img 14754
    with diss
    teacher "..."
    img 14755
    with fade
    teacher "Ну... Я даже не знаю... Документы уже подготовлены."
    teacher "Боюсь, что ничего уже нельзя изменить."
    # Барди подглядывает через приоткрытую дверь, переживает
    music Sneaky_Snitch
    img 14756
    with fade
    bardie_t "Черт!"
    bardie_t "..."
    bardie_t "Эта деревенщина не сможет договориться с преподом. Надо было гувернантку посылать к нему."
    # Бетти продолжает уговаривать учителя
    music Groove2_85
    img 14757
    with diss
    betty "Личный файл Барди все еще находится у вас. Значит, именно от вас зависит, дойдут ли документы до директора."
    betty "Что я могу сделать для того, чтобы Барди остался в колледже?"
    # препод снова залипает на груди Бетти, задумчиво
    img 14758
    with diss
    teacher "Хм. Я вижу, что вы искренне переживаете за сына, Миссис Робертс."
    # Бетти расплывается в улыбке
    img 14759
    with diss
    betty_t "Ненавижу этого сопляка!"
    img 14760
    with fade
    teacher "Возможно, я смогу что-нибудь придумать. Это будет непросто... Ведь, помимо меня, и другие учителя в курсе ситуации с Барди."
    teacher "Мне придется как-то аргументировать то, что я изменил свое решение..."
    img 14761
    with diss
    betty "Мистер Эдвардс, я понимаю, что это сложный процесс. Если я смогу чем-то вам помочь, то я буду только рада."
    # тут Бетти случайно роняет паку Барди на пол
    img 14762
    with vpunch
    #sound папка падает на пол
    sound down7
    betty "Oй!"
    img 14763
    with diss
    w
    # наклоняется за ней, поворачивает голову и видит, что учитель сидит с внушительным стояком
    img 14764
    with diss
    w
    sound Jump1
    img 14765
    with diss
    betty "!!!"
    # Бетти зависает на этом зрелище, но тут же берет себя в руки, выпрямляется. Глаза у нее заблестели, но она делает вид, что ничего не видела
    #video teacher dick up
    img black_screen
    with diss
    sound erection1
    scene black
    image videov_Teacher_Betty_DickUp_1 = Movie(play="video/v_Teacher_Betty_DickUp_1.mkv", fps=30, loop=False, image="/images/Slides/v_Teacher_Betty_DickUp_1_stop.jpg")
    show videov_Teacher_Betty_DickUp_1
#        with fadelong
    wclean

#       img 14766
#        with diss
    betty "..."

    music stop
    img black_screen
    with diss
    pause 2.0
    music Hidden_Agenda
    img 14767
    with fade
    betty "Так на чем мы остановились, мистер Эдвардс?.."
    # учитель догадался, что она его спалила, и принимает решение развести Бетти на "помощь"
    img 14768
    with diss
    teacher "На том, что вы могли бы мне помочь в этом непростом деле."
    # Бетти воодушевленно
    img 14769
    with fade
    betty "Да, конечно. Я буду рада помочь вам. Что мне нужно будет сделать?"
    img 14770
    with diss
    teacher "..."
    # учитель встает со стула, поправляет ширинку и пристально смотрит на Бетти. Бетти сидит на стуле и не может оторвать взгляд от его стояка, который прямо перед ее лицом
    music Loved_Up
    img 14771
    with fadelong
    w
    img 14772
    with diss
    betty "М-м-мистер Эд-д-двардс... Я н-не совсем вас п-п-понимаю..."
    img 14773
    with fade
    betty_t "Вот черт. Что же мне делать?"
    betty_t "Так, стоп! Я же замужняя женщина и верная жена."
    betty_t "Тем более, я разговариваю с учителем Барди! Я не должна так смотреть на то, что у него в штанах!"
    # Бетти поднимает взгляд от ширинки препода и смотрит ему в глаза. Говорит возмущенно
    label gallery_14785:
    music Groove2_85
    img 14774
    with fade
    betty "Мистер Эдвардс! Я замужем! Как вы можете предлагать мне подобное?!"
    img 14775
    with diss
    teacher "Вы же сами предложили мне помощь, миссис Робертс... Это очень помогло бы мне..."
    # Бетти снова уставилась на его стояк
    img 14776
    with diss
    teacher "Тем более, я не прошу о многом. Вы могли бы просто приласкать его рукой. У меня так давно не было никого."
    teacher "А вы такая красивая, миссис Робертс, что я просто не в силах держать себя в руках."
    # учитель медленно начинает расстегивать ремень
    sound snd_zip
    img 14777
    with fade
    betty_t "..."
    betty_t "Я не должна этого делать! Что вообще себе позволяет этот мистер Эдвардс?!"
    # учитель расстегивает молнию на брюках, Бетти не в силах отвести взгляд
    img 14781
    with diss
    betty_t "С другой стороны..."
    betty_t "Хм... Если я просто потрогаю его, это же не будет считаться изменой?"
    img 14782
    with fade
    betty "М-мистер Эд-двардс, если об этом кто-нибудь узнает..."
    img 14783
    with diss
    teacher "Миссис Робертс, это не в моих интересах, чтобы кто-либо узнал о нашей с вами договоренности."
    teacher "Я в виде исключения предлагаю вам единственный из всех возможных способов решить эту проблему с вашим сыном."
    teacher "Для этого вам достаточно просто протянуть руку..."
    # препод достает свой стояк
    music Loved_Up
    sound Jump1
    img 14784
    with diss
    teacher "... и немного погладить его."
    img 14785
    with diss
    betty "!!!"
    img 14786
    with diss
    menu:
        "Убежать.":
            music Groove2_85
            betty "Я не буду этого делать!!!"
            return
        "Постараться убедить учителя не делать этого":
            music Hidden_Agenda
            img 14787
            with fade
            betty "Мистер Эдвардс, я никогда себе не позволяю такого с другими мужчинами. Только с мужем..."
        "Поддаться давлению со стороны учителя":
            music Hidden_Agenda
            img 14788
            with fade
            betty "Мистер Эдвардс, я, конечно, не совсем уверена. Это единственный способ?"
            betty_t "У него просто каменный стояк. Если я к нему притронусь... Так интересно ощутить его."
    music Loved_Up
    img 14789
    with fade
    teacher "Это единственный способ, миссис Робертс. Просто прикоснитесь ко мне."
    # Бетти протягивает руку и замирает буквально в сантиметре от члена
    label gallery_14799:
    music Hidden_Agenda
    img 14790
    with diss
    betty_t "Что я делаю? Это так неправильно..."
    betty_t "Я просто потрогаю его и вопрос с Барди будет решен. Я делаю это не ради своего удовольствия!"
    # препод берет ее за запястье и притягивает ее руку к своему члену, Бетти прикасается к нему пальцами
    img 14791
    with diss
    w
    img 14792
    with diss
    betty_t "Ммм... Он и правда каменный. И такой горячий..."
    img 14793
    with fade
    betty "Мистер Эдвардс, я... мне... это так неправильно..."
    music Loved_Up
    img 14794
    with diss
    teacher "Вы уже делаете это, миссис Робертс. Еще совсем немного. Сожмите его своей ручкой."
    # препод убирает свою руку, Бетти обхватывает его член рукой
    img 14795
    with fade
    betty_t "Ооо! У этого мистера Эдвардса просто отличный член. Интересно, какой он на вкус?"
    betty_t "!!!"
    betty_t "О боже! О чем я думаю?!"
    # Бетти медленно начинает дрочить ему
    img 14796
    with diss
    sound drkanje5
    teacher "Да, так! У вас отлично получается, миссис Робертс! Быстрее!"
    # Бетти пристально смотрит на член и старается с удвоенной силой
    # Барди все видит и слышит. Волнение на его лице сменяется злорадной ухмылкой. Он достает свой смартфон и делает фото.
    music Sneaky_Snitch
    img 14797
    with fadelong
    bardie_t "Офигеть! Бетти даже в колледже умудрилась подержать чужой член в руке!"
    bardie_t "!!!"
    bardie_t "Может, будет какое-то продолжение?"

    # Бетти продолжает усердно работать рукой, не отрывая глаз от члена учителя
    img 14798
    with diss
    sound drkanje5
    w
    music Loved_Up2
    img 14799
    with fade
    sound drkanje5
    teacher "Ооо, миссис Робертс... Да, так! Еще..."
    teacher "Ммм... Еще быстрее!"
    #видео teacher_betty_handjob
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_1 = Movie(play="video/v_Teacher_Betty_HandJob_1_1.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_1
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
        scene black
        image videov_Teacher_Betty_HandJob_1_2 = Movie(play="video/v_Teacher_Betty_HandJob_1_2.mkv", fps=30)
        show videov_Teacher_Betty_HandJob_1_2
        wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_3 = Movie(play="video/v_Teacher_Betty_HandJob_1_3.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_4 = Movie(play="video/v_Teacher_Betty_HandJob_1_4.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_4
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
        scene black
        image videov_Teacher_Betty_HandJob_1_5 = Movie(play="video/v_Teacher_Betty_HandJob_1_5.mkv", fps=30)
        show videov_Teacher_Betty_HandJob_1_5
        wclean

    #препод со стоном кончает на личный файл Барди, который на столе, попадает и Бетти на руку
    stop music
    music stop
    music Loved_Up2
    sound bulk1
    img 14800
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "ООООООООО!!!"
    sound man_moan18
#    sound bulk1
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
    w

    # препод крайне доволен, надевает обратно брюки и садится за стол, а Бетти, изображая из себя оскорбленную невинность, вытирает руку

    # sound звук падающей спермы на папку (вввиухх...)
    sound hlup2
    music Groove2_85
    img 14801
    betty "Вы испачкали документы Барди, мистер Эдвардс."
    img 14802
    with fade
    teacher "Ничего страшного, миссис Робертс. Директор все равно этого не заметит."
    # Бетти в шоке, учитель с улыбочкой
    img 14803
    with diss
    betty "В смысле?! Мы же с вами договорились, что эти документы не дойдут до директора!"
    img 14804
    with fade
    teacher "Миссис Робертс, в моих силах пока только притормозить это дело."
    img 14805
    with diss
    betty "???"
    img 14807
    with fade
    teacher "Но если вы еще раз посетите меня на днях, то, возможно, я смогу закрыть этот вопрос."
    # Бетти удивленно
    img 14808
    betty "Еще раз?!"
    img 14809
    with diss
    teacher "Именно. Мне может снова потребоваться ваша помощь."
    # Барди злорадно ухмыляется за дверью
    music Sneaky_Snitch
    img 14806
    with fade
    bardie_t "!!!"
    bardie_t "Отлично! Нужно будет дождаться продолжения!"
    # Барди убегает, Бетти, сидя напротив учителя, пристально смотрит на него
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14810
    with fadelong
    betty_t "Из-за этого сопляка мне придется тащиться сюда снова. Он теперь в долгу передо мной. Нужно только окончательно уговорить учителя."
    img 14811
    with diss
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И, надеюсь, мы с вами закроем этот вопрос."
    img 14812
    with fade
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return

label gallery_14648:
    sound ball4
    # Барди снова делает вид, что не замечает ее. Бетти стоит, руки в боки и зовет его
    music Groove2_85
    img 14643
    with fadelong
    betty "Эй, ты! Иди сюда!"
    # Барди к ней подходит и, делая вид, что ничего не знает, вопросительно смотрит на нее
    # Барди держит мяч
    sound Jump1
    img 14644
    with fade
    bardie "???"
    bardie "Что?"
    # Бетти ему высокомерно
    img 14645
    with diss
    betty "Я договорилась с твоим преподавателем. Это было непросто, но я смогла его убедить не отчислять тебя из колледжа."
    betty "Он очень не хотел оставлять тебя. Мне пришлось три раза посетить его и, в итоге, я смогла его уговорить."
    # Барди продолжает молча смотреть на нее, но уже едва сдерживает улыбку
    img 14646
    with diss
    bardie "..."
    img 14647
    with fade
    betty "Я сделала то, о чем ты меня попросил. Но хочу сразу тебя предупредить, что я в любой момент могу позвонить мистеру Эдвардсу..."
    # Бетти с угрозой
    img 14648
    with diss
    betty "... и он выкинет твою задницу из колледжа!"
    betty "!!!"
    betty "Поэтому с этого дня ты перестаешь строить из себя здесь хозяина и командовать мною! Если будешь хорошо себя вести, то с твоей учебой все будет в порядке."
    # Бетти с торжествующей улыбкой на лице
    img 14649
    with fade
    betty_t "Вот ты и попался, мелкий сопляк! Попробуй теперь покомандовать в моем доме!"
    img 14650
    with diss
    bardie "..."
    # На это Барди, не выдерживая, злорадно хохочет
    img 14651
    with fade
    bardie "Аха-ха!!! Ты это серьезно сейчас?!"
    bardie "!!!"
    bardie "Жду тебя через пять минут в своей комнате! И не задерживайся!"
    bardie "Аха-ха!!!"
    # Барди уходит, Бетти в недоумении
    img 14652
    with diss
    betty_t "???"
    sound snd_runaway
    img 14653
    with fade
    betty_t "Что еще этому мерзкому мальчишке нужно от меня?"
    betty_t "Почему я, такая порядочная и умная женщина, должна терпеть такое в своем же доме?!"
    betty_t "!!!"
    betty_t "Он, наверное, не понял, что он больше здесь не хозяин. Хм, что ж... Пойду к нему, объясню ему еще раз, более доходчиво!"
    # Бетти с уверенным видом уходит
    sound highheels_run2
    img 14654
    with diss
    w
    return
