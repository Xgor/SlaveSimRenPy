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
image bg concept = "Kruka-Conept.jpg"
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
        global tempGotItem
        tempGotItem = gotItem;
        if g_Item == "":
            
            g_Item = gotItem;
            renpy.say("","Got [tempGotItem]");
        else:
            renpy.say("","You already got [g_Item]! \nDo you want to switch to [tempGotItem]?");
            while True:
                ui.vbox(xpos=0.5,ypos=0.5,)
                ui.adjustment()
                ui.textbutton("Switch to the [tempGotItem]", clicked=ui.returns(("change", True)),xanchor=0.5, xpos=0.5, xalign=0.5)
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
        global tempGotItem

    scene bg concept
    "The low rumbling underground wake you from your pained sleep."
    "As you open your eyes you see that the Master have moved you back to the slave quarters after the whipping he gave you last night.\nThe dried blood covering your back and part of the floor was evidence of it"
    "Trying to move your sore back hurt and most of all you would like to just go back to sleep and hope that the sleep would give you some relief from your throbbing back."
    "But one of the other slaves could help you with your wounds and that would help the healing."
    "Looking around you find that the slave quarters are empty."
    "That is not a usual occurance, usually the slave quarters are bustling with other slaves trying to do their jobs or assigned tasks as fast as possible. What has happened? Why is no one here?"
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
            "As you get to the plaza you see people running around in panic trying to pick up as much as possible as they are trying to get away from the place."
            "Some people seems to be looking through the pockets of people that look like they just fell where they stood. A couple of buildings seems to have toppled over because of the earthwuake that you felt before."
            "But it does not seem like just an earthquake, the air is filled with flakes falling everywhere like a grey rain coating everything in a layer of ash."
            

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
                "???"
                
            else:
                "The slave tries to get in a couple of punches as you roll around on the ground trying to get the advantage."
                "With a lucky blow to his temple he slumps over and you skurry away with the item."
                $ Damage(1)
                $ GetItem("Item")

            $ Lava += 1

        "Attack them.":
            if g_Item == "Knife":
                $ Damage(1)
                
            else:
                "The slave tries to get in a couple of punches as you roll around on the ground trying to get the advantage."
                "With a lucky blow to his temple he slumps over and you skurry away with the item."
                $ Damage(2)
                $ GetItem("Item")


        "Walk on by.":
            "..."

    $ LavaCheck();
    return


