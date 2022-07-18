label test:

    "Choose one?"
    menu:
        "Sun Wukong":

            "You chose Sun Wukong"
            jump wukong_test


        "Six-Eared Macaque":

            show wukong placeholder at offscreenleft with moveoutleft
            show macaque placeholder at center with moveinright
            "You chose the Six-Eared Macaque"
            jump macaque_test


label wukong_test:

    "This is to test the trust points."
    "Choose an option"
    menu:

        "Trust":
            $ Wukong_Trust += 5
            $ renpy.notify ("Trust with Wukong  +5")
            jump wukong

        "Don't Trust":
            "Nothing happened"
            jump wukong


label macaque_test:

    "This is to test the trust points."
    "Choose an option"
    menu:

        "Trust":
            $ Macaque_Trust += 5
            $ renpy.notify ("Trust with Macaque  +5")
            jump macaque

        "Don't Trust":
            "Nothing happened"
            jump macaque



label wukong:
    if Wukong_Trust > 4:
        jump wukong_good
    else:
        jump wukong_bad


label macaque:

    if Macaque_Trust > 4:
        jump mac_good
    else:
        jump mac_bad

label wukong_good:
    "Sun Wukong trusts you!"
    pause
    return

label wukong_bad:
    "Sun Wukong does not trust you."
    pause
    return


label mac_good:
    "The Six-Eared Macaque trusts you."
    pause
    return


label mac_bad:
    "The Six-Eared Macaque does not trust you."
    pause
    return
