\# Medical Drug Knowledge Base (Qdrant Snapshot)



This repository contains a pre-built medical drug knowledge base stored as a Qdrant snapshot.



\## Contents

\- RxNorm-normalized drug entities

\- DrugBank clinical information

\- Vector embeddings (MiniLM)

\- Ready-to-use Qdrant snapshot



\## Requirements

\- Docker

\- Python 3.10+

\- qdrant-client

\- requests



\## Restore Instructions



```bash

docker run -d --name qdrant-medical-kb -p 6333:6333 -v qdrant\_med\_storage:/qdrant/storage qdrant/qdrant

python restore\_kb.py



