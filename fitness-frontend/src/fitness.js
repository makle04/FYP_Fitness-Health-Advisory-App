import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Fitness() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    Age: "",
    Weight_kg: "",
    Height_m: "",
    Session_Duration_hours: 1,
    Calories_Burned: "",
    Max_BPM: "",
    Resting_BPM: "",
    Avg_BPM: "",
    Water_Intake_liters: 1
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [pageLoading, setPageLoading] = useState(true);
  const [showText, setShowText] = useState(false);

  useEffect(() => {
    setTimeout(() => setShowText(true), 200);
    setTimeout(() => setPageLoading(false), 1600);
  }, []);

  // 🔥 UPDATED: only allow numeric input
  const handleChange = (e) => {
    const { name, value } = e.target;

    if (value === "" || /^[0-9]*\.?[0-9]*$/.test(value)) {
      setFormData({
        ...formData,
        [name]: value
      });
    }
  };

  const isValid = Object.entries(formData).every(([key, value]) => {
    if (key === "Session_Duration_hours" || key === "Water_Intake_liters") {
      return true;
    }
    return value !== "";
  });

  const bmi =
    formData.Weight_kg && formData.Height_m
      ? (formData.Weight_kg / (formData.Height_m ** 2)).toFixed(1)
      : null;

  const intensity =
    formData.Avg_BPM > 140 ? "High"
    : formData.Avg_BPM > 110 ? "Moderate"
    : "Low";

  const hydration =
    formData.Water_Intake_liters >= 2 ? "Good" : "Needs Improvement";

  const bmiCategory = bmi
    ? bmi < 18.5 ? "Underweight"
    : bmi < 25 ? "Healthy"
    : "Overweight"
    : null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isValid) return;

    setLoading(true);
    setError("");

    const payload = {};
    Object.keys(formData).forEach((key) => {
      payload[key] = Number(formData[key]);
    });

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      const explanation = `
You fall into a ${intensity.toLowerCase()} intensity fitness profile based on your heart rate patterns.

Your hydration level is ${hydration.toLowerCase()}, and your BMI is ${bmi} (${bmiCategory} range).

This suggests your current training load is ${intensity.toLowerCase()} and your recovery condition is ${hydration.toLowerCase()}.

Recommended Plan:
${data.recommendation}
      `;

      setResult({
        ...data,
        explanation
      });

    } catch (err) {
      setError("Unable to connect to server. Please try again.");
    }

    setLoading(false);
  };

  const handleReset = () => {
    setFormData({
      Age: "",
      Weight_kg: "",
      Height_m: "",
      Session_Duration_hours: 1,
      Calories_Burned: "",
      Max_BPM: "",
      Resting_BPM: "",
      Avg_BPM: "",
      Water_Intake_liters: 1
    });
    setResult(null);
    setError("");
  };

  const styles = {
    loader: {
      position: "fixed",
      top: 0,
      left: 0,
      width: "100%",
      height: "100%",
      background: "black",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      zIndex: 2000,
      opacity: pageLoading ? 1 : 0,
      transition: "opacity 0.8s ease",
      pointerEvents: pageLoading ? "all" : "none"
    },

    loaderText: {
      color: "white",
      fontSize: "42px",
      fontWeight: "600",
      letterSpacing: "2px",
      opacity: showText ? 1 : 0,
      transform: showText ? "translateY(0)" : "translateY(20px)",
      transition: "all 1s ease"
    },

    page: {
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
    },

    container: {
      background: "rgba(255, 255, 255, 0.85)",
      backdropFilter: "blur(10px)",
      padding: "30px",
      borderRadius: "16px",
      width: "100%",
      maxWidth: "650px",
      boxShadow: "0 15px 40px rgba(0,0,0,0.2)",
      textAlign: "center"
    },

    title: {
      textAlign: "center",
      marginBottom: "20px"
    },

    section: {
      marginTop: "15px",
      marginBottom: "10px",
      fontWeight: "bold"
    },

    grid: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "15px"
    },

    inputGroup: {
      display: "flex",
      flexDirection: "column"
    },

    input: {
      padding: "10px",
      borderRadius: "6px",
      border: "1px solid #ddd"
    },

    slider: {
      width: "100%"
    },

    button: {
      width: "100%",
      padding: "12px",
      marginTop: "15px",
      border: "none",
      borderRadius: "8px",
      background: "#2ecc71",
      color: "white",
      fontSize: "16px",
      cursor: "pointer",
      transition: "0.3s",
      fontFamily: "'Manrope', sans-serif",
    },

    resetBtn: {
      width: "100%",
      padding: "10px",
      marginTop: "10px",
      borderRadius: "8px",
      border: "1px solid #ccc",
      background: "#f5f5f5",
      fontFamily: "'Manrope', sans-serif",
      cursor: "pointer"
    },

    result: {
      marginTop: "25px",
      padding: "20px",
      borderRadius: "10px",
      background: "#f0fff4",
      border: "1px solid #2ecc71",
      textAlign: "left",
      whiteSpace: "pre-line"
    },

    error: {
      marginTop: "15px",
      color: "red"
    }
  };

  return (
    <>
      <div style={styles.loader}>
        <div style={styles.loaderText}>
          Loading Fitness Module...
        </div>
      </div>

      <div style={styles.page}>
        <div style={styles.container}>

          <h1 style={styles.title}>Fitness Advisory System</h1>

          <form onSubmit={handleSubmit}>

            <div style={styles.section}>Personal Info</div>
            <div style={styles.grid}>
              <div style={styles.inputGroup}>
                <label>Age</label>
                <input type="number" name="Age" value={formData.Age} style={styles.input} onChange={handleChange} />
              </div>

              <div style={styles.inputGroup}>
                <label>Weight (kg)</label>
                <input type="number" name="Weight_kg" value={formData.Weight_kg} style={styles.input} onChange={handleChange} />
              </div>

              <div style={styles.inputGroup}>
                <label>Height (m)</label>
                <input type="number" name="Height_m" value={formData.Height_m} style={styles.input} onChange={handleChange} />
              </div>
            </div>

            {bmi && <p>BMI: <b>{bmi}</b> ({bmiCategory})</p>}

            <div style={styles.section}>Workout Stats</div>
            <div style={styles.grid}>
              <div style={styles.inputGroup}>
                <label>Calories Burned</label>
                <input type="number" name="Calories_Burned" value={formData.Calories_Burned} style={styles.input} onChange={handleChange} />
              </div>

              <div style={styles.inputGroup}>
                <label>Max BPM</label>
                <input type="number" name="Max_BPM" value={formData.Max_BPM} style={styles.input} onChange={handleChange} />
              </div>

              <div style={styles.inputGroup}>
                <label>Resting BPM</label>
                <input type="number" name="Resting_BPM" value={formData.Resting_BPM} style={styles.input} onChange={handleChange} />
              </div>

              <div style={styles.inputGroup}>
                <label>Avg BPM</label>
                <input type="number" name="Avg_BPM" value={formData.Avg_BPM} style={styles.input} onChange={handleChange} />
              </div>
            </div>

            <br />

            <label>Workout Duration (hours/per session): {formData.Session_Duration_hours}</label>
            <input
              type="range"
              min="0.3"
              max="3"
              step="0.1"
              name="Session_Duration_hours"
              value={formData.Session_Duration_hours}
              onChange={handleChange}
              style={styles.slider}
            />

            <br /><br />

            <div style={styles.section}>Hydration</div>

            <label>Water Intake (liters): {formData.Water_Intake_liters}</label>
            <input
              type="range"
              min="0.5"
              max="4"
              step="0.1"
              name="Water_Intake_liters"
              value={formData.Water_Intake_liters}
              onChange={handleChange}
              style={styles.slider}
            />

            <button
              type="submit"
              style={styles.button}
              disabled={!isValid || loading}
            >
              {loading ? "Analyzing..." : "Get Recommendation"}
            </button>

            <button type="button" style={styles.resetBtn} onClick={handleReset}>
              Reset
            </button>

          </form>

          {error && <div style={styles.error}>{error}</div>}

          {result && (
            <div style={styles.result}>
              <h2>Analysis</h2>
              <p>{result.explanation}</p>

              <button
                style={styles.button}
                onClick={() =>
                  navigate("/diet", {
                    state: {
                      type: intensity.toLowerCase(),
                      weight: formData.Weight_kg,
                      height: formData.Height_m,
                      age: formData.Age
                    }
                  })
                }
              >
                View Diet Plan
              </button>
            </div>
          )}

        </div>
      </div>
    </>
  );
}

export default Fitness;