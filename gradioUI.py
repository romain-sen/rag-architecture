import requests
import gradio as gr


def interroger_modele(prompt):
    url = "http://127.0.0.1:5000/query"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}

    # Envoyer la requête au modèle
    response = requests.post(url, headers=headers, json=data)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Extraire et retourner la réponse
        data_response = response.json()
        print(data_response)
        # Directly return the 'response' content from the JSON, no nested 'get' needed
        return data_response.get("response", "Aucune réponse")
    else:
        return "Erreur lors de la communication avec le modèle."


# Créer l'interface Gradio
interface = gr.Interface(
    fn=interroger_modele,
    inputs=gr.Textbox(lines=2, placeholder="Entrez votre question ici..."),
    outputs="text",
    title="Interrogation du Modèle de Langage",
    description="Entrez une question pour obtenir une réponse du modèle.",
)

# Lancer l'interface
interface.launch()
