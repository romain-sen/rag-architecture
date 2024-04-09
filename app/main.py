from flask import Flask, request, render_template, jsonify
import threading
from agent.agent import agent
from llama_index.core.base.response.schema import Response

app = Flask(__name__)


class NodeWithScore:
    def to_dict(self):
        return {
            "attr1": self.attr1,
            "attr2": self.attr2,
            # Ajoutez tous les attributs pertinents ici
        }


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
            result = result.response
        elif isinstance(result, NodeWithScore):
            # Convert NodeWithScore to dict if necessary.
            result = result.to_dict()
        # Assume 'result' is otherwise serializable; wrap in a dict if it's not.
        else:  # not isinstance(result, (dict, list, str, int, float)):
            print(f"Warning: Unhandled result type: {type(result)}")
            result = str(result)  # Fallback conversion to string as last resort.

        return jsonify({"response": result})
        # return jsonify({"response": str(result)})
        # # if isinstance(result, NodeWithScore):
        # #     result_dict = result.to_dict()  # Conversion en dictionnaire
        # #     return jsonify({"response": result_dict})
        # # else:
        # #     return jsonify({"response": result})


if __name__ == "__main__":
    threading.Thread(
        target=lambda: app.run(port=5000, debug=True, use_reloader=False)
    ).start()
