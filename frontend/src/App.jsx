
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Monitor, Chrome, FileText } from "lucide-react";
import { AnimatePresence, motion } from "framer-motion";
import './styles/digitalWellbeing.css';

const App = () => {
  const [usageData, setUsageData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/usage');
        setUsageData(response.data);
      } catch (error) {
        console.error('Error fetching usage data:', error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 60000);
    return () => clearInterval(interval);
  }, []);

  const getAppIcon = (appName) => {
    if (appName.toLowerCase().includes('chrome')) {
      return <Chrome size={24} color="#60A5FA" />;
    } else if (appName.toLowerCase().includes('code')) {
      return <FileText size={24} color="#34D399" />;
    }
    return <Monitor size={24} color="#A78BFA" />;
  };

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    if (hours > 0) {
      const remainingMinutes = minutes % 60;
      return `${hours}h ${remainingMinutes}m`;
    }
    return `${minutes}m`;
  };

  return (
    <div className="wellbeing-container">
      <div className="content-wrapper">
        <div className="header">
          <h1 className="header-title">Digital Wellbeing Tracker</h1>
          <p className="header-subtitle">Monitor your app usage and stay mindful of your digital habits</p>
        </div>

        <div className="cards-grid">
          <AnimatePresence>
            {Object.entries(usageData)
              .sort(([, a], [, b]) => b - a)
              .map(([app, time], index) => (
                <motion.div
                  key={app}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{ duration: 0.2, delay: index * 0.05 }}
                >
                  <div className="app-card">
                    <div className="card-content">
                      <div className="icon-wrapper">
                        {getAppIcon(app)}
                      </div>
                      <div className="card-details">
                        <h3 className="app-name">
                          {app.replace(/\u25cf/g, '')}
                        </h3>
                        <p className="time-text">
                          {formatTime(time)}
                        </p>
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
          </AnimatePresence>
        </div>
      </div>
    </div>
  );
};

export default App;
