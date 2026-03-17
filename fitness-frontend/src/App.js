import React, { useEffect, useState } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
import Home from "./home";
import Fitness from "./fitness";
import Diet from "./diet";
import logo from "./land_title.png";

function App() {
  const navigate = useNavigate();

  const [scrollProgress, setScrollProgress] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      setScrollProgress(Math.min(scrollY / 150, 1));
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const styles = {
    app: {
      minHeight: "100vh",
      background: `
        radial-gradient(circle at 20% 20%, rgba(255,255,255,0.4), transparent 40%),
        radial-gradient(circle at 80% 80%, rgba(255,255,255,0.3), transparent 40%),
        linear-gradient(135deg, #667eea, #764ba2)
      `
    },

    logoImg: {
      height: `${80 - scrollProgress * 20}px`,
      objectFit: "contain",
      cursor: "pointer",
      transform: `scale(${1 - scrollProgress * 0.2}) translateY(${scrollProgress * -8}px)`,
      opacity: 1 - scrollProgress * 0.4,
      transition: "all 0.2s ease"
    },

    logoFloating: {
      position: "fixed",
      top: "0px",
      left: "50%",
      transform: "translateX(-50%)",
      zIndex: 1100,
      padding: "6px 12px",

      background: `rgba(255,255,255,${0.2 + scrollProgress * 0.4})`,
      backdropFilter: `blur(${scrollProgress * 12}px)`,

      borderRadius: "0 0 12px 12px",
      transition: "all 0.2s ease"
    },

    navbar: {
      position: "fixed",
      top: 30,
      left: "20px",
      padding: "10px 16px",
      borderRadius: "16px",

      background: `rgba(255,255,255,${0.2 + scrollProgress * 0.4})`,
      backdropFilter: `blur(${scrollProgress * 12}px)`,

      display: "flex",
      alignItems: "center",

      boxShadow:
        scrollProgress > 0.2
          ? "0 8px 20px rgba(0,0,0,0.2)"
          : "none",

      transition: "all 0.2s ease",
      zIndex: 1000
    },

    navLeft: {
      display: "flex",
      gap: "16px"
    },

    navBtn: {
      padding: "8px 14px",
      borderRadius: "8px",
      border: "none",
      background: "rgba(255,255,255,0.4)",
      color: "#1f2937",
      cursor: "pointer",
      transition: "0.2s"
    },

    content: {
      paddingTop: "100px"
    }
  };

  return (
    <div style={styles.app}>

      {/* 🔥 NAVBAR */}
      <nav style={styles.navbar}>
        <div style={styles.navLeft}>
          <button
            style={styles.navBtn}
            onClick={() => navigate("/fitness")}
            onMouseOver={(e) =>
              (e.target.style.background = "rgba(255,255,255,0.9)")
            }
            onMouseOut={(e) =>
              (e.target.style.background = "rgba(255,255,255,0.4)")
            }
          >
            Fitness
          </button>

          <button
            style={styles.navBtn}
            onClick={() => navigate("/diet")}
            onMouseOver={(e) =>
              (e.target.style.background = "rgba(255,255,255,0.9)")
            }
            onMouseOut={(e) =>
              (e.target.style.background = "rgba(255,255,255,0.4)")
            }
          >
            Diet Plans
          </button>
        </div>
      </nav>

      {/* 🔥 LOGO → HOME */}
      <div style={styles.logoFloating}>
        <img
          src={logo}
          alt="FitSense AI"
          style={styles.logoImg}
          onClick={() => navigate("/")}
        />
      </div>

      {/* 🔥 ROUTES */}
      <div style={styles.content}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/fitness" element={<Fitness />} />
          <Route path="/diet" element={<Diet />} />
        </Routes>
      </div>

    </div>
  );
}

export default App;