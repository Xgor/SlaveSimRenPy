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
image bg cell = "cell.png"
image bg street = "townstreet.png"
image bg sea = "winning.png"
#image bg volcano = "titlescreen_volcano.png"

image character1 fighting = "slavesFighting_01.png"
image character1 begging = "slaveBegging_01.png"

# Declare characters used by this game.



init python:
    def GameOver():
        renpy.say("","Game Over!");
        renpy.full_restart();

    def LavaCheck():
        if Lava >= 3:
#            window.background = "titlescreen_volcano.png";
            renpy.say("","The heat radiates from the oncoming lava as it is coming closer and closer. Your blood is starting to boil from the heat and the energy is disappearing from your body.")
            renpy.say("","You fall over as the last of your energy drains.")
            renpy.say("","Now you cannot do anything more than slowly drag yourself away from the lava and postpone your demise or just stop and accept your impending demise.")


            GameOver();
        return
    def EnergyCheck():
        if Energy <= 0:
            renpy.say("","You start breathing heavily and you are winded from all the physical exertion.")
            renpy.say("","You need to rest even if the lava is advancing towards you.")
            Lava += 1

            GameOver();
        return


    def GetItem(gotItem):
        global g_Item
        global tempString
        tempString = gotItem;
        
        renpy.say("","Got [tempString]");
        if g_Item != "":

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
        else:
            g_Item = gotItem;
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
                renpy.say("","The blow knocks you over and spots starts dancing in front of your eyes because of the pain.")
                renpy.say("","You try to keep your eyes open but to no avail. \nYour eyes flutters shut and you are barely present as your life ends.")
                GameOver();

    def AddSlave(slaveType):
        if len(Slaves) < 3:
            Slaves.append(Slave(slaveType));
            global tempString
            tempString = slaveType;
            renpy.say("","You got [tempString]");
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
        window_yminimum=0.5,
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

    python:
        NotSelected1 = True;

        NotSelected2 = True;

        NotSelected3 = True;





    $ renpy.movie_cutscene("intro.ogv")

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

        "Go back to sleep" if NotSelected1:
            "You turn your head to the wall and try to go back to sleep. The other slaves are probably taking care of a small kitchen fire that fell on some hay when the small earthquake hit."
            with vpunch
            with hpunch
            $ Lava += 1
            $ Energy = 5
            $ NotSelected1 = False
            jump startChoice

