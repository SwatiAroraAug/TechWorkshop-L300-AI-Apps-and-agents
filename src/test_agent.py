import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

load_dotenv()
cred = DefaultAzureCredential()
client = AIProjectClient(endpoint=os.environ["FOUNDRY_ENDPOINT"], credential=cred)

agent_names = ["cora", "inventory-agent", "customer-loyalty",
               "interior-designer", "cart-manager", "handoff-service"]

with client:
    for name in agent_names:
        try:
            versions = list(client.agents.list_versions(agent_name=name))
            if versions:
                print(f"  ✅ {name}: {[a.id for a in versions]}")
            else:
                print(f"  ❌ {name}: NOT FOUND")
        except Exception as e:
            print(f"  ❌ {name}: ERROR - {e}")