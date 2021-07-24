def addToItems(item):
    Items.append(item)


Items = []
while True:

    def main_quarters():
        global Items
        print("You wake up in your quarters aboard space station AG1627 orbiting the 5th moon of the planet Golaris.")
        print()
        print("You hear the other members of the crew outside your door.")
        print("It’s an unfamiliar commotion.")
        print("You hear weapons fire and screams coming from all over the station.")
        print(
            " You realize you do not have your weapon and you need your advanced combat suit, there may be an extra one around the station, to defend from enemy fire.")
        print()
        print("You try to take deep breaths and realize the life support is also failing.")
        print("You need to get an oxygen tank to survive.")
        print("you know what needs to be done and you are hesitent but ready to take action")
        print(
            "You need to collect all the items and make it to the bridge to activate the escape pods and alert the crew to abandon ship but first you need to also locate the access codes to activate the main computer.")
        print("")


    startgame = input("Would you like to save the crew of Space Station AG1627? yes/no     .")
    if startgame.lower() == "no":
        print("Thats a shame... you could have been a hero and saved the crew from certain death... ")
        break
    elif startgame.lower() == "yes":
        main_quarters()
        print('You creep slowly toward the door.')
        print('the sounds have subsided for now.')
        print('you walk slowly toward the door.')
        print('It seems the main power has caused your door to malfunction.')
        print('You pull the manual release lever located in the console next to the door.')
        print('The door releases and you slide it open')
        print('')
        print('It\'s hard to see but you inch your body out of the door.')
        print('You look up and down the main corridor.')
        print('Burn marks and blood trails litter the main cooridor. ')
        print(
            'It is hard to see because the lights are flashing on and off but you can faintly see an oxygen mask sticking out of the adjacent bulkhead compartment')
    else:
        print('Invalid input... Game Over!')
        break
    oxygen_mask = input('do you put it on? yes/no    .')
    if oxygen_mask.lower() == "no":
        print()
        print('you become disoriented and out of sorts. You feel faint and everything goes black... GAME OVER')
        break
    elif oxygen_mask.lower() == "yes":

        addToItems('Oxygen Respirator')
        print('')
        print('')
        print('You can breath again. you gasp for air as you slowly feel the fresh air fill you lungs.')
        print('')
        print(Items)
        print('')
        print('the monitor in the mask informs you that you will need a refil soon')
        print('Now that you are becoming more alert you look up the hallway and down.')
        print('you see three possible ways to go.')
        print('')
        print('you can make out the writing on the doors despite the lights flickering on and off')
        print('The door to your left says H1, the door to your right says M3, and the door in front of you says 2B...')
    door_1 = input('which door will you chose? H1 / M3 / or 2B?     .')
    if door_1.lower() == "h1":
        print('')
        print('')
        print('You pass through the door. you are now in cargo bay 1...')
        print('your oxygen respirator is still running low... ')
        print('')
        print('')
        print(
            'you look down... and through the flickering lights you see a blood trail leeding off around the hallway...')
        print(
            'Against your better judgement you follow it... there the trail stops. you see one of your fellow crew members.')
        print('You bend down and check his pulse... nothing... he\'s dead...')
        print('')
        print(
            'but you look at his respirator... its nearly full... enough oxygen to last you for at least a couple hours...')
        print(
            'You disconect his refil tank from his mask... and connect it to your own... the screen on your mask reads full... ')
        addToItems('Oxygen Respirator Refill')
        print('')
        print(Items)
        print('')
        print('you hear yelling and screams coming from somewhere close... and you know you have to keep moving...')
        print('you look up and see a door that says main engeneering... ')
        print('the access codes to the ships main computer have to be in there...')
        main_engineering = input('Do you continue though the door? or turn back? continue/turn back     .')
        if main_engineering.lower() == 'continue':
            print('')
            print('')
            print('you have made it to main engineering')
            print('sparks flying and lights strobing in a disorienting way...')
            print(
                'lets hope there is enough power left in the backup reserves to turn on the console to retreive the access codes to the main computer.')
            print('')
            print('you look around no one is left in engineering. hopefully, they are safe somewhere. ')
            print('you walk over to the computer console... there is a red flashing light. ')
            print('you look down and see the chief engineer on the floor')
            save_chief = input('do you check to see if he is alive? yes/no    .')
            if save_chief == "yes":
                print('')
                print('')
                print('you slowly lower yourself and put your finger on his neck...')
                print('it is faint but there is a pulse.')
                print(
                    'you see his oxygen resperator on the floor next to him. Almost as if he was trying to put it on before he ran out of oxygen.')
                print('you put on his mask... then... you see his eyes slowly open.')
                print('you ask him \" WHAT HAPPENED HERE?!\"')
                print(
                    'in almost a whisper you hear him say... \"They came out of no where... they started shooting the crew... pushed me to the ground and i cant remember much after that... i started gasping for air then everything went black.\"')
                print('')
                print(
                    '\" How to i get the access codes for the main computer on the bridge to turn on the escape pods and tell the remaining crew to abandon the station and head to the surface?\" ')
                print(
                    'he reached his hand over, opened the hatch on the side of the main compartment console and reached in and began the auto restart...')
                print('')
                print('You hear the system restart and the screen starts to flicker...')
                print(
                    '\" COMPUTER..\" the chief says. \"beep boop beep\" the computer responds. \" Show access codes for main computer on the bridge... autorization ZULU ALPHA ONE ONE FIVE ALPHA FOUR...\" ')
                print('\"ACCESS CODES FOR MAIN COMPUTER ARE... 78-649-036')
                addToItems('Access Codes')
                print('')
                print(Items)
                print('')
                print(
                    'the chief tells you to take the codes and get to the bridge... but first you must get yourself a weapon and some armor...')
                print(
                    '\" These things are big! and strong! and very dangerous\" he says... \" you must save the crew!\"')
                print(
                    'you start walking to the door. but you stop... you see a green flashing light above a door to your right... the sign below the light says ESCAPE POD/ENGINEERING')
                exit_engineering = input('Do you go into the escape pod and save yourself? yes/no    .')
                if exit_engineering == "yes":
                    print('')
                    print('')
                    print(
                        'you climb into the escape pod and push the eject button... you are suddenly drifting in space toward the planet. you inter the atmosphere and find yourself plunging toward the planet. your body shakes and jolts until you feel your pod crash into the planet... disoriented you climb from the pod... you look up into the night sky and you see a bright flash as the station explodes... you made it out alive but the rest of the crew had not survived. GAME OVER...')
                    break
                else:
                    print('')
                    print('')
                    print(
                        'you look back at the chief laying helplessly on the floor. you load him into the escape pod and wish him the best of luck. you exit through the door into cargo bay where you just were and look around for any type of weapon... ')
                    print('you look amung the dead, both human and alien, trying to find a weapon of any kind. ')
                    print('you see a mixture of blue blood and red sprayed on the walls.')
                    print(
                        'burn marks on just about everything you see from the shots fired and return fire from the alien entities...')
                    print('there nothing of any use here... ')
                    Back_to_main_cor = input(
                        'should you stay and look through the canage? or continue on to the main corridor and try to find a weapon? stay/continue     .')
                    if Back_to_main_cor == "stay":
                        print(
                            'you continue to look among the dead... but then you notice one of the alien creatures starts to move...')
                        print('you slowly back away as it regains conciousness... ')
                        print('you try to hide yourself... ')
                        print('it sees you... and stands up... ')
                        print('you start to run toward the door... ')
                        print(
                            'you hear a loud noise, almost like an explosion... your back gets suddenly hot and the sensation turns into a burn... you drop to your knees... looking down you see a pool of what apears to be your own blood... ')
                        print('')
                        print('')
                        print('you look up... desprate to move... but you can\'t... ')
                        print('the creature pulls a blade from its armor... ')
                        print(
                            'before another thought inters your head... he plunges his blade through your core into the depths of your soul...')
                        print('everything around you goes black... ')
                        print('GAME OVER...')
                        break
                    else:
                        print('you have made it back to where this whole thing began... ')
                        print('suddenly a russeling noise comes from behind...')
                        print('you see the creature sturring... ')
                        print('It suddenly spots you... and stands up..')
                        print('you feel your body freeze... almost as if you dont move he wont see you...')
                        print(
                            'but he does see you... he pulls a blade out of his armor and starts to run toward you...')
                        print(
                            'You turn to run... the lights still flickering makes it hard to see where you are going... you just came from door H1...')
                        print('so that only leaves you with two choices')
                        two_choice_door = input('Do you run through door 2B or M3?     ')
                        if two_choice_door.lower() == 'm3':
                            print('')
                            print('The door is stuck... ')
                            print('you start to panic...')
                            print('the alien is almost at you...')
                            print('Suddenly the door springs open... and you feel a hand grab you and pull you in...')
                            print('The door closes behind you with a click of the lock')
                            print(
                                'You start to fight... kicking and punching and defending yourself the best you can...')
                            print('')
                            print('you then realize the hand that pulled you in was one of your crew members...')
                            print('\"I\'m so sorry! I thought you were one of them...\"')
                            print('You hear the alien clawing and pounding on the door behind you...')
                            print('')
                            print('\"Dont worry about him. I locked the door and this is triple plated chromium...')
                            print(
                                'unless he can get his fat little fingers in the manual release console... I think we\'re safe for now...\"')
                            print(
                                'Although you hear his words you cant help but think he will come through the door at any moment. ')
                            print(
                                '\"Have you been walking around this alien infested station with no protection???\" He asks')
                            print('\" You better take one of these... the last two in the science lab...\"')
                            print('He hands you a slightly dinged up battle rifle.. ')
                            addToItems('Battle Rifle')
                            print('')
                            print(Items)
                            print('')
                            print('\"I didnt want one of those freaks to find it...\"')
                            print('you thank him and quickly rack a proton round in the weapon')
                            print('you look around... you see the only way out is the ladder...')
                            up_ladder = input("do you go up the ladder? yes/no    ")
                            if up_ladder.lower() == "yes":
                                print('')
                                print('You look back at the fellow crew mate... ')
                                print('\"I\'m going to go look for a suit...\" you say to him')
                                print('\"It\'ll be up there if those things havent got to it yet...\" he says')
                                print('you look up the shoot where the ladder leads... its pitch black... ')
                                print('\"HEY!\" he says... \"take this too...\"')
                                print(
                                    'He tosses you a flashlightc attachment for your resperator... you attach it at push the button on the side...')
                                addToItems('Head Light')
                                print('')
                                print(Items)
                                print('')
                                print('You start the climb... one rung at a time you start going up... ')
                                print('you look up... and you can see its about 100ft to the top...')
                                print(
                                    'about halfway up the ladder you hear a loud explosion from below... you see fire at the bottom...')
                                press_on = input(
                                    'do you continue up the ladder or climb down to see?  continue/climb down     ')
                                if press_on.lower() == "continue":
                                    print('')
                                    print('you reach the top... everything is dark.. you\'re in the weapons bay... ')
                                    print('but it looks like its been raided... ')
                                    print(
                                        'through the single beam from your light you can see broken items and empty shelves')
                                    print('you see an advanced combat suit! you walk over to it...')
                                    print(
                                        'you pick it up and it falls apart in your hands... it is beyond damaged.. its destroyed..')
                                    print(
                                        'you hear a *clink* and *clunk* of someone or something coming up the ladder..')
                                    print('')
                                    print('there has to be another suit up here...')
                                    print('you continue to look though the rubble... ')
                                    print('to no avail... theres nothing here!')
                                    print(
                                        'the noise is getting closer and you can tell whatever it is... its almost to the top...')
                                    print('with your light fixated on the top of the ladder...')
                                    print('you have no chance agains an alien without a combat suit...')
                                    print('walking backward you trip...')
                                    print('you quickly get your light back on the top of the ladder...')
                                    print(
                                        'it\'s too late, a creature energes from the hole where the ladder came up... ')
                                    print('you suddenly remember... your weapon... ')
                                    print('on the ground next to you...')
                                    print(
                                        'the creature starts running toward you... you feel the rifle on the floor... quickly shoulder it..')
                                    print(
                                        '\"SUCK ON THIS!\" you unload your weapon on the creature as he is almost on top of you... ')
                                    print(
                                        'showers of blue blood rain down on you as he smacks the ground in front of you... ')
                                    print(
                                        'you stand up and look at where the alien body lies in a pool of blue jello...')
                                    print('the thing you tripped on was a combat suit!')
                                    print(
                                        'you pick it up and inspect it... press the button near the neck of the suit...')
                                    print('the smart wear technology kicks in and attaches itself to your body...')
                                    addToItems('Advanced Combat Suit')
                                    print('')
                                    print(Items)  # keeps printing doubles
                                    print('')
                                    Down_ladder = input('Head back down the ladder?  yes/no    ')
                                    if Down_ladder.lower() == "yes":
                                        print('')
                                        print('You head down the ladder back toward where you heard the explosion')
                                        print('now that you have your combat suit you feel a little more confident...')
                                        print('you start down the ladder... one rung at a time... ')
                                        print('a thick layer of smoke still blankets the science lab... ')
                                        print('you look around for the other crew member...')
                                        print(
                                            'your heart starts to think when you realize the alien that came up the ladder probably killed him.')
                                        print('')
                                        print('but wait... you see his hand sticking out from a pile of rubble... ')
                                        print(
                                            'you run over to grab his hand. you grab hold and pull to try to get him out from the pile on top of him...')
                                        print(
                                            'but when you pull all you get is a severed arm that slips out of the wreck...')
                                        print('')
                                        print(
                                            'you can hear more shooting coming from down the hall you exit the door and are now back in the main corridor...')
                                        print(
                                            'suddenly your combat suit lights up and you see a heat signature coming around the corner...')
                                        print('its not human... the heat is too cold... and the image is huge!')
                                        print('you shoulder your rifle again...')
                                        print(
                                            'the creature emerges from the corner and before he can spot you... you vaporize him with your rifle... ')
                                        print(
                                            'round after round you put so many holes in the creature that he looks like a mixture of blue and swiss cheese..')
                                        print('you see more heat signatures... these look humanoid...')
                                        print('you run to them...')
                                        print('')
                                        print('its other members of the crew! alive! ')
                                        print('\" Are you okay?!\" you shout at them...')
                                        print('\" We\'re alright... just a little banged up...\"')
                                        print(
                                            'you ask if they are able to walk and if they know where the rest of the crew is...')
                                        print(
                                            'they tell you that they can walk and that the other members of the crew are hiding out in various compartments and their quarters through out the station...')
                                        print(
                                            '\"I have everything i need to activate the escape pods and get us out! you get these people to safety and ill get to the bridge...')
                                        print('')
                                        bridge = input('Continue to bridge? yes/no    ')
                                        if bridge.lower() == 'yes':
                                            print(
                                                'as soon as the other crew members are out of sight you start toward the bridge...')
                                            print('your combat suit starts beeping...')
                                            print('\"WHAT NOW?!\"')
                                            print(
                                                'you turn around and another alien creature is coming straight toward you.')
                                            print('again you shoulder your rifle...')
                                            print('you get the creature in your sights... pull the trigger...')
                                            print('')
                                            print('**CLICK**')
                                            print('')
                                            print('your battle rifle is jammed')
                                            print(
                                                'you turn around and the door is right behind you... its 2b! the final door!')
                                            print(
                                                'you pry the door open and get inside before the creature reaches you...')
                                            print(
                                                'you get the door shut and locked... then try to activate the turbo lift...')
                                            print(
                                                'The turbo lift is stuck... you\'ll need to engauge the manual override')
                                            print('THUD!! THUD!! ')
                                            print('')
                                            print('there is an alien creature outside trying to break down the door...')
                                            print(
                                                'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                                            print(
                                                'you turn on the lift crank and feel the turbo lift start to rise... ')
                                            print('you\'re safe... for now... ')
                                            print(
                                                'you look at your rifle... its out of ammo... must have wasted it all on that last pile of blue slime...')
                                            print('wait... there is an emergency compartment on the turbo lift...')
                                            print('perhaps theres ammo in there...')
                                            print('')
                                            print('you open the compartent...')
                                            print(
                                                'medical supplies... no... flashlight... no... various hand tools and such... NO!')
                                            print('There! in the back! a fresh cartridge! ')
                                            addToItems('Ammo')
                                            print('')
                                            print(Items)
                                            print('')
                                            print('you feel the lift stop... you must be at the top... main bridge... ')
                                            print('you open the door...')
                                            print(
                                                'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                                            print(
                                                'they are all gathered around the computer in the center of the room..')
                                            print('suddenly the door latch engauges.. and causes a loud thunk... ')
                                            print('they all whip around... ')
                                            print('they are armed to the teeth with space age looking weapons... ')
                                            print('they open fire...')
                                            print('but you quickly jump behind the nearest control panel...')
                                            print('you see the panel you need to access..')
                                            go_for_it = input(
                                                'despite the enemy fire, should you go for the panel or not?  yes/no    ')
                                            if go_for_it.lower() == 'yes':
                                                print('you make a run for it! ')
                                                print(
                                                    'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                                                print('GAME OVER...')
                                                break
                                            elif go_for_it.lower() == 'no':
                                                print('what can you do??')
                                                print('you look up...')
                                                print('there is a mirror on the cieling... ')
                                                print('you see there are 2 on the right... and three on the left... ')
                                                print('there is a pause in the shooting... ')
                                                print('you spring up and take out the two on the right... ')
                                                print('then duck back down before the shooting starts back up...')
                                                print(
                                                    'there is a thick cloud of smoke billowing from the console you are ducking behind...')
                                                print(
                                                    'you dive to the next console over... but its not the one you need... ')
                                                print('one shot strikes your leg...')
                                                print('but its just a flesh wound... you\'ll take care of it later...')
                                                print(
                                                    'you look up again at the mirror... they are standing in a line...')
                                                print('still shooting at where you just were... ')
                                                print('did they not see you move to the other console??? ')
                                                print('you charge your weapon to unload every proton round at once...')
                                                print('deep breath.... whoooooo')
                                                print('you stand up and take aim at the first ones head...')
                                                print('fire your last round...')
                                                print(
                                                    'it goes right though all three of them and a spray of blue litters the bridge...')
                                                print('')
                                                print(
                                                    'it goes quiet other than the pops and cracks of the station slowly falling apart from all of the explosions and gun fire...')
                                                print(
                                                    'you quickly run to the main console and press the cracked screen... ')
                                                print('a crackled voice comes though the intecom...')
                                                print(
                                                    'its the computer \" I\'m sorry the station is on full lockdown, without the access code you can not authorize any funtions\"')
                                                access_codes = input('Please enter access code...    ')
                                                if access_codes == '78-649-036':
                                                    print('access granted')
                                                    print('what function would you like to access?')
                                                    first_function = input(
                                                        'what do you want to do first? activate pods or alert crew?')
                                                    if first_function == 'activate pods':
                                                        print('')
                                                        print('\"Computer! Activate escape pods!\"')
                                                        print('Escape pods active')
                                                        print('\"Computer! Open a channel!')
                                                        print(
                                                            'the signal that a channel is open comes over the intercom...')
                                                        print(
                                                            '\" Attention crew! i am about to activate all escape pods!')
                                                        print(
                                                            'Hurry to the nearest escape pod with as many people as possible!\"')
                                                        print(
                                                            '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                                        print('\"COMPUTER!\" you yell...')
                                                        print(
                                                            '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                                        print('the computer agknowledges and confirms')
                                                        print(
                                                            'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                                        print(
                                                            'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                                        captain = input(
                                                            "Do you check the captains quarters?  yes/no     ")
                                                        if captain == 'no':
                                                            print('')
                                                            print('you\'re sure he\'s dead... ')
                                                            print(
                                                                'you climb into the escape pod entrance on the bridge and eject yourself')
                                                            print(
                                                                'you are suddenly drifting in space toward the planet...')
                                                            print(
                                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                                            print(
                                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                                            print('disoriented you climb from the pod... ')
                                                            print(
                                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                                            print(
                                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                                            break
                                                        elif captain == 'yes':
                                                            print('')
                                                            print('you open the door to the captains quarters...')
                                                            print('there he is lifeless in front of his desk...')
                                                            print('you check for a pulse...')
                                                            print('there is a pulse! but its faint...')
                                                            print(
                                                                'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                                            print(
                                                                'you take one last look for human life signs...no one... ')
                                                            print(
                                                                'you climb into the escape pod entrance on the bridge and eject the both of you')
                                                            print(
                                                                'you are suddenly drifting in space toward the planet...')
                                                            print(
                                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                                            print(
                                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                                            print('disoriented you climb from the pod... ')
                                                            print(
                                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                                            print(
                                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                                            break

                                                    elif first_function == 'alert crew':
                                                        print('')
                                                        print(
                                                            'the signal that a channel is open comes over the intercom...')
                                                        print(
                                                            '\" Attention crew! i am about to activate all escape pods! Hurry to the nearest escape pod with as many people as possible!\"')
                                                        print(
                                                            '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                                        print('\"COMPUTER!\" you yell...')
                                                        print(
                                                            '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                                        print('the computer agknowledges and confirms')
                                                        print(
                                                            'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                                        print(
                                                            'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                                        captain = input(
                                                            "Do you check the captains quarters?  yes/no     ")
                                                        if captain == 'no':
                                                            print('')
                                                            print('you\'re sure he\'s dead... ')
                                                            print(
                                                                'you climb into the escape pod entrance on the bridge and eject yourself')
                                                            print(
                                                                'you are suddenly drifting in space toward the planet...')
                                                            print(
                                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                                            print(
                                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                                            print('disoriented you climb from the pod... ')
                                                            print(
                                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                                            print(
                                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                                            break
                                                        elif captain == 'yes':
                                                            print('')
                                                            print('you open the door to the captains quarters...')
                                                            print('there he is lifeless in front of his desk...')
                                                            print('you check for a pulse...')
                                                            print('there is a pulse! but its faint...')
                                                            print(
                                                                'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                                            print(
                                                                'you take one last look for human life signs...no one... ')
                                                            print(
                                                                'you climb into the escape pod entrance on the bridge and eject the both of you')
                                                            print(
                                                                'you are suddenly drifting in space toward the planet...')
                                                            print(
                                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                                            print(
                                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                                            print('disoriented you climb from the pod... ')
                                                            print(
                                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                                            print(
                                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                                            break
                                                else:
                                                    print('access denied')
                                                    print(
                                                        'remember those codes! and dont forget the - after the numbers. scroll back to engeneering if you have to..')
                                                    access_codes2 = input(
                                                        'Please reenter access code... (last attempt)')
                                                    if access_codes2 == '78-649-036':
                                                        print('')
                                                        print('access granted')
                                                    print('what function would you like to access?')
                                                    first_function = input(
                                                        'what do you want to do first? activate pods or alert crew?')
                                                    if first_function == 'activate pods':
                                                        print('')
                                                        print('\"Computer! Activate escape pods!\"')
                                                        print('Escape pods active')
                                                        print('\"Computer! Open a channel!')
                                                        print(
                                                            'the signal that a channel is open comes over the intercom...')
                                                        print(
                                                            '\" Attention crew! i am about to activate all escape pods!')
                                                        print(
                                                            'Hurry to the nearest escape pod with as many people as possible!\"')
                                                        print(
                                                            '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                                        print('\"COMPUTER!\" you yell...')
                                                        print(
                                                            '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                                        print('the computer agknowledges and confirms')
                                                        print(
                                                            'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                                        print(
                                                            'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                                        captain = input(
                                                            "Do you check the captains quarters?  yes/no     ")
                                                        if captain == 'no':
                                                            print('')
                                                            print('you\'re sure he\'s dead... ')
                                                            print(
                                                                'you climb into the escape pod entrance on the bridge and eject yourself')
                                                            print(
                                                                'you are suddenly drifting in space toward the planet...')
                                                            print(
                                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                                            print(
                                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                                            print('disoriented you climb from the pod... ')
                                                            print(
                                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                                            print(
                                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                                            break
                                                        elif captain == 'yes':
                                                            print('')
                                                            print('you open the door to the captains quarters...')
                                                            print('there he is lifeless in front of his desk...')
                                                            print('you check for a pulse...')
                                                            print('there is a pulse! but its faint...')
                                                            print(
                                                                'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                                            print(
                                                                'you take one last look for human life signs...no one... ')
                                                            print(
                                                                'you climb into the escape pod entrance on the bridge and eject the both of you')
                                                            print(
                                                                'you are suddenly drifting in space toward the planet...')
                                                            print(
                                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                                            print(
                                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                                            print('disoriented you climb from the pod... ')
                                                            print(
                                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                                            print(
                                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                                            break
                                    elif Down_ladder.lower() == "no":
                                        print('you have no choice you must go down the ladder...')
                                        print('you head down the ladder..')
                                        print(
                                            'PLEASE CHECK BACK LATER... THE GAME IS STILL BEING WRITTEN... GREAT JOB SO FAR')
                                    else:
                                        print('not sure what you typed... but it was not yes or no... start over... ')
                                else:
                                    print(
                                        'you get almost to the bottom when another explosion from an alien frag granade engulfs your body... ')
                                    print('um... you dead... GAME OVER...')
                                    break
                            elif up_ladder.lower() == "no":
                                print('\" I think ill stay...\"')
                            else:
                                print('dang... GAME OVER...')
                                break
                        elif two_choice_door.lower() == '2B':  # NOT WORKING>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            print('The door is stuck... he is almost at you... ')
                            print('wait this is a turbo lift... ')
                            print('this leads to the bridge... ')
                            print('but you know the access codes and you have plenty of oxygen.')
                            print('should you just get to the bridge without the rest of the item?')
                            continue_to_bridge = input('Continue to bridge?  yes/no     ')
                            if continue_to_bridge.lower == 'yes':
                                print('The turbo lift is stuck... you\'ll need to engauge the manual override')
                                print('THUD!! THUD!! ')
                                print('')
                                print('the alien creature is trying to break down the door...')
                                print(
                                    'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                                print('you turn on the lift crank and feel the turbo lift start to rise... ')
                                print('you\'re safe... for now... ')
                                print('')
                                print('you feel the lift stop... you must be at the top... main bridge... ')
                                print('you open the door...')
                                print(
                                    'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                                print('they are all gathered around the computer in the center of the room..')
                                print('suddenly the door latch engauges.. and causes a loud thunk... ')
                                print('they all whip around... ')
                                print('they are armed to the teeth with space age looking weapons... ')
                                print('they open fire...')
                                print(
                                    'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                                print('GAME OVER...')
                                break
                            elif continue_to_bridge == "no":
                                print(
                                    'the alien is still outside the door... he is pounding feriously trying to get in...')
                                print(
                                    'theres nothing you can do other than engauge the manual override and press on to the bridge...')
                                print('THUD!! THUD!! ')
                                print('')
                                print('the alien creature is trying to break down the door...')
                                print(
                                    'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                                print('you turn on the lift crank and feel the turbo lift start to rise... ')
                                print('you\'re safe... for now... ')
                                print('')
                                print('you feel the lift stop... you must be at the top... main bridge... ')
                                print('you open the door...')
                                print(
                                    'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                                print('they are all gathered around the computer in the center of the room..')
                                print('suddenly the door latch engauges.. and causes a loud thunk... ')
                                print('they all whip around... ')
                                print('they are armed to the teeth with space age looking weapons... ')
                                print('they open fire...')
                                print(
                                    'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                                print('GAME OVER...')
                                break
                            else:
                                print('invalid answer... you must have had a leak in your oxygen... GAME OVER...')
                                break
            else:
                print('')
                print('')
                print(
                    'you push him aside regarless of if he is alive or not \" I have a job to do\" you tell yourself.')
                print(
                    'you cannot figure out how to turn on the computer. you fidget frantically... open the side pannel and start pulling wires and pushing all buttons')
                print(' \" Damn it man! Im a doctor! not a computer technicion!\" ')
                print(
                    'You reach in the back of the console... your hand slips and you touch an exposed wire... ten thousand volts go streaming through your body... you shake violently and fall to the ground next to the lifeless chief engineer... you smell burning hair and flesh... you go limp... and slip into darkness... GAME OVER...')
                break
        elif main_engineering.lower() == "turn back":
            print('')
            print('')
            print(
                'you turn back. passing through door H1... suddenly out of now where an unknown alien species comes from around the corner..')
            print(
                'you are frozen with fear... the alien comes closer to you and you can see its sharp claw like hands... ')
            print('before you can run it plunges its claw through your chest severing your heart... ')
            print('you feel the blood run out of your veins and you fall to the ground... GAME OVER...')
            break
    elif door_1.lower() == "m3":
        print('')
        print('The door is stuck... ')
        print('you start to panic...')
        print('the alien is almost at you...')
        print('Suddenly the door springs open... and you feel a hand grab you and pull you in...')
        print('The door closes behind you with a click of the lock')
        print('You start to fight... kicking and punching and defending yourself the best you can...')
        print('')
        print('you then realize the hand that pulled you in was one of your crew members...')
        print('\"I\'m so sorry! I thought you were one of them...\"')
        print('You hear the alien clawing and pounding on the door behind you...')
        print('')
        print('\"Dont worry about him. I locked the door and this is triple plated chromium...')
        print(
            'unless he can get his fat little fingers in the manual release console... I think we\'re safe for now...\"')
        print('Although you hear his words you cant help but think he will come through the door at any moment. ')
        print('\"Have you been walking around this alien infested station with no protection???\" He asks')
        print('\" You better take one of these... the last two in the science lab...\"')
        print('He hands you a slightly dinged up battle rifle.. ')
        addToItems('Battle Rifle')
        print('')
        print(Items)
        print('')
        print('\"I didnt want one of those freaks to find it...\"')
        print('you thank him and quickly rack a proton round in the weapon')
        print('you look around... you see the only way out is the ladder...')
        up_ladder = input("do you go up the ladder? yes/no    ")
        if up_ladder.lower() == "yes":
            print('')
            print('You look back at the fellow crew mate... ')
            print('\"I\'m going to go look for a suit...\" you say to him')
            print('\"It\'ll be up there if those things havent got to it yet...\" he says')
            print('you look up the shoot where the ladder leads... its pitch black... ')
            print('\"HEY!\" he says... \"take this too...\"')
            print(
                'He tosses you a flashlightc attachment for your resperator... you attach it at push the button on the side...')
            addToItems('Head Light')
            print('')
            print(Items)
            print('')
            print('You start the climb... one rung at a time you start going up... ')
            print('you look up... and you can see its about 100ft to the top...')
            print('about halfway up the ladder you hear a loud explosion from below... you see fire at the bottom...')
            press_on = input('do you continue up the ladder or climb down to see?  continue/climb down     ')
            if press_on.lower() == "continue":
                print('')
                print('you reach the top... everything is dark.. you\'re in the weapons bay... ')
                print('but it looks like its been raided... ')
                print('through the single beam from your light you can see broken items and empty shelves')
                print('you see an advanced combat suit! you walk over to it...')
                print('you pick it up and it falls apart in your hands... it is beyond damaged.. its destroyed..')
                print('you hear a *clink* and *clunk* of someone or something coming up the ladder..')
                print('')
                print('there has to be another suit up here...')
                print('you continue to look though the rubble... ')
                print('to no avail... theres nothing here!')
                print('the noise is getting closer and you can tell whatever it is... its almost to the top...')
                print('with your light fixated on the top of the ladder...')
                print('you have no chance agains an alien without a combat suit...')
                print('walking backward you trip...')
                print('you quickly get your light back on the top of the ladder...')
                print('it\'s too late, a creature energes from the hole where the ladder came up... ')
                print('you suddenly remember... your weapon... ')
                print('on the ground next to you...')
                print(
                    'the creature starts running toward you... you feel the rifle on the floor... quickly shoulder it..')
                print('\"SUCK ON THIS!\" you unload your weapon on the creature as he is almost on top of you... ')
                print('showers of blue blood rain down on you as he smacks the ground in front of you... ')
                print('you stand up and look at where the alien body lies in a pool of blue jello...')
                print('the thing you tripped on was a combat suit!')
                print('you pick it up and inspect it... press the button near the neck of the suit...')
                print('the smart wear technology kicks in and attaches itself to your body...')
                addToItems('Advanced Combat Suit')
                print('')
                print(Items)  # keeps printing doubles
                print('')
                Down_ladder = input('Head back down the ladder?  yes/no    ')
                if Down_ladder.lower() == "yes":
                    print('')
                    print('You head down the ladder back toward where you heard the explosion')
                    print('now that you have your combat suit you feel a little more confident...')
                    print('you start down the ladder... one rung at a time... ')
                    print('a thick layer of smoke still blankets the science lab... ')
                    print('you look around for the other crew member...')
                    print(
                        'your heart starts to think when you realize the alien that came up the ladder probably killed him.')
                    print('')
                    print('but wait... you see his hand sticking out from a pile of rubble... ')
                    print(
                        'you run over to grab his hand. you grab hold and pull to try to get him out from the pile on top of him...')
                    print('but when you pull all you get is a severed arm that slips out of the wreck...')
                    print('')
                    print(
                        'you can hear more shooting coming from down the hall you exit the door and are now back in the main corridor...')
                    print(
                        'suddenly your combat suit lights up and you see a heat signature coming around the corner...')
                    print('its not human... the heat is too cold... and the image is huge!')
                    print('you shoulder your rifle again...')
                    print(
                        'the creature emerges from the corner and before he can spot you... you vaporize him with your rifle... ')
                    print(
                        'round after round you put so many holes in the creature that he looks like a mixture of blue and swiss cheese..')
                    print('you see more heat signatures... these look humanoid...')
                    print('you run to them...')
                    print('')
                    print('its other members of the crew! alive! ')
                    print('\" Are you okay?!\" you shout at them...')
                    print('\" We\'re alright... just a little banged up...\"')
                    print('you ask if they are able to walk and if they know where the rest of the crew is...')
                    print(
                        'they tell you that they can walk and that the other members of the crew are hiding out in various compartments and their quarters through out the station...')
                    print(
                        '\"I have everything i need to activate the escape pods and get us out! you get these people to safety and ill get to the bridge...')
                    print('')
                    bridge = input('Continue to bridge? yes/no    ')
                    if bridge.lower() == 'yes':
                        print('as soon as the other crew members are out of sight you start toward the bridge...')
                        print('your combat suit starts beeping...')
                        print('\"WHAT NOW?!\"')
                        print('you turn around and another alien creature is coming straight toward you.')
                        print('again you shoulder your rifle...')
                        print('you get the creature in your sights... pull the trigger...')
                        print('')
                        print('**CLICK**')
                        print('')
                        print('your battle rifle is jammed')
                        print('you turn around and the door is right behind you... its 2b! the final door!')
                        print('you pry the door open and get inside before the creature reaches you...')
                        print('you get the door shut and locked... then try to activate the turbo lift...')
                        print('The turbo lift is stuck... you\'ll need to engauge the manual override')
                        print('THUD!! THUD!! ')
                        print('')
                        print('there is an alien creature outside trying to break down the door...')
                        print(
                            'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                        print('you turn on the lift crank and feel the turbo lift start to rise... ')
                        print('you\'re safe... for now... ')
                        print(
                            'you look at your rifle... its out of ammo... must have wasted it all on that last pile of blue slime...')
                        print('wait... there is an emergency compartment on the turbo lift...')
                        print('perhaps theres ammo in there...')
                        print('')
                        print('you open the compartent...')
                        print('medical supplies... no... flashlight... no... various hand tools and such... NO!')
                        print('There! in the back! a fresh cartridge! ')
                        addToItems('Ammo')
                        print('')
                        print(Items)
                        print('')
                        print('you feel the lift stop... you must be at the top... main bridge... ')
                        print('you open the door...')
                        print(
                            'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                        print('they are all gathered around the computer in the center of the room..')
                        print('suddenly the door latch engauges.. and causes a loud thunk... ')
                        print('they all whip around... ')
                        print('they are armed to the teeth with space age looking weapons... ')
                        print('they open fire...')
                        print('but you quickly jump behind the nearest control panel...')
                        print('you see the panel you need to access..')
                        go_for_it = input('despite the enemy fire, should you go for the panel or not?  yes/no    ')
                        if go_for_it.lower() == 'yes':
                            print('you make a run for it! ')
                            print(
                                'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                            print('GAME OVER...')
                            break
                        elif go_for_it.lower() == 'no':
                            print('what can you do??')
                            print('you look up...')
                            print('there is a mirror on the cieling... ')
                            print('you see there are 2 on the right... and three on the left... ')
                            print('there is a pause in the shooting... ')
                            print('you spring up and take out the two on the right... ')
                            print('then duck back down before the shooting starts back up...')
                            print(
                                'there is a thick cloud of smoke billowing from the console you are ducking behind...')
                            print('you dive to the next console over... but its not the one you need... ')
                            print('one shot strikes your leg...')
                            print('but its just a flesh wound... you\'ll take care of it later...')
                            print('you look up again at the mirror... they are standing in a line...')
                            print('still shooting at where you just were... ')
                            print('did they not see you move to the other console??? ')
                            print('you charge your weapon to unload every proton round at once...')
                            print('deep breath.... whoooooo')
                            print('you stand up and take aim at the first ones head...')
                            print('fire your last round...')
                            print('it goes right though all three of them and a spray of blue litters the bridge...')
                            print('')
                            print(
                                'it goes quiet other than the pops and cracks of the station slowly falling apart from all of the explosions and gun fire...')
                            print('you quickly run to the main console and press the cracked screen... ')
                            print('a crackled voice comes though the intecom...')
                            print(
                                'its the computer \" I\'m sorry the station is on full lockdown, without the access code you can not authorize any funtions\"')
                            access_codes = input('Please enter access code...    ')
                            if access_codes == '78-649-036':
                                print('access granted')
                                print('what function would you like to access?')
                                first_function = input('what do you want to do first? activate pods or alert crew?')
                                if first_function == 'activate pods':
                                    print('')
                                    print('\"Computer! Activate escape pods!\"')
                                    print('Escape pods active')
                                    print('\"Computer! Open a channel!')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print('\" Attention crew! i am about to activate all escape pods!')
                                    print('Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break

                                elif first_function == 'alert crew':
                                    print('')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print(
                                        '\" Attention crew! i am about to activate all escape pods! Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                            else:
                                print('access denied')
                                print(
                                    'remember those codes! and dont forget the - after the numbers. scroll back to engeneering if you have to..')
                                access_codes2 = input('Please reenter access code... (last attempt)')
                                if access_codes2 == '78-649-036':
                                    print('')
                                    print('access granted')
                                print('what function would you like to access?')
                                first_function = input('what do you want to do first? activate pods or alert crew?')
                                if first_function == 'activate pods':
                                    print('')
                                    print('\"Computer! Activate escape pods!\"')
                                    print('Escape pods active')
                                    print('\"Computer! Open a channel!')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print('\" Attention crew! i am about to activate all escape pods!')
                                    print('Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break

                                else:
                                    print(
                                        'wow... you had two chances guess you should play again and maybe write it down... GAME OVER...')
                    elif bridge.lower() == 'no':
                        print('you have no choice... you must proceed...')
                        print('as soon as the other crew members are out of sight you start toward the bridge...')
                        print('your combat suit starts beeping...')
                        print('\"WHAT NOW?!\"')
                        print('you turn around and another alien creature is coming straight toward you.')
                        print('again you shoulder your rifle...')
                        print('you get the creature in your sights... pull the trigger...')
                        print('')
                        print('**CLICK**')
                        print('')
                        print('your battle rifle is jammed')
                        print('you turn around and the door is right behind you... its 2b! the final door!')
                        print('you pry the door open and get inside before the creature reaches you...')
                        print('you get the door shut and locked... then try to activate the turbo lift...')
                        print('The turbo lift is stuck... you\'ll need to engauge the manual override')
                        print('THUD!! THUD!! ')
                        print('')
                        print('there is an alien creature outside trying to break down the door...')
                        print(
                            'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                        print('you turn on the lift crank and feel the turbo lift start to rise... ')
                        print('you\'re safe... for now... ')
                        print(
                            'you look at your rifle... its out of ammo... must have wasted it all on that last pile of blue slime...')
                        print('wait... there is an emergency compartment on the turbo lift...')
                        print('perhaps theres ammo in there...')
                        print('')
                        print('you open the compartent...')
                        print('medical supplies... no... flashlight... no... various hand tools and such... NO!')
                        print('There! in the back! a fresh cartridge! ')
                        addToItems('Ammo')
                        print('')
                        print(Items)
                        print('')
                        print('you feel the lift stop... you must be at the top... main bridge... ')
                        print('you open the door...')
                        print(
                            'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                        print('they are all gathered around the computer in the center of the room..')
                        print('suddenly the door latch engauges.. and causes a loud thunk... ')
                        print('they all whip around... ')
                        print('they are armed to the teeth with space age looking weapons... ')
                        print('they open fire...')
                        print('but you quickly jump behind the nearest control panel...')
                        print('you see the panel you need to access..')
                        go_for_it = input('despite the enemy fire, should you go for the panel or not?  yes/no    ')
                        if go_for_it.lower() == 'yes':
                            print('you make a run for it! ')
                            print(
                                'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                            print('GAME OVER...')
                            break
                        elif go_for_it.lower() == 'no':
                            print('what can you do??')
                            print('you look up...')
                            print('there is a mirror on the cieling... ')
                            print('you see there are 2 on the right... and three on the left... ')
                            print('there is a pause in the shooting... ')
                            print('you spring up and take out the two on the right... ')
                            print('then duck back down before the shooting starts back up...')
                            print(
                                'there is a thick cloud of smoke billowing from the console you are ducking behind...')
                            print('you dive to the next console over... but its not the one you need... ')
                            print('one shot strikes your leg...')
                            print('but its just a flesh wound... you\'ll take care of it later...')
                            print('you look up again at the mirror... they are standing in a line...')
                            print('still shooting at where you just were... ')
                            print('did they not see you move to the other console??? ')
                            print('you charge your weapon to unload every proton round at once...')
                            print('deep breath.... whoooooo')
                            print('you stand up and take aim at the first ones head...')
                            print('fire your last round...')
                            print('it goes right though all three of them and a spray of blue litters the bridge...')
                            print('')
                            print(
                                'it goes quiet other than the pops and cracks of the station slowly falling apart from all of the explosions and gun fire...')
                            print('you quickly run to the main console and press the cracked screen... ')
                            print('a crackled voice comes though the intecom...')
                            print(
                                'its the computer \" I\'m sorry the station is on full lockdown, without the access code you can not authorize any funtions\"')
                            access_codes = input('Please enter access code...    ')
                            if access_codes == '78-649-036':
                                print('access granted')
                                print('what function would you like to access?')
                                first_function = input('what do you want to do first? activate pods or alert crew?')
                                if first_function == 'activate pods':
                                    print('')
                                    print('\"Computer! Activate escape pods!\"')
                                    print('Escape pods active')
                                    print('\"Computer! Open a channel!')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print('\" Attention crew! i am about to activate all escape pods!')
                                    print('Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break

                                elif first_function == 'alert crew':
                                    print('')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print(
                                        '\" Attention crew! i am about to activate all escape pods! Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                elif Down_ladder.lower() == "no":
                    print('you have no choice you must go down the ladder...')
                    print('you head down the ladder..')
                    print('')
                    print('')
                    print('You head down the ladder back toward where you heard the explosion')
                    print('now that you have your combat suit you feel a little more confident...')
                    print('you start down the ladder... one rung at a time... ')
                    print('a thick layer of smoke still blankets the science lab... ')
                    print('you look around for the other crew member...')
                    print(
                        'your heart starts to think when you realize the alien that came up the ladder probably killed him.')
                    print('')
                    print('but wait... you see his hand sticking out from a pile of rubble... ')
                    print(
                        'you run over to grab his hand. you grab hold and pull to try to get him out from the pile on top of him...')
                    print('but when you pull all you get is a severed arm that slips out of the wreck...')
                    print('')
                    print(
                        'you can hear more shooting coming from down the hall you exit the door and are now back in the main corridor...')
                    print(
                        'suddenly your combat suit lights up and you see a heat signature coming around the corner...')
                    print('its not human... the heat is too cold... and the image is huge!')
                    print('you shoulder your rifle again...')
                    print(
                        'the creature emerges from the corner and before he can spot you... you vaporize him with your rifle... ')
                    print(
                        'round after round you put so many holes in the creature that he looks like a mixture of blue and swiss cheese..')
                    print('you see more heat signatures... these look humanoid...')
                    print('you run to them...')
                    print('')
                    print('its other members of the crew! alive! ')
                    print('\" Are you okay?!\" you shout at them...')
                    print('\" We\'re alright... just a little banged up...\"')
                    print('you ask if they are able to walk and if they know where the rest of the crew is...')
                    print(
                        'they tell you that they can walk and that the other members of the crew are hiding out in various compartments and their quarters through out the station...')
                    print(
                        '\"I have everything i need to activate the escape pods and get us out! you get these people to safety and ill get to the bridge...')
                    print('')
                    bridge = input('Continue to bridge? yes/no    ')
                    if bridge.lower() == 'yes':
                        print('as soon as the other crew members are out of sight you start toward the bridge...')
                        print('your combat suit starts beeping...')
                        print('\"WHAT NOW?!\"')
                        print('you turn around and another alien creature is coming straight toward you.')
                        print('again you shoulder your rifle...')
                        print('you get the creature in your sights... pull the trigger...')
                        print('')
                        print('**CLICK**')
                        print('')
                        print('your battle rifle is jammed')
                        print('you turn around and the door is right behind you... its 2b! the final door!')
                        print('you pry the door open and get inside before the creature reaches you...')
                        print('you get the door shut and locked... then try to activate the turbo lift...')
                        print('The turbo lift is stuck... you\'ll need to engauge the manual override')
                        print('THUD!! THUD!! ')
                        print('')
                        print('there is an alien creature outside trying to break down the door...')
                        print(
                            'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                        print('you turn on the lift crank and feel the turbo lift start to rise... ')
                        print('you\'re safe... for now... ')
                        print(
                            'you look at your rifle... its out of ammo... must have wasted it all on that last pile of blue slime...')
                        print('wait... there is an emergency compartment on the turbo lift...')
                        print('perhaps theres ammo in there...')
                        print('')
                        print('you open the compartent...')
                        print('medical supplies... no... flashlight... no... various hand tools and such... NO!')
                        print('There! in the back! a fresh cartridge! ')
                        addToItems('Ammo')
                        print('')
                        print(Items)
                        print('')
                        print('you feel the lift stop... you must be at the top... main bridge... ')
                        print('you open the door...')
                        print(
                            'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                        print('they are all gathered around the computer in the center of the room..')
                        print('suddenly the door latch engauges.. and causes a loud thunk... ')
                        print('they all whip around... ')
                        print('they are armed to the teeth with space age looking weapons... ')
                        print('they open fire...')
                        print('but you quickly jump behind the nearest control panel...')
                        print('you see the panel you need to access..')
                        go_for_it = input('despite the enemy fire, should you go for the panel or not?  yes/no    ')
                        if go_for_it.lower() == 'yes':
                            print('you make a run for it! ')
                            print(
                                'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                            print('GAME OVER...')
                            break
                        elif go_for_it.lower() == 'no':
                            print('what can you do??')
                            print('you look up...')
                            print('there is a mirror on the cieling... ')
                            print('you see there are 2 on the right... and three on the left... ')
                            print('there is a pause in the shooting... ')
                            print('you spring up and take out the two on the right... ')
                            print('then duck back down before the shooting starts back up...')
                            print(
                                'there is a thick cloud of smoke billowing from the console you are ducking behind...')
                            print('you dive to the next console over... but its not the one you need... ')
                            print('one shot strikes your leg...')
                            print('but its just a flesh wound... you\'ll take care of it later...')
                            print('you look up again at the mirror... they are standing in a line...')
                            print('still shooting at where you just were... ')
                            print('did they not see you move to the other console??? ')
                            print('you charge your weapon to unload every proton round at once...')
                            print('deep breath.... whoooooo')
                            print('you stand up and take aim at the first ones head...')
                            print('fire your last round...')
                            print('it goes right though all three of them and a spray of blue litters the bridge...')
                            print('')
                            print(
                                'it goes quiet other than the pops and cracks of the station slowly falling apart from all of the explosions and gun fire...')
                            print('you quickly run to the main console and press the cracked screen... ')
                            print('a crackled voice comes though the intecom...')
                            print(
                                'its the computer \" I\'m sorry the station is on full lockdown, without the access code you can not authorize any funtions\"')
                            access_codes = input('Please enter access code...    ')
                            if access_codes == '78-649-036':
                                print('access granted')
                                print('what function would you like to access?')
                                first_function = input('what do you want to do first? activate pods or alert crew?')
                                if first_function == 'activate pods':
                                    print('')
                                    print('\"Computer! Activate escape pods!\"')
                                    print('Escape pods active')
                                    print('\"Computer! Open a channel!')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print('\" Attention crew! i am about to activate all escape pods!')
                                    print('Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break

                                elif first_function == 'alert crew':
                                    print('')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print(
                                        '\" Attention crew! i am about to activate all escape pods! Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                            else:
                                print('access denied')
                                print(
                                    'remember those codes! and dont forget the - after the numbers. scroll back to engeneering if you have to..')
                                access_codes2 = input('Please reenter access code... (last attempt)')
                                if access_codes2 == '78-649-036':
                                    print('access granted')
                                    print('what function would you like to access?')
                                    first_function = input('what do you want to do first? activate pods or alert crew?')
                                    if first_function == 'activate pods':
                                        print('')
                                        print('\"Computer! Activate escape pods!\"')
                                        print('Escape pods active')
                                        print('\"Computer! Open a channel!')
                                        print('the signal that a channel is open comes over the intercom...')
                                        print('\" Attention crew! i am about to activate all escape pods!')
                                        print('Hurry to the nearest escape pod with as many people as possible!\"')
                                        print(
                                            '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                        print('\"COMPUTER!\" you yell...')
                                        print(
                                            '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                        print('the computer agknowledges and confirms')
                                        print(
                                            'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                        print(
                                            'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                        captain = input("Do you check the captains quarters?  yes/no     ")
                                        if captain == 'no':
                                            print('')
                                            print('you\'re sure he\'s dead... ')
                                            print(
                                                'you climb into the escape pod entrance on the bridge and eject yourself')
                                            print('you are suddenly drifting in space toward the planet...')
                                            print(
                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                            print(
                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                            print('disoriented you climb from the pod... ')
                                            print(
                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                            print(
                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                            break
                                        elif captain == 'yes':
                                            print('')
                                            print('you open the door to the captains quarters...')
                                            print('there he is lifeless in front of his desk...')
                                            print('you check for a pulse...')
                                            print('there is a pulse! but its faint...')
                                            print(
                                                'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                            print('you take one last look for human life signs...no one... ')
                                            print(
                                                'you climb into the escape pod entrance on the bridge and eject the both of you')
                                            print('you are suddenly drifting in space toward the planet...')
                                            print(
                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                            print(
                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                            print('disoriented you climb from the pod... ')
                                            print(
                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                            print(
                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                            break

                                    elif first_function == 'alert crew':
                                        print('')
                                        print('the signal that a channel is open comes over the intercom...')
                                        print(
                                            '\" Attention crew! i am about to activate all escape pods! Hurry to the nearest escape pod with as many people as possible!\"')
                                        print(
                                            '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                        print('\"COMPUTER!\" you yell...')
                                        print(
                                            '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                        print('the computer agknowledges and confirms')
                                        print(
                                            'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                        print(
                                            'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                        captain = input("Do you check the captains quarters?  yes/no     ")
                                        if captain == 'no':
                                            print('')
                                            print('you\'re sure he\'s dead... ')
                                            print(
                                                'you climb into the escape pod entrance on the bridge and eject yourself')
                                            print('you are suddenly drifting in space toward the planet...')
                                            print(
                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                            print(
                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                            print('disoriented you climb from the pod... ')
                                            print(
                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                            print(
                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                            break
                                        elif captain == 'yes':
                                            print('')
                                            print('you open the door to the captains quarters...')
                                            print('there he is lifeless in front of his desk...')
                                            print('you check for a pulse...')
                                            print('there is a pulse! but its faint...')
                                            print(
                                                'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                            print('you take one last look for human life signs...no one... ')
                                            print(
                                                'you climb into the escape pod entrance on the bridge and eject the both of you')
                                            print('you are suddenly drifting in space toward the planet...')
                                            print(
                                                'you inter the atmosphere and find yourself plunging toward the planet...')
                                            print(
                                                'your body shakes and jolts until you feel your pod crash into the planet...')
                                            print('disoriented you climb from the pod... ')
                                            print(
                                                'you look up into the night sky and you see a bright flash as the station explodes...')
                                            print(
                                                'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                            break
                                else:
                                    print(
                                        'wow... you had two chances and you blew it... guess they all die... GOME OVER...')
                                    break




                    elif bridge.lower() == 'no':
                        print('you have no choice... you must proceed...')
                        print('as soon as the other crew members are out of sight you start toward the bridge...')
                        print('your combat suit starts beeping...')
                        print('\"WHAT NOW?!\"')
                        print('you turn around and another alien creature is coming straight toward you.')
                        print('again you shoulder your rifle...')
                        print('you get the creature in your sights... pull the trigger...')
                        print('')
                        print('**CLICK**')
                        print('')
                        print('your battle rifle is jammed')
                        print('you turn around and the door is right behind you... its 2b! the final door!')
                        print('you pry the door open and get inside before the creature reaches you...')
                        print('you get the door shut and locked... then try to activate the turbo lift...')
                        print('The turbo lift is stuck... you\'ll need to engauge the manual override')
                        print('THUD!! THUD!! ')
                        print('')
                        print('there is an alien creature outside trying to break down the door...')
                        print(
                            'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
                        print('you turn on the lift crank and feel the turbo lift start to rise... ')
                        print('you\'re safe... for now... ')
                        print(
                            'you look at your rifle... its out of ammo... must have wasted it all on that last pile of blue slime...')
                        print('wait... there is an emergency compartment on the turbo lift...')
                        print('perhaps theres ammo in there...')
                        print('')
                        print('you open the compartent...')
                        print('medical supplies... no... flashlight... no... various hand tools and such... NO!')
                        print('There! in the back! a fresh cartridge! ')
                        addToItems('Ammo')
                        print('')
                        print(Items)
                        print('')
                        print('you feel the lift stop... you must be at the top... main bridge... ')
                        print('you open the door...')
                        print(
                            'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
                        print('they are all gathered around the computer in the center of the room..')
                        print('suddenly the door latch engauges.. and causes a loud thunk... ')
                        print('they all whip around... ')
                        print('they are armed to the teeth with space age looking weapons... ')
                        print('they open fire...')
                        print('but you quickly jump behind the nearest control panel...')
                        print('you see the panel you need to access..')
                        go_for_it = input('despite the enemy fire, should you go for the panel or not?  yes/no    ')
                        if go_for_it.lower() == 'yes':
                            print('you make a run for it! ')
                            print(
                                'there is a burning sensation all over your body... then your lifeless body falls to the ground...')
                            print('GAME OVER...')
                            break
                        elif go_for_it.lower() == 'no':
                            print('what can you do??')
                            print('you look up...')
                            print('there is a mirror on the cieling... ')
                            print('you see there are 2 on the right... and three on the left... ')
                            print('there is a pause in the shooting... ')
                            print('you spring up and take out the two on the right... ')
                            print('then duck back down before the shooting starts back up...')
                            print(
                                'there is a thick cloud of smoke billowing from the console you are ducking behind...')
                            print('you dive to the next console over... but its not the one you need... ')
                            print('one shot strikes your leg...')
                            print('but its just a flesh wound... you\'ll take care of it later...')
                            print('you look up again at the mirror... they are standing in a line...')
                            print('still shooting at where you just were... ')
                            print('did they not see you move to the other console??? ')
                            print('you charge your weapon to unload every proton round at once...')
                            print('deep breath.... whoooooo')
                            print('you stand up and take aim at the first ones head...')
                            print('fire your last round...')
                            print('it goes right though all three of them and a spray of blue litters the bridge...')
                            print('')
                            print(
                                'it goes quiet other than the pops and cracks of the station slowly falling apart from all of the explosions and gun fire...')
                            print('you quickly run to the main console and press the cracked screen... ')
                            print('a crackled voice comes though the intecom...')
                            print(
                                'its the computer \" I\'m sorry the station is on full lockdown, without the access code you can not authorize any funtions\"')
                            access_codes = input('Please enter access code...    ')
                            if access_codes == '78-649-036':
                                print('access granted')
                                print('what function would you like to access?')
                                first_function = input('what do you want to do first? activate pods or alert crew?')
                                if first_function == 'activate pods':
                                    print('')
                                    print('\"Computer! Activate escape pods!\"')
                                    print('Escape pods active')
                                    print('\"Computer! Open a channel!')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print('\" Attention crew! i am about to activate all escape pods!')
                                    print('Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break

                                elif first_function == 'alert crew':
                                    print('')
                                    print('the signal that a channel is open comes over the intercom...')
                                    print(
                                        '\" Attention crew! i am about to activate all escape pods! Hurry to the nearest escape pod with as many people as possible!\"')
                                    print(
                                        '\" Once you have as many people in the pod and you are safe... we will rendezvous on the planet surface...\"')
                                    print('\"COMPUTER!\" you yell...')
                                    print(
                                        '\"Activate any and all escape pod and reroute all remaining power to the pods!\"')
                                    print('the computer agknowledges and confirms')
                                    print(
                                        'you see escape pods start to jet to the surface. you only hope that you too can get out safely.')
                                    print(
                                        'you quickly scan the room for any humans.. you see a door to the captains quaters...')
                                    captain = input("Do you check the captains quarters?  yes/no     ")
                                    if captain == 'no':
                                        print('')
                                        print('you\'re sure he\'s dead... ')
                                        print('you climb into the escape pod entrance on the bridge and eject yourself')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break
                                    elif captain == 'yes':
                                        print('')
                                        print('you open the door to the captains quarters...')
                                        print('there he is lifeless in front of his desk...')
                                        print('you check for a pulse...')
                                        print('there is a pulse! but its faint...')
                                        print(
                                            'you drag him to the escape pod... hoping that you can help him when you get to the surface...')
                                        print('you take one last look for human life signs...no one... ')
                                        print(
                                            'you climb into the escape pod entrance on the bridge and eject the both of you')
                                        print('you are suddenly drifting in space toward the planet...')
                                        print(
                                            'you inter the atmosphere and find yourself plunging toward the planet...')
                                        print(
                                            'your body shakes and jolts until you feel your pod crash into the planet...')
                                        print('disoriented you climb from the pod... ')
                                        print(
                                            'you look up into the night sky and you see a bright flash as the station explodes...')
                                        print(
                                            'you made it out alive and you have saved the crew!!! CONGRATULATIONS! YOU WIN!')
                                        break

            else:
                print(
                    'you get almost to the bottom when another explosion from an alien frag granade engulfs your body... ')
                print('um... you\'re dead... GAME OVER...')
                break
        else:
            print('dang... you made it so far... GAME OVER...')
            break
    elif door_1.lower() == "2b":
        print('')
        print('wait this is a turbo lift... ')
        print('this leads to the bridge... ')
        print('but you dont know the access codes...')
        print('should you just get to the bridge without the rest of the items?')
        continue_to_bridge = input('Continue to bridge?  yes/no     ')
        if continue_to_bridge.lower() == 'yes':
            print('The turbo lift is stuck... you\'ll need to engage the manual override')
            print('THUD!! THUD!! ')
            print('')
            print('there is an alien creature outside trying to break down the door...')
            print(
                'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
            print('you turn on the lift crank and feel the turbo lift start to rise... ')
            print('you\'re safe... for now... ')
            print('')
            print('you feel the lift stop... you must be at the top... main bridge... ')
            print('you open the door...')
            print(
                'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
            print('they are all gathered around the computer in the center of the room..')
            print('suddenly the door latch engages.. and causes a loud thunk... ')
            print('they all whip around... ')
            print('they are armed to the teeth with space age looking weapons... ')
            print('they open fire...')
            print('there is a burning sensation all over your body... then your lifeless body falls to the ground...')
            print('GAME OVER...')
            break
        elif continue_to_bridge.lower() == "no":
            print('there is alien outside the door... he is pounding furiously trying to get in...')
            print('theres nothing you can do other than engage the manual override and press on to the bridge...')
            print('THUD!! THUD!! ')
            print('')
            print('the alien creature is trying to break down the door...')
            print(
                'you found the panel that has the manual override... you tear it off and muscle the lever... from auto to... hmmmph! manual... whew... ')
            print('you turn on the lift crank and feel the turbo lift start to rise... ')
            print('you\'re safe... for now... ')
            print('')
            print('you feel the lift stop... you must be at the top... main bridge... ')
            print('you open the door...')
            print(
                'You look up to see a group of 5 or 6 aliens... its hard to tell because they are so big and ugly that they all sort of blend together...')
            print('they are all gathered around the computer in the center of the room..')
            print('suddenly the door latch engages.. and causes a loud thunk... ')
            print('they all whip around... ')
            print('they are armed to the teeth with space age looking weapons... ')
            print('they open fire...')
            print('there is a burning sensation all over your body... then your lifeless body falls to the ground...')
            print('GAME OVER...')
            break
        else:
            print('invalid answer... you must have had a leak in your oxygen... GAME OVER...')
            break
    else:
        print('That is not a valid input... next time pay attention! GAME OVER')
