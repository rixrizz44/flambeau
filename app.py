import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Le Flambeau de Suaudeau", page_icon="🔥", layout="centered")

# --- SYSTÈME DE BASE DE DONNÉES ---
DB_FILE = "flambeau_db.json"

def charger_donnees():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {
        "detenteur": "FC Nantes",
        "prochain_match": "FC Nantes vs Clermont Foot 63",
        "date_match": "Vendredi 30 octobre 2026",
        "possessions": {"FC Nantes": 1, "Clermont Foot": 0, "AS Saint-Étienne": 0}
    }

def sauvegarder_donnees(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

data = charger_donnees()

# --- HEADER : LOGO DU SITE ---
# On affiche ton magnifique logo rond centré tout en haut
st.image("image_joDeO3.png.jpeg", use_container_width=True)

st.title("🔥 Le Flambeau de Suaudeau")
st.subheader("Le trophée virtuel dynamique de la Ligue 2 BKT")
st.write("---")

# Section 1 : Détenteur Actuel
st.header("👑 Détenteur Actuel")
col1, col2 = st.columns([1, 1])

with col1:
    # On affiche ton magnifique trophée 3D ici
    st.image("image_3jnHhV.png.jpeg", caption="Le Flambeau physique actuel", use_container_width=True)
    
with col2:
    st.markdown(f"### **{data['detenteur']}**")
    st.markdown(f"**Statut :** Le Flambeau est actuellement à la Beaujoire, protégé par la légende de Coco Suaudeau.")
    st.markdown("⚠️ *Lancement officiel de la première défense ce vendredi !*")

st.write("---")

# Section 2 : Prochain Match
st.header("📅 Prochain Match de Titre")
st.success(f"⚽ **{data['prochain_match']}**")
st.write(f"**Date prévue :** {data['date_match']}")

st.write("---")

# Section 3 : Classement Dynamique
st.header("🏆 Classement Historique des Possessions")
clubs_ordonnes = sorted(data["possessions"].items(), key=lambda x: x[1], reverse=True)

rangs, clubs, possessions, statuts = [], [], [], []
for i, (club, poss) in enumerate(clubs_ordonnes):
    rangs.append(f"{i+1}er" if i==0 else f"{i+1}e")
    clubs.append(club)
    possessions.append(poss)
    statuts.append("👑 Détenteur" if club == data["detenteur"] else "Aspirant")

df = pd.DataFrame({"Rang": rangs, "Club": clubs, "Possessions": possessions, "Statut": statuts})
st.dataframe(df, use_container_width=True, hide_index=True)

st.write("---")

# Section 4 : Les Règles
st.header("📜 Les Règles d'Or")
st.markdown("""
1. **La Transmission :** Le Flambeau se transmet uniquement lorsqu'une équipe bat le détenteur actuel en Ligue 2.
2. **Le Match Nul :** En cas de match nul, le détenteur conserve le Flambeau.
3. **Le Pacte de l'Ascenseur :** Si le détenteur monte en Ligue 1, il lègue le Flambeau au premier club non-promu pour qu'il reste en Ligue 2.
""")

# --- 🔐 PANNEAU ADMIN SECRET ---
st.write("---")
with st.expander("🔐 Espace Administrateur (Bastien)"):
    st.write("Utilise cet espace secret pour mettre à jour le site après un match !")
    
    nouveau_score = st.text_input("Entre le résultat (ex: Nantes 2 - 0 Clermont)")
    nouveau_detenteur = st.selectbox("Qui a gagné le Flambeau ?", list(data["possessions"].keys()))
    futur_match = st.text_input("Prochain match à afficher", value="Clermont Foot vs Amiens SC")
    future_date = st.text_input("Date du prochain match", value="Vendredi 6 novembre 2026")
    
    if st.button("Mettre à jour le site officiellement 🚀"):
        data["detenteur"] = nouveau_detenteur
        data["prochain_match"] = futur_match
        data["date_match"] = future_date
        data["possessions"][nouveau_detenteur] = data["possessions"].get(nouveau_detenteur, 0) + 1
        sauvegarder_donnees(data)
        st.success("Le site a été mis à jour avec succès ! Rafraîchis la page.")

st.caption("Créé avec passion par Bastien. Tous droits réservés.")
