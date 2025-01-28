from agency_swarm import Agency

from agents.DA_Insights_Agent import DA_Insights_Agent

da_insights_agent = DA_Insights_Agent()
agency = Agency([da_insights_agent])

demo = agency.demo_gradio(height=700)