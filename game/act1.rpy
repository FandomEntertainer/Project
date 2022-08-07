label act_one:

    $ quick_menu = False
    scene temp
    with fade
    $ quick_menu = True

##### SCENE ONE #####

    "{i}Ah, Megapolis, my home town!{/i}"
    "{i}And what a great day to come back for a visit too!{/i}"
    "You take a deep breath as you walk down the street that's decorated from top to bottom with lanterns and hearts."
    "Truly a sight to behold!"
    "{i}I should probably start making my way to the stadium{/i}"
    "Coming back to your hometown was quite the addition to what you were there to do."
    "What were you there to do?"
    "Why to judge the Annual Qixi Cooking Competition of course!"
    "An old friend of yours had told you not only about the competition, but also about the wonderful festival that surrounded the competition!"
    "And, as the renowned food critic, Fyuree Pashé, it was your job to participate in cooking competitions as a judge."
    "So, that was exactly what you were here to do! Who knew that you would one day judge a competition that would bring you back to your hometown!"
    "You continue your walk to the stadium, a smile on your face as you reminisce on the days you used to walk these same streets when you were younger."
    "Though your thoughts are cut short when you feel a soft collision"
    $ quick_menu = False
    scene temp with hpunch
    pause
    "..."
    $ quick_menu = True
    a "And who do you think you are?"
    "You stare at the person in front of you."
    a "You incompetent peasant! How dare you bump into me! Do you know who I am?"
    "Um, not really"
    "The young man is shocked, but his previous scowl returns as he lets out a frustrated yell before stomping away."
    "{i}What a peculiar man.{/i}"
    "Though the sudden, and quite frankly, weird interaction with the fiery young man had stunned you a bit."
    "A smile grew on your face as you noticed a quaint noodle shop nearby."
    "Pigsy's Noodle Shop, a shop you knew all too well."
    "{i}Maybe I can take some time to catch up with an old friend.{/i}"
    "You take a step towards the shop and take a deep breath before going inside."

    ##### SCENE TWO #####

    "You walk into Pigsy’s Noodle Shop and breathe in the smell of delicious noodles. You spot Pigsy behind the counter and walk over to him."
    fp "Hi Pigsy!"
    "Pigsy looks up from his noodles and notices you."
    pig "Fyuree? Is that you?"
    "You nod."
    pig "It's been a while, huh? It's good to see you. So, what are you doing here?"
    fp "I'm here to judge the cooking competition for the Qixi Festival."
    a "You're a judge for the cooking competition?"
    "You turn and realize there is someone sitting at the counter, a bowl of noodles in front of them."
    "The person is staring at you with look that's somewhere between intrigue and judgement."
    fp "Yeah."
    a "I wonder what made you special enough to be a judge. I applied, but they wouldn't let me."
    fp "Well, I am {b}the{/b} renowned food critic, Fyuree Pashé, after all!"
    a "Oh, really? Well, I'm a food critic too! Have you heard of 'Golden Cicada Yum Yum'?"
    fp "Um... no"
    "The person starts slurping their noodles in an annoyed fashion. Were you supposed to know someone named, Golden Cidada Yum Yum?"
    pig "Tang, you still only have one follower.{w} Yourself."
    pig "Don't be upset Fyuree doesn't know who you are."
    "Okay, so you weren't supposed to know someone named Golden Cicada Yum Yum{w}... You  think."
    show mk neutral at center with moveinleft
    "You look away and notice a young man listening to music on a pair of headphones dance his way into the store."
    "Pigsy's attention immediately shifts to the young man."
    pig "MK! There you are. I've got some more orders for you to take out."
    mk "Alright, Pigsy!"
    "MK walks over to the counter to pick up the noodles and accidentally bumps into you as he wasn't paying that much attention to his surroundings."
    mk "Oh, sorry!"
    fp "It's okay. So, you do deliveries for Pigsy?"
    mk "Yeah!"
    "You really had been gone for a while. You wonder if Pigsy had any other new staff you haven't met."
    mk "Who are you?"
    fp "I'm Fyuree Pashé. I'm in town for the Qixi Festival."
    mk "Oh, cool! Festivals are so much fun! What's your favorite part?"
    fp "That would probably have to be the cooking competition, since I am one of the judges!"
    mk "You're a judge? That's so cool! I can't wait to see that!"
    pig "Yeah? Well, if you want to see that you  better finish these deliveries first."
    mk "Right boss!"
    hide mk at offscreenleft with moveoutleft
    "MK rushes out of the store with the noodles. Pigsy sure does run a tight ship. It looks like some things never change."
    "You look down at your watch and realize that the cooking competition is about to start in fifteen minutes."
    "It's been great seeing you again, Pigsy, but I've gotta. The competition will be starting soon!"
    tang "If you're feeling nervous, I could take your place as a judge."
    fp "Um... I'm good."
    pig "Leave her alone ya, freeloader."
    "You run out of the shop, hoping you'll make it to the competition on time."


    pause
    return
