from agency_swarm.tools import BaseTool
import pandas as pd

class QueryTool(BaseTool):
    def run(self, query: str, data: pd.DataFrame):
        if "highest sales" in query.lower():
            return data.nlargest(5, 'Sales')[['Product', 'Sales']]
        elif "last month" in query.lower():
            data['Date'] = pd.to_datetime(data['Date'])
            last_month = pd.Timestamp.now() - pd.DateOffset(months=1)
            return data[data['Date'] > last_month].shape[0]
        elif "average revenue" in query.lower() and "per category" in query.lower():
            return data['Revenue'].mean()
