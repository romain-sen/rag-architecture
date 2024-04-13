# Rag-architecture

Try of lliama-index to create a rag architecture

## Usage

To run the project, you need to run the server and the client.

To run the server, use the following command:

```bash
cd app
python3 main.py
```

To run the web client, use the following command:

```bash
cd web
python3 interface.py
```

When running for the first time the server, it will create indexes for the documents in the `data` folder. This process may take a while, depending on the number of documents. Then, it saves it in the `index` folder.
