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
    def LavaCheck():
        if Lava >= 3:
            renpy.say("","FAIL");
            renpy.full_restart();
        return

    def GetItem(gotItem):
        global g_Item
        global tempGotItem
        tempGotItem = gotItem;
        if g_Item == "":
            
            g_Item = gotItem;
            renpy.say("","Got [tempGotItem]");
        else:
            renpy.say("","You already got [g_Item]! /n Do you want to switch to [tempGotItem]?");
            while True:
                ui.vbox(xpos=0.5,ypos=0.5,)
                ui.adjustment()
                ui.textbutton("Keep going", clicked=ui.returns(("keep", True)),xanchor=0.5, xpos=0.5, xalign=0.5)
                ui.textbutton("Finish", clicked=ui.returns(("done", True)) , xpos=0.5, xalign=0.5)
                ui.close()
            
                type, value = ui.interact()

                if type == "done":
                    break
        return

        


  

# The game starts here.
label start:
    
# Game variables
 
# Range ???
    $ Lava = 0    
# Range 0-5
    $ Health = 5
# Range 0-5
    $ Energy = 3
# Range 0-5
    $ Trust = 2
# Only one item at a time
    $ global g_Item
    $ g_Item = "";
    $ global tempGotItem

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
        "Leta efter din ägare." if Energy > 2:
            "Hittade [g_Item]"
            $ GetItem("Kniv");
            $ Lava += 1
            $ Energy -= 1
            jump startChoice     
            
        "Leta efter slav kvarteret efter andra slavar.":
            "Hittade en slav (Inte implementerad...)"
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


