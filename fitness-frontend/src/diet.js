import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

function Diet() {

  const location = useLocation();

  const [goal, setGoal] = useState("");
  const [plan, setPlan] = useState(null);

  // ✅ Auto-fill from Fitness page
  useEffect(() => {
    if (location.state?.type === "high") setGoal("gain");
    if (location.state?.type === "moderate") setGoal("maintain");
    if (location.state?.type === "low") setGoal("loss");
  }, [location]);

  // ✅ Generate smart diet plan
  const generatePlan = () => {
    let dietPlan = "";
    let calories = "";
    let protein = "";
    let carbs = "";
    let fats = "";
    let explanation = "";

    if (goal === "loss") {
      calories = "1800 - 2200 kcal";
      protein = "120 - 150g";
      carbs = "150 - 200g";
      fats = "50 - 70g";

      explanation = "You are targeting fat loss. A calorie deficit with high protein will help preserve muscle while reducing body fat.";

      dietPlan = `
Focus: Calorie deficit, high protein

Breakfast:
- Oats with eggs or yogurt

Lunch:
- Grilled chicken or fish with vegetables

Dinner:
- Lean protein with salad

Snacks:
- Fruits, nuts

Avoid:
- Sugary drinks, fried food
      `;
    }

    if (goal === "gain") {
      calories = "2500 - 3000 kcal";
      protein = "150 - 180g";
      carbs = "300 - 400g";
      fats = "70 - 90g";

      explanation = "You are aiming for muscle gain. A calorie surplus with sufficient protein supports muscle growth and recovery.";

      dietPlan = `
Focus: Calorie surplus, high protein

Breakfast:
- Eggs, toast, milk

Lunch:
- Chicken rice with vegetables

Dinner:
- Beef or chicken with carbs

Snacks:
- Peanut butter, protein shakes

Include:
- More carbs and healthy fats
      `;
    }

    if (goal === "maintain") {
      calories = "2000 - 2500 kcal";
      protein = "100 - 140g";
      carbs = "200 - 300g";
      fats = "60 - 80g";

      explanation = "You are maintaining your current physique. Balanced nutrition ensures energy stability and long-term health.";

      dietPlan = `
Focus: Balanced nutrition

Breakfast:
- Eggs and whole grains

Lunch:
- Protein + carbs + vegetables

Dinner:
- Light protein with vegetables

Snacks:
- Fruits, yogurt

Maintain:
- Consistent calorie intake
      `;
    }

    setPlan({
      dietPlan,
      calories,
      protein,
      carbs,
      fats,
      explanation
    });
  };

  const styles = {
    page: {
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      fontFamily: "Arial"
    },

    container: {
      background: "white",
      padding: "30px",
      borderRadius: "12px",
      width: "100%",
      maxWidth: "650px",
      boxShadow: "0 10px 25px rgba(0,0,0,0.15)",
      textAlign: "center"
    },

    title: {
      marginBottom: "20px"
    },

    select: {
      padding: "10px",
      width: "100%",
      borderRadius: "6px",
      border: "1px solid #ddd",
      marginBottom: "20px"
    },

    button: {
      padding: "12px",
      width: "100%",
      borderRadius: "8px",
      border: "none",
      background: "#3498db",
      color: "white",
      cursor: "pointer"
    },

    card: {
      marginTop: "20px",
      padding: "20px",
      background: "#f4f8ff",
      borderRadius: "10px",
      textAlign: "left"
    },

    macros: {
      marginTop: "10px",
      padding: "10px",
      background: "#eef3ff",
      borderRadius: "8px"
    },

    plan: {
      marginTop: "15px",
      whiteSpace: "pre-line"
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.container}>

        <h1 style={styles.title}>Diet Plan Generator</h1>

        <select
          style={styles.select}
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
        >
          <option value="">Select your goal</option>
          <option value="loss">Weight Loss</option>
          <option value="gain">Muscle Gain</option>
          <option value="maintain">Maintenance</option>
        </select>

        <button onClick={generatePlan} disabled={!goal}>
          Generate Plan
        </button>

        {plan && (
          <div style={styles.card}>

            <h3>Diet Analysis</h3>
            <p>{plan.explanation}</p>

            <div style={styles.macros}>
              <strong>Daily Targets:</strong>
              <p>Calories: {plan.calories}</p>
              <p>Protein: {plan.protein}</p>
              <p>Carbs: {plan.carbs}</p>
              <p>Fats: {plan.fats}</p>
            </div>

            <div style={styles.plan}>
              <h4>Recommended Plan</h4>
              <p>{plan.dietPlan}</p>
            </div>

          </div>
        )}

      </div>
    </div>
  );
}

export default Diet;