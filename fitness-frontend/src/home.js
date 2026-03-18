import React, { useRef, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import heroUI from "./assets/hero-ui.png";
import workoutIcon from "./assets/icon-workout.png";
import dietIcon from "./assets/icon-diet.png";
import trackingIcon from "./assets/icon-tracking.png";

function Home() {
  const featuresRef = useRef(null);
  const navigate = useNavigate();

  const [visibleCards, setVisibleCards] = useState([false, false, false]);
  const [loading, setLoading] = useState(true);
  const [showText, setShowText] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      setShowText(true);
    }, 300);

    setTimeout(() => {
      setLoading(false);
    }, 2500);
  }, []);

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

    loader: {
      position: "fixed",
      top: 0,
      left: 0,
      width: "100%",
      height: "100%",
      background: "#111",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      zIndex: 2000,
      opacity: loading ? 1 : 0,
      transition: "opacity 0.8s ease",
      pointerEvents: loading ? "all" : "none"
    },

    loaderText: {
      color: "white",
      fontSize: "42px",
      fontWeight: "700",
      letterSpacing: "3px",
      opacity: showText ? 1 : 0,
      transform: showText ? "translateY(0px)" : "translateY(20px)",
      transition: "all 1.2s ease"
    },

    hero: {
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      textAlign: "center"
    },

    heroText: {
      maxWidth: "800px",
      textAlign: "center"
    },

    heroTitle: {
  fontSize: "64px",
  fontWeight: "700",
  marginBottom: "20px",
  fontFamily: "Lora, serif",
  lineHeight: "1.2",
  whiteSpace: "nowrap",
  textAlign: "center",
  display: "flex",
  justifyContent: "center"
},

    heroSubtitle: {
  fontSize: "18px",
  opacity: 0.85,
  marginBottom: "30px",
  fontFamily: "Lora, serif",
  whiteSpace: "nowrap",
  display: "flex",
  justifyContent: "center"
},

    button: {
      padding: "14px 28px",
      borderRadius: "999px",
      border: "none",
      background: "white",
      color: "#333",
      fontWeight: "600",
      cursor: "pointer",
      fontFamily: "'Manrope', sans-serif"
    },

    heroImage: {
      width: "600px",
      maxWidth: "90%",
      borderRadius: "20px",
      boxShadow: "0 20px 60px rgba(0,0,0,0.4)",
      marginTop: "60px"
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
    <>
      <div style={styles.loader}>
        <div style={styles.loaderText}>
          FitSense AI
        </div>
      </div>

      <div style={styles.page}>

        <div style={styles.hero}>
          <div style={styles.heroText}>
            <h1 style={styles.heroTitle}>
              Upgrade Your Body. Optimize Your Life.
            </h1>

            <p style={styles.heroSubtitle}>
              AI-powered fitness and diet advisory built to help you reach your goals faster with personalized plans.
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

        <div style={styles.section} ref={featuresRef}>
          <h2>Everything You Need</h2>

          <div style={styles.grid}>
            <div className="feature-card" data-index="0" style={styles.card(visibleCards[0], 0)}>
              <img src={workoutIcon} style={styles.icon} alt="Workout" />
              <h3>Smart Workouts</h3>
              <p>Personalized routines based on your fitness level</p>
            </div>

            <div className="feature-card" data-index="1" style={styles.card(visibleCards[1], 0.15)}>
              <img src={dietIcon} style={styles.icon} alt="Diet" />
              <h3>Diet Plans</h3>
              <p>Structured nutrition plans tailored to your goals</p>
            </div>

            <div className="feature-card" data-index="2" style={styles.card(visibleCards[2], 0.3)}>
              <img src={trackingIcon} style={styles.icon} alt="Tracking" />
              <h3>Progress Tracking</h3>
              <p>Monitor improvements and stay consistent</p>
            </div>
          </div>
        </div>

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

        <div style={styles.section}>
          <h2>Start Your Fitness Journey Today</h2>
          <div style={{ marginTop: "20px", display: "flex", justifyContent: "center", gap: "20px" }}>
            <button
              style={styles.button}
              onClick={() => navigate("/fitness")}
            >
              Let's Go
            </button>
          </div>
        </div>

      </div>
    </>
  );
}

export default Home;