#        "Leta efter din ägare." if Energy > 2:
        "Look for your master." if NotSelected2:
            "You start to move to the upper floors to try and find your master."
            "If you find him you are almost guaranteed to find other slaves and if there are none close to him, he will call on some to get you out of his sight and back to the quarters at least."
            "As you walk into the lavish living areas above you see that they are empty. \nNot just empty of people but also of most things."
            "Where there used to be colourful carpets and beutifully painted urns and vases there was nothing. A few of the urns were left but those were either too heavy for one person to move or shattered on the floor."
            "As you make your way through the place you see one of your masters possessions glittering on a table were it lay getting hit by the suns rays. "
            python:
                GetItem("Knife");
                Lava += 1
                Energy -= 1
            with vpunch
            with hpunch
            $ NotSelected2 = False;
            jump startChoice     
            
        "Look for the other slaves." if NotSelected3:
            "You move with a pained grunt and start to work your way through the slave quarters to try and find some of the other slaves. \nThey cannot all have disappeared."
            "As you get further in you see the silouette of one of the other slaves sitting in one of the corners staring blankly into the air."
            "You approach and try to talk to the slave."
            show character1 begging
            "As you get close the other slave finally notices your presence and when he looks up you can see the tears lining his face."
            "His eyes betrays the fear he feels but as he sees you he seems to steel himself and rises to meet you."
            hide character1 begging
            $ AddSlave("The Slave")
            $ Lava += 1
            $ Energy -= 1
            $ NotSelected3 = False;
            with vpunch
            with hpunch
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

            $ AddSlave("The Looter")
            $ Lava += 1
            $ Trust += 1

        "Search for items on the body.":
            
            "There seems to be something of interest lying close to the body. \nYou move closer to try and pick it up without them noticing."
            "As you inch closer you find that it is not possible wen one of them turns around and sees you eying the item on the ground. \nYou both start running towards it, throwing yourself forward trying to get at it. "
            if g_Item == "Knife":
                "You manage to be a little faster than your opponent and you get to the item first. However you are not fast enough to pick it up before he gets close to you and all you can do is defend it."
                "You defend the item on the ground with your blade drawn trying to make him back away. As you lower yourself down to pick up the item, the slave lunges at you.\nYour body reacts by itself and puts the knife between you and your attacker."
                "The slave noticed your movement first when your blade was burried deep within his chest. As he is falling over, you pick up the item and run."
                $ GetItem("Valuable")

            else:
                "The slave tries to get in a couple of punches as you roll around on the ground trying to get the advantage."
                "With a lucky blow to his temple he slumps over and you skurry away with the item."
                $ Damage(1)
                $ GetItem("Valuable")


            $ Lava += 1
            $ Energy -= 1


        "Attack them.":
            if g_Item == "Knife":
                "As you slowly walk closer you pull your blade and steel your thoughts at what you are going to do."
                "When you are just a step behind one of them you reach forward and cut his throat open before he notice that you have even moved."
                "The only thing that is heard is a low gurgling from the slave and the thump of his body falling to the ground."
                "The other slave however does not seem to notice over all other noices that can be heard around them."
                "You prepare to do the same thing to this other slave but as you are just a couple of steps behind him he notices you and launches himself at you. After a couple of frantic stabs at his torso he also stills."
                $ Damage(1)
                "You lost the Knife"
                $ g_Item = "";
                $ GetItem("Valuable")
                
            else:
                "The first thing you do is pick up a rock of the ground to hit one of the slaves in the back of the head. \nHe slumps over and does not appear to be moving anymore as a small stream of blood runs out onto the ground below."
                "The other notices what you are doing but is to slow to save the slave. \nHowever he is fast enough to pull a small blade from his clothing and stab you before you can bring the rock down on his head aswell."
                $ Damage(2)
                $ GetItem("Valuable")

            $ Energy += 1


        "Walk on by.":
            "You choose to leave the scene more focused on your own survival than that of others. The thought that you must get to the docks to flee this place firm in your mind."
            $ Energy -= 1
    $ EnergyCheck();
    $ LavaCheck();

    jump scene3

label scene3:
    show character1 fighting 
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
            $ AddSlave("The Aggressor")
            $ Lava += 1
            $ Energy -= 1

    
        "Help The Frightened man":
            "You rush forward and grab onto the arms of the man on top and drag him of the man with his back on the ground."
            "As you do the man becomes aggrssive towards you instead and swings at you as he is shouting profanities at you."
            "To protect yourself you raise your hands in front of you. The man just keeps swinging at you and does not seem to let up so when you see an oppurtunity to strike back you do. \nYour fist connects with his jaw and he starts to stumble backwards."
            "Your fist connects with his jaw and he starts to stumble backwards. The other man is suddenly in front of the Aggressor and he pushes him."
            "In his already somewhat groggy state the Aggressor has no way to stop himself from falling over."
            "With a crack the Aggressors head makes contact with the rocky ground and his eyes fall shut. He isn't moving anymore."
            "As you turn to walk away the man you just saved starts to follow you."
            $ AddSlave("The Frightened")
            $ Damage(1)
            $ Lava += 1
            $ Energy -= 1
            $ Trust += 1


    
        "Watch the scene unfold":
            "You stand and watch as the two men struggle for power over the other. You see their clothes getting ripped to pieces as they fight each other with tooth and nail."
            "As the fight goes on the man that got attackeds attempts to get away gets weaker and weaker until he just lies there waiting for the inevitable.."
            "As the Aggressor rips of the last scraps of clothing you turn your head."
            $ Energy += 1
            $ Lava += 1
    
        "Walk on by":
            "You turn your away from the scene and walk by. \nYou have neither the time or energy to waste on a lovers quarrel."
            $ Energy -= 1

    hide character1 fighting 
    $ EnergyCheck();
    $ LavaCheck();
    jump scene4

