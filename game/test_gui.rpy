label gui:

    default cherry_drag = True
    default cherry_list = []

    default lemon_drag = True
    default lemon_list = []

    default cake_loop = True

    init python:
        def drag_placed(drags, drop):
            if not drop:
                return

            store.draggable = drags[0].drag_name
            store.droppable = drop.drag_name
            store.cherry_drag = True

            return True
        def on_cherry_drag(drags, drop):
            if drop:
                store.cherry_drag = False
                drags[0].snap(160, 180, 0)
                store.cherry_list.append(drags[0])
                renpy.restart_interaction()
        def on_lemon_drag(drags, drop):
            if drop:
                store.lemon_drag = False
                drags[0].snap(160, 360, 0)
                store.lemon_list.append(drags[0])
                renpy.restart_interaction()

    screen drag_objects:
        draggroup:
            for c in cherry_list:
                drag:
                    drag_name c.drag_name
                    xpos c.x
                    ypos c.y
                    child "Cake/Toppings/single_cherry.png"
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
            for lem in lemon_list:
                drag:
                    drag_name lem.drag_name
                    xpos lem.x
                    ypos lem.y
                    child "Cake/Toppings/single_lemon.png"
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True

    screen drag_cake:
        imagebutton auto "Cake/Toppings/%s_cherry.png" action SetVariable("cherry_drag", True) xpos 0.125 ypos 0.25
        imagebutton auto "Cake/Toppings/%s_lemon.png" action SetVariable("lemon_drag", True) xpos 0.125 ypos 0.5
        textbutton "FINISH CAKE" action SetVariable("cake_loop", False)
        draggroup:
            drag:
                drag_name "Cake"
                xpos 0.25
                ypos 1
                child "Cake/Tiers/tier_3.png"
                draggable False
                droppable True
            if cherry_drag:
                drag:
                    drag_name "New Cherry"
                    child "Cake/Toppings/single_cherry.png"
                    xpos 0.125
                    ypos 0.25
                    draggable True
                    dragged on_cherry_drag
            if lemon_drag:
                drag:
                    drag_name "New Lemon"
                    child "Cake/Toppings/single_lemon.png"
                    xpos 0.125
                    ypos 0.5
                    draggable True
                    dragged on_lemon_drag

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
    show cake at center with moveinright
    "Pick tiers on cake."
    menu:
        "1":
            $ tiers = 1
        "2":
            $ tiers = 2
        "3":
            $ tiers = 3
    "Pick topping on cake."
    menu:
        "cherry":
            $ topping = "cherry"
        "lemon":
            $ topping = "lemon"
    "Here's the cake!"
    show cake at offscreenleft with moveoutleft

    $ tiers = 3
    $ topping = False

    "Drag and Drop!"

    window hide dissolve
    show screen drag_cake

    label cake_create:
        if cake_loop:
            show screen drag_objects
            pause
            hide screen drag_objects
            jump cake_create
    hide screen drag_cake

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
