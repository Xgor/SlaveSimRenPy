# You can place the script of your game in this file.

init python:    
    class Execute(Action):
        def __init__(self, func, *args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs
       
        def __call__(self):
            self.func(*self.args, **self.kwargs)
            return "__"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg cell = "cell.jpg"
image bg street = "townstreet.png"
image bg sea = "winning.png"

# Declare characters used by this game.



init python:
    def GameOver():
        renpy.say("","Game Over!");
        renpy.full_restart();

    def LavaCheck():
        if Lava >= 3:
            GameOver();
        return

    def GetItem(gotItem):
        global g_Item
        global tempString
        tempString = gotItem;
        if g_Item == "":
            
            g_Item = gotItem;
            renpy.say("","Got [tempGotItem]");
        else:
            renpy.say("","You already got [g_Item]! \nDo you want to switch to [tempString?");
            while True:
                ui.vbox(xpos=0.5,ypos=0.5,)
                ui.adjustment()
                ui.textbutton("Switch to the [tempString]", clicked=ui.returns(("change", True)),xanchor=0.5, xpos=0.5, xalign=0.5)
                ui.textbutton("Keep the [g_Item]", clicked=ui.returns(("keep", True)) , xpos=0.5, xalign=0.5)
                ui.close()
            
                type, value = ui.interact()
                if type == "change":
                    g_Item = gotItem;
                    break
                if type == "keep":
                    break
        return
    
    def Damage(damage):

        global Slaves
        if len(Slaves) > 0:
            randNmr = renpy.random.randint(0,len(Slaves)-1)
            randSlave = Slaves[randNmr]
            randSlave.health -= damage
        
            if randSlave.health <= 0:
                renpy.say("","A slave died.");
                Slaves.pop(randNmr)

        else:
            global Health
            Health -= damage
            if Health <= 0:
                GameOver();

    def AddSlave(slaveType):
        if len(Slaves) < 3:
            Slaves.append(Slave(slaveType));
            global tempString
            tempString = slaveType;
            renpy.say("","You got [slaveType]");
        else:
            renpy.say("","You already got 3 slaves, you can't more with you!");

    def GotSlaveType(slaveType):
        global Slaves
        for Slave in Slaves:
            if Slave.slaveType == slaveType:
                return True
        return False




# The game starts here.
label start:
    
# Game variables
    $ Dialog = Character(None,
        what_size=28,
        what_outlines=[(3, "#0008", 2, 2), (3, "#FFFF", 0, 0)],
        what_layout="subtitle",
        what_xalign=0.5,
        what_text_align=0.5,
        window_background=None,
        window_yminimum=0,
        window_xfill=False,
        window_xalign=0.5)

 #   $ from collections import namedtuple
 #   $ Slave = namedtuple("Slaves", "slaveType health")
    python:
        class Slave(object):
    
            def __init__(self, slaveType):
                self.slaveType = slaveType
                self.health = 3
       
   

        global Slaves
        Slaves = list()
#    $ Slaves.
#    $ slave1 Slave

# Range ???
        Lava = 0    
# Range 0-5
        global Health
        Health = 5
# Range 0-5
        Energy = 3
# Range 0-5
        Trust = 2
# Only one item at a time
        global g_Item
        g_Item = "";
        global tempString

    "The low rumbling underground wake you from your pained sleep."

    scene bg cell
    with pixellate

    with hpunch


    "As you open your eyes you see that the Master have moved you back to the slave quarters after the whipping he gave you last night.\nThe dried blood covering your back and part of the floor was evidence of it"
    "Trying to move your sore back hurt and most of all you would like to just go back to sleep and hope that the sleep would give you some relief from your throbbing back."
    "But one of the other slaves could help you with your wounds and that would help the healing."
    "Looking around you find that the slave quarters are empty."
    "That is not a usual occurance, usually the slave quarters are bustling with other slaves trying to do their jobs or assigned tasks as fast as possible. What has happened? Why is no one here?"
    with vpunch
    with hpunch
    "Then the rumbling started again this time it was stronger and with it came a faint smell of something burning in the air. What are you going to do?"

label startChoice:
    $ LavaCheck();
    
    menu:

        "Go back to sleep":
            "You turn your head to the wall and try to go back to sleep. The other slaves are probably taking care of a small kitchen fire that fell on some hay when the small earthquake hit."
            $ Lava += 1
            $ Energy = 5
            jump startChoice

#        "Leta efter din ägare." if Energy > 2:
        "Look for your master.":
            "You start to move to the upper floors to try and find your master."
            "If you find him you are almost guaranteed to find other slaves and if there are none close to him, he will call on some to get you out of his sight and back to the quarters at least."
            "As you walk into the lavish living areas above you see that they are empty. \nNot just empty of people but also of most things."
            "Where there used to be colourful carpets and beutifully painted urns and vases there was nothing. A few of the urns were left but those were either too heavy for one person to move or shattered on the floor."
            "As you make your way through the place you see one of your masters possessions glittering on a table were it lay getting hit by the suns rays. "
            python:
                GetItem("Knife");
                Lava += 1
                Energy -= 1
            jump startChoice     
            
        "Look for the other slaves.":
            "You move with a pained grunt and start to work your way through the slave quarters to try and find some of the other slaves. \nThey cannot all have disappeared."
            "As you get further in you see the silouette of one of the other slaves sitting in one of the corners staring blankly into the air."
            "You approach and try to talk to the slave."
            "As you get close the other slave finally notices your presence and when he looks up you can see the tears lining his face."
            "His eyes betrays the fear he feels but as he sees you he seems to steel himself and rises to meet you."
            
            $ AddSlave("Boring")
            $ Lava += 1
            $ Energy -= 1
            jump startChoice

        "Walk out onto the plaza.":
            "You decide that you want to know what that rumbling and smell of ash is coing from. \nSo you start to make your way to the plaza outside your masters home to find out."
            
            show bg street
            with fade
            "As you get to the plaza you see people running around in panic trying to pick up as much as possible as they are trying to get away from the place."
            "Some people seems to be looking through the pockets of people that look like they just fell where they stood. A couple of buildings seems to have toppled over because of the earthwuake that you felt before."
            "But it does not seem like just an earthquake, the air is filled with flakes falling everywhere like a grey rain coating everything in a layer of ash."
            jump scene2
            
label scene2:
    "In front of you, you see two slaves hunched over the fallen body of what seems to be one of the wealthier residents of the area."
    "They are pulling on his clothes and rummaging through his pockets their bodies covering the body's face."
    "The body could be that of your master and you feel a that you are about to go and try to help him but you stop yourself."
    "Is it of genuine concern that was about to move you or was it simply reflexes after so many years working for him and his household?"
    "You could walk away and not bother to look at the mans face. Not knowing who he was and hopefully not care who he was. \nOr you could approach the slaves to see if you could see the fallen mans face knowing full well that they could see that as threatening."

    menu:

        "Try to talk to them.":
            "You walk up to them slowly holding your hands in the air so not to appear threatening. \nThey turn towards you with suspicion in their eyes."
            "When they see that you are not about to attack them they wait for you to speak."

            $ AddSlave("Boring")
            $ Lava += 1
            $ Trust += 1

        "Search for items on the body.":
            "There seems to be something of interest lying close to the body. \nYou move closer to try and pick it up without them noticing."
            "As you inch closer you find that it is not possible wen one of them turns around and sees you eying the item on the ground. \nYou both start running towards it, throwing yourself forward trying to get at it. "
            if g_Item == "Knife":
                "You manage to be a little faster than your opponent and you get to the item first. However you are not fast enough to pick it up before he gets close to you and all you can do is defend it."
                "You defend the item on the ground with your blade drawn trying to make him back away. As you lower yourself down to pick up the item, the slave lunges at you.\nYour body reacts by itself and puts the knife between you and your attacker."
                "The slave noticed your movement first when your blade was burried deep within his chest. As he is falling over, you pick up the item and run."

            else:
                "The slave tries to get in a couple of punches as you roll around on the ground trying to get the advantage."
                "With a lucky blow to his temple he slumps over and you skurry away with the item."
                $ Damage(1)
                $ GetItem("Item")

            $ Lava += 1

        "Attack them.":
            if g_Item == "Knife":
                "As you slowly walk closer you pull your blade and steel your thoughts at what you are going to do."
                "When you are just a step behind one of them you reach forward and cut his throat open before he notice that you have even moved."
                "The only thing that is heard is a low gurgling from the slave and the thump of his body falling to the ground."
                "The other slave however does not seem to notice over all other noices that can be heard around them."
                "You prepare to do the same thing to this other slave but as you are just a couple of steps behind him he notices you and launches himself at you. After a couple of frantic stabs at his torso he also stills."
                $ Damage(1)
                
            else:
                "The first thing you do is pick up a rock of the ground to hit one of the slaves in the back of the head. \nHe slumps over and does not appear to be moving anymore as a small stream of blood runs out onto the ground below."
                "The other notices what you are doing but is to slow to save the slave. \nHowever he is fast enough to pull a small blade from his clothing and stab you before you can bring the rock down on his head aswell."
                $ Damage(2)
                $ GetItem("Item")


        "Walk on by.":
            "You choose to leave the scene more focused on your own survival than that of others. The thought that you must get to the docks to flee this place firm in your mind."
    $ LavaCheck();

    jump scene3

label scene3:

    "As you walk along the edge of the plaza you see a person stumbling forward towards one of the side passages."
    "Another one is following, but this one with power in his step. The first one periodically throws a look over his shoulder to see if the other if still following him and everytime a renewed look of fear enters his features as he tries to run a little bit faster."
    "Just as the Frightened one is about to enter the side passage the Aggressor catch up to him and throws him to the ground."
    "The Aggressors face is framed by tears but his eyes now only conveys anger."
    "He yells at the Frightened one but you cannot hear it over the rumbling and panic that is filling the air with noise. When the Frightened one tries to scramble backwards away from him he tries to grab him but his hands only catches the fabric of his clothes. \nThey rip."
    "As the clothes rip the Aggressor's eyes grows darker and a second later he is on top of the frightened one who is trying to fight back."

    menu:

        "Help The Aggressor":
            "You step forward to help the Aggressor as the Frightened one has obviously done something to incur this ones wrath."
            "That and if you do he most likely will follow along to try and flee this doomed isle."
            "You place yourself between the Frightened one and the side passage to stop him from running away if he manages to get the upper hand."
            "The Aggressor sees you standing there and loses his focus for a second and that is all the time the man under him needs."
            "With a swift blow to the side of his Aggressors head and a scramble to his feet the Frightened one tries to flee past you into the side alley but you stop him in his tracks."
            "As you struggle to keep the man there the one he knocked to the ground is now moving again and getting to his feet. He seems a little dizzy at first but soon regains his balance. He walks up to you and the man you try to keep put."
            "As he comes up besidehind the Frightened man he grabs his shoulders and spins him around. You see the tears running down his face again."
            "He hits the frightened man in the face, his closed fist containing enough force to make the Frightened man fall down beside you."
            "As the Frightened man once again scrambles backwards his Aggressor screams at him."
            Dialog "I loved you! And you just left me to die!"
            "After he said that he made no attempt to get to the man lying on the ground. He let him scramble away without a word."
            "Then he turned to you and voiced a low thank you. \nAs you were continuing to make your way towards the docks the man started to follow you."
    
    
        "Help The Frightened man":
            "You rush forward and grab onto the arms of the man on top and drag him of the man with his back on the ground."
            "As you do the man becomes aggrssive towards you instead and swings at you as he is shouting profanities at you."
            "To protect yourself you raise your hands in front of you. The man just keeps swinging at you and does not seem to let up so when you see an oppurtunity to strike back you do. \nYour fist connects with his jaw and he starts to stumble backwards."
            "Your fist connects with his jaw and he starts to stumble backwards. The other man is suddenly in front of the Aggressor and he pushes him."
            "In his already somewhat groggy state the Aggressor has no way to stop himself from falling over."
            "With a crack the Aggressors head makes contact with the rocky ground and his eyes fall shut. He isn't moving anymore."
            "As you turn to walk away the man you just saved starts to follow you."
    
        "Watch the scene unfold":
            "You stand and watch as the two men struggle for power over the other. You see their clothes getting ripped to pieces as they fight each other with tooth and nail."
            "As the fight goes on the man that got attackeds attempts to get away gets weaker and weaker until he just lies there waiting for the inevitable.."
            "As the Aggressor rips of the last scraps of clothing you turn your head."
    
        "Walk on by":
            "You turn your away from the scene and walk by. \nYou have neither the time or energy to waste on a lovers quarrel."


    jump scene4

label scene4:

    "As you walk by a small statue of Poseidon you see someone kneeling infornt of it and talking in prayer." 
    "It seems this person is doing all to avoid Posiedons wrath and survive this without actually having to move or do anything that requires anything but faith."

    menu:

        "Talk to the Faithful":
            "You walk up to the Faithful with the intent to talk to her. \nYou cannot just leave her here to be consumed by the lava."
            "As you approach her you lower yourself down so that you are on more or less the same level."
            "By talking to the Faithful you convince her to leave with you as she sees you as a messenger of Posiedon and his way of helping her off of this doomed island."
    
    
        "Steal the statue":
            "That statue seems to be worth quite a bit both because of its gold value and the value for believers."
            "It would be so easy for you to just steal it as she is kneeling in front of it."
            "You walk past the statue and as you pass you lift it from it's intended place and carries it effortless with you. When the priestess notices it is gone so are you."
    
        "Listen to the Faithful":
            "You stop and kneel in front of the statue of Posiedon to listen to her prayer as the priestess starts on a new verse."

            python:
                if GotSlaveType("The Frightened"):
                    renpy.say("","As you listen you see that the Frightened man beside you seems to relax and listen intently at the priestesses prayer.")
                    renpy.say("","When he can he joins in the prayer. As the verse ends you stand to leave relieved that Posiedon might look upon you now.")
                    renpy.say("","However the Frightened man does not rise and as you start to walk towards the harbour it is obvious that he is not coming along with you.")
                # TA BORT DEN SLAVEN!'
    
        "Walk on by":
            "You have more pressing matters than to listen to a priestess pray to Poseidon as the city is falling apart around you."

    jump endScene

label endScene:

    show bg sea
    with fade

    "As you approach the crowd around the lone boat left in the harbour you see how guards are trying to control the mass of people trying to board the ship to flee this doomed city."
    "You appraise the ship to be capable to hold most of the ones waiting to flee but then you would be optimistic as there will be those who will either have to find another way or count their last moments."
    "Getting close you see how there is also several guards helping loading what seems to be valuables such as expensive pottery and similiar luxuries in hopes to save tome of the citys treasury."

    with vpunch
    with hpunch
    with vpunch
    with hpunch

    "You can feel another rumble as a reminder that you have not too much time left and you will have to take your chances with this boat before its too late."
    $ endQuests = 0
    
label endMenu:

    menu:

        "Talk with the guards trying to gain compassion to get aboard.":
            if trust > 3:
                "Trying to convince the guards they seem to want to let you on the boat and it does not take too long before you are allowed to walk onto the ship where you are assigned to help with the preparations."
                "You help the guards with several other waiting to get on the ship and the loading of some resources deemed more worthy then those who are left behind."
                $ endQuests +=1

            else:
                "Trying to convince the guards they seem to want to let you on the boat but they are not completely convinced."
                "They explain that they can not just let eanyoneon the boat and that they do not have time to evaluate the preferred crew for this emergency voyage."
                "You are for now sent back to wait untill they have decided if the want to let on on board or not."
                $ Lava += 1

#        "Let the guard with you talk for you with the other guards":


 #       "Try to bribe them":

 #       "Try to preach to them":


  #      "Try to turn the crowd against the guards":


    return