label scene4:

    "As you walk by a small statue of Poseidon you see someone kneeling infornt of it and talking in prayer." 
    "It seems this person is doing all to avoid Posiedons wrath and survive this without actually having to move or do anything that requires anything but faith."

    menu:


        "Talk to the Faithful":
            "You walk up to the Faithful with the intent to talk to her. \nYou cannot just leave her here to be consumed by the lava."
            "As you approach her you lower yourself down so that you are on more or less the same level."
            "By talking to the Faithful you convince her to leave with you as she sees you as a messenger of Posiedon and his way of helping her off of this doomed island."
            $ AddSlave("The Faithful")
            $ Lava += 1
            $ Trust += 1
    
        "Steal the statue":
            "That statue seems to be worth quite a bit both because of its gold value and the value for believers."
            "It would be so easy for you to just steal it as she is kneeling in front of it."
            "You walk past the statue and as you pass you lift it from it's intended place and carries it effortless with you. When the priestess notices it is gone so are you."
            $ GetItem("Valuable")
            $ Energy -= 1
            $ Trust -= 1

        "Listen to the Faithful":
            "You stop and kneel in front of the statue of Posiedon to listen to her prayer as the priestess starts on a new verse."
            $ Energy += 1
            $ Trust += 1
            $ Lava += 1
            python:
                if GotSlaveType("The Frightened"):
                    renpy.say("","As you listen you see that the Frightened man beside you seems to relax and listen intently at the priestesses prayer.")
                    renpy.say("","When he can he joins in the prayer. As the verse ends you stand to leave relieved that Posiedon might look upon you now.")
                    renpy.say("","However the Frightened man does not rise and as you start to walk towards the harbour it is obvious that he is not coming along with you.")


                # TA BORT DEN SLAVEN!'
    
        "Walk on by":
            "You have more pressing matters than to listen to a priestess pray to Poseidon as the city is falling apart around you."
            

    $ EnergyCheck();
    $ LavaCheck();

    jump scene5

