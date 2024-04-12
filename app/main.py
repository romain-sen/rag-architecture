from flask import Flask, request, render_template, jsonify
import threading
from agent.agent import agent
from llama_index.core.base.response.schema import Response, NodeWithScore

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    data = request.json
    prompt = data["prompt"]
    if prompt == "q":
        return jsonify({"response": "Session ended"})
    else:
        result = agent.query(prompt)  # Utilisez votre modèle ici
        # Convertir le résultat en dictionnaire si c'est une instance de NodeWithScore
        print("Prompt: ", prompt)
        print(result)
        # Always convert the result to a serializable format before returning.
        if isinstance(result, Response):
            result = dict(
                response=result.response,
                source_nodes=[
                    {"text": sources.node.get_content(), **sources.to_dict()}
                    for sources in result.source_nodes
                ],
                metadata=result.metadata,
            )
        elif isinstance(result, NodeWithScore):
            # Convert NodeWithScore to dict if necessary.
            result = result.to_dict()
        # Assume 'result' is otherwise serializable; wrap in a dict if it's not.
        else:
            print(f"Warning: Unhandled result type: {type(result)}")
            result = str(result)  # Fallback conversion to string as last resort.

        return jsonify({"response": result})


if __name__ == "__main__":
    threading.Thread(
        target=lambda: app.run(port=5000, debug=True, use_reloader=False)
    ).start()
