label name:

    "What's your name?"

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Player")
    if name =="":
            "Please enter a name."

    "[name], is this correct?"

    menu:

        "Yes":
            $ renpy.notify ("You have a name!")
            "Wonderful!"
            jump pronouns

        "No":

            "That's alright!?"
            jump name


label pronouns:

    "What are your pronouns?"

    menu:

        "She/Her":

            "She/Her {p}Is this correct?"
            menu:
                "Yes":

                    "Great!"
                    jump start_girl

                "No":
                    "Alright, that's okay!"
                    jump pronouns

        "They/Them":

            "They/Them. {p}Is this correct?"
            menu:
                "Yes":

                    "Great!"
                    jump start_game

                "No":
                    "Alright, that's okay!"
                    jump pronouns

        "He/Him":

            "He/Him {p}Is this correct?"
            menu:
                "Yes":

                    "Great!"
                    jump start_male

                "No":
                    "Alright, that's okay!"
                    jump pronouns

label start_game:

    show wukong placeholder at slightleft with move
    show mk placeholder at right with moveinright
    show redson placeholder at farleft with moveinleft
    swk "You chose They/Them Pronouns."
    swk "Hello, [name]!"
    pause
    return

label start_girl:

    show wukong placeholder at farleft with move
    show mei placeholder at center with moveinright
    show mk placeholder at farright with moveinright
    mei "You chose She/Her Pronouns."
    pause
    return

label start_male:

    show wukong placeholder at center:
        xoffset -300           #value can be decreased to push the character further off the screen to the left
        easein 0.5 xoffset 0

    show macaque placeholder at right:
        xoffset 200             #value can be increased to push the character further off the screen to the right
        easein 0.5 xoffset 0

    #the rest of this code is sort of optional
    with Pause(0.2)

    show wukong placeholder at farleft with move:
        xoffset 0
    show macaque placeholder at center with moveinright:
        xoffset 0
    with None

    show tang placeholder at farrightmac with moveinright

    mac "You chose He/Him Pronouns."
    pause
    return
