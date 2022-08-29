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
    show redson placeholder with dissolve
    a "You incompetent peasant! How dare you bump into me! Do you know who I am?"
    "Um, not really"
    "The young man is shocked, but his previous scowl returns as he lets out a frustrated yell before stomping away."
    hide redson placeholder at offscreenleft with easeoutleft
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
    show pigsy placeholder at center with dissolve
    pig "Fyuree? Is that you?"
    "You nod."
    pig "It's been a while, huh? It's good to see you. So, what are you doing here?"
    fp "I'm here to judge the cooking competition for the Qixi Festival."
    a "You're a judge for the cooking competition?"
    show pigsy placeholder at center:
        xoffset -18      #value can be decreased to push the character further off the screen to the left
        easein 0.9 xoffset 0

    show tang placeholder at right:
        xoffset 200           #value can be increased to push the character further off the screen to the right
        easein 0.5 xoffset 0

    #the rest of this code is sort of optional
    with Pause(0.2)

    show pigsy placeholder at left with move:
        xoffset 0
    show tang placeholder at right with moveinright:
        xoffset 0
    with None
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
    hide pigsy placeholder
    hide tang placeholder
    with dissolve
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

######## ONE #########

    "You look down at your watch and realize that the cooking competition is about to start in fifteen minutes."
    "It's been great seeing you again, Pigsy, but I've gotta. The competition will be starting soon!"
    show tang placeholder at right
    show pigsy placeholder at left
    with dissolve
    tang "If you're feeling nervous, I could take your place as a judge."
    fp "Um... I'm good."
    pig "Leave her alone ya, freeloader."
    "You run out of the shop, hoping you'll make it to the competition on time."

######## TWO #######

    "An alarm goes off on your phone. Taking out your phone, you gasp at the time."
    fp "Oh shoot! I'm going to be late. Sorry Pigsy, let's catch up after the competition. Dinner's on me."
    pig "Looking foward to it. Good luck!"
    "Waving goodbye to Pigsy and Tang, you leave the noodle shop and head out to the competition site."
    hide tang placeholder
    hide pigsy placeholder
    with dissolve

######### SCENE 2.5 AND THREE #########

    "Outside of Pigsy's noodle shop, you notice a young woman playing an arcade machine."
    show mei placeholder at center with dissolve
    "{i}Monkey Mech, huh? That's new.{/i}"
    "As much as you want to ask about it, you decide to keep your sights set on reaching the stadium."
    hide mei with dissolve
    "So much had changed since the last time you were home. So much to the point that you hardly recognize it anymore."
    "While the streets looked the same, there was a distinct in the city's once carefree ambiance."
    "You've heard of the countless battles that have occured in Megapolis, and wondered how it affected your friends and family."
    "However, it wasn't the time to dwell on the past. Today was the Qixi Festival. A celebration of love and friendships."
    "An event the city had been looking foward to for months, and you were going to be apart of it."
    "Distracted by thoughts, you accidentally bump into someone in the street."
    $ quick_menu = False
    scene temp with hpunch
    $ quick_menu = True
    fp "Oh, sorry. I didn't see you there."
    show wukong placeholder with dissolve
    "The stranger mumbles something under his breath."
    fp "Right... sorry again."
    hide wukong placeholder with dissolve
    "You continue towards the stadium."

######## SCENE FOUR ##########

    "You ran, and looked for a shortcut. You looked to your left as you spotted an alleyway."
    "Something about it with it being around stores you vaguely remember going to, so you went toward that direction."
    "It wasn’t the best time to take a rest, but you could hear your heartbeat thumping in your ears."
    "You bent down in a half-crouch, and rested my hands on your knees, breathing slowly."
    "You're not going to get there on time at this rate.{w} Ugh."
    "You raised your head. Standing not too far away from you was a figure, wearing a red robe with their face cast in shadow."
    "You weren't sure if he saw you or not, but moments after, you spotted a portal the color of poison from behind him and they melted into it."
    fp "What the heck was that?"
    "The whole ordeal came and went quick, and it left an impression, but you pushed it to the back of your mind."
    "You will have enough time to think about that weird thing tomorrow."
    "It turns out, your hunch was right about the alleyway being a shortcut as you spotted the booths to sign up for the competition. You sighed in relief."
    "After this, you don't want to run for the rest of the Qixi Festival."
    "You reach the stadium where the food contest is and breathe a sigh of relief. Just in time!"
    "You look around and spot someone with a badge. They can probably tell you where to go. You walk over to the person."
    fp "Hi, I'm here to-"
    show placeholder at center with dissolve
    st "Oh my gosh, it's you! Fyruee Pashé! I'm a huge fan!"
    fp "Thanks. So where do I-"
    st "Oh, right, yes. Follow me!"
    show placeholder at offscreenright with moveoutleft
    "The person with the badge heads into the stadium and you follow them. Assuming they were taking you to the judges table."
    show placeholder at offscreenleft
    show placeholder at center with moveinright
    "You are surprised when they stop in front of a baking station."
    st "Here’s your station! Good luck! Knowing you, you’re totally going to win!"
    "The person with the badge smiles at you, then starts to walk away."
    hide placeholder at offscreenleft with easeoutleft
    fp "Wait, what do you mean my station?"
    "The person doesn’t hear you and keeps walking."
    "What did they mean by your station? You were a judge, not a contestant."
    "You hear the speakers crackle to life as a voice booms through out the stadium."
    an "{b}{u}Welcome everyone to Qixi festival’s cooking contest! We have our three judges, and now let’s meet them!{/b}{/u}"
    "How could they have all the judges? You weren’t there."
    "You rush up to the baking station to get a better view and see that there are three judges."
    an "{b}{u}Our first judge used to run a spicy barbeque food stand known as Dine or Die. Give it up for Red Son!{/b}{/u}"
    show redson placeholder at farleft with dissolve
    "You looked up at the judges table and recognized the guy you had bumped into outside Pigsy’s shop."
    "Hadn’t he called you a peasant?"
    an "{b}{u}Our next judge has some previous judging experience in competitions such as the highly acclaimed Food Wars!{/b}{/u}"
    an "{b}{u}Let’s welcome Princess Iron Fan!{/b}{/u}"
    show placeholder at center with dissolve
    "A judge for Food Wars?{w=0.3} Impressive."
    an "{b}{u}And as a last minute special request, our final judge is none other than the Monkey King!{/b}{/u}"
    "Last minute? This must be the person who replaced you. As you get a better look at the Monkey King you suddenly realize it’s just a cardboard cutout. You were replaced with a cardboard cutout?"
    show placeholder at farright with dissolve
    "Obviously, something got mixed up. Wait, so if you weren’t a judge, and the person with the badge had taken you to a baking station, were you actually one of the contestentants?"
    "Well, good thing you actually knew how to cook then. If you were going to be a contestant, you were going to do your best to win."
    hide redson placeholder
    hide placeholder
    with dissolve
    an "{b}{u}And let the contest begin in three, two, one, go!{/b}{/u}"
    "What to make? You examine the ingredients, and an idea pops into your head. You immediately get to work, rushing around measuring ingredients and combining them."
    "You tune out everything except your baking, and the next thing you know, it’s done. You stand back with a sigh of satisfaction, looking at the final result."
####"You take in your {flavor of cake} with {number of tiers} covered in {frosting flavor} with its {specific} decorations and a {cake topper of their choosing} to top it off.
    "A gong sound resounds as the time ends. Looks like you finished just in time."
####### PART TWO ########


    show redson placeholder at farleft
    show placeholder at center
    show placeholder at farright
    with dissolve
    "You watch as the judges try some of your cake. You feel somewhat nervous, but confident at the same time."
    "The judges take their time deciding, but eventually each of them vote for your cake to win first place. Your face, along with a picture of your cake, is projected on various screens around the stadium."
    an "{b}{u}Time to celebrate with some food!{/b}{/u}"
    hide redson placeholder
    hide placeholder
    with dissolve
    "That’s when you notice that the stadium is lined with food stalls. You must have been so in the zone that you missed them earlier."
    "People from the stands begin to flood down to the stalls. You look at all the stalls and spot one of your favorites."
    "You start to head towards it, but are suddenly stopped when the person with a badge from before steps in front of you."
    show placeholder at center with dissolve
    st "As the winner of the competition, you can get free food from any of the stalls."
    "They hold out a ticket to you."
    st "Just show them this."
    "You take the ticket and look at it."
    fp "Cool."
    "You pause as an idea pops into your head."
    fp "Wait, I have a question. Can I give the ticket back and in exchange everyone else here can get one free fruit from my favorite fruit stall?"
    st "I’m sure that could be arranged."
    "You hand the ticket back to the staff member, who walks off."
    hide placeholder at offscreenright with moveoutright
######### PART THREE #############

    "You stand at your station, unsure of what to do next. A few seconds later the speakers crackle to life."
    an "{b}{u}Attention everyone.{/b}{/u}"
    "{b}{u}The contest winner Fyuree Pashé has used her winnings to allow each person here to get one order at the (fruit stall name).{/b}{/u}"
    "The crowd immediately congregates at the fruit stand, and you smile as you watch them all get some fruit from the stand. They bite into the fruit, then look up, seeming somewhat dazed."
    "Their eyes focus on the giant screens that are still showing your face along with your cake. They all drop the fruit, and you raise an eyebrow in confusion."
    "Why would they waste the fruit after just one bite? They start looking around, their gazes quickly settling on you."
    "You couldn’t put your finger on what it was exactly, but something about the way they were looking at you made you feel uncomfortable."
    "That uncomfortable feeling turns into straight up fear when they all suddenly rush towards you. You start running, wondering what was going on."
    "You hear voices from the crowd overlapping each other, but you can make out some of what they’re saying. You hear them begging you to stop running, that they love you.{w=0.3} What?"
    fp "Leave me alone! I don’t like you!"
    "The people keep chasing you though. You run through some alleys and manage to lose them. Why were they chasing you? And why were they saying they loved you?"
    "You needed answers. You hesitantly peek your head out of the alley, determined to find answers, but also to avoid that crazy crowd. The coast looked clear, so you begin to head out."

    "What route?"
    $ quick_menu = False

    menu:
        "MK Route":
            jump mk_route

        "Mei Route":
            jump mei_route

        "Monkey King Route":
            jump swk_route






    pause
    return
