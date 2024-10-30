import random
import json
import datetime
import time

# Naam van het spel
def random_getallen_spel():
    getal = random.randint(1, 100)
    pogingen = 0
    Maximale_pogingen = 7

    while True: 
        try: 
            Raad = input("📚 Wiskundeles: Raad een getal tussen 1 en 100. Type 'stop' om de les te verlaten. Je hebt nog " + str(Maximale_pogingen - pogingen) + " pogingen over. ")
            if Raad.lower() == "stop":
                print("De les is gestopt. Ga maar naar de gang! 🎒")
                break

            Raad = int(Raad) 
        except ValueError: 
            print("Ongeldig antwoord, probeer een cijfer of type 'stop' om te stoppen.")
            continue
        pogingen += 1 

        if pogingen > Maximale_pogingen:
            print("Je hebt " + str(Maximale_pogingen) + " pogingen gebruikt. Het geheime getal was " + str(getal) + ".")
            break

        if Raad < getal:
            print("Te laag, probeer een hoger getal.")
        elif Raad > getal:
            print("Te hoog, probeer een lager getal.")
        else:
            print("🎉 Hoera! Je hebt het geheime getal geraden!")
            print(f"Tot de volgende les!")
            break

def log_resultaten(naam, resultaat, foute_pogingen):
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("spel_log.txt", "a") as log_file:
        log_file.write(f"Naam: {naam}, Resultaat: {resultaat}, Aantal pogingen: {foute_pogingen}, Datum: {datum}\n")

def laad_woordenlijst(json_bestand):
    with open(json_bestand, 'r') as file:
        woorden = json.load(file)
    return woorden

def kies_woord(moeilijkheidsgraad):
    woorden = laad_woordenlijst('Nano\woorden.json')
    if moeilijkheidsgraad in woorden:
        return random.choice(woorden[moeilijkheidsgraad])
    else:
        print("Kies een geldige moeilijkheidsgraad.")
        return None

def toon_woord(woord, geraden_letters):
    resultaat = ""
    for letter in woord:
        if letter in geraden_letters:
            resultaat += letter
        else:
            resultaat += "_"
        resultaat += " "
    return resultaat

def kies_moeilijkheidsgraad():
    while True:
        Kies = input("📘 Taalles: Kies een moeilijkheidsgraad: makkelijk, medium of moeilijk, of type 'stop' om te stoppen: ")
        if Kies.lower() == "stop":
            print("De taalles is gestopt. Neem een pauze! ☕")
            return None
        elif Kies.lower() in ["makkelijk", "medium", "moeilijk"]:
            return Kies.lower()
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

# De verschillende stadia van het galgje-poppetje
galgje_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def galgje():
    naam = input("Wat is je naam, leerling? ")

    moeilijkheidsgraad = kies_moeilijkheidsgraad()

    if moeilijkheidsgraad is None:
        return
    
    geraden_letters = []
    foute_pogingen = 0

    if moeilijkheidsgraad == 'moeilijk':
        max_fouten = 7
    elif moeilijkheidsgraad == 'medium':
        max_fouten = 6
    else:
        max_fouten = 5

    woord = kies_woord(moeilijkheidsgraad)

    print(f"Je hebt voor de moeilijkheidsgraad {moeilijkheidsgraad} gekozen, {naam}.")
    print(f"Je hebt maximaal {max_fouten} pogingen om het woord te raden. Succes in de taalles! ✏️")

    while foute_pogingen < max_fouten:
        print(galgje_stages[foute_pogingen])
        print(f"Het huidige woord: {toon_woord(woord, geraden_letters)}")

        gok = input("Raad een letter: ").lower()

        if gok in geraden_letters:
            print(f"Je hebt al {gok} geraden. Probeer een andere letter.")

        elif gok in woord:
            print(f"Goed gedaan! {gok} zit in het woord. 📝")
            geraden_letters.append(gok)

        else:
            print(f"Helaas, {gok} zit niet in het woord.")
            foute_pogingen += 1
            geraden_letters.append(gok)
            print(f"Foute pogingen: {foute_pogingen} van {max_fouten}")

        alle_geraden = True
        for letter in woord:
            if letter not in geraden_letters:
                alle_geraden = False

        if alle_geraden:
            print(f"Topper! {naam}, je hebt het woord geraden: {woord}. 🎉")
            print(f"Tot de volgende les!")
            resultaat = 'geraden'
            break
    else:
        print(f"Helaas, {naam}. Het woord was: {woord}. Probeer het de volgende keer opnieuw. 📚")
        print(f"Tot de volgende les!")
        resultaat = 'niet geraden'

    log_resultaten(naam, resultaat, foute_pogingen)

def schrijf_in_schooldagboek(dagboek_bestand):
    # Schrijft een nieuwe schoolinput naar het dagboek.
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    vak = input("Voor welk vak schrijf je? ")
    ervaring = input("Beschrijf je ervaring of gebeurtenissen van vandaag: ")
    
    with open(dagboek_bestand, 'a') as bestand:
        bestand.write(f"{datum} - {vak}: {ervaring}\n")
    
    print("Je reflectie is succesvol in je Schooldagboek opgeslagen! 📚✏️  Tijd om verder te leren en te groeien!")

def lees_schooldagboek(dagboek_bestand):
    # Leest en toont de inhoud van het schooldagboek.
    try:
        with open(dagboek_bestand, 'r') as bestand:
            inhoud = bestand.readlines()
            if inhoud:
                print("Inhoud van je schooldagboek 👀:")
                for regel in inhoud:
                    print(regel.strip())
            else:
                print("Je schooldagboek is nog leeg.")
    except FileNotFoundError:
        print("Schooldagboekbestand niet gevonden. 📓 Tijd om met een schone lei te beginnen")

def schooldagboek():
    dagboek_bestand = "school_dagboek.txt"
    
    while True:
        print("Kies een optie:")
        print("1. Schrijf in schooldagboek")
        print("2. Lees schooldagboek")
        print("3. Stop")

        keuze = input("Voer je keuze in (1/2/3): ")

        if keuze == '1':
            schrijf_in_schooldagboek(dagboek_bestand)
        elif keuze == '2':
            lees_schooldagboek(dagboek_bestand)
        elif keuze == '3':
            print("Bedankt voor het gebruik van je schooldagboek. Tot ziens 🎒!")
            break
        else:
            print("Ongeldige keuze. 🚫 Probeer het opnieuw.")

def breuk_naar_decimaal():
    # Zet de breuken om naar decimalen.
    naam = input("Wat is je naam, leerling? ")
    print(f"Welkom, {naam}! Het is tijd voor de Wiskundewedstrijd! 🧮")

    score = 0  # Begin met een score van 0
    start_time = time.time()  # Slaat de starttijd op als het spel begint
    tijdslimiet = 60  # Het spel duurt 60 seconden (1 minuut)

    # Terwijl de tijd nog niet om is
    while time.time() - start_time < tijdslimiet:
        teller = random.randint(1, 10)  # Kies een willekeurige bovenkant van de breuk
        noemer = random.randint(1, 10)
        juiste_antwoord = teller / noemer  # Bereken het juiste decimale antwoord

        print(f"Breuk: {teller}/{noemer}")
        try:
            # Vraag de speler om het decimale getal in te voeren of om te stoppen
            invoer = input("Zet de breuk om naar een decimaal (type 'stop' om te stoppen): ")
            if invoer.lower() == 'stop':  # Controleer of de speler 'stop' heeft getypt
                print("Het spel is gestopt. Tot ziens! 🎒")
                break  # Stop het spel
            antwoord = float(invoer)  # Probeer de invoer om te zetten naar een float
        except ValueError:
            print("Ongeldig antwoord. Probeer een getal in te voeren of type 'stop' om te stoppen.")  # Foutmelding als het geen geldig getal is
            continue  # Ga terug naar het begin van de lus

        # Controleer of het antwoord juist is
        if antwoord == juiste_antwoord:
            print("Correct! 🎉")  # Als het juist is
            score += 1  # Verhoog de score met 1
        else:
            print(f"Helaas, het juiste antwoord was {juiste_antwoord:.2f}. Probeer het opnieuw.")

    # Als de tijd om is of als het spel is gestopt
    print(f"Je eindscore is: {score}. Goed gedaan, {naam}!")

