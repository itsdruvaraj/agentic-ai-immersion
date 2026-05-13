"""Hosted Agent - Credit Risk & Compliance Skills."""
import os
from pathlib import Path

from agent_framework import Agent, SkillsProvider
from agent_framework_foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

INSTRUCTIONS = (
    "You are a financial services AI agent deployed on Azure Foundry. "
    "Use your available skills to assess credit risk and screen transactions "
    "for AML/KYC compliance. Provide clear, actionable guidance while noting "
    "regulatory disclaimers."
)


def main():
    credential = DefaultAzureCredential()

    client = FoundryChatClient(
        credential=credential,
        model=os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4o"),
    )

    skills_provider = SkillsProvider.from_paths(
        str(Path(__file__).parent / "skills"),
    )

    agent = Agent(
        client=client,
        instructions=INSTRUCTIONS,
        context_providers=[skills_provider],
        default_options={"store": False},
    )

    server = ResponsesHostServer(agent)
    server.run()


if __name__ == "__main__":
    main()
