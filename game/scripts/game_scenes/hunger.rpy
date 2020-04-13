define ylajaliName = "????"

define hungerProtagonist = Character("Narrator", what_prefix="\"", what_suffix="\"", what_style="hunger_protagonist", image="hunger_narrator")
define ylajali = Character("ylajaliName", dynamic=True, what_prefix="\"", what_suffix="\"", what_style="hunger_ylajali", image="ylajali")
define hungerNarration = Character(what_style="hunger_narration")


label hunger:

    scene bg hunger street
    with fade

    show hunger_narrator bored at center

    ylajali "Hmm!"
    hungerNarration """
        the noise came from behind me.

        I heard this sounds, and I also heard light footsteps nearby;
        but I didn't turn round, only stared up at the tall flight of steps before me.
    """

    ylajali "Good evening!"

    show ylajali tired at left

    hungerNarration "I forgot to smile, I didn't even tip my hat right away, being greatly surprised to see her coming from that direction."

    show hunger_narrator surprised at right
    $ ylajaliName = "Woman"

    show hunger_narrator neutral at right
    show ylajali neutral at left
    ylajali "Have you been waiting long? {=hunger_narration} She was breathing rapidly after her walk."
    hungerProtagonist "No, not at all, I only came a short while ago"
    hungerProtagonist "Besides, what would it matter if I had waited long? By the way I thought you would be coming from another direction"
    ylajali "I took Mama to see some friends - Mama will be away this evening"
    hungerProtagonist "Is that so!"
    hungerNarration "We had started walking now. A policeman stands on the corner looking at us"
    ylajali "Where are we actually going?"
    hungerProtagonist "Wherever you want, just where you want"
    ylajali "Oh dear. But it's such a bore to decide that yourself"
    hungerProtagonist "..."
    hungerProtagonist "Your windows are dark, I see"
    ylajali @ excited "Yes! {=hunger_narration} she answers vivaciously"
    ylajali "The maid is off this evening, too. So I'm home all alone."
    hungerProtagonist @ nervous """
        Can we go up to your place then?

        I'll sit by the door the whole time if you want me to...
        """
    hungerNarration "I was now trembling with emotion and feeling very sorry I had been so brash. What if she became offended and walked away?"
    ylajali "You certainly won't sit by the door"


    hungerNarration "We went up."
    scene bg hunger hallway

    hungerNarration "In the hallway where it was dark, she took my hand and led me on. I didn't have to be so quiet, she said, I could very well talk."

    scene bg hunger womans room
    hungerNarration "We went in."

    ylajali "But now you mustn't look at me. Oh, I'm so ashamed! But I'll never do it again"
    hungerProtagonist "What won't you ever do again?"
    ylajali "I'll never... oh, dear, God forbid... I'll never kiss you again"
    hungerProtagonist "You won't?"

    hungerNarration """
     We both laughed

     I stretched out my arms for her but she slid aside, slipping away on the other side of the table.

        We stood looking at each other for a little while, with the candle between us.

        Then she began to untie her veil and take off he hat, while her sparkling eyes were glued to me, watching my movements to keep me from catching her

        I made another large lunge forard, tripped on the carpet and fell; my sore foot refused to hold me up any longer.

        I got up, extremely embarassed
    """

    ylajali """
        My goodness, how red you became!

        Was it as clumsy as all that?
    """
    hungerProtagonist "Yes, it was"
    ylajali "You seem to be limping"
    hungerProtagonist "I may be limping a little - just a little, though"
    ylajali "The last time you had a sore finger, now you have a sore foot."
    ylajali "You certainly have a lot of troubles"
    hungerProtagonist "I was run over a bit the other day"
    ylajali """
        Run over? Drunk again, then? Good heavens, what a life you're leading, young man!
        {=hunger_narration} she threatened me with he fore-finger and put up a serious face


        {=hunger_ylajali}Let's sit down!

        No, not there by the door. You're too shy. Over here - you there and I here, that's it...

        Oh, shy people are such a bore! One has to say and do everything oneself, they on't help out with anything.

        For example, I wouldn't mind if you put your hand on the back of my chair right now, you could easily hve dreamed up that much by yourself,
        couldn't you?

        Because if I says something like that your eyes pop as if you don't quite believe me.

        Yes it's really true, I've seen it several times, you're doing it now too.

        But don't try to tell me you are tht modest when you dare come on.

        You were brazen enough that day when you were tipsy and followed me straight home, perstering me with your witticisms

        'You're losing you book, miss!\'

        Ha-ha-ha! Goodness you ought to be ashamed of yourself!

        Why don't you say something?
    """

    hungerProtagonist """
        Ah, how sweet you are!

        I'm sitting here getting fascinated by you, at this moment I', thorougly fascinated.

        I can't help it. You are the strangest person that...

        Sometimes your eyes  are so radiant, I've never seen anything like it, they look like flowers.

        Eh? No, no, maybe not like flowers

        but... I'm madly in love with you, and it won't do me a bit of good.

        What's your name? Really, you must tell me what your name is...
    """

    ylajali """
        No, what's {i}your{/i} name?

        Goodness, I almost forgot again! I was thinkign all day yesterday that I must ask you.

        Well, that is, not {i}all{/i} day yesterday, I certainly didn't think about you all day yesterday.
     """

    hungerProtagonist "Do you know what I've called you? I have called you Ylajali. How do you like it? Such a gliding sound---"

    $ ylajaliName = "Ylajali?"

    ylajali "Ylajali?"
    hungerProtagonist "Yes"
    ylajali "Is it a foreign language?"
    hungerProtagonist "Hmm. No, it's not"
    ylajali "Well, it isn't ugly."


    hungerNarration "After long negotiations we told each other our names..."

    $ hasNotReadHunger = False
    jump finished_book