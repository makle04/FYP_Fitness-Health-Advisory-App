import React, { useState } from "react";

function App() {

  const [formData, setFormData] = useState({
    Age: "",
    Weight_kg: "",
    Height_m: "",
    Session_Duration_hours: "",
    Calories_Burned: "",
    Max_BPM: "",
    Resting_BPM: "",
    Avg_BPM: "",
    Water_Intake_liters: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {};

    Object.keys(formData).forEach((key) => {
      payload[key] = Number(formData[key]);
    });

    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div style={{padding:"40px", fontFamily:"Arial"}}>
      <h1>Fitness Health Advisory System</h1>

      <form onSubmit={handleSubmit}>

        <input name="Age" placeholder="Age" onChange={handleChange} /><br/><br/>

        <input name="Weight_kg" placeholder="Weight (kg)" onChange={handleChange} /><br/><br/>

        <input name="Height_m" placeholder="Height (m)" onChange={handleChange} /><br/><br/>

        <input name="Session_Duration_hours" placeholder="Workout Duration (hours)" onChange={handleChange} /><br/><br/>

        <input name="Calories_Burned" placeholder="Calories Burned" onChange={handleChange} /><br/><br/>

        <input name="Max_BPM" placeholder="Max BPM" onChange={handleChange} /><br/><br/>

        <input name="Resting_BPM" placeholder="Resting BPM" onChange={handleChange} /><br/><br/>

        <input name="Avg_BPM" placeholder="Average BPM" onChange={handleChange} /><br/><br/>

        <input name="Water_Intake_liters" placeholder="Water Intake (liters)" onChange={handleChange} /><br/><br/>

        <button type="submit">Get Recommendation</button>

      </form>

      {result && (
        <div style={{marginTop:"30px"}}>
          <h2>Cluster: {result.cluster}</h2>
          <h3>{result.recommendation}</h3>
        </div>
      )}

    </div>
  );
}

export default App;