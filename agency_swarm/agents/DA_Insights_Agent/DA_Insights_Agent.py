from agency_swarm.agents import Agent

from .tools import QueryTool, CleanTool, FilterTool, StatsTool, VisualizationTool


class DA_Insights_Agent(Agent):
    def __init__(self):
        super().__init__(
            name="DA_Insights_Agent",
            description="Agent that enables users to query, analyze, and visualize CSV data using natural language",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[QueryTool, CleanTool, FilterTool, StatsTool, VisualizationTool],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message



