import React, { useRef, useEffect, useState } from "react";

import heroUI from "./assets/hero-ui.png";
import workoutIcon from "./assets/icon-workout.png";
import dietIcon from "./assets/icon-diet.png";
import trackingIcon from "./assets/icon-tracking.png";

function Home() {
  const featuresRef = useRef(null);

  // 🔥 track visible cards
  const [visibleCards, setVisibleCards] = useState([false, false, false]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const index = Number(entry.target.dataset.index);

            setVisibleCards((prev) => {
              const updated = [...prev];
              updated[index] = true;
              return updated;
            });
          }
        });
      },
      { threshold: 0.2 }
    );

    const elements = document.querySelectorAll(".feature-card");
    elements.forEach((el) => observer.observe(el));

    return () => observer.disconnect();
  }, []);

  const styles = {
    page: {
      color: "white",
      padding: "120px 20px",
      position: "relative",
      overflow: "hidden"
    },

    hero: {
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      flexWrap: "wrap",
      gap: "60px"
    },

    heroText: {
      maxWidth: "500px",
      textAlign: "left"
    },

    heroTitle: {
      fontSize: "52px",
      fontWeight: "700",
      marginBottom: "20px"
    },

    heroSubtitle: {
      fontSize: "18px",
      opacity: 0.85,
      marginBottom: "30px"
    },

    button: {
      padding: "14px 28px",
      borderRadius: "999px",
      border: "none",
      background: "white",
      color: "#333",
      fontWeight: "600",
      cursor: "pointer",
      transition: "0.3s"
    },

    heroImage: {
      width: "420px",
      borderRadius: "20px",
      boxShadow: "0 20px 60px rgba(0,0,0,0.4)"
    },

    section: {
      marginTop: "180px",
      paddingTop: "100px",
      textAlign: "center"
    },

    grid: {
      display: "flex",
      justifyContent: "center",
      gap: "40px",
      flexWrap: "wrap",
      marginTop: "50px"
    },

    // 🔥 ANIMATED CARD
    card: (visible, delay) => ({
      background: "rgba(255,255,255,0.1)",
      backdropFilter: "blur(12px)",
      padding: "30px",
      borderRadius: "20px",
      width: "260px",

      opacity: visible ? 1 : 0,
      transform: visible ? "translateY(0px)" : "translateY(40px)",

      transition: `all 0.6s ease ${delay}s`
    }),

    icon: {
      width: "60px",
      marginBottom: "15px"
    },

    stat: {
      fontSize: "40px",
      fontWeight: "700"
    },

    smallText: {
      opacity: 0.8
    }
  };

  return (
    <div style={styles.page}>

      {/* 🔥 HERO */}
      <div style={styles.hero}>
        <div style={styles.heroText}>
          <h1 style={styles.heroTitle}>
            Train Smarter. Eat Better. Live Stronger.
          </h1>

          <p style={styles.heroSubtitle}>
            AI-powered fitness and diet advisory built to help you reach your
            goals faster with personalized plans.
          </p>

          <button
            style={styles.button}
            onClick={() =>
              featuresRef.current.scrollIntoView({ behavior: "smooth" })
            }
          >
            Start Your Journey
          </button>
        </div>

        <img src={heroUI} alt="App UI" style={styles.heroImage} />
      </div>

      {/* 🔥 FEATURES */}
      <div style={styles.section} ref={featuresRef}>
        <h2>Everything You Need</h2>

        <div style={styles.grid}>
          <div
            className="feature-card"
            data-index="0"
            style={styles.card(visibleCards[0], 0)}
          >
            <img src={workoutIcon} style={styles.icon} alt="Workout" />
            <h3>Smart Workouts</h3>
            <p>Personalized routines based on your fitness level</p>
          </div>

          <div
            className="feature-card"
            data-index="1"
            style={styles.card(visibleCards[1], 0.15)}
          >
            <img src={dietIcon} style={styles.icon} alt="Diet" />
            <h3>Diet Plans</h3>
            <p>Structured nutrition plans tailored to your goals</p>
          </div>

          <div
            className="feature-card"
            data-index="2"
            style={styles.card(visibleCards[2], 0.3)}
          >
            <img src={trackingIcon} style={styles.icon} alt="Tracking" />
            <h3>Progress Tracking</h3>
            <p>Monitor improvements and stay consistent</p>
          </div>
        </div>
      </div>

      {/* 🔥 STATS */}
      <div style={styles.section}>
        <h2>Real Impact</h2>

        <div style={styles.grid}>
          <div>
            <div style={styles.stat}>3x</div>
            <div style={styles.smallText}>Faster progress</div>
          </div>

          <div>
            <div style={styles.stat}>90%</div>
            <div style={styles.smallText}>Consistency rate</div>
          </div>

          <div>
            <div style={styles.stat}>100%</div>
            <div style={styles.smallText}>Personalized</div>
          </div>
        </div>
      </div>

      {/* 🔥 CTA */}
      <div style={styles.section}>
        <h2>Start Your Fitness Journey Today</h2>
        <button style={styles.button}>
          Explore Plans
        </button>
      </div>

    </div>
  );
}

export default Home;