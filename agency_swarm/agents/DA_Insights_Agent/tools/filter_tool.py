from agency_swarm.tools import BaseTool
import pandas as pd

class FilterTool(BaseTool):
    def run(self, condition: str, data: pd.DataFrame):
        return data.query(condition)

class SortTool(BaseTool):
    def run(self, column: str, data: pd.DataFrame, ascending=True):
        return data.sort_values(by=column, ascending=ascending)
