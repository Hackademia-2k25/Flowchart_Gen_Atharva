from flask import Flask, request, jsonify, send_file
import requests
import os
from graphviz import Digraph

# Set up Flask
app = Flask(__name__)

# Set environment for Ollama or Gemini models
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

# Function to call LLaMA or Gemini model API
def llama_process_text(description):
    """Send the algorithm description to LLaMA or Gemini API for processing."""
    payload = {"input": description}  # Prepare payload for the API

    try:
        # Replace with the actual LLaMA or Gemini API endpoint (Ollama or Gemini 1.5)
        response = requests.post("http://localhost:5001/process", json=payload)  # Example endpoint
        response.raise_for_status()
        return response.json()  # Assumes the response is structured as JSON containing nodes and edges
    except Exception as e:
        print(f"Error processing the description: {e}")
        return {
            "nodes": [
                {"id": "start", "type": "start", "label": "Start"},
                {"id": "step1", "type": "process", "label": "Load data from database"},
                {"id": "step2", "type": "process", "label": "Preprocess the data"},
                {"id": "step3", "type": "decision", "label": "Is data clean?"},
                {"id": "step4", "type": "process", "label": "Clean data"},
                {"id": "end", "type": "end", "label": "End"}
            ],
            "edges": [
                {"from": "start", "to": "step1"},
                {"from": "step1", "to": "step2"},
                {"from": "step2", "to": "step3"},
                {"from": "step3", "to": "step4", "condition": "No"},
                {"from": "step3", "to": "end", "condition": "Yes"},
                {"from": "step4", "to": "end"}
            ]
        }

# Function to generate flowchart/diagram using Graphviz
def generate_diagram(data):
    """Generate a flowchart/diagram from the structured data."""
    dot = Digraph(format="png")
    
    # Add nodes to the graph
    for node in data["nodes"]:
        shape = "ellipse" if node["type"] in ["start", "end"] else "box"
        dot.node(node["id"], node["label"], shape=shape)
    
    # Add edges between nodes
    for edge in data["edges"]:
        dot.edge(edge["from"], edge["to"], label=edge.get("condition", ""))
    
    # Save diagram as PNG file
    output_path = "generated_diagram"
    dot.render(output_path, view=False)
    return f"{output_path}.png"

@app.route("/generate", methods=["POST"])
def generate():
    """API endpoint to process the algorithm description and generate a diagram."""
    data = request.json  # Expect a JSON body with {"description": "your text here"}
    description = data.get("description", "")

    if not description:
        return jsonify({"error": "Description is required"}), 400

    # Process description with LLaMA/Gemini model
    structured_data = llama_process_text(description)
    
    # Generate diagram from the structured data
    diagram_path = generate_diagram(structured_data)
    
    # Return the diagram as a file response
    return send_file(diagram_path, mimetype="image/png")

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
