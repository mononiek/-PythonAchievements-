#Schrijf een function met de naam bereken_maandkosten() die 1 argument accepteert: km_per_maand.
#Zorg dat de functie de maandelijkse kosten volgens de bovenstaande regels uitrekent 
#en deze met een return statement teruggeeft
#Maak gebruik van de input() functie om het aantal kilometers per maand te vragen 
#aan de gebruiker van je programma.
#Zorg dat je controleert of de invoer wel echt een getal is.

#Een scooter rijden kost geld. Je hebt een verzekering nodig, benzine en je hebt kosten voor het onderhoud.
#Stel dat de volgende variabelen en regels er zijn om de kosten per maand te bereken 
#voor het rijden van een scooter.:

#verzekering_per_maand = € 23
#benzine_kosten_per_liter = € 1.54
#liter_per_kilometer = 0.2L 

#maandkosten = (km_per_maand x liter_per_kilometer x benzine_kosten_per_liter) + verzekering_per_maand

#Roep daarna de bereken_maandkosten() function aan met de ingevoerde kilometers 
#en gebruik de print() function om de kosten per maand op het scherm te zetten.

#Dit is het begin van de code.

import time

def bereken_maandkosten():
    km_per_maand = float(input("Schrijf hier alleen in cijfers hoeveel km je deze maand hebt gereden\n"))
    liter_per_kilometer = 0.2
    benzine_kosten_per_liter = 1.54
    verzekering_per_maand = 23
    maandkosten = km_per_maand * liter_per_kilometer * benzine_kosten_per_liter + verzekering_per_maand
    print("€" + str(maandkosten))

print("Hoi! Ik ben hier om je te helpen met het uitreken hoeveel je per maand kwijt bent aan je scooter\n Hiervoor moet ik straks van jou alleen weten hoeveel km je deze maand hebt gereden\n (of in een andere maand die je wilt uitrekenen)")

time.sleep(2)

bereken_maandkosten()

print("Het bedrach dat je hierboven ziet is hoeveel euro je kwijt bent aan je scooter.\n Let wel goed op dat de . in dit bedrag voor een komma staat, je bent dus niet zoveel duizende euro's kwijt!")
