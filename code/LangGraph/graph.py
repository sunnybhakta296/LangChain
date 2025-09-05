# graph.py
from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from agents import supervisor_agent, research_agent, code_agent
from IPython.display import Image, display


class AgentState(TypedDict):
    task: str
    result: Optional[str]
    next: Optional[str]

builder = StateGraph(AgentState)

builder.add_node("supervisor_agent", supervisor_agent)
builder.add_node("research_agent", research_agent)
builder.add_node("code_agent", code_agent)

def route_to_agent(state):
    return state.get("next", "research_agent")

builder.set_entry_point("supervisor_agent")
builder.add_conditional_edges(
    "supervisor_agent",
    route_to_agent,
    {
        "research_agent": "research_agent",
        "code_agent": "code_agent"
    }
)

builder.add_edge("research_agent", END)
builder.add_edge("code_agent", END)

graph = builder.compile()
try:
    print("Displaying graph at location in code: /c:/Users/sunnykumar.bhakta/sunny-dev/options/LLM-RAG-AGENTIC-AI/code/AGENTIC-AI/graph.py")
    img = graph.get_graph().draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(img)
    print("Graph image saved as graph.png in the current folder.")
    print("Graph visualization generated successfully.")
except Exception:
    print("Graph visualization could not be generated.")
    # This requires some extra dependencies and is optional
    # pass