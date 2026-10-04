from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Base de données en mémoire pour simuler le stockage des courses
commandes_centralisees = []

@app.route('/api/nouvelle-commande', methods=['POST'])
def recevoir_commande_site():
    """Point d'entrée pour recevoir les commandes des différents sites web"""
    donnees = request.json
    
    # Structure de la commande
    nouvelle_course = {
        "id": len(commandes_centralisees) + 1,
        "client": donnees.get("client", "Anonyme"),
        "telephone": donnees.get("telephone", "Non fourni"),
        "depart": donnees.get("depart", "Non spécifié"),
        "arrivee": donnees.get("arrivee", "Non spécifié"),
        "message": donnees.get("message", ""),
        "url_recu": donnees.get("url_recu", ""),
        "date_reception": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "statut": "En attente"
    }
    
    commandes_centralisees.append(nouvelle_course)
    print(f"[NOUVELLE COURSE REÇUE] ID: {nouvelle_course['id']} de {nouvelle_course['client']}")
    
    return jsonify({"status": "Succès", "course_id": nouvelle_course["id"]}), 201

@app.route('/api/courses', methods=['GET'])
def recuperer_toutes_les_courses():
    """Permet à l'application Boss Pro de récupérer toutes les courses synchronisées"""
    return jsonify(commandes_centralisees), 200

if __name__ == '__main__':
    print("Serveur Backend Karim Job Pro démarré et en écoute...")
    # Lancement du serveur sur le port 5000
    app.run(port=5000, debug=True)