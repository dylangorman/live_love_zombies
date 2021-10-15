import time
import sys
import random

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    value = input()  
    return value 

def game():
    print("""██▓     ██▓ ██▒   █▓▓█████                 ██▓     ▒█████   ██▒   █▓▓█████                ▒███████▒ ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓▓█████   ██████  ▐██▌  ▐██▌  ▐██▌ 
            ▓██▒    ▓██▒▓██░   █▒▓█   ▀                ▓██▒    ▒██▒  ██▒▓██░   █▒▓█   ▀                ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒▓█   ▀ ▒██    ▒  ▐██▌  ▐██▌  ▐██▌   
            ▒██░    ▒██▒ ▓██  █▒░▒███                  ▒██░    ▒██░  ██▒ ▓██  █▒░▒███                  ░ ▒ ▄▀▒░ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒▒███   ░ ▓██▄    ▐██▌  ▐██▌  ▐██▌ 
            ▒██░    ░██░  ▒██ █░░▒▓█  ▄                ▒██░    ▒██   ██░  ▒██ █░░▒▓█  ▄                  ▄▀▒   ░▒██   ██░▒██    ▒██ ▒██░█▀  ░██░▒▓█  ▄   ▒   ██▒ ▓██▒  ▓██▒  ▓██▒ 
            ░██████▒░██░   ▒▀█░  ░▒████▒ ██▓  ██▓  ██▓ ░██████▒░ ████▓▒░   ▒▀█░  ░▒████▒ ██▓  ██▓  ██▓ ▒███████▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░░▒████▒▒██████▒▒ ▒▄▄   ▒▄▄   ▒▄▄  
            ░ ▒░▓  ░░▓     ░ ▐░  ░░ ▒░ ░ ▒▓▒  ▒▓▒  ▒▓▒ ░ ▒░▓  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░ ▒▓▒  ▒▓▒  ▒▓▒ ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░ ░▀▀▒  ░▀▀▒  ░▀▀▒ 
            ░ ░ ▒  ░ ▒ ░   ░ ░░   ░ ░  ░ ░▒   ░▒   ░▒  ░ ░ ▒  ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░ ░▒   ░▒   ░▒  ░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░ ░ ░  ░░ ░▒  ░ ░ ░  ░  ░  ░  ░  ░ 
            ░ ░    ▒ ░     ░░     ░    ░    ░    ░     ░ ░   ░ ░ ░ ▒       ░░     ░    ░    ░    ░   ░ ░ ░ ░ ░░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░   ░   ░  ░  ░      ░     ░     ░ 
                ░  ░ ░        ░     ░  ░  ░    ░    ░      ░  ░    ░ ░        ░     ░  ░  ░    ░    ░    ░ ░        ░ ░         ░    ░       ░     ░  ░      ░   ░     ░     ░    
                            ░            ░    ░    ░                        ░            ░    ░    ░  ░                                  ░                                       """)
    def start_game():
        time.sleep(1)
                                                                                                                                                                                      
        typingPrint("WELCOME TO THE GAME, LIVE...LOVE...ZOMBIES!!!\n")
        time.sleep (2)
        response = typingInput("Enter if You dare!!! \n[Y/N]\n")
        if response.upper() == "Y" or response.upper() == "YES":
            time.sleep (2)
            typingPrint ("SO BE IT...")
            intro_func()
        elif response.upper() == "N" or response.upper() == "NO":
            typingPrint("Wise choice... you coward!!!")
            start_game()
        else:
            typingPrint("Are you Braindead I didn't recognise that!")
            start_game()

    def intro_func():
        time.sleep (2)
        typingPrint("""\n\nMONDAY, 19th FEBRUARY 2001. 
You are David D’Accourt, an experienced commercial airline Pilot, for Nice & Safe Airlines. Flying 200 passengers plus crew to Manchester from Rio de Janeiro. 
It’s a cold, wet night, you are currently flying close to Cape Verde and conditions are very poor, however you are making good progress on your flight. 
Your hands are tightly gripped on the controls and a single bead of sweat trickles down your forehead…\n""")
        time.sleep(1)
        print("""                                            
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@, .(@@&    @@@@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@*    %*     (@@* &@@@@@@@@
                                            @@@@@@@@@@*                          @@@@@@@@
                                            @@,        ,   (                    @@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@.              #@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@ @    *@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@&&  .@@
                                            @@@@@@@@@@@@@@@@@@@@%    @@@@@@@@@@@@@@@@@@%@
                                            @@@@@@@@@@@@@@@@@@@@@  /@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@&&/  @@&@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@(      .@&   /@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@@@@@@@@@@. *@@@@@@@@@@@@@@@@@@
""")
        time.sleep(1)
        typingPrint("""All 200 passengers and the Flight Crew are completely unaware that in the hold of the plane is a containment carrying 5000 vials of an extremely dangerous and rare chemical created by the 
US Government, called Z-101. 
Z-101 was created by the US Government as an enhancement drug in a Vein attempt to turn their front-line personnel into Super Soldiers. 
The formula made its way into the wrong hands... a Brazilian drug Cartel, who made 5000 vials of the formula and sold them on the Black market to the KGB. 
The KGB have blackmailed you into escorting the vials to Manchester, where they have several gang members awaiting your arrival.  You are tense and nervous…
\nA flight attendant comes into the cockpit and offers you a drink \n""")

        time.sleep (2)
        response = typingInput("Flight attendant – “Hello David, what would you like to drink? Coffee or Whiskey?\n")
        if response.upper() == "COFFEE" or response.upper() == "coffee":
            time.sleep(1)
            drinks_coffee()
            time.sleep (2)
        elif response.upper() == "WHISKEY":
            typingPrint("""You decide to have a whiskey to try and calm your nerves, and after all, it is your favourite tipple.  However, the whiskey is spiked, and it knocks you out. """)
            check_survivors()
        else:
            typingPrint("Incorrect answer, try again")
            intro_func()
            
    def drinks_coffee():
        typingPrint("""\nYou take the coffee and swig it down. It makes you instantly alert and focused. 
You carry on flying the plane,  however a few moments later there is a HUGE EXPLOSION in the hold and the vials shatter releasing a toxic gas which encompasses the entire cabin instantly
mutating everyone into ZOMBIES!!!
The whole cabin is in absolute chaos and the zombies manage to break into cockpit, you manage to fend them off and get the door shut, but they drag your co-pilot into the cabin
biting you on the arm in the process.
While the zombies feed on your co-pilot you need to make a fast and decisive decision…\n\n""")
        time.sleep(1)
        print("""            
                                            @@@@@@@@@@@&     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@#      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@/      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@@@&     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@            (@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@&                 @@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@*                @@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@             /  %@@@@@@@@@@@@@@@@@    @@@
                                            @@@@@@@@@            .@   .@@@@@@@@@@@@@@@*    @@@
                                            @@@@@@&   @          *@@@   #@@@@@@@@@@@&@@   @@@@
                                            @@@@@  .@@@            @@@@   @@@@@@@.        @@@@
                                            @@@  @@@@@@            ,@@@@%  @@@@@@            @
                                            @@  @@@@@@@             @@@@ % @@@@   @          @
                                            @ @ @@@@@@      &@      @@@@@ &&/  &@@       ,  @@
                                            @@@@@@@@@@/    #@@(    &@@@@@@@ @&@@@@       @  @@
                                            @@@@@@@@@@#    @@@@     @@@@@@@@@@@@@        @@  @
                                            @@@@@@@@@@.    #@@@     &@@@@@@@@@@@         @@@ @
                                            @@@@@@@@@@    /@@@@@      @@@@@@@@@@         ,@@ @
                                            @@@@@@@@*   *%@@@@@@@ /    @@@@@@@@/    @%    @@@@
                                            @@@@@@@@    @@@@@@@@@@@     @@@@@@@    @@@.   @@@@
                                            @@@@@@@    @@@@@@@@@@@@@&   @@@@@@@    @@@&    @@@
                                            @@@@@@*   #@@@@@@@@@@@@@@@  @@@@@@@  @.@@@@&@. @@@
                                            @@@@@    @@@@@@@@@@@@@@@@&   @@@@@@.,@@@@@@@@@. @@
                                            @@@@@    @@@@@@@@@@@@@@@     @@@@@,  @@@@@@@@@@  ,\n""")
        time.sleep(1)
        response = typingInput("\nMake a break for the aircraft LAVATORY or try and get into the cargo HOLD?\n")
        if response.upper() == "LAVATORY":
            typingPrint(""" \nYou decide to get to the restroom. Once inside you clean up the wound, however after several minutes you start to sweat profusely, and you now realise you have been infected. 
You turn into a Zombie, the plane currently flying over North Africa, descends crashes into the Sahara Desert and the zombies including yourself start infecting people and eventually the rest of the world is a nation of zombies. 
GAME OVER! START AGAIN?\n""")
            game_over()
        elif response.upper() == "HOLD":
            cargo_hold()
        else:
            typingPrint("Answer not recognised")
            drinks_coffee()
            
    def cargo_hold():
        typingPrint("""\nYou decide to make your way to the Hold, knowing there is a vaccine for Z-101 stored with the chemical. \n
You make your way past the Zombies while they feast on your co-pilot. Once safely inside the hold you find the Vaccine and inject yourself.  
You also find a parachute.""")
        answer = typingInput("""\nKnowing everyone is a zombie, do you decide to take the parachute and JUMP from the plane, or do you make your way back to the COCKPIT and try and 
land this thing?\n \nType 'jump' or 'cockpit'\n""")
        if answer.upper() == "JUMP":
            print("""\n                 
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@.             *@@@@@@@@@@@@@@@@@@@@@##@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@                             @@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@                              ,@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@  @@@#    @@@,   ,@@@    &@@@  @@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@ @@@@@@ @@@@@@ @@@@@@ @@@@@@,@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@ @@@@@ @@@@@ @@@@@ @@@@@ @@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@@@@ @@@@#@@@@.@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@.@@@@ @@@@(@@@ @@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@ @@@ @@@ @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@ @@ @@ @@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @ @ @ @ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
            
            typingPrint("""\nYou grab the parachute and jump; the plane descends and crashes into the sea killing all the Zombies. Saving the world!! 
You float down onto a small island. Safe from the zombies and no sign of turning into a zombie. \n
Unfortunately, the island is deserted and there is no food, and you die of starvation.\n""")
            game_over()
        elif answer.upper() == "COCKPIT":
            typingPrint("""\nYou make your way back to the cockpit and barricade yourself in, you take control of the plane, you think you are going to make it, you send a distress signal and are about to land back into Manchester, but the Zombies break in and devour you.
The plane miraculously lands and the zombies including yourself evacuate the plane infecting everyone and the entire UK becomes a nation of Zombies.\n""")
            game_over()
        else:
            typingPrint("Type 'jump' or 'inject'")
            cargo_hold()

    def check_survivors():
        typingPrint("""\nYou awaken and realise the plane has crash landed, you don’t know where, but you are by the sea on a beach and next to a jungle, you surmise it’s an island. 
You are very confused and concussed. \nYou must decide what to do!\n""") 
        answer = typingInput("""\nDo you CHECK the wreckage for survivors or do you LEAVE into the dense jungle immediately?\n""") 
        if answer.upper() == "CHECK": 
            check_plane()
        elif answer.upper() == "LEAVE":
            typingPrint("""\nYou decide to make a break for the Jungle, after a while you trip and fall to the ground. You look up and see a figure in the distance. 
The figure gets closer and closer. It is a woman. She puts out her hand in a mysterious manner and says ‘come with me if you want to live’.
\nDo you Trust them?\n""")
            print("""
        w*W*W*W*w
         \"."."/
          //`\\
         (/a a\)
         (\_-_/) 
        .-~'='~-.
       /`~`"Y"`~`\
      / /(_ * _)\ \
     / /  )   (  \ \
     \ \_/\\_//\_/ / 
      \/_) '*' (_\/
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
jgs     |       |
        w*W*W*W*w""")

            leave()
        else:
            typingPrint("Answer not recognised")
            check_survivors()

    def leave():
        question = typingInput("\nGo with mysterious woman? Y/N?\n")
        if question.upper() == "YES" or question.upper() == "Y":
            typingPrint("""\nYou agree to follow her, and she tells you that she was on your flight, and she spiked your drink! The reason being is that she secretly works for the CIA and the Z-101 vials had to be disposed 
of otherwise they could infect people turning them into Zombies. 
She explains you are on an island and that no one can ever leave, but there is a safe camp, and you will be safe with her once you get there.
You arrive at the safe camp and start a new life with the woman.
For several months everything seems to be going alright until one day someone in the camp gets infected by a rabid Zombie Dog and the whole camp turns into...\n""")
            time.sleep(2)
            typingPrint("\nZOMBIES!\n")
            typingPrint("\nYou saved the world but are now a zombie\n\n")

            print("""
                                        MMMMMMMMMWX0kxOXWMMMMMMMMMMWNNXX0kx:'..:clx0NWWWMMMMMMXx;. ,
                                        MMMMMMMN0l,...;ok0K00Oxxdlc:;,''...    ....';:clkKKKOo,. .lO
                                        MMMMWXx:....   .......          ....            ....   .c0WM
                                        X0Oxl,. ..ld'                  ..  ..      .          'kNWMM
                                        ,'.     ....             ........           ...      ,OWMMMM
                                        l.',,::;;'..              ......                    .xWMMMMM
                                        Xdcox0K0c. ..              .                        lXMMMMMM
                                        MWKOK00k:':;...,;.    ...             .,:;.         oNMMMMMM
                                        MMMNk:;;:::clxKWNl    ...          .;oONWWo.        :XMMMMMM
                                        MMMXxc:dO0KNMMMMWo   ..   .:cccldxx0NMMMMMO.        cXMMMMMM
                                        MMMMWWMMMMMMMMMM0,    ..  cXMWWMMMMMMMMMMMNo.       lNMMMMMM
                                        MMMMMMMMMMMMMMMXc  .'. . .kMMMMMMMMMMMMMMMMWk'   .. ,0MMMMMM
                                        MMMMMMMMMMMMMWO;  'o:....dWMMMMMMMMMMMMMMMMMWd. .c,  'xXMMMM
                                        MMMMMMMMMMMNk:.  ,o;  .'xWMMMMMMMMMMMMMMMMMMXc  ,0O'   lNMMM
                                        MMMMMMMMMMMO. ..,:'  .'kWMMMMMMMMMMMMMMMKd::,. .dNK; . cNMMM
                                        MMMMMMMMMMMNkdl,.   .dKWMMMMMMMMMMMMMMMNo.....;dOx:.  .dWMMM
                                        MMMMMMMMMMMMMXc.  .'dNMMMMMMMMMMMMMMMMMWXKKKKXNO,    'oXMMMM
                                        MMMMMMMMMMMMMW0dodkKNMMMMMMMMMMMMMMMMMMMMMMMMMMKl'..,oNMMMMM""")
            game_over()
        elif question.upper() == "N" or question.upper() == "NO":
            typingPrint ("You say no and make your way on your own. Unfortunately, you are suddenly attacked by a rabid dog. \nIt takes a hefty chunk out of your thigh.\n") # go to hut
            run()
        else:
        	typingPrint("Answer not recognised")
        	leave()

    def check_plane():

        print("""                              
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@(@@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*@@@@,,@@%,@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(*/@@&(/@@.*@@@@@@@@@@
                                    @@@@@@@@@@@@@@(. @@*, @@@@@@@@@@@@@@@@@,//@/*%@((@@@.@@@@@@@
                                    @@@@@@@@@@@(, @,*@@.,@@@@@@@@@@@@./@@@@@*/(#/*,/@@/*@@@@@@@@
                                    @@@@@@@@*,%@*,*/,**//@@@@@@@@@@@@.*@@@@*/*/,*/(/(/@@@@@@@@@@
                                    @@@@@@@@@#*(//**,*.,*/@@@@@@@@@@@@.*///(##%/(,,((@@@@@@@@@@@
                                    @@@@@@@@@@@../,//*,..*#,.((@@@@@@@@&.*//,/*/**//@@@@@@@@@@@@
                                    @@@@@@@@@@@@,///**/**,..../@@@@@@@@@@@,..**,*/#*@@@@@@@@@@@@
                                    @@@@@@@@@@@@*,**./,.....@@@@@@@@@@@@@@@@...,*,*@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@*,...  .*@@@@@@@@@@@@@@@@@@..///,,@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@*/*,**,(@@@@@@@@@@@@@@@@@@@@.,,*(*@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@*///**,@@@@@@@@@@@@@@@@@@@@@. ,,#(*@@@@@@@@@@@@
                                    @@@@@@@@@@@@,*/(/**@@@@@@@@@@@@@@@@@@@@@@*..*(#/@@@@@@@@@@@@
                                    @@@@@@@@@@@@,.*/**,@@@@@@@@@@@@@@@@@@@@@@&.,/(//@@@@@@@@@@@@
                                    @@@@@@@@@@@, ,.*,*@@@@@@@@@@@@@@@@@@@@@@@@ ,./**,@@@@@@@@@@@
                                    @@@@@@@@@@.,,***,*@@@@@@@@@@@@@@@@@@@@@@@@../#%/*@@@@@@@@@@@""")
        typingPrint("""\nYou go to check if there are any survivors and are attacked by one of the passengers, she bites you on the arm. 
A sense of dread hangs over you and you now realise that the vials containing Z-101 must have exploded and infected the whole plane turning everyone into flesh eating Zombies.\n""")
        answer = typingInput("You must decide whether to dress the WOUND or make a RUN for it?\n")
        if answer.upper() == "WOUND":
            typingPrint("""\nYou decide to get to the restroom of the plane. Once inside you clean up the wound, however after several minutes you start to sweat profusely, and you now realise
you have been infected. You turn into a Zombie.\n""")
            game_over()
        elif answer.upper() == "RUN":
            run()
        else:
        	typingPrint("Answer not recognised")
        	check_plane()

    def run():
        typingPrint("""\n\nAlthough bitten you decide to make a run for it. You manage to find an abandoned hut and inside the hut there is a dismembered body, a gun, a knife and a box marked vaccine for Z-101!
You can’t believe your luck and you don’t even question why they are there. 
Upon opening the box you see that inside is a vaccine revolver.\n""")
        time.sleep(2)
        print("""
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    &@@@
                                    @@@@@@@@@@@@@@@@*  #(                                    @@@
                                    @@@@@@@@@@@@@@@@@@@                                      @@@
                                    @@@@@@@@@@@@@.                                         (@@@@
                                    @@@@@@@@@@@@                           @@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@@@                           &@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@               @   @@@@@% @@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@         .@@@* @@@  @@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@#         %@@@@@@ @@@@@@# @@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@/          /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@/           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@%           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """)                  
        time.sleep(1)                   
        typingPrint("""\nThats right, a vaccine revolver, with 3 chambers, each containing a vial. You can't tell if the vials are full or not, but you take your chances anyway. 

It’s a game of Zombie roulette!\n""")
        vaccine_roulette()

    vial = ["The vial contained the vaccine.\n"]
    chamber = random.choice(vial)
    safe = "The vial contained the vaccine.\n"
    def vaccine_roulette():
                trigger= typingInput("\nWith shaking hands you put the vaccine gun to your neck, praying that no one has had the same idea and used all three doses. \nType 'fire' to pull trigger of the vaccine gun. \n")
                if trigger.upper() == "FIRE":
                    typingPrint(chamber)
                if chamber == safe:
                    typingPrint("You feel the vaccine enter your bloodstream and you allow the fear in your mind to dissipate for a moment.\n")
                    typingPrint("""You decide to rest up for the night. 

In the morning you are awoken by a moaning sound. 
You look out of the window on the hut, and you are surrounded by...""")
                    time.sleep(1)
                    typingPrint("\n...\n")
                    time.sleep(1)
                    typingPrint("...\n")
                    time.sleep(1)
                    typingPrint("ZOMBIES!!!\n")
                    choose_weapon()
                else:
                    vaccine_roulette2() 
                
    def vaccine_roulette2(): 
                time.sleep(1)
                trigger= typingInput("You were not vaccinated. Two rounds remaining. Type 'fire' to pull the trigger and try again. \n")
                if trigger.upper() == "FIRE":
                    typingPrint(chamber)
                if chamber == safe:
                    typingPrint("\nYou feel the vaccine enter your bloodstream and you allow the fear in your mind to dissipate for a moment.\n")
                    typingPrint("""You decide to rest up for the night. 

In the morning you are awoken by a moaning sound. 
You look out of the window on the hut, and you are surrounded by...""")
                    time.sleep(1)
                    typingPrint("\n...\n")
                    time.sleep(1)
                    typingPrint("...\n")
                    time.sleep(1)
                    typingPrint("ZOMBIES!!!\n")

                    choose_weapon()
                else:
                    vaccine_roulette3()

    def vaccine_roulette3():
                time.sleep(1)
                trigger = typingInput("You were not vaccinated. One round remaining. Type 'fire' to pull the trigger and try again.  \n")
                typingPrint(chamber)
                if trigger.upper() == "FIRE":
                    typingPrint(chamber)
                if chamber == safe:
                    typingPrint("\nYou feel the vaccine enter your bloodstream and you allow the fear in your mind to dissipate for a moment.\n")
                    typingPrint("""Yyou decide to rest up for the night. 

In the morning you are awoken by a moaning sound. 
You look out of the window on the hut, and you are surrounded by...""")
                    time.sleep(1)
                    typingPrint("\n...\n")
                    time.sleep(1)
                    typingPrint("...\n")
                    time.sleep(1)
                    typingPrint("ZOMBIES!!!\n")


                    choose_weapon()
                else:
                    time.sleep(1)
                    typingPrint("\nYou fail to vaccinate yourself and Z-101 takes over your body and you mutate into a ZOMBIE.\n ")
                    game_over()

    
    def choose_weapon():

    
        answer = typingInput("""\nYou look around you for a weapon. You see a rifle, a knife and a decapitated limb! What do you decide to use?\n""") 
        if answer.upper() == "RIFLE": 
            rifle()
        elif answer.upper() == "KNIFE":
            typingPrint("""\nThe knife! Oh dear, bad decision. It's a butter knife. This is not the time to be making sandwiches.
You head outside and somehow get a couple of kills. In a fit of manic fear you scream "ITS PEANUT BUTTER JELLY TIME" but you are eventually swarmed by dozens of Zombies, 
and they EAT YOU ALIVE!! 
Frankly you deserved it.\n""")
            game_over() #peanut butter ascii art
        elif answer.upper() == "LIMB":
            map()
        else:
        	typingPrint("Answer not recognised")
        	choose_weapon()
            
    def rifle():
        typingPrint("The gun! Not a bad choice! It has 10 bullets inside, you decide to leave the hut and take on the Zombies outside, but how many are there...?\n")
        zombies = random.randint(1,20)
        if zombies <= int (10):
            typingPrint(f"""{zombies} zombies! You have enough rounds in the rifle!
Your pilot training floods back to you and you execute each zombie with a clean headshot.\n""")
            beach()
        if zombies > int(10):
            answer = typingInput("\nYou peek out the door and don't really the look of how many zombies there are. Are you sure you really want to choose the rifle?\n")
            if answer.upper() == "YES" or answer.upper() == "Y":
                typingPrint(f"{zombies} zombies! You dont have enough rounds in the rifle!\nThe zombies rip you limb from limb and you die an agonising death, regretting every decision you made in your life leading to this point")
                game_over() #extend with an action
            elif answer.upper() == "NO" or answer.upper() == "N":
                choose_weapon()

    def beach():###############################################
        print("""
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  .@@@@@@@@@@,@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            @ @@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %    #  @@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@.       /@@@@@@@@@@@@@@@@@    @@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@*                      ,(    @@ @ @@@@@@@@@@@@@@@@@@@@@@  .@@@@@
                                                @@@@@@@@                                                        @@@@@@
                                                @@@@@@@@@@%                                                    @@@@@@@
                                                @@@@@@@@@@@@@@@@@&                                            @@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@%@&%%%##%%%&@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@  /@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@   @@@@  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")


        answer = typingInput("""\nAfter clearing the path of zombies you make a dart through the trees. You run nonstop for what seems like an eternity you find the coastline. There is a boat. Its small but you feel like 
its your only option to get off the island. 
The weather has taken a turn for the worse and a massive thunderstorm looms overhead. The sea looks choppy and unforgiving. Afterall you are a pilot and not a sailor. 
Do you want to risk pushing the boat out NOW or wait until the weather passes LATER.\n""")
        if answer.upper() == "NOW":
            typingPrint("""\nDeciding you have nothing to lose, you risk it and push the boat out into the swelling ocean. 
You endure hours of brutal ten story waves but somehow survive long enough to be spotted by a surfaced submarine.
They take you onboard, under the condition that you clean the toilets.""")
            game_over()
        elif answer.upper() == "LATER":
            typingPrint("""\nYou wait until the sea has calmed down, but night has fallen and it is pitch black and freezing. Against your better judgement you push the boat out. 
Unfortunately you are not spotted by the the passing cargo ship as it is too dark for them to see you. 
You dont even notice as you fall asleep in the subzero tempuratures and freeze to death.
But you at least you didn't become a zombie \n""")
            game_over()


            
    def map():
        print("""
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...................@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,...................@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@#...................@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@ ..................@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@,................*@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@...............@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@/.............,@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@.............@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@............*@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@&............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@  . ...   ./@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@  .. ..   ..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@............*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@..............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@..............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@*............*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@ ..........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@#,......&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n""")
        typingPrint("""\nA dismembered limb from the dead body! Wow you are a nihilist!! Although you have questionable taste, it is the best decision you have made so far! 
The Limb is a leg, and you manage to beat off the zombies and make a break for it! Once you know you are safe you slow down and realise you are still carrying the leg, you inspect it and find a 
map of the island tangled up in some of the flesh. 
There is a huge red X on it! \n""")
        response = typingInput("\nDo you follow the map to the X or Ignore the MAP and just EXPLORE the island instead? \n")
        if response.upper() == "MAP":
            map_func()
        elif response.upper() == "EXPLORE":
            typingPrint ("""\nYou ignore the map and decide to make your own way. You follow a path and it leads you to a run-down building, you sneak inside, you discover an office full of plans on a full Zombie apocalypse 
and this is where they are trying to produce and train them, but you realise it all went wrong and there are thousands of zombies on the island! 
The dismembered leg must have belonged to one of the staff on the island! 
				 
You turn around to find a mysterious woman standing there, you ask her what is going on and she explains that she spiked your drink on the flight as she needed the vials on that flight to land 
here to save the world. 
She says the experiments got out of hand and when they found out more vials had been made, they had to make urgent decisions. 
You ask her how you can leave, and she tells you there is a plane on a disused runway not far from here. You say thank you and leave. 

You make you way out of the building and...
...
...
are suddenly attacked by thousands of Zombies.\n""")
            game_over()
        else:
            typingPrint("Incorrect answer, try again")  
            map()
            
    def map_func():
        print("""
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@%/(///.#/,/#(*/*((&#&@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@
                                        @@@@@@&&@#@@&/(**&@/*/***,****/#@@@@@@@@%#&@@@@@@@@@%@@@&@@&@%(@@@@@@@@@@@
                                        @@@@@&(*/@#&###**/(@@@&*/**/*//&@@@@@@@@@@@@@@@@@(%@%/*(/*/**/*/****@#@%(&
                                        (*(,///(,(//(*/(&%%(#&@((,(%@@&&%@@@@@@%*#(/(##(//*(,(**(,(*//,(*//*(,(*,(
                                        %%#*/**(,(**(#@@@(,&&&@@&%@@@@@@@@@&@((/*&,//,(,(/*(,(**/,(**/.(,//,#,//*#
                                        @@@@@/*(,(**#,#*##*(*/&@@@@@@@@@@@###%##,(*//*(,(**/,(*//,(*/(,(,//,(.#&@@
                                        @@@@@@((,(*/(,((/#*&&@@@@@@@@@@@@@&&%(%(((,%@&#(@/*(,(//(,#*((,(*/(,%%@%@@
                                        @@@@@@##./,*(,(*/#@@@@@@@@@@@@@@@&%%#*/@@@@@@((,#**(.(**/.(,//.(./@%#/&@@@
                                        @@@@@@@@##//%@@@%@@@@@@@@@@@@@@@@#/*(*//*/*/(#(,###%//**/*/****/*/&@@@@@@@
                                        @@@@@@@@@@@&&#*#@@@@@@&@@@@@@@@@//**/****/*/****#%@@@@//@@@&*/(@@%&@@@@@@@
                                        @@@@@@@@@@@@@&@@&//*/*(&@@@@@@@@@#((&(**/****/*/@@@@@@@@@@@@(%@@&&%%@@@@@@
                                        @@@@@@@@@@@@@@@@&*(.(/*(.//%@@@@@@@@@@@/(,/**(@@@@@@@@@@@@@@@(%%##@@@(,%@@
                                        @@@@@@@@@@@@@@@@@@#.(**(.((@@@@@@@@@@@@&(.(**(%&#@@@@@@@@@@@@@@@@@@&,#%/@@
                                        @@@@@@@@@@@@@@@@@@& (,*( &@@@@@@@@@@@@@@#.(**&@%@@@@@@@@@@@@@@&@#/,(,(**(%
                                        @@@@@@@@@@@@@@@@@@&.(*/&@@@@@@@@@@@@@@@@&*#@@@@@@@@@@@@@@@@@@@@&@((&&%//((
                                        @@@@@@@@@@@@@@@@@@#.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@""")
        time.sleep (2)
        typingPrint ("""\nYou follow the map, You discover an old Biplane on an abandoned runway.
You check the engine, and it doesn’t work, you need FUEL! On further inspection of the plane you see that it is missing a WHEEL and the PROPELLER, which is fairly essential to fly a plane. 
You take a look at the map and see several other marks on there! 
There are 6 places in total and you need these 3 items, lets find them!!\n\n""")
        
        choice_func()
    inventory = []
    def choice_func():
        time.sleep (1)
        list = ("Jungle", "Old Mine", "Runway", "Cave", "Disused Garage", "Abandoned Hotel", "Fly Home")

        for items in list:
            print(list.index(items), items)
        
        response = input("Where would you like to go? \n")
        
        if response == "0":
            typingPrint("\nYou go to the jungle \n")
            jungle_func()
        if response == "1":
            typingPrint ("\nYou go to the Old Mine\n")
            old_mine_func()
        if response == "2":
            typingPrint ("\nYou go to the Runway\n")
            runway_func()
        if response == "3":
            typingPrint ("\nYou go to the Cave\n")
            cave_func()
        if response == "4":
            typingPrint ("\nYou go to the Disused Garage\n")
            garage_func()
        if response == "5":
            typingPrint ("\nYou go to the Abandoned Hotel\n")
            hotel_func()
        elif response == "6":
            is_plane_ready()
        else:
            typingPrint ("\nIncorrect Answer Try again!\n")
            choice_func()
    
    def is_plane_ready():
        if len(inventory) == 3:
            plane()
        else:
            print("You dont have all the parts to fix the plane, dummy! \nKeep looking. \n")
            choice_func()

    
    def jungle_func():
        time.sleep (2)
        print("""    
                                                    @@@@@@@@@@@.*@@@@@@@@@@@@@@@@@
                                                    @@@@@@@@       @@@@@@@@@@@@@@@
                                                    @@@@@@@/          %@@@@@@@@@@@
                                                    @@                    @@@@@@@@
                                                    @@@,.,                 %@@@@@@
                                                    @@@@@@@@@@  #            /@@@@
                                                    @@@    %@@@,                 (
                                                    @@@*  @ @@@@    @          &@@
                                                    @@@@@@@@@    @.@@           @@
                                                    @@@@@@@@@@@   @@% @%         @
                                                    @@@@@@@@@@@  @@  @@@@@@@@@@@@@
                                                    @@@@@@@@@@@     @@@@@@@@@@@@@@
                                                    @@@@@@@@@@%    @@@@@@@@@@@@@@@
                                                    @@@@@@@@@@@,   @@@@@@@@@@@@@@@
                                                    @@@@@@@@@@@@    @@@@@@@@@@@@@@
                                                    @@@@@@@@@@@@(    @@@@@@@@@@@@@
                                                    @@@@@@@@@@@@     @@@@@@@@@@@@@
                                                    @@@@@@@@@@@         @@@@@@@@@@\n""")
        typingPrint (""" You make your way through some vines and come to a clearing. You look around and see nothing. Suddenly you hear some branches snapping above you! You look up and another plane wreckage is hanging within the trees! As it starts to come crashing down you dive out of the way. You are ok and once the dust settles you go and inspect the plane and with all your might you manage to pull off the propeller! You can use this to fix your plane.\n""")
        response = typingInput("\nPick up propeller?\n")
        if response.upper() == "Y" or response.upper() == "YES":
            typingPrint("\nGreat this will help the plane fly!\n\n")
            typingPrint("\nYou take another look at the map\n\n")
            inventory.append("propeller")
            print(f"Items in inventory {inventory}\n")
            choice_func()
        elif response.upper() == "N" or response.upper() == "NO":
            typingPrint("Do you Not want to get out of here?\n")
            jungle_func()
        else:
            typingPrint("Incorrect Answer Try again!\n")
            jungle_func()

    def old_mine_func():
        time.sleep(2)
        typingPrint ("""You get to the old mine and there is nothing here!\n""")
        response = typingInput("\nGo back to check the Map again? [Y/N]\n\n")
        if response.upper() == "Y" or response.upper() == "YES":
        	typingInput("You check the map again")
        	choice_func()
        elif response.upper() =="N" or response.upper() == "NO":
            typingInput("Why not, do you not want to Live?\n")
            old_mine_func()
        else: 
            typingInput("Incorrect Answer Try again!")
            old_mine_func()

    def runway_func():
        time.sleep (2)
        typingPrint("You check the runway for parts of the plane. There is nothing at all. Suddenly a rabid dog starts chasing you.\n""")
        response = typingInput("\nDo you try and 'KILL' it or throw it a 'BONE' you find on the floor?\n")
        if response.upper() == "KILL":
            typingPrint("You decide to kill the dog, but as you strike it down, he howls and howls and several more dogs come running, they take a bite out of you, you need to get back to the hut and use the vacinne gun again!\n\n")
            vaccine_roulette()
        elif response.upper() == "BONE":
            typingPrint("You throw the dog a bone and it loves it, it then wanders off into the jungle. \nYou also find some food yourself and it lifts your spirits. Its not all bad! \nYou go back to check the map.\n\n")
            choice_func()
        else:
            typingPrint("Incorrect Answer Try again!\n")
            runway_func()
 
    def cave_func():
        print("""
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%&@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%&@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%#%%%%%@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%&@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@
                                        @@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@
                                        @@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
                                        @@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%%%%&@
                                        @@@@@@@@@@@@@@@@%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&
                                        @@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&
                                        @@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&
                                        @@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%&&&
                                        @@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%&&/,,&&%%%%%%%%%%%%%%%
                                        @@@@@&((###%%%%%%%%%%%%%%%%%%%%%%%&&#,,,,,,#(((%%%%%%%%%%%%%
                                        @@@((((((####%%%%%%%%%%%%%%%%%&*,,,,,,,,,,,,,,(((#%%%%%%%%%%
                                        @@(((((((((#####%%%%%%%%%%%%&,,,,,,,,,,,,,,,,,,,(((((#%%%%%%
                                        (((((((((((#####%%%%%%%%%%%%&,,,,,,,,,,,,,,,,,,,,,,((((%%%%%
                                        (((((((((((#####%%%%%%%%%%%(,,,,,,,,,,,,,,,,,,,,,,,((((%%%%%
                                        (((((((((#######%%%%%%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,(((((%%%%
                                        (((((((((((######%#%%%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,(((((%%%%
                                        (((((((((((########%%%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,,((((%%%%\n""")


        time.sleep (2)
        typingPrint("You follow the map down the beach to some rocks and discover the cave. There is no sign of any zombies and you make your way in. \nYou see something floating around in the water. It's the wheel off the plane! \nIt must have fallen off when the plane crashed and made its way into the cave. Well done.\n")
        response = typingInput("\nPick up wheel? [Y/N]\n")
        if response.upper() == "Y" or response.upper() == "YES":
            typingPrint("\nYou can drive the plane on the runway!\n\n")
            typingPrint("You take another look at the map\n\n")
            inventory.append("wheel")
            print(f"Items in inventory {inventory}\n")
            choice_func()
        elif response.upper() == "N" or response.upper() == "NO":
            typingPrint("Do you Not want to get out of here?\n")
            cave_func()
        else:
            typingPrint("Incorrect Answer Try again!\n")
            cave_func()
        
    def garage_func():
        time.sleep (2)
        print("""
                                            @@   %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@,    /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@@@    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            @@@@@@@@@@@@@@#    (@@@@@@@&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@
                                            @@@@@@@@@@@@@@@,      ,                           @       (@
                                            @@@@@@@@@@@@@@@&              @@@@@@@@@@@@@@@@%            @
                                            @@@@@@@@@@@@@@               &@@@@@@@@@@@@@@@@@            @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                 Airplane Fuel                @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@                                              @
                                            @@@@@@@@@@@@@.                                             @
                                            @@@@@@@@@@@@@@&                                          #@@\n""")
        typingPrint ("It's not far from the coast line. You make your way there and loads of zombies are surrounding the garage. You are dissapointed but not surprised. \nYou create a diversion by throwing a rock at some rubbish bins, the zombies head towards the bins and you make a run to the garage. \nYou quickly find a jerry can marked 'airplane fuel'!")
        response = typingInput("\nUse this to fill Up Plane? [Y/N]\n")
        if response.upper() == "Y" or response.upper() == "YES":
            typingPrint("The Plane has fuel!\n\n")
            typingPrint("You take another look at the map\n\n")
            inventory.append("fuel")
            print(f"Items in inventory {inventory}\n")
            choice_func()
        elif response.upper() == "N" or response.upper() == "NO":
            typingPrint("Do you Not want to get out of here?\n")
            garage_func()
        else:
            typingPrint("Incorrect Answer Try again!\n")
            garage_func()

    def hotel_func():
        time.sleep(2)
        print("""
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@   @@@   @@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@   @@@      @@@   @@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@                           @@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@   @@@      @@@      @@@   @@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@   @@@      @@@      @@@   @@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@                           @@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@   @@@      @@@      @@@   @@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@                           @@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n""")
        typingPrint("""You check the map and see there is an old hotel up on the cliffs, you bravely scramble up the side of the cliff and finall reach the summit. You are exhausted and need some rest, so decide to take a break.\nYou fall asleep for several hours only to be awoken by the hotel manager, who of course is a zombie!! 

Obviously he goes to bite you\n""")
        response = typingInput("Do you jump left or right? [L/R]\n")
        if response.upper() == "L" or response.upper() == "LEFT":
            typingPrint ("""You jump to the left dodging the zombie and pick up a heavy piece of wood lying on the ground. You take a swing, knocking the zombies head off. Great shot!
You head into the hotel. However, there is nothing there and it was a wasted journey. You head back to the plane. \n\nGo back to map.\n\n""")
            choice_func()
        elif response.upper() == "R" or response.upper() == "RIGHT":
            typingPrint ("You jump right and trip over! The zombie takes a bite out of you, you need to head back to the hut and use the vaccine gun again!.")
            vaccine_roulette() #question input 
        else:
            typingPrint("Incorrect Answer Try again!")
            hotel_func()
    

    def plane():
        typingPrint ("WELL DONE YOU HAVE MANAGED TO FIX THE PLANE!!\n")
        response = typingInput("Start Engine [Y/N]\n")
        if response.upper() == "Y" or response.upper() == "YES":
            typingPrint ("\nThe Engine Starts!!\n")
            finish_game()
        elif response.upper() == "N" or response.upper() == "NO":
            typingPrint ("\nDo you Not want to get out of here?\n")
            plane()
        else:
            typingPrint("Incorrect Answer Try again!\n")
            plane()
 
 
    def finish_game():
            typingPrint("""\nYou check the mirrors and see a swarm of Zombies running after you. You start up the biplane and you take off; 
you have managed to Survive and being an experienced pilot, you know you can safely make your way home with just enough fuel.
With the vials all destroyed and the Zombies stranded on the Island, you have SAVED THE WORLD AND SURVIVED!! 
WELL DONE!!!!\n""")
            

            print("""                                           
                                            WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                                            WWWWWWWWWWWNOddddONWWWWWWWWWWWWWWWWWWWWWWNOddddkXWWWWWWWWWWW
                                            WWWWWWWWWWW0' '. ,0OlllccccccccclllcllllO0; .' 'OWWWWWWWWWWW
                                            WWWWWWWWWWM0'.x0;.,:.                  .;;.,Ok.'OWWWWWWWWWWW
                                            WWWWWWWWWWWX;.oWXxc'.                   .cxXWd.,KMWWWWWWWWWW
                                            WWWWWWWWWWWNo.;KWWWKx'                .dKWWWX:.lNWWWWWWWWWWW
                                            WWWWWWWWWWWW0,.oNWWWNd.               oNWWWNd.'0WWWWWWWWWWWW
                                            WWWWWKodXWWWWk'.dNWWWX:              :KWWWNd..kWWWWNdl0WWWWW
                                            WWWWNl .kWWWWWO;.;kXWWKc            :KWWXk:.,kWWWWWO. cXMWWW
                                            WXO0Nx';kkONWWWXx;'';clc.          .:oc:'.;dXWWWNOkk:.dX0OXW
                                            WO'.cOkx: ;KMWWWWNKxolc:,..      ..,:clox0NWWWWWX; ;dxOl.'OW
                                            WXd'.:lc'.oXWWWWWWWWWWWWNKKd.  .o0KNWWWWWWWWWWWWXo..:l:..oXW
                                            W0c;:dookl,oXWWWWWWWWWWWWWWNc  :XWWWWWWWWWWWWWWNo,cxood:,:OW
                                            WXl..;lod, ,k0XWWWWWWWWWNKkc.  .:xKNWWWWWWWWWN0k; 'doo:..lKW
                                            WWNd,,od:,:o,.oNWWWWNOl:,.        .,:lkNWWWWNd.,o:,:od,'oXWW
                                            WWWk,..,llxd. :odKWNx.                .dNWXddc..dkll;. 'xNWW
                                            WWWWXd,'colc;ox. cXW0,'x0OO0OxodkOOOk,'OWNl 'xo;cloc',oXWWWW
                                            WWWWW0c...cxddo,.cXMK,;XWWWKo'.;0WWWX:,0MNo.,oddxl...:OWWWWW
                                            WWWWWWNX0d:,'',cco0WK,;KWWWXd. 'OWWWX:,0WKocc,'',;d0KNWWWWWW
                                            WWWWWWWWWKxc:lxXXO0NK,;KWWWWK; '0WWWX:,0W0OXXklccdKWWWWWWWWW
                                            WWWWWWWWWWWWWWWWWWWWO',kKKKK0dcoOKKKO,'OWWWWWWWWWWWWWWWWWWWW
                                            WWWWWWWWWWWWWWWWWWWK;  ..............  ;0WWWWWWWWWWWWWWWWWWW
                                            WWWWWWWWWWWWWWWWWWWx................. ..dWWWWWWWWWWWWWWWWWWW
                                            WWWWWWWWWWWWWWWWWWWX00000000000000000000XWWWWWWWWWWWWWWWWWWW
                                            WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW""")
            answer = typingInput("Continue? Y/N\n")
            if answer.upper() == "Y" or answer.upper() == "YES":
                credits()
            else:
                credits()    
            
            credits()
                
    def credits():
        typingPrint("""\n\n                                           
                                                        Thank you for playing Live Love Zombies!
                                                    A text based adventure game created using Python 
                                                                        by

                                                                        TEAM 3

                                                                    Dylan Gorman
                                                                    Naghmeh Abdolkarim
                                                                    Thomas Windle
                                                                    Ayomide Ibrahim
                                                                    Alex Bailey\n\n\n""")
        print("""
                                                        .-') _     ('-.   ('-.     _   .-')                                                
                                                        (  OO) )  _(  OO) ( OO ).-.( '.( OO )_                                              
                                                        /     '._(,------./ . --. / ,--.   ,--.)       .-----.                              
                                                        |'--...__)|  .---'| \-.  \  |   `.'   |       /  -.   \                             
                                                        '--.  .--'|  |  .-'-'  |  | |         |       '-' _'  |                             
                                                           |  |  (|  '--.\| |_.'  | |  |'.'|  |          |_  <                              
                                                           |  |   |  .--' |  .-.  | |  |   |  |       .-.  |  |                             
                                                           |  |   |  `---.|  | |  | |  |   |  |       \ `-'   /                             
                                                           `--'   `------'`--' `--' `--'   `--'        `----''                              
                             _ (`-. _  .-')               _ .-') _                        .-') _                            .-') _  .-')    
                            ( (OO  | \( -O )             ( (  OO) )                      (  OO) )                          ( OO ) )( OO ).  
                           _.`     \,------.  .-'),-----. \     .'_ ,--. ,--.     .-----./     '._ ,-.-')  .-'),-----. ,--./ ,--,'(_)---\_) 
                          (__...--''|   /`. '( OO'  .-.  ',`'--..._)|  | |  |    '  .--./|'--...__)|  |OO)( OO'  .-.  '|   \ |  |\/    _ |  
                           |  /  | ||  /  | |/   |  | |  ||  |  \  '|  | | .-')  |  |('-.'--.  .--'|  |  \/   |  | |  ||    \|  | )  :` `.  
                           |  |_.' ||  |_.' |\_) |  |\|  ||  |   ' ||  |_|( OO )/_) |OO  )  |  |   |  |(_/\_) |  |\|  ||  .     |/ '..`''.) 
                           |  .___.'|  .  '.'  \ |  | |  ||  |   / :|  | | `-' /||  |`-'|   |  |  ,|  |_.'  \ |  | |  ||  |\    | .-._)   \ 
                           |  |     |  |\  \    `'  '-'  '|  '--'  ('  '-'(_.-'(_'  '--'\   |  | (_|  |      `'  '-'  '|  | \   | \       / 
                           `--'     `--' '--'     `-----' `-------'  `-----'      `-----'   `--'   `--'        `-----' `--'  `--'  `-----'  """ )      
        game_over()

    def game_over():
        answer = typingInput("\nGAME OVER. START AGAIN? Y/N\n")
        if answer.upper() == "Y" or answer.upper() == "YES":
            start_game()
        elif answer.upper()== "N" or answer.upper() == "NO":
            game_over()    
        else:
            typingPrint("Please type Y or N")
            game_over()

    start_game()
game()