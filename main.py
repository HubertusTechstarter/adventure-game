from game_utils import solve_riddle, end_game

def greeting():
    print("Willkommen zu 'Die verlorene Schatzsuche'!")
    print("Navigiere durch die Räume, löse Rätsel und finde den Schatz.")
    print("Verwende Befehle wie 'norden', 'süden', 'osten', 'westen', um dich zu bewegen.\n")

def enter_room(room):
    print(f"\nDu bist im {room['name']}.")
    print(room['description'])
    if not room['solved']:
        if solve_riddle(room['riddle'], room['answer']):
            room['solved'] = True
    directions = ""
    for direction in room['exits']:
        directions += direction + ", "
    directions = directions[:-2]  # Entfernt das letzte Komma und Leerzeichen
    print("Verfügbare Richtungen:", directions)

def main():
    rooms = {
        'Eingang': {
            'name': 'Eingang',
            'description': 'Ein heller Raum mit Türen in alle Richtungen.',
            'exits': {'norden': 'Bibliothek', 'osten': 'Küche'},
            'riddle': {'question': 'Ich habe Städte, aber keine Häuser. Ich habe Berge, aber keine Bäume. Was bin ich?'},
            'answer': 'karte',
            'solved': False
        },
        'Bibliothek': {
            'name': 'Bibliothek',
            'description': 'Regale voller Bücher umgeben dich.',
            'exits': {'süden': 'Eingang', 'osten': 'Gehege'},
            'riddle': {'question': 'Was kann brechen, ohne jemals zu fallen oder zu stehen?'},
            'answer': 'tag',
            'solved': False
        },
        'Küche': {
            'name': 'Küche',
            'description': 'Der Duft von frisch gebackenem Brot liegt in der Luft.',
            'exits': {'westen': 'Eingang', 'norden': 'Schatzkammer'},
            'riddle': {'question': 'Ich habe viele Schlüssel, aber kann keine Türen öffnen. Was bin ich?'},
            'answer': 'klavier',
            'solved': False
        },
        'Gehege': {
            'name': 'Gehege',
            'description': 'Ein kleiner Raum mit einem alten Globus in der Mitte.',
            'exits': {'westen': 'Bibliothek'},
            'riddle': {'question': 'Was läuft, aber hat keine Beine?'},
            'answer': 'uhr',
            'solved': False
        },
        'Schatzkammer': {
            'name': 'Schatzkammer',
            'description': 'Glitzernde Schätze liegen vor dir.',
            'exits': {},
            'riddle': {'question': 'Was wird beim Teilen größer?'},
            'answer': 'freude',
            'solved': False
        }
    }

    current_room = 'Eingang'
    greeting()

    while True:
        room = rooms[current_room]
        enter_room(room)
        
        if current_room == 'Schatzkammer' and room['solved']:
            print("Herzlichen Glückwunsch! Du hast den Schatz gefunden.")
            end_game()
        
        move = input("Wohin möchtest du gehen? ").strip().lower()
        if move in room['exits']:
            current_room = room['exits'][move]
        else:
            print("Ungültige Richtung. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
