import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.title('Opa')

nodes = []
edges = []

nodes.append(Node(id="A1", 
                   size=100)
            ) 

nodes.append( Node(id="A2", 
                   size=100) 
            )
nodes.append( Node(id="A5", 
                   size=100) 
            )


edges.append( Edge(source="A1",
                     target="A2"
                   )
            ) 


config = Config(directed=False,
                width=500, 
                height=500, 
            
                # **kwargs
                ) 


return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config,
                      
                      )