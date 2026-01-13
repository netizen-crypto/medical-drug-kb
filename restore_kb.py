import requests
from pathlib import Path

QDRANT_URL = "http://localhost:6333"
COLLECTION = "drug_kb"
SNAPSHOT_PATH = Path("snapshots/drug_kb_v1.snapshot")

if not SNAPSHOT_PATH.exists():
    raise FileNotFoundError(f"Snapshot not found: {SNAPSHOT_PATH}")

url = f"{QDRANT_URL}/collections/{COLLECTION}/snapshots/recover"

with open(SNAPSHOT_PATH, "rb") as f:
    response = requests.post(
        url,
        files={"snapshot": f},
        timeout=300
    )

response.raise_for_status()

print("✅ Drug knowledge base restored successfully")
