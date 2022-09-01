# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define swk = Character("Sun Wukong")
define u = Character("[name]")
define fp = Character("Fyuree Pashé")
define ma = Character("Ai Mishaekho")
define mac = Character("Macaque")
define mk = Character("MK")
define mei = Character("Mei")
define rs = Character("Red Son")
define tang = Character("Tang")
define a = Character("???")
define pig = Character("Pigsy")

#Colors for Character names

define swk = Character("Sun Wukong", color ="#fcfcfc",who_outlines=[(absolute(3),"#fca503",absolute(0),absolute(0))])
define u = Character("[name]", color ="#fcfcfc",who_outlines=[(absolute(3),"#000000",absolute(0),absolute(0))])
define fp = Character("Fyuree Pashé", color ="#fcfcfc",who_outlines=[(absolute(3),"#000000",absolute(0),absolute(0))])
define ma = Character("Ai Mishaekho", color ="#fcfcfc",who_outlines=[(absolute(3),"#e319b7",absolute(0),absolute(0))])
define mac = Character("Macaque", color ="#fcfcfc",who_outlines=[(absolute(3),"#6f048c",absolute(0),absolute(0))])
define mk = Character("MK", color ="#fcfcfc",who_outlines=[(absolute(3),"#d1870f",absolute(0),absolute(0))])
define mei = Character("Mei", color ="#fcfcfc",who_outlines=[(absolute(3),"#29c910",absolute(0),absolute(0))])
define rs = Character("Red Son", color ="#fcfcfc",who_outlines=[(absolute(3),"#f00905",absolute(0),absolute(0))])
define tang = Character("Tang", color ="#fcfcfc",who_outlines=[(absolute(3),"#e3d509",absolute(0),absolute(0))])
define a = Character("???", color ="#fcfcfc",who_outlines=[(absolute(3),"#000000",absolute(0),absolute(0))])
define pig = Character("Pigsy", color ="#fcfcfc")

# Positions for the spritesS

transform slightleft:
    xalign 0.25
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

transform left:
    xalign 0.0
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform farleft:
    xalign -0.30
    yalign 1.0

transform farrightmac:
    xalign 1.2
    yalign 1.0

transform farright:
    xalign 1.1
    yalign 1.0

transform offscreenleft:
    xalign -1.5
    yalign 1.0

transform offscreenright:
    xalign 1.5
    yalign 1.0

#Random Transitions

init:
    $ eyeopen = ImageDissolve("eyeopen.png", 1.5, 100)
    $ eyeclose = ImageDissolve("black.jpg", 1.5, 100, reverse=True)

    define fade = Fade(2.0, 0.0, 2.0)



##### Don't know what to call these ######

init python:
    hpunch = Move((5, 0), (-5, 0), .10, bounce=True, repeat=True, delay=.275)


# Music for the game goes here:



#Important codes to reuse


### For points

# $ Point_System += 5
# $ renpy.notify ("Message  +5")

###Else if Statement

# if Macaque_Trust > 4:
#jump mac_good
#else:
#jump mac_bad



#Character sizes

image mk placeholder = im.Scale("mk placeholder.png", 530, 630)

image macaque placeholder = im.Scale("macaque placeholder.png", 700, 660)

image wukong placeholder = im.Scale("wukong placeholder.png", 730, 800)

image mei placeholder = im.Scale("mei placeholder.png", 750, 780)

image temporary = im.Scale("temporary.jpg", 1300, 800)

image temporary = im.Scale("temporary.jpg", 1300, 800)



### Here are the points that will be included in the game

# With enough trust points, love interest will take off their glamour

define Wukong_Trust = 0
define Macaque_Trust = 0

#Random things




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show wukong placeholder at center

    # These display lines of dialogue.





    menu:

        "Demo":
            jump actual_game

###        "Test":
###            jump test

###        "Name":
###            jump name

###            jump actual_game

        "Test GUI":
           jump gui

label actual_game:

    $ quick_menu = False
    show temporary
    with fade
    $ quick_menu = True
    "Long ago, seven goddesses blessed the skies with beautiful woven clouds. They were known as the weaver maids."
    "One day, the Emperor of the Heavens allowed the sisters to bathe in a sacred pool on Earth. The maids enjoyed the cool waters and alluring scenery."
    "As the night drew near, the sisters gathered their clothes and headed back to Heaven."
    "However,{w} they had not realized the eldest sister was left behind, searching for her clothes."
    "A handsome cowherd was walking nearby, was his ox, and found the silk robe, blown away by the wind."
    "He looked around to find the owner and noticed a maid searching by a pool."
    "The cowherd handed the clothes back to the maid. She thanked him and returned to Heaven."
    "Over time,{w} the weaver maid watched over the cowherd with admiration. She decided to visit him and the two fell in love."
    "They were soon married and had two children, a boy and a girl."
    "The Empress of the Heavens found out about her daughter's marriage and was enraged."
    "It was strictly forbidden for a goddess to fall in love with a mortal."
    "She sent troops to retrieve her daughter while she was home alone."
    "Upon his return, the cowherd wept. His trusty ox told him what had happened and offered his hide for the cowherd to use to go after his wife."
    "The cowherd took the ox's hide and traveled to Heaven with his two children."
    "Noticing the mortal's speed, the Empress took her jade pin and used it to draw a river between them."
    "The lovers would forever be seperated from one another."
    "The family's cries were heard by magpies, who took pity on them. They flew up into the Heavens and began to form a bridge."
    "Moved by the starcrossed lovers, the Empress allowed the family to be reunited once a year."
    "In honor of the lovers, we celebrate their reunion during the Qixi Festival."
    a "No one should be kept from someone they love!"
    jump act_one


    pause
    return



    pause
    return


    # This ends the game.

    return
