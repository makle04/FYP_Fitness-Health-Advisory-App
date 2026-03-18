import React, { useState, useEffect, useCallback } from "react";
import { useLocation } from "react-router-dom";

function Diet() {

  const location = useLocation();

  const [goal, setGoal] = useState("");
  const [plan, setPlan] = useState(null);

  const calculateDiet = useCallback((inputGoal) => {
    const selectedGoal = inputGoal || goal;

    const weight = Number(location.state?.weight);
    const height = Number(location.state?.height) * 100;
    const age = Number(location.state?.age);

    if (!weight || !height || !age) return;

    const BMR = 10 * weight + 6.25 * height - 5 * age + 5;

    let activityMultiplier = 1.4;
    if (location.state?.type === "high") activityMultiplier = 1.75;
    if (location.state?.type === "moderate") activityMultiplier = 1.55;
    if (location.state?.type === "low") activityMultiplier = 1.3;

    const TDEE = Math.round(BMR * activityMultiplier);

    let targetCalories = TDEE;
    if (selectedGoal === "loss") targetCalories -= 400;
    if (selectedGoal === "gain") targetCalories += 400;

    const protein = Math.round(weight * 2);
    const fats = Math.round(weight * 0.8);
    const carbs = Math.round((targetCalories - (protein * 4 + fats * 9)) / 4);

    const explanation = `
Your estimated BMR is ${Math.round(BMR)} kcal/day.

Based on your activity level, your daily energy expenditure (TDEE) is about ${TDEE} kcal.

For your goal (${selectedGoal}), your recommended intake is ${targetCalories} kcal/day.
    `;

    let meals = "";

    if (selectedGoal === "loss") {
      meals = `
🍳 Breakfast:
- Oats + boiled eggs / Greek yogurt

🍗 Lunch:
- Grilled chicken + vegetables + small rice

🥗 Dinner:
- Salad + lean protein (fish/chicken)

🥜 Snacks:
- Fruits, nuts

🚫 Avoid:
- Sugary drinks, fried food
      `;
    }

    if (selectedGoal === "gain") {
      meals = `
🍳 Breakfast:
- Eggs, toast, milk

🍗 Lunch:
- Chicken rice / beef + rice + veggies

🍝 Dinner:
- Pasta / rice + protein

🥤 Snacks:
- Peanut butter sandwich, protein shake

✅ Include:
- More carbs + healthy fats
      `;
    }

    if (selectedGoal === "maintain") {
      meals = `
🍳 Breakfast:
- Eggs + whole grain toast

🍗 Lunch:
- Balanced meal (protein + carbs + veg)

🥗 Dinner:
- Light protein + vegetables

🍎 Snacks:
- Fruits, yogurt

⚖️ Maintain:
- Balanced intake
      `;
    }

    setPlan({
      calories: targetCalories,
      protein,
      carbs,
      fats,
      explanation,
      meals
    });

  }, [goal, location]);

  useEffect(() => {
    if (!location.state?.type) return;

    let detectedGoal = "";

    if (location.state.type === "high") detectedGoal = "gain";
    if (location.state.type === "moderate") detectedGoal = "maintain";
    if (location.state.type === "low") detectedGoal = "loss";

    setGoal(detectedGoal);
    calculateDiet(detectedGoal);

    // eslint-disable-next-line
  }, []);

  const styles = {
    page: {
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      fontFamily: "'Manrope', sans-serif"
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

    select: {
      padding: "10px",
      width: "100%",
      borderRadius: "6px",
      border: "1px solid #ddd",
      marginBottom: "20px"
    },

    button: {
      padding: "14px 28px",
      width: "100%",
      borderRadius: "999px",
      border: "none",
      background: "white",
      color: "#333",
      fontWeight: "600",
      cursor: "pointer",
      fontFamily: "'Manrope', sans-serif",
      boxShadow: "0 6px 15px rgba(0,0,0,0.15)",
      transition: "all 0.2s ease"
    },

    card: {
      marginTop: "20px",
      padding: "20px",
      background: "#f4f8ff",
      borderRadius: "10px",
      textAlign: "left"
    },

    meals: {
      marginTop: "15px",
      whiteSpace: "pre-line"
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.container}>

        <h1>Smart Diet Calculator</h1>

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

        <button
          style={styles.button}
          onMouseOver={(e) => (e.target.style.transform = "scale(1.05)")}
          onMouseOut={(e) => (e.target.style.transform = "scale(1)")}
          onClick={() => calculateDiet()}
        >
          Recalculate
        </button>

        {plan && (
          <div style={styles.card}>

            <h3>Calorie Analysis</h3>
            <p>{plan.explanation}</p>

            <h4>Daily Targets</h4>
            <p><b>Calories:</b> {plan.calories} kcal</p>
            <p><b>Protein:</b> {plan.protein} g</p>
            <p><b>Carbs:</b> {plan.carbs} g</p>
            <p><b>Fats:</b> {plan.fats} g</p>

            <h4>Recommended Meals</h4>
            <p style={styles.meals}>{plan.meals}</p>

          </div>
        )}

      </div>
    </div>
  );
}

export default Diet;