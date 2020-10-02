#Schrijf een script dat aftelt van 1000 naar 0. 
#Als de 0 bereikt is moet er iets spannends gebeuren. 
#Een explosie (sound)? of een bos bloemen (ascii art)? 
#Een mooie RickRoll? iig iets creatiefs waar je trots op bent.

#De code moet met het veranderen van 1 variabele aan te passen zijn zodat deze aftelt van 10000 naar 0.

#Dit is het begin.

import time

aftellen = 1000
while aftellen > -1:
	print(aftellen)
	if aftellen == 0:
		print("                             ____  ")
		print("                     __,-~~/~    `---. ")
		print("                   _/_,---(      ,    ) ")
		print("               __ /        <    /   )  \___  ")
		print("- ------===;;;'====------------------===;;;===----- -  - ") 
		print("                  \/  ~'~'~'~'~'~\~'~)~'/ ") 
		print("                  (_ (   \  (     >    \) ")
		print("                   \_( _ <         >_>' ") 
		print("                      ~ `-i' ::>|--' ")
		print("                          I;|.|.| ")
		print("                         <|i::|i|`. ")
		print("                        (` ^''`-' ') ")
	aftellen -= 1
	time.sleep(0.125)





