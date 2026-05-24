import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from services.handoff_service import HandoffService

load_dotenv()

deployment = os.getenv("gpt_deployment")

project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

llm_client = project_client.get_openai_client()

svc = HandoffService(azure_openai_client=llm_client, deployment_name=deployment)

print("\n--- First message ---")
print("RESULT 1:", svc.classify_intent("What colors of green paint do you have?", session_id="t1"))

print("\n--- Second message (real LLM classification) ---")
print("RESULT 2:", svc.classify_intent("How much PROD0018 is in stock?", session_id="t1"))