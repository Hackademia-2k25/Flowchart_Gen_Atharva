# Algorithm Diagram Generator

## Overview

This tool generates block diagrams, flowcharts, or illustrative representations from textual descriptions of algorithms. It supports algorithms from domains such as Database Management Systems (DBMS) and Machine Learning (ML). The backend leverages cost-free AI solutions like LLaMA (via Ollama) or Gemini 1.5 Flash API for processing.

---

## Features

- **Text-to-Diagram Conversion**: Parses algorithm descriptions and creates intuitive visual representations.
- **Domain-Specific Support**: Tailored for DBMS and ML algorithms.
- **Backend Flexibility**: Uses cost-free AI backends like LLaMA and Gemini 1.5 Flash API.
- **Customizable Outputs**: Generates diagrams in multiple formats (e.g., block diagrams, flowcharts).

---

## Requirements

### Hardware

- A system capable of running the required APIs or tools (basic computational resources suffice).

### Software

- Python 3.8+
- Required Python libraries (specified in `requirements.txt`)
- Internet connection for API calls

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/algorithm-diagram-generator.git
   cd algorithm-diagram-generator
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Access:**

   - For LLaMA: Ensure Ollama is set up locally or accessible via network.
   - For Gemini 1.5 Flash API: Obtain API keys and set them in the environment variables.
     ```bash
     export GEMINI_API_KEY=your_api_key
     ```

---

## Usage

1. **Input Algorithm Description:**
   Provide the textual description of the algorithm as input via the CLI or GUI.

2. **Generate Diagram:**
   Run the following command to generate a diagram:

   ```bash
   python main.py --input "path_to_algorithm_description.txt" --output "output_diagram.png"
   ```

3. **Output:**
   The tool will save the generated diagram in the specified output format and location.

---

## Backend Models

### LLaMA via Ollama

- Lightweight and efficient for natural language processing tasks.
- Easy to integrate and run locally.

### Gemini 1.5 Flash API

- Advanced processing capabilities for generating insights from textual input.
- Requires API key configuration.

---

## Contributing

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For questions or feedback, please contact [vivekanandojha09\@gmail.com]
