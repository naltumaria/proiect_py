from logica import creeaza_petrecere, adauga_invitat

def main():
    print("=== Organizare Petrecere ===")
    parola = input("Introdu parola de admin: ")
    
    if parola != "admin":
        print("Acces respins!")
        return

    print("\n--- Seteaza Detaliile Petrecerii ---")
    try:
        nume = input("Nume petrecere: ")
        data = input("Data si Ora: ")
        locatie = input("Locatia: ")
        dress = input("Dress Code: ")
        
        petrecere = creeaza_petrecere(nume, data, locatie, dress)
        print(f"\nPetrecerea {petrecere['nume']} a fost creata!")
        
        print("\n--- RSVP Invitat ---")
        nume_invitat = input("Numele tau: ")
        status = input("Participi? (Da/Nu/Poate): ")
        meniu = input("Meniu (Normal/Vegetarian/Vegan): ")
        melodie = input("Melodia preferata: ")
        
        adauga_invitat(petrecere, nume_invitat, status, meniu, melodie)
        print("\nInregistrare completa! Datele actuale sunt:")
        print(petrecere)
        
    except ValueError as eroare:
        print(f"Eroare: {eroare}")

if __name__ == "__main__":
    main()