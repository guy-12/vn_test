layeredimage augustina:

    always:
        "augustina_base"

    group outfit:

        attribute dress:
            "augustina_outfit_dress"

        attribute jeans:
            "augustina_outfit_jeans"

    group eyes:

        attribute open default:
            "augustina_eyes_open"
            default True

        attribute wink:
            "augustina_eyes_wink"

    group eyebrows:

        attribute normal default:
            "augustina_eyebrows_normal"

        attribute oneup:
            "augustina_eyebrows_oneup"

    group mouth:

        pos (100, 100)

        attribute smile default:
            "augustina_mouth_smile"

        attribute happy:
            "augustina_mouth_happy"

    if evil:
        "augustina_glasses_evil"
    else:
        "augustina_glasses"