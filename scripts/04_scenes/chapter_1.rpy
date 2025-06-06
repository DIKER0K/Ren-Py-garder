# Первая глава

label chapter_1:
    scene road

    show baker_idle

    menu optional_name:
        "Выбери"
        "да":
            $ points["baker"] += 5
            baker "Кайф"
        "нет":
            baker "Не кайф"

    if points["baker"] >= 4:
        baker "Больше или равно 4 очков"
    
    else: 
        baker "Меньше 4 очков"

    return

        