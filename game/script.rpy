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
            randSlave = renpy.random.choice(Slaves)
            randSlave.health -= damage
        
            if randSlave.health <= 0:
                renpy.say("","A slave died.");

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
    "Du vaknar i slavarnas kvarter och ser ingen runt om kring dig. \nDu hör ett dovt muller i bakgrunden."



label startChoice:
    $ LavaCheck();
    
    menu:

        "Lämna Hushållet.":
            "Woop ,[Lava]."
            $ Lava += 1
 #           $ DistanceFromLava += 10
            

#        "Leta efter din ägare." if Energy > 2:
        "Leta efter din ägare.":
            $ Damage(3)
            $ GetItem("Kniv");
            $ Lava += 1
            $ Energy -= 1
            jump startChoice     
            
        "Leta efter slav kvarteret efter andra slavar.":
            "Hittade en slav"
            $ AddSlave("Boring")
            $ Lava += 1
            $ Energy -= 1
            jump startChoice

        "Lägg dig ner och sov ner.":
            "Du sov"
            $ Energy = 100
            $ Lava += 1
            jump startChoice


    "Once you add a story, pictures, and music, you can release it to the world!"

    return


