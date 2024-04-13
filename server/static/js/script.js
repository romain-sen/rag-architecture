function queryModel() {
  const prompt = document.getElementById("prompt").value;
  fetch("/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt: prompt }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Vérifiez que la structure de 'data' est celle que vous attendez.
      if (data.response && data.response.response) {
        document.getElementById("response").innerText = data.response.response;
      } else if (data.response) {
        document.getElementById("response").innerText = data.response;
      } else {
        // Gérez le cas où la structure de la réponse n'est pas celle attendue.
        document.getElementById("response").innerText =
          "Réponse inattendue : " + JSON.stringify(data);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("response").innerText =
        "Erreur lors de la requête.";
    });
}
