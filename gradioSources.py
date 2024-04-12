import gradio as gr
import requests
import json
import re

all_sources = []


def interroger_modele_prod(prompt):
    url = "http://127.0.0.1:5000/query"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        data_response = response.json()
        print(data_response)
        response_text = data_response["response"]["response"]
        source_nodes = data_response["response"]["source_nodes"]
        source_list = [
            {
                "name": f"{node['node']['metadata']['file_name']} - Page: {node['node']['metadata']['page_label']} - Score: {node['score']:.2f}",
                "text": node["text"],
            }
            for node in source_nodes
        ]
        global all_sources
        all_sources = source_list
        sources_dropdown = gr.Dropdown(
            label="Choisissez une source",
            choices=(
                [node["name"] for node in source_list]
                if len(source_list) > 0
                else ["Aucune source"]
            ),
        )
        sources_markdown = "\n".join([f"- {node['name']}" for node in source_list])
        return prompt, response_text, sources_markdown, sources_dropdown
    else:
        return (
            prompt,
            "Erreur lors de la communication avec le modèle.",
            "",
            gr.Dropdown(label="Choisissez une source", choices=["Aucune source"]),
        )


def afficher_source(source_name):
    source_text = next(
        (node["text"] for node in all_sources if node["name"] == source_name), None
    )
    if source_text is None:
        source_text = "Aucun texte trouvé pour cette source."
    else:
        # Remove the "\n" characters from the text
        source_text = re.sub(r"\n", " ", source_text)
    return source_text


with gr.Blocks() as demo:
    with gr.Column():
        title = gr.Markdown(
            """
        # TNP x CentraleSupélec - Projet RAG
        Ce démonstrateur permet d'interroger un modèle de langage pour obtenir des réponses à des questions utilisant la génération de texte augmentée par récupération (RAG).

        La librairie Gradio est utilisée pour créer l'interface utilisateur. Pour la partie serveur, un serveur Flask est utilisé pour communiquer avec le modèle de langage.
        Enfin, le modèle de langage utilise la librarie LlamaIndex pour interroger différentes sources de données.

        **Instructions:**
        - Entrez une question dans le champ de texte ci-dessous.
        - Cliquez sur le bouton "Interroger" pour obtenir une réponse du modèle.
        - Choisissez une source parmi celles listées pour afficher le texte correspondant.

        **Hyperparamètres de la RAG:**
        - The chunk size is 1024.
        - The chunk overlap is 20.
        - The embedding model is 'BAAI/bge-small-en-v1.5'.
        - The tokenization model is 'mistralai/Mistral-7B-Instruct-v0.2'.
        """
        )
    with gr.Row():
        prompt_input = gr.Textbox(
            label="Entrez votre question ici...", placeholder="Tapez votre prompt"
        )
        submit_button = gr.Button("Interroger")

    with gr.Column():
        prompt_output = gr.Textbox(label="Prompt", interactive=False)
        response_output = gr.Textbox(label="Réponse de l'agent", interactive=False)
        sources_markdown = gr.Markdown(label="Sources")

    with gr.Column():
        sources_dropdown = gr.Dropdown(
            label="Choisissez une source", choices=["Exemple de source..."]
        )
        source_text = gr.Textbox(
            label="Détails de la source sélectionnée", interactive=False
        )

    submit_button.click(
        interroger_modele_prod,
        inputs=prompt_input,
        outputs=[prompt_output, response_output, sources_markdown, sources_dropdown],
    )
    # When selecting a source from the dropdown, display the source text
    sources_dropdown.change(
        afficher_source, inputs=sources_dropdown, outputs=source_text
    )

demo.launch(debug=True)
