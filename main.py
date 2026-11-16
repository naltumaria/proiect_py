from logica import creeaza_petrecere, adauga_invitat, obtine_petreceri_active

def meniu_admin():
    print("=== Autentificare ===")
    parola = input("Introdu parola: ")
    if parola != "admin":
        print("Acces respins!")
        return

    while True:
        print("\n=== MENIU PRINCIPAL ADMIN ===")
        print("1. Creeaza o petrecere noua")
        print("2. Vezi petrecerile in desfasurare")
        print("3. Iesire")
        
        optiune = input("Alege o optiune (1/2/3): ")
        
        if optiune == "1":
            print("\n--- Seteaza Detaliile ---")
            try:
                nume = input("Nume petrecere: ")
                data = input("Data si Ora: ")
                locatie = input("Locatia: ")
                dress = input("Dress Code: ")
                
                petrecere = creeaza_petrecere(nume, data, locatie, dress)
                print(f"-> Succes! Petrecerea '{petrecere['nume']}' a fost creata.")
            except ValueError as eroare:
                print(f"Eroare: {eroare}")
                
        elif optiune == "2":
            print("\n--- Petreceri Active ---")
            try:
                petreceri = obtine_petreceri_active()
                for p in petreceri:
                    print(f"- {p['nume']} | Locatia: {p['locatia']} | Data: {p['data_ora']}")
            except ValueError as eroare:
                print(f"Info: {eroare}")
                
        elif optiune == "3":
            print("Iesire din aplicatie...")
            break
        else:
            print("Optiune invalida! Te rog alege 1, 2 sau 3.")

if __name__ == "__main__":
    meniu_admin()