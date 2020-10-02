#Welke keuzes maak jij op een dagelijkse basis? 
#Snooze je je telefoon of sta je gelijk op? 
#Eet je een broodje of kies je voor een kom muesli? 
#Neem je het OV of pak je de brommer? 
#Ga je vooraan of achteraan in de klas zitten?

#Maak een programma met daarin 5 verschillende keuzes die je kunt na elkaar kunt maken. 
#Gebruik hiervoor de if, elif, else structuur. 
#Voor het invoeren van keuzes kun je de input() functie van python gebruiken.

#Geef de speler dus de mogelijkheid om dezelfde keuzes te maken die jij ook maakt op een dagelijkse basis.

#De gemaakte keuze hoeft geen invloed te hebben op de nieuwe keuze. 
#Als de speler een niet aangeboden keuze maakt hoeft de keuze niet opnieuw aangeboden te worden.

#Hier begint het

import time

print("Het is Dinsdag ochtend en je wekker gaat.")
print("Wat doe je? \nA. Nog 5 minuutjes. B. Gelijk opstaan.")
Antwoord01 = input("Schrijf A of B \n")
if Antwoord01.upper() == "A":
	print("Oeps! die 5 minuten zijn er 10 geworden.. dan maar iets korter onder de douche.")
elif Antwoord01.upper() == "B":
	print("Je gaat gelijk je bed uit en gaat je wassen.")
else:
	print("je hebt geen A of B ingevult, maar ik trek je wel gewoon uit je bed.")

time.sleep(1)

print("Oke je bent je bed uit en heb je gewassen. Zullen we gaan onbijten?")
print("A. Ja lekker! B. Nee geen trek.")
Antwoord02 = input("Schrijf A of B \n")
if Antwoord02.upper() == "A":
	print("Is kijken wat we in huis hebben.")
elif Antwoord02.upper() == "B":
	print("Weet je het zeker?.. Weet je wat? We gaan het toch gewoon doen!")
else:
	print("je hebt geen A of B ingevult, maar geen zorgen we gaan als nog ontbijt maken.")

time.sleep(1)

print("Ontbijt dus.. mmmhh.. Wat zullen we maken?")
print("A. Een broodje uit de vrieser met chocopast. \nB. Een paar geklutste eieren. \nC. Ontbijtkoek met hagelslag.")
Antwoord03 = input("Schrijf A, B of C \n")
if Antwoord03.upper() == "A":
	print("Het is wat droog en taai, maar het gaat.")
elif Antwoord03.upper() == "B":
	print("Het duurt wat langer om te maken, maar daarna kan wel echt genieten.")
elif Antwoord03.upper() == "C":
	print("Snel, makkelijk en lekker, Wat wil je nog meer?")
else:
	print("je hebt geen A, B of C ingevult, en dus geen ontbijt genomen. Niet slim van je.")

time.sleep(1)

print("Nu alleen nog aankleden en dan kan je naar school")
print("Wat ga je vandaag dragen? \nA. Iets dat lekker zit. bvb. jogging broek met vest. \nB. Iets dat leuk staat. bvb. nep leren broek met tshirt. \nC. Iets over de top. bvb. een fel rood mantel pak. \nD. Een jurk.")
Antwoord04 = input("Schrijf A, B, C of D\n")
if Antwoord04.upper() == "A":
	print("Het kan, als jij je er maar fijn in voelt.")
elif Antwoord04.upper() == "B":
	print("Het zit misschien minder lekker, maar het staat wel leuk.")
elif Antwoord04.upper() == "C":
	print("Gedurft, maar het staat je goed hoor.")
elif Antwoord04.upper() == "D":
	print("Een jurk? Met dit weer?.. You do you..")
else:
	print("je hebt geen A, B, C of D ingevult, en heb dus geen kleding uit gekozen. \nGeen zorgen, ik kies wel gewoon wat voor je uit.")

time.sleep(1)

print("Heb je alles bij je? Jas, tas, ov? En vergeet je mondkapje niet!")
print("Je hebt alles? Gelukkig, laten we nu maar snel naar de bushalte lopen voor dat.....\nOhw nee he? De bus staat er al.")
print("Als we rennen hallen we hem misschien nog net!")
Antwoord05 = input("Kies A of B! \nGeen tijd om uit te leggen welk antwoord wat is!\n")
if Antwoord05.upper() == "A":
	print("Het scheelde maar weinig of we hadden de bus gemist, maar gelukkig toch nog net gehaald.")
elif Antwoord05.upper() == "B":
	print("Ohw nee, je struikelde bijna en hebt daardoor de bus gemist! \nGeen zorgen over 5 minuten komt de volgende, die halen we zeker.")
else:
	print("je hebt geen A of B ingevult, en hebt dus de bus gemist!")

print("gefeliciteerd! Ondanks alles ben je op tijd op school aangekomen.")

