from date_invitati import invitati_petrecere, lista_petreceri

def creeaza_petrecere(nume, data_ora, locatia, dress_code):
    nume = nume.strip()
    if not nume:
        raise ValueError("Numele petrecerii nu poate fi gol.")
    
    petrecere = {
        "nume": nume,
        "data_ora": data_ora,
        "locatia": locatia,
        "dress_code": dress_code,
        "invitati": invitati_petrecere
    }
    
    lista_petreceri.append(petrecere)
    return petrecere

def obtine_petreceri_active():
    if not lista_petreceri:
        raise ValueError("Momentan nu există nicio petrecere în desfășurare.")
    return lista_petreceri

def adauga_invitat(petrecere, nume, status, meniu, melodie):
    nume = nume.strip()
    if not nume:
        raise ValueError("Numele invitatului este obligatoriu.")
        
    status = status.capitalize()
    if status not in ["Da", "Nu", "Poate"]:
        raise ValueError("Statusul trebuie să fie: Da, Nu sau Poate.")
        
    invitat_nou = {
        "id": len(petrecere["invitati"]) + 1,
        "nume": nume,
        "status": status,
        "meniu": meniu,
        "melodie": melodie
    }
    
    petrecere["invitati"].append(invitat_nou)
    return petrecere