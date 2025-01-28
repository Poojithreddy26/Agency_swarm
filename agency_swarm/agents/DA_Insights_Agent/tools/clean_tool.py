from agency_swarm.tools import BaseTool
import pandas as pd

class CleanTool(BaseTool):
    def run(self, data: pd.DataFrame):
        missing_values = data.isnull().sum()
        duplicates = data.duplicated().sum()
        return {"missing_values": missing_values, "duplicates": duplicates}
