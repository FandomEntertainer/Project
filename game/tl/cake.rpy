default tiers = 0 # betw 1-3

default topping = False # cherry. lemon

image cake = LiveComposite((730,800),
    (0,0), "Cake/Tiers/tier_[tiers].png",
    (0,0), ConditionSwitch(
        "topping", "Cake/Toppings/[topping]_[tiers].png",
        "True", "Cake/Toppings/none.png"
    )
)