label scene5:

    "At the end of the plaza you see a soldier trying to help a woman who has been trapped under parts of a wall that has fallen."
    "The soldier is trying to move away the rubble as fast he can but since no one is helping him it is going slow."
    "Some parts are to big for him to move by himself but he is still trying to move what he can to get her out of there as he searches the plaza for help with his eyes."

    menu:

        "Help him":
            "You step forward to try and help the soldier move the bricks. \nWith a look of thanks he turns to you and tells you how you are going to get the woman out from under there."
            if Energy > 1:
                $ Energy -= 2
                $ Trust -= 2
                $ Lava += 1

                "As the Soldier tells you what you need to do you are already moving in to place to lift."
                "The pieces of wall that lies over her are heavy but together with the Soldier you manages to lift piece after piece of her back until you can manage to pull her out."
                "She thanks you as she is freed from the rubble. \nWhen she rise, she starts to shake having difficulty standing straight but at least she is out of harm for now."
                $ criterias = 0;
                if g_Item != "Knife":
                    $ criterias += 1;
                python:
                    if GotSlaveType("The Frightened"):
                        criterias += 1;
                if Trust > 1:
                    $ criterias += 1;

                if criterias > 1:
                     "The soldier makes sure that she can walk without to much of a problem. \nHe even lends her his spear so that she can lean on it when she needs to."
                     "As she walks away he comes to stand beside you. \nHe nods at you and with a move of his hand he shows that he will follow you out of this hell."
                     $ AddSlave("The Soldier")


            else:
                $ Energy -= 1
                $ Trust -= 2
                $ Lava += 1
                "You follow the Soldiers orders as you try to help move the fallen wall but it is to heavy for you to lift even with the help."
                "You start to move small pieces to at least help with something but it goes to slow to be of any help and you choose to leave as there is nothing you can do to help."
                "You hear the woman scream as you turn your back to her."


        "Look through the fallen building":
            "As the Soldier is preoccupied with the trapped woman you take that time to search through the house for anything valuable."
            "Most of the things have been destroyed by the panic and the mini earthquakes that accompanies the volcanos eruption but under a pile of destroyed fabric you find something that is small enough to carry and worth your time."
            $ GetItem("Valuable")

        "Attack him":
            $ Damage(1)
            "The Soldier turns his head back to the woman and tries to ensure her that she will be safe. \nHe will get her out of there is probably what he is saying."
            "You however know that it will never happen. The woman is dead she just doesn't know it yet."
            "The Soldier is carrying a sword that could help you save yourself."
            "Sneaking up behind the Soldier with the chaos around you wasnt to hard and with a swift blow to the back of his head he falls to the ground."
            "The womans scream cuts through the air starting to ring in your ear but you ignore her and pick up the soldiers blade and turn around."
            $ GetItem("Sword")



        "Walk on by":
            "It seems you don't have time to help them in their struggle and you move on."
 


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
    $ guardTrust = 0
    $ guardOverthrow = 0


    $ NotSelected4 = True;

    $ NotSelected5 = True;

    $ NotSelected6 = True;

    $ NotSelected7 = True;

    $ NotSelected8 = True;
    
