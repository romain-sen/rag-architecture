# Rag-architecture

try of lliama-index to create a rag architecture

## Usage

```bash
docker run -d -p 3000:8080 \
-v open-webui:/app/backend/data \
 -e OLLAMA_BASE_URLS="http://ollama-one:11434;http://localhost:5000/query" \
 --name open-webui \
 --restart always \
 ghcr.io/open-webui/open-webui:main
```

```bash
curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d "{\"prompt\":\"How many people live in France and in Canada ?\"}"
{
  "response": {
    "metadata": null,
    "response": "In France, about 64,756,584 people live and in Canada, approximately 38,781,291 people reside.",
    "source_nodes": []
  }
}
```
