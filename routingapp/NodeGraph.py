import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

# Your XML data
xml_data = """
  xml data goes here
"""

# Parse the XML
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

# Create a graph
G = nx.Graph()

# Add nodes to the graph
for node in root.findall('node'):
    node_id = node.get('id')
    lat = float(node.find('lat').text)
    lon = float(node.find('lon').text)
    G.add_node(node_id, pos=(lon, lat))

# Add edges to the graph
for way in root.findall('way'):
    nodes = way.findall('node')
    for i in range(len(nodes) - 1):
        G.add_edge(nodes[i].text, nodes[i+1].text)

# Extract positions
pos = nx.get_node_attributes(G, 'pos')

print()
# Draw the graph
nx.draw(G, pos, node_size=20, node_color='blue', with_labels=True)
plt.show()