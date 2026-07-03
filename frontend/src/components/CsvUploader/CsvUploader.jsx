import { useState } from "react";
import "./CsvUploader.css";
import API from "../../services/api";

function CsvUploader({
  setData,
  setSummary,
  loading,
  setLoading,
}) {
  const [success, setSuccess] = useState(false);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];

    if (!file) return;

    // Reset previous success message
    setSuccess(false);

    // Start loading
    setLoading(true);

    try {
      // Create FormData
      const formData = new FormData();
      formData.append("file", file);

      // Upload CSV
      await API.post("/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      // Analyze uploaded CSV
      const response = await API.post("/analyze/");

      // Update Dashboard Cards
      setSummary(response.data.summary);

      // Update Table
      setData(response.data.table_data);

      // Show success message
      setSuccess(true);
    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.detail ||
        "Something went wrong."
      );
    } finally {
      // Stop loading whether success or error
      setLoading(false);
    }
  };

  const handleDownload = () => {
  window.open(
    "http://127.0.0.1:8000/download/",
    "_blank"
    );
  };

  return (
    <section className={`upload-card ${loading ? "loading" : ""}`}>
      <div className="upload-header">
        <h2>Upload Inventory Dataset</h2>

        <p>
          Upload a CSV file to generate forecasts,
          risk analysis, and inventory insights.
        </p>
      </div>

      <label className="upload-zone">
        <div className="upload-icon">
          📂
        </div>

        <h3>
          Drag & Drop CSV File
        </h3>

        <p>
          or click to browse
        </p>

        <input
          type="file"
          accept=".csv"
          onChange={handleFileUpload}
          disabled={loading}
        />

        {loading && (
          <div className="loading-overlay">
          <div className="spinner"></div>

          <p>Analyzing Inventory...</p>

          <small>Please wait</small>
        </div>
        )}

        {success && (
          <p className="success-text">
            ✓ Analysis Completed
          </p>
        )}
        {success && (
        <button
          className="download-btn"
          onClick={handleDownload}
          disabled={loading}
        >
          {loading
            ? "Preparing..."
           : "⬇ Download Prediction"}
        </button>
        )}
      </label>
    </section>
  );
}


export default CsvUploader;