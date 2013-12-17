#!/usr/bin/env python3

import time

def intro():
	"""This is the introduction for Pokemon Gridiron"""

	print()
	print("                              .;:**'                          ")
	print("                              `                               ")
	print("  .:XHHHHk.              db.   .;;.     dH  MX                ")
	print("oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN     ")
	print('QMMMMMb  "MMX       MMMMMMP !MX' + "' :M~   MMM MMM  .oo. XMMM 'MMM")
	print('  `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP')
	print("   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" + '" MX MMXXMM ')
	print('    ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP ')
	print('     ?MMM>  YMMMMMM! MM   `?MMRb.    `"""   !L"MMMMM XM IMMM  ')
	print('      MMMX   "MMMM"  MM       ~%:           !Mh.""" dMI IMMP  ')
	print("      'MMM.                                             IMX   ")
	print("       ~M!M                                             IMP   ")
	print("              Gridiron: The Text-Based Battle Arena           ")
	
	time.sleep(3)
	
	print("\n                          Press Enter                         ")
	
	A_button = input()
	
	print("                          .,M... ....                                           ")
	print("                    ..  . ...~=M....                                            ")
	print("                     ...?ZDZ+=~~==N....                                         ")
	print("                    ...Z============~IMO.........                               ")
	print("                    ,$MM8==================~+8N~......                          ")
	print("                    ..M$=====================~====~D=....                       ")
	print("               ..~N~=================================+8..                       ")
	print("             .,N~~===================================++~:                       ")
	print("               .M:========:=~=~=============~======~====~7..                    ")
	print("               ..=========M:::+DI~======~~=~IM7~~~D=+~~~~~=..                   ")
	print("              .$..======~?::~~~:::~:N~~=8:~:~:~~~~?N===~?==..                   ")
	print("             . .M~?O===~~$~~~~~~~~~~:Z~~:~~~~~~~~~?II==$$77,.                   ")
	print("             . ZZIZ+====+:~~~~~~~~~~~::~=~~~~~~~~~?II?7$$$$D.                   ")
	print("               .I~======O~~~~~~~~~~~~~:~~~~~~~~~~~=II78$$$$M                    ")
	print("               ..,O=====8~:~:~~~~~~~~~~~~~~~~~~~~~=IIID$$$$N.                   ")
	print("               ....M====Z~~~:~~~~~~~~~~~~~~~~~~~~~+IIIO$$$$M.                   ")
	print("                  ..$===7~~NMM,~~~~~~~~~~~~~:~~~:MD??IZ$$$$M.                   ")
	print("                    .M~~Z:MMMMMM:~~~~~~:~~~~:~$MMMMMN?O$$$OM.                   ")
	print("                   ..,DM$,OMMMMMMM~::~::~~~~DMMMMMMN7?Z7$N$M..                  ")
	print("               . ...$~~:N:~~?.~MMMMD:Z~:~:IMMMM=..NIIII7D~~I...                 ")
	print("               .....~~N8::~~M... N~8MM~~~M8I?.N...=IIIIM???IM..                 ")
	print("               .....~~IIM::~M....M,~~~~~~~~~~.M...IIII7??ZI78.                  ")
	print("               .. ..~=+$$:~=Z....I::~~~~~~~~~.~...DIII$IN?II8..                 ")
	print("                    :~~~N:::M~~::M8:~~~~~~~~DN:=:~=MIIIIINI7?..                 ")
	print("                    .7:~8~~~~~~~~~~~~::~~~~~~~~~~~~~IIO+D7IN...                 ")
	print("                    ..,MM=~~~~~~~~~~~77~~~~~~~~~~~~~IINII+,....                 ")
	print("                    ....N~~~~~~~~~~~~M7~~~~~~~~~~~~~IIN+$..                     ")
	print("                    .  .?~~~~~~~~~~~~~OI=~~~~~~~~~~~?IM... .                    ")
	print("                    ....8~~~~~~~:~~~:::::~~~~~::~~=7I7M...                      ")
	print("                     . ...M~~~=8:$~:~~~~~~~:OM:M~??I7+...                       ")
	print("                        ....M,:~~~~~$MNMOI~~~~:=77D,...                         ")
	print("                         .....=Z~:~~~~~I?:~~=~??M:...                           ")
	print("                         ....MI7Z=~~:~~~~~~~:?8I8M...                           ")
	print("                       . ..MN777~?7~~=~~~:~:$II?NNNN... .                       ")
	print("               .    .,.:M$.O7777:~~II?IIIIIIIII?MNDM,ZD$.. .                    ")
	print("                ..,,I . +.O77777:~~~~I?IIIIIIII?NDOO7.Z...+M                    ")
	print("          .. ..7$ . .....?777778,~~~:~~?+~~~~::7$777$..+....  +M,....           ")
	print("       .... N+ .. .....Z.$77777Z+~~~~:~:~~~~::7777777M.~..   .  ..M7.....       ")
	print("      . DZ.         ..M.O$77777$7D:~~~~~~~~~Z$I7777777I.N...      ....:M~.,     ")
	print("   .. 7. .         ..I M$DMNDNM8$7$N~~:~~~~N7777$77$8NM..$..             .Z  ...")
	print("  .  :, .          ..  .......,77$7N77:~~:$7DOI$8......  7..             .,,M..I")
	print("  . 8.  ..         .+.........,777777$M:8D777777D....... .N              .:..Z.M")
	print("   7....,.        .,.....,..::=777$7I$$7$77$7$77D. .~,......             .,...ZM")
	
	time.sleep(2)
	print()

	A_button = input("Hello there! Welcome to the world of POKEMON!")
	A_button = input("My name is OAK! People call me the POKEMON PROF!")
	A_button = input("This world is inhabited by creatures called POKEMON!")
	A_button = input("For some people, POKEMON are pets. Others use them for fights.")
	A_button = input("Myself... I study POKEMON as a profession.")
	player_name = input("First, what is your name? ")
	
	while player_name == "":
		player_name = input("Don't be shy! What's your name? ")
	
	A_button = input("Right! So your name is " + player_name + "!")
	print()
	
	A_button = input("This is my grandson. He's been your rival since you were a baby.")
	rival_name = input("... Erm, what is his name again? ")
	
	while rival_name == "":
		rival_name = input("Oh, you must know! What's his name? ")
	
	A_button = input("That's right! I remember now! His name is " + rival_name  + "!")
	print()
	A_button = input(player_name + "!")
	A_button = input("Your very own POKEMON legend is about to unfold!")
	A_button = input("A world of dreams and adventures with POKEMON awaits!")
	A_button = input("Let's go!")
	print()
	return rival_name
