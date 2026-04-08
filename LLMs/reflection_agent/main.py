from dotenv import load_dotenv

# Load the keys in the env.
load_dotenv()

# THIS IS 
from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, MessagesState, StateGraph

# importing the modules that we built.
from chains import generate_chain, reflect_chain

REFLECT = "reflect"
GENERATE = "generate"



# Now nodes receive a SATATE DICT instead of raw list
def generation_node(state: MessagesState):
    return {"messages": [ generate_chain.invoke({"messages": state["messages"]}) ]}

def reflection_node(state: MessagesState):
    # get the reflection suggestion of ai
    respuesta = reflect_chain.invoke({ "messages": state["messages"] })
    # return the properly format and tell this was Humman
    return {"messages": [ HumanMessage(content=respuesta.content) ] }

def should_continue(state: MessagesState):
    if len(state["messages"]) > 6:
        return END 
    return REFLECT

# build the graph 
# old version
# my_graph = MessagesState()

my_graph = StateGraph(MessagesState) # new version

my_graph.add_node(GENERATE, generation_node)
my_graph.add_node(REFLECT, reflection_node)
my_graph.set_entry_point(GENERATE)

# building the edges.
my_graph.add_conditional_edges(GENERATE, should_continue, {END:END, REFLECT:REFLECT})
my_graph.add_edge(REFLECT, GENERATE)

# build the graph
built_graph = my_graph.compile()

# show the graph with mermaid
print(built_graph.get_graph().draw_mermaid())


if __name__=='__main__':
    print("hello langGraph")

    input ={
            "messages": HumanMessage(content=" write me a tweet about the future of AI agents.")
            }

    bot_answer = built_graph.invoke(input)
    # print all the list generated with the graph
    # print(bot_answer)

    ## gnerate all the sequence and thinking.
    for i, answer in enumerate(bot_answer["messages"]):
        print(f"\n --- Message {i+1} [{answer.type.upper()}] ---")
        print(answer.content)
    