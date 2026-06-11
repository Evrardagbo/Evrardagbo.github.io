import tkinter as tk
import random

def generer_nombres():
    # On vide l'ancien résultat
    resultat_text.delete(1.0, tk.END)
    
    # Pour chaque cadran de 1 à 5
    for cadran in range(1, 6):
        # Génère 5 nombres aléatoires entre 1 et 100 par exemple
        nombres = [random.randint(1, 100) for _ in range(5)]
        
        # Affiche ça joliment
        ligne = f"Cadran {cadran} : {nombres}\n"
        resultat_text.insert(tk.END, ligne)

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur par Cadran")
fenetre.geometry("350x400")

# Style un peu moderne
fenetre.configure(bg="#2E2E2E")

# Titre
titre = tk.Label(fenetre, 
                 text="Générateur Aléatoire", 
                 font=("Arial", 16, "bold"),
                 bg="#2E2E2E", 
                 fg="white")
titre.pack(pady=15)

# Bouton générer
bouton = tk.Button(fenetre, 
                   text="Générer les 5 cadrans", 
                   command=generer_nombres,
                   font=("Arial", 12),
                   bg="#0078D4", 
                   fg="white",
                   activebackground="#005A9E",
                   relief=tk.FLAT,
                   padx=20, 
                   pady=10)
bouton.pack(pady=10)

# Zone de résultat
resultat_text = tk.Text(fenetre, 
                        height=12, 
                        width=35,
                        font=("Consolas", 11),
                        bg="#1E1E1E",
                        fg="#00FF00",
                        relief=tk.FLAT)
resultat_text.pack(pady=10, padx=20)

fenetre.mainloop()