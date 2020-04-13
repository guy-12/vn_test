# define augustina = Character("Augustina")

label layered_images_example:

    scene bg dressing room

    "This is a test to see how layered images can be used in RenPy"

    show augustina_base

    "You are now looking at the image 'augustina_base.png'"

    hide augustina_base



    show augustina

    "You are now looking at the 'augustina' layeredimage"
    "This has two additional images upon 'augustina_base.png'"
    "These images are 'augustina_eyes_open.png' and 'augustina_eyesbrows_one_raised.png'"

    "We can also change these images separately"

    show augustina wink

    "Augustina is now winking!"


    show augustina one_raised

    "Now she has one eye brow raised"


    show augustina open

    "Her eyes are open again but the eyebrow stays up"


    "That all for layered images for now!"

    $ hasNotReadLayeredImagesExample = False
    jump finished_book