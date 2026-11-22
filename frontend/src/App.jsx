
import { useState } from "react";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleImage = (file) => {
    if (!file) return;

    if (!file.type.startsWith("image/")) {
      setError("Please select a valid image.");
      return;
    }

    if (preview) URL.revokeObjectURL(preview);

    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
    setError("");
  };

  const handlePredict = async () => {
    if (!image) return;

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("image", image);

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/predict",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Prediction failed.");
      }

      setResult(data);
    } catch (err) {
      setError(err.message || "Unable to connect to the server.");
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    if (preview) URL.revokeObjectURL(preview);

    setImage(null);
    setPreview(null);
    setResult(null);
    setError("");
  };

  return (
    <div className="app">
      <nav className="navbar">
        <a href="/" className="logo">
          <span>✳</span> PlantCare AI
        </a>
        <span className="nav-text">Plant Disease Detection</span>
      </nav>

      <main className="container">
        <section className="hero">
          <span className="tag">AI-POWERED PLANT ANALYSIS</span>

          <h1>
            Plant health,
            <br />
            <span>simplified.</span>
          </h1>

          <p>
            Upload a leaf image to identify possible plant diseases
            using artificial intelligence.
          </p>
        </section>

        <section className="analyzer">
          <div className="upload-card">
            <h2>Upload a leaf image</h2>
            <p className="subtitle">
              Choose an image from your device or drag it below.
            </p>

            <label
              className="drop-zone"
              onDragOver={(e) => e.preventDefault()}
              onDrop={(e) => {
                e.preventDefault();
                handleImage(e.dataTransfer.files[0]);
              }}
            >
              <input
                type="file"
                accept="image/*"
                onChange={(e) => {
                  handleImage(e.target.files[0]);
                  e.target.value = "";
                }}
              />

              {preview ? (
                <img
                  src={preview}
                  alt="Selected plant leaf"
                  className="preview-image"
                />
              ) : (
                <>
                  <span className="upload-symbol">↑</span>
                  <strong>Drop your image here</strong>
                  <span className="browse-text">
                    or browse files
                  </span>
                  <span className="file-info">
                    PNG, JPG or JPEG
                  </span>
                </>
              )}
            </label>

            {image && (
              <p className="selected-file">{image.name}</p>
            )}

            <button
              className="predict-button"
              onClick={handlePredict}
              disabled={!image || loading}
            >
              {loading ? "Analyzing..." : "Analyze leaf"}
            </button>

            {image && (
              <button
                className="reset-button"
                onClick={handleReset}
                disabled={loading}
              >
                Remove image
              </button>
            )}

            {error && <p className="error">{error}</p>}
          </div>

          <div className="result-card">
            <span className="result-label">ANALYSIS RESULT</span>

            {!result && !loading && (
              <div className="empty-result">
                <span>✳</span>
                <p>Your result will appear here.</p>
              </div>
            )}

            {loading && (
              <div className="empty-result">
                <p>Analyzing your image...</p>
              </div>
            )}

            {result && (
              <div className="result-content">
                <span className="result-status">
                  ANALYSIS COMPLETE
                </span>

                <h2>
                  {result.predicted_disease.replaceAll("_", " ")}
                </h2>

                <div className="confidence-row">
                  <span>Model confidence</span>
                  <strong>{result.confidence}%</strong>
                </div>

                <div className="progress-track">
                  <div
                    className="progress-fill"
                    style={{
                      width: `${Math.min(
                        100,
                        Math.max(0, result.confidence)
                      )}%`,
                    }}
                  />
                </div>

                <p className="disclaimer">
                  AI predictions are not guaranteed diagnoses.
                  Consult an agricultural expert for confirmation.
                </p>
              </div>
            )}
          </div>
        </section>
      </main>

      <footer>
        Built with TensorFlow, Flask and React
      </footer>
    </div>
  );
}

export default App;
