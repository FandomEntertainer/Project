default wukong_talking = False

default wukong_expression = "Happy" # Happy, Sad

# im.Scale("wukong placeholder.png", 730, 800)
image wukong placeholder base = "Wukong/wukong placeholder base.png"

image wukong mouth still = "Wukong/[wukong_expression]/[wukong_expression]_0000s_0000_mouth.png"

image wukong mouth talking:
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0000_mouth.png"
    0.2
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0001_mouth.png"
    0.3
    repeat

image wukong eyes:
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0002_eyes.png"
    choice:
        2.0
    choice:
        3.1
    choice:
        4.2
    choice:
        3.3
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0003_eyes.png"
    .23
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0002_eyes.png"
    .25
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0003_eyes.png"
    .33
    "Wukong/[wukong_expression]/[wukong_expression]_0000s_0002_eyes.png"
    .13
    repeat

image wukong = LiveComposite((730,800),
    (0,0), "Wukong/wukong placeholder base.png",
    (0,0), "wukong eyes",
    (0,0), ConditionSwitch(
        "wukong_talking", "wukong mouth talking",
        "True", "wukong mouth still"
    )
)
