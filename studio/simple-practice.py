import random 
from typing import Literal,List
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    graph_state : str
    node_ran: List[int]

# Conditional edge
def decision_node(state:State) -> Literal["node_2", "node_3", "node_4"]:
    print("--Decision Node--")
    return random.choice(["node_2", "node_3", "node_4"])

# Nodes
def node_1(state: State):
    print("--Node 1--")
    new_node_ran = state.get("node_ran",[]) + [1]
    return {"graph_state": "Bilal is" ,"node_ran":new_node_ran}

def node_2(state: State):
    print("--Node 2--")
    new_node_ran = state["node_ran"] + [2]
    return {"graph_state": state["graph_state"] + " happy.","node_ran":new_node_ran}

def node_3(state: State):
    print("--Node 3--")
    new_node_ran = state["node_ran"] + [3]
    return {"graph_state": state["graph_state"] + " sad.","node_ran":new_node_ran}


def node_4(state: State):
    print("--Node 4--")
    new_node_ran = state["node_ran"] + [4]
    return {**state,"node_ran":new_node_ran}

# Build graph
graph_builder = StateGraph(State)
graph_builder.add_node("node_1", node_1)
graph_builder.add_node("node_2", node_2)
graph_builder.add_node("node_3", node_3)
graph_builder.add_node("node_4", node_4)

## Logic for the graph
graph_builder.add_edge(START, "node_1")
graph_builder.add_conditional_edges("node_1", decision_node)
graph_builder.add_edge("node_4", "node_1")
graph_builder.add_edge("node_2", END)
graph_builder.add_edge("node_3", END)

# Compile graph
graph = graph_builder.compile()