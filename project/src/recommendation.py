def give_recommendation(cluster_id):
rec = {
0: "Increase overall activity. Try 5,000–7,000 steps daily.",
1: "You are moderately active. Add strength training 2–3x weekly.",
2: "High activity level! Maintain training and monitor recovery.",
3: "Low sleep quality detected. Improve sleep hygiene.",
4: "Balanced fitness profile. Continue current routine."
}


return rec.get(cluster_id, "No recommendation available.")