import React, { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";
import "./App.css";

const App: React.FC = () => {
  const [description, setDescription] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [imageUrl, setImageUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Handle input change
  const handleInputChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
    setDescription(event.target.value);
  };

  // Handle form submission
  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    setImageUrl(null);
  
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/generate", // Flask backend URL
        { description },
        { responseType: "blob" } // Expect an image blob
      );
  
      const url = URL.createObjectURL(response.data);
      setImageUrl(url);
    } catch (err) {
      setError("Error generating diagram. Please try again.");
    } finally {
      setLoading(false);
    }
  };
  

  return (
    <div className="App">
      <h1>Text to Flowchart</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={description}
          onChange={handleInputChange}
          placeholder="Enter description for diagram..."
          rows={5}
          cols={40}
        />
        <br />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Diagram"}
        </button>
      </form>

      {error && <p>{error}</p>}

      {imageUrl && (
        <div>
          <h2>Generated Diagram</h2>
          <img src={imageUrl} alt="Flowchart" />
        </div>
      )}
    </div>
  );
};

export default App;
