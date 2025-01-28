from agency_swarm.tools import BaseTool
import pandas as pd

class StatsTool(BaseTool):
    def run(self, column: str, data: pd.DataFrame):
        return {
            "total": data[column].sum(),
            "average": data[column].mean(),
            "median": data[column].median(),
            "std_dev": data[column].std()
        }