def rock_paper_scissors():
    opties = ["steen", "papier", "schaar"]
    klasgenoten = [
        {"naam": "Priscillia", "special": "Verdubbel je punten als je wint"},
        {"naam": "Tom", "special": "Krijg een herkansing als je verliest"},
        {"naam": "Sara", "special": "Kies een optie voor de tegenstander"},
        {"naam": "Jasper", "special": "Krijg een herstart als je twee keer verliest"},
        {"naam": "Lisa", "special": "Verlies geen punten bij gelijkspel"}
    ]

    print("Welkom bij het Steen-Papier-Schaar Toernooi in de klas! 🎓")
    print("Je hebt speciale vaardigheden die je kunt gebruiken om te winnen!")

    speler_score = 0
    tegenstander_score = 0
    rondes = 3  # Aantal rondes in het toernooi

    for ronde in range(1, rondes + 1):
        print(f"\n--- Ronde {ronde} van {rondes} ---") #\n, wordt gebruikt voor witte regel
        tegenstander = random.choice(klasgenoten)
        print(f"Je speelt tegen {tegenstander['naam']} in de school! Speciale vaardigheid: {tegenstander['special']} ⚔️")

        speler_keuze = input("Kies steen, papier of schaar (of typ 'stop' om te stoppen): ").lower()
        if speler_keuze == "stop":
            print("Bedankt voor het spelen! Tot de volgende les! 📚")
            return  # Stopt het spel

        if speler_keuze not in opties:
            print("Ongeldige keuze, probeer het opnieuw.")
            continue

        computer_keuze = random.choice(opties)
        print(f"{tegenstander['naam']} kiest: {computer_keuze}")

        # Bepaalt de uitkomst
        if speler_keuze == computer_keuze:
            print("Gelijkspel! Jullie zijn gelijkwaardige tegenstanders! 🤼")
            if tegenstander['naam'] == "Lisa":
                print("Je verliest geen punten!")
            continue  # Gaat naar de volgende ronde

        elif (speler_keuze == "steen" and computer_keuze == "schaar") or \
             (speler_keuze == "papier" and computer_keuze == "steen") or \
             (speler_keuze == "schaar" and computer_keuze == "papier"):
            print("Je wint deze ronde! Geweldig gedaan! 🎉")
            speler_score += 1
            if tegenstander['naam'] == "Priscillia":
                speler_score += 1  # Verdubbelt score als je wint
                print("Je score is verdubbeld door Priscillia's special!")

        else:
            print("Je verliest deze ronde! Beter de volgende keer! 😢")
            tegenstander_score += 1
            if tegenstander['naam'] == "Tom":
                print("Je krijgt een herkansing!")
                speler_keuze = input("Kies steen, papier of schaar voor je herkansing: ").lower()
                if speler_keuze not in opties:
                    print("Ongeldige keuze, je hebt geen herkansing gewonnen.")
                    continue

                computer_keuze = random.choice(opties)
                print(f"{tegenstander['naam']} kiest: {computer_keuze}")
                if (speler_keuze == "steen" and computer_keuze == "schaar") or \
                   (speler_keuze == "papier" and computer_keuze == "steen") or \
                   (speler_keuze == "schaar" and computer_keuze == "papier"):
                    print("Je wint de herkansing! 🎉")
                    speler_score += 1

            if tegenstander['naam'] == "Jasper":
                print("Je hebt een herstart gekregen, laten we de ronde opnieuw spelen. 💪")
                ronde -= 1  # Herstart de ronde

        print(f"Scores na ronde {ronde} - Jij: {speler_score}, {tegenstander['naam']}: {tegenstander_score}")

    # Einde van het toernooi
    print("\n--- Einde van het toernooi! ---")
    if speler_score > tegenstander_score:
        print(f"Gefeliciteerd! Je hebt het toernooi gewonnen met {speler_score} punten! 🏆")
    elif speler_score < tegenstander_score:
        print(f"Helaas, je hebt verloren met {tegenstander_score} punten. Probeer het opnieuw! 😔")
    else:
        print("Het toernooi eindigt in een gelijkspel! Mooi gedaan! 🤝")

def menu():
    while True:
        print("Welkom bij de Schoolspellen Academie! 🎓\nLeren door te spelen, winnen door te leren!")
        print("1. ✏️   Galgje (Taalles)")
        print("2. 📚  Random Getallen Spel (Rekenles)")
        print("3. 📓  Dagboek (Mijn Schoolreis Reflecties)")
        print("4. 🧮  Breuken naar Decimalen (Wiskundeles)")
        print("5. 🎲  Steen, Papier, Schaar (Speel met je klasgenoten)")
        print("6. 🏫  Stop (School uit)")

        keuze = input("Maak je keuze (1, 2, 3, 4, 5 of 6): ")
        
        if keuze == '1':
            galgje()
            
        elif keuze == '2':
            random_getallen_spel()

        elif keuze == '3':
            schooldagboek()

        elif keuze  == '4':
            breuk_naar_decimaal()

        elif keuze ==  '5':
            rock_paper_scissors()

        elif keuze == '6':
            print("Tot ziens, ga maar lekker naar huis! 🎒")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

# Start het menu en de ander spellen
menu()
