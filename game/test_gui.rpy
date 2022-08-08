label gui:

    scene temporary
    show wukong
    "This is Sun Wukong"
    $ wukong_talking = True
    swk "Hello"
    swk "How you doing"
    $ wukong_expression = "Sad"
    swk "I'm doing terrible... The absolute WORST..."
    show wukong placeholder at offscreenleft with moveoutleft
    show mk placeholder at center with moveinright
    mk "..."
    show mk placeholder at offscreenleft with moveoutleft
    show mei placeholder at center with moveinright
    mei "..."
    show mei placeholder at offscreenleft with moveoutleft
    show redson placeholder at center with moveinright
    rs "..."
    show redson placeholder at offscreenleft with moveoutleft
    show macaque placeholder at center with moveinright
    mac "..."
    show macaque placeholder at offscreenleft with moveoutleft
    show tang placeholder at center with moveinright
    tang "..."
    pause
    return