label endMenu:
    $ EnergyCheck();
    $ LavaCheck();
    menu:

        "Talk with the guards trying to gain compassion to get aboard.":
            if guardTrust+Trust > 6:
                "Trying to convince the guards they seem to want to let you on the boat and it does not take too long before you are allowed to walk onto the ship where you are assigned to help with the preparations."
                "You help the guards with several other waiting to get on the ship and the loading of some resources deemed more worthy then those who are left behind."
                jump ending

                

            else:
                "Trying to convince the guards they seem to want to let you on the boat but they are not completely convinced."
                "They explain that they can not just let any one on the boat and that they do not have time to evaluate the preferred crew for this emergency voyage."
                "You are for now sent back to wait untill they have decided if the want to let on on board or not."
                $ Lava += 1
            
        "Attack!":
            if guardOverthrow > 1:
                "With the owerwhelming force of you and those around you turn the scene into bloody combat."
                "Several dies at the blade and fist but at the end you are now commandeering the boat."
                "Luckily for you after some quick treasure throwing there is enough room for those who survived."
            elif guardOverthrow > 0:
                "The scene into bloody combat, it's uncertain if you'll surive."
                $ Damage("3")
                $ Damage("3")
                $ Damage("3")
                if g_Item != "Sword":
                    $ Damage("3")
                "Several dies at the blade and fist but at the end you are now commandeering the boat."
                "Luckily for you after some quick treasure throwing there is enough room for those who survived."
            else:
                "You unleash your strength at the guards only to find yourself surrounded and dealt with quicker then you imagined."
                "The fight is quick and merciless and you slump down with more punctures then you can count. \nAt least you died in glorius combat."
                $ GameOver();
        "Try to bribe them" if NotSelected4:
            
            python:
                NotSelected4 = false;
                if GotSlaveType("The Looter"):
                    renpy.say("","With some help you give a hefty offer that would shame many corrupted merchants.")
                    renpy.say("","Whispers showing signs of progress for you but you are pretty sure there might need to be some more work to be done.")
                    renpy.say("","You walk back to the crowd to think something else out.")
                    guardTrust += 1;
                    guardOverthrow += 1
                else:
                    renpy.say("","You are attempting to offer them with gold that you do not have and the guards are not interested in such empty offers.")
                    renpy.say("","You are sent back to the crowd to await futher word.")


        "Let the guard with you talk for you with the other guards" if NotSelected5:
            python:
                NotSelected5 = false;
                if GotSlaveType("The Guard"):
                    renpy.say("","The guard with you walks up to the other guards and explains the situation for them in order to let you go through to the boat.")
                    renpy.say("","His words calls to his comrades to sympathise those who have helpeed others in these chaotic moments.")
                    renpy.say("","He goes on with helping the other guards to quicken the process and tells you that he will do his best to help you on board as well as many as possible.")
                    guardTrust += 1;
                else:
                    renpy.say("","As you try to impose your position onto the guards they simply mock you and push you aside.")
                    renpy.say("","Ignoring your lowly prescense to them as they continiue their business.")

        "Try to preach to them" if NotSelected6:
            python:
                NotSelected6 = false;
                if GotSlaveType("The Faithful"):
                    renpy.say("","With a soft but resolute voice the man of faith walks up to the guards speaking as if empowered by a god.")
                    renpy.say("","The guards are almost completely distracted by the prescense of him as his words call to them.")
                    renpy.say("","He then points to you and continiues with trying to convince free passage for him and you.")
                    renpy.say("","You are sure you have improved the favor of both the guards and the gods.")
                    guardTrust += 1;
                else:
                    renpy.say("","Your word fall on deaf or ignorant ears as you seem to lack the faith to empower your speech.")
                    renpy.say("","You are soon empty of holy words to say and the response is clear and hollow leaving you without what you desired.")

        "Try to turn the crowd against the guards" if NotSelected7:
            python:
                NotSelected7 = false;
                if GotSlaveType("The Faithful"):
                    renpy.say("","You and the aggressor star to scream with impatience and 	dissatisfaction. Empowering the situation in your words you heat the situation and the temper of the people around you.")
                    renpy.say("","Your words ignite thoughts of voilence and anger.")
                    renpy.say("","The crowd around you follow your lead and they show more and more of their anger against those who would rather save gold rather then human lives.")
                    renpy.say("","You're sensing an oppurtunity approaching.")
                    guardOverthrow += 1;
                else:
                    renpy.say("","Your word fall on deaf or ignorant ears as you seem to lack the faith to empower your speech.")
                    renpy.say("","You are soon empty of holy words to say and the response is clear and hollow leaving you without what you desired.")

        "Try to gain the sympathy of the crowd" if NotSelected8:
            python:
                NotSelected8 = false;
                if GotSlaveType("The Frightened"):
                    renpy.say("","Alongside your frightened companian you start acummulating sympathy from those around you.")
                    renpy.say("","Invoking a desire to help the poor thing and to take care of the selfish guards who think of none other then themselves.")
                    renpy.say("","You are pretty sure you got this crowd around your finger with the help of this frightened one.")
                    guardOverthrow += 1;
                else:
                    renpy.say("","They look at you but you are otherwise ignored. \nYou seem to lack something you usually dont. \nThe lack of lacking bravery.")
                    renpy.say("","And you curse the gods quietly for being unable to gain the favor of the crowd with the sympathy for the weak and cowardly.")

label ending:
    "You feel an odd relief as you watch the city burn. There is relief despite all the things that have happened but more so because of those things that did not happen."
    "You not only alive but also free. You outlived your former life as a slave and is born again as someone who is free to choose."
    "You tug at some food you found in the hull of the ship and you look to the horizon and ponder to yourself of what things you will be able to do."

    "You watch the city again as it diminishes with only a column of smoke behind you."
    "You feel calmer as if you have left something behind. Something that would be best lying in the ruins of your past."
    "THE END!"
    $ renpy.full_restart()

#        "Let the guard with you talk for you with the other guards":


 #       "Try to bribe them":

 #       "Try to preach to them":


  #      "Try to turn the crowd against the guards":


    return