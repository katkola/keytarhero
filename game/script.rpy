
define e = DynamicCharacter("hero_name")
define hero_name = "Heroine"

image eidel:
    "eidel.png"

define k = DynamicCharacter("keytar_name")
define keytar_name = "???"

image keytar:
    "goldmarblekeytar.png"
    zoom 0.45
    pos (300,.8)

image home:
    "home.png"
    xsize 1.0
    ysize 1.0

label start:

    scene home


    show eidel
# a half-giant women wearing a flouncy rennaissance shit and wide-legged capris
# her hair flows effortlessly in the wind
# a strong frame and jaw, but gentle eyes and smile
    e "Man... I cant find anywhere to practice my lyre"

    e "My family is practicing battles cries...I should go to the woods. Nothing but druids and acorns out there."
# family is barbarians, fighters, paladins training bombastically
    e "Perfect, now I can--"

    show keytar with moveinright
    show eidel at right with move
    k "HELLO!"

    e "GOOD HEAVENS!"

    k "So sorry to bother you, I thought I sensed a bard."

    e "Well, I... You sensed right! Talking instrument, How do you do?"

    k "Oh- my apologies! Bard! I have been waiting for one musically inclined as yourself for a quest?"

    e "A jam fest quest?"

    k "a ROCKIN squacking jam fest quest"

    e "A Jam Band rocking squacking jam bam thank you Ma'aM fest quest??"

    k "...a quest, yes"

    k "...you down?"

    e "Please, tell me about this quest, arane twang"

    k "Aight, hear me out. You, me: Adventure. Should you accept, we shall mount an expendition."

    k "We will edure a harrowing route to reach the crucible of my power, the ancient workshop that crafted me."

    e "Home for the holidays, I dig. I'm kinda busy though..."

    k "Aha! But a bard worth their salt must see venture first hand to inspire their work!"

    e "..."

    k "...Also, if you accompany me, you will prove yourself worth to me my weilder."

    k "Once I return to the place of my first awaking, I will regain my full power! And you will became AN ARTIST OF THE HEIGHEST REGARD"

    e "How exciting! Forgive me, what manner of instrument are you? What shall I call you?"

    $ keytar_name = "Great Magical Keytar"
    k "I am the epic combination of melodies, the flying ebonies, the twinkliest ivories. MELODY OF THE STARS- I AM THE GREAT KEYTAR!!"
# change name to "Great Magical Keytar"
    e "nice"

    k "And you, good Bard. How are you called?"

    $ hero_name = "Eidel"
    e "Eidel"
#change name to Eidel
    k "Well then, Eidel! Let us awwaaaaaaaaay~"

label chp_one:
#transition to town, keytar is about to give specifics
    scene bg town



    return
