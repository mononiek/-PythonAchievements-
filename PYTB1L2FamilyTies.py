#Schrijf een Python script waarin je gegevens over jezelf (en je familie?) eerst in een aantal variabelen opslaat en daarna op het scherm print en mixt met gewone tekst.

#Door het print() statement te gebruiken en een concatenation operator (een komma of een plus) zet je de inhoud van de variabelen als een goed lopende zin op het scherm.

#Kies voor elk gegeven het juiste data type: string, int of float en verzin zelf duidelijke namen voor de variabelen:

#Je naam
#Je leeftijd
#Je woonplaats
#Afstand tot school in kilometers, met tenminste 1 cijfer achter de komma
#... andere leuke informatie over jezelf
#Uiteindelijk zet je alle gegevens met de print() functie op het scherm.

#De output van het Python script is dan bijvoorbeeld:

#Mijn naam is Hidde, ik ben 45 jaar oud en woon in Amsterdam.
#Ik woon 4.3 kilometer van het Mediacollege.

#Dit is het begin.

Voornaam = " Monique,"
Leeftijd = 19
Woonplaats01 = "Almere."
Woonplaats02 = "Amsterdam."
AfstandSchool01 = 46.4
AfstandSchool02 = 12.2
School = "van het Mediacollege vandaan."
Diplomas = " Ik 14 zwem diploma's heb."
Huisdier = True

print("Hallo! Mijn naam is" + Voornaam)
print("en ik ben" + str(Leeftijd))
print("Ik woon het meeste bij mijn vader in " + Woonplaats01)
print("dat is ongeveer" + str(AfstandSchool01) + " km " + School)
print("Ook woon ik veel bij mijn moeder in " + Woonplaats02)
print("dat is ongeveer" + str(AfstandSchool02) + " km " + School)
print("Een leuk feitje over mij is dat," + Diplomas)
print("Heb ik een huisdier?" + str(Huisdier))


