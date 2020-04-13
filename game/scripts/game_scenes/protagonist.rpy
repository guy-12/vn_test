define protagonistName = "Anon"
define protagonist = Character(protagonistName, what_style="protagonist_thoughts")


default hasNotReadCrimeAndPunishment = True
default hasNotReadHunger = True
default hasNotReadLayeredImagesExample = True


label start:

    scene bg room

    protagonist """
        Another day in quarantine...

        It's been a month since this started, the days have been dragging on longer and longer each day
    """
    protagonist "*sigh*" (what_style="protagonist_speech")
    protagonist "I guess I could read a book..."

    jump choose_book


label choose_book:

    scene bg room

    menu:
        "what book should I read?"

        "Hunger - Knut Hamsun" if hasNotReadHunger:
            protagonist "I decide to read a passage from Hunger"
            jump hunger

        "Crime and Punishment - Fyodor Dostoevsky" if hasNotReadCrimeAndPunishment:
            jump crime_and_punishment


        "Layered Images Examples - Guy" if hasNotReadLayeredImagesExample:
            jump layered_images_example



label finished_book:
    scene bg room

    if hasNotReadHunger or hasNotReadCrimeAndPunishment:
        "You finish there and decide to read another book"
        jump choose_book
    else:
        jump end


label end:
    scene bg room

    protagonist "You decide to call it a day and end there..."
    return