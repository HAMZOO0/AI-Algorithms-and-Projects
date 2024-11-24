# Step 1: Install Necessary Libraries
# !pip install pgmpy networkx matplotlib

# Step 2: Define the Network Structure
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

# Define the network structure
model = BayesianNetwork([
    ('Rain', 'Sprinkler'), 
    ('Rain', 'GrassWet'), 
    ('Sprinkler', 'GrassWet')
])

print("Network Structure: ", model.edges())

# Step 3: Define Conditional Probability Tables (CPTs)
cpd_rain = TabularCPD(variable='Rain', variable_card=2, 
                      values=[[0.8], [0.2]])  # P(Rain) = [0.8, 0.2]

cpd_sprinkler = TabularCPD(variable='Sprinkler', variable_card=2, 
                           values=[[0.6, 0.99], [0.4, 0.01]],
                           evidence=['Rain'], evidence_card=[2])  # P(Sprinkler | Rain)

cpd_grasswet = TabularCPD(variable='GrassWet', variable_card=2, 
                          values=[[1, 0.1, 0.1, 0.01], [0, 0.9, 0.9, 0.99]],
                          evidence=['Sprinkler', 'Rain'], evidence_card=[2, 2])  # P(GrassWet | Sprinkler, Rain)

# Add the CPTs to the model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_grasswet)

# Validate the model
print("Model is valid: ", model.check_model())

# Step 4: Perform Inference
# Perform inference using Variable Elimination
inference = VariableElimination(model)

# Example 1: Probability of Grass being Wet
prob_grasswet = inference.query(variables=['GrassWet'])
print("P(GrassWet):")
print(prob_grasswet)

# Example 2: Update belief with evidence: It rained (Rain = 1)
prob_grasswet_given_rain = inference.query(variables=['GrassWet'], evidence={'Rain': 1})
print("\nP(GrassWet | Rain = 1):")
print(prob_grasswet_given_rain)

# Example 3: Update belief with evidence: It didn't rain, but the sprinkler was on (Rain = 0, Sprinkler = 1)
prob_grasswet_given_evidence = inference.query(variables=['GrassWet'], evidence={'Rain': 0, 'Sprinkler': 1})
print("\nP(GrassWet | Rain = 0, Sprinkler = 1):")
print(prob_grasswet_given_evidence)

# Step 5: Visualize the Bayesian Network using networkx and matplotlib
# Manually create the graph from model edges
graph = nx.DiGraph()  # Directed graph since Bayesian networks are directed
graph.add_edges_from(model.edges())

# Plot the graph using matplotlib
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph)  # Layout for nodes
nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold")
plt.title("Bayesian Network Structure")
plt.show()
