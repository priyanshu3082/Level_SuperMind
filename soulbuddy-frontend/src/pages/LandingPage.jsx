import React from "react";
import { FaGem, FaRegStar, FaRegCommentDots } from "react-icons/fa";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import '@fontsource/poppins'; // Using Poppins font

const LandingPage = () => {
  const navigate = useNavigate(); // Initialize the navigate function

  const handleGetStartedClick = () => {
    navigate("/form"); // Navigate to the FormPage
  };

  return (
    <div className="bg-gradient-to-b from-purple-900 to-black text-white min-h-screen flex items-center">
      <div className="container mx-auto px-4 py-12">
        <div className="flex flex-col lg:flex-row items-center justify-between h-full">
          {/* Left Section */}
          <div className="lg:w-1/2 space-y-6">
            <motion.h1
              className="text-4xl lg:text-6xl font-extrabold"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1 }}
            >
              SoulBuddy - AI-Powered Spiritual Guide
            </motion.h1>
            <motion.p
              className="text-lg lg:text-xl"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1, delay: 0.5 }}
            >
              Unlock personalized spiritual insights and guidance using
              astrology and numerology. Let SoulBuddy guide your spiritual
              journey.
            </motion.p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-6">
              <motion.div
                className="bg-purple-800 p-6 rounded-lg shadow-lg hover:scale-105 transform transition-all"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 1, delay: 0.8 }}
              >
                <div className="flex items-center space-x-4">
                  <FaRegStar className="text-2xl" />
                  <h3 className="font-semibold text-xl">Kundali & Horoscope</h3>
                </div>
                <p className="text-sm">
                  Get personalized birth charts, career, and relationship
                  insights with daily and monthly horoscopes.
                </p>
              </motion.div>
              <motion.div
                className="bg-purple-800 p-6 rounded-lg shadow-lg hover:scale-105 transform transition-all"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 1, delay: 1 }}
              >
                <div className="flex items-center space-x-4">
                  <FaGem className="text-2xl" />
                  <h3 className="font-semibold text-xl">AI Recommendations</h3>
                </div>
                <p className="text-sm">
                  Gemstone suggestions, pooja recommendations, and Do’s & Don’ts
                  tailored to your birth details.
                </p>
              </motion.div>
              <motion.div
                className="bg-purple-800 p-6 rounded-lg shadow-lg hover:scale-105 transform transition-all"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 1, delay: 1.2 }}
              >
                <div className="flex items-center space-x-4">
                  <FaRegStar className="text-2xl" />
                  <h3 className="font-semibold text-xl">Spiritual Content</h3>
                </div>
                <p className="text-sm">
                  Receive meditation, workout, and sleep content aligned with
                  your horoscope.
                </p>
              </motion.div>
              <motion.div
                className="bg-purple-800 p-6 rounded-lg shadow-lg hover:scale-105 transform transition-all"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 1, delay: 1.4 }}
              >
                <div className="flex items-center space-x-4">
                  <FaRegCommentDots className="text-2xl" />
                  <h3 className="font-semibold text-xl">Chatbot Interaction</h3>
                </div>
                <p className="text-sm">
                  Chat with our natural language AI for spiritual guidance and
                  recommendations.
                </p>
              </motion.div>
            </div>
            <motion.button
              className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-6 rounded-lg shadow-lg transform transition-all mt-6"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={handleGetStartedClick} // Add the onClick handler to redirect
            >
              Get Started
            </motion.button>
          </div>

          {/* Right Section */}
          <div className="lg:w-1/2 mt-8 lg:mt-0 flex justify-center">
            <img
              src="1.webp"
              alt="Spiritual Guide"
              className="w-full max-w-lg rounded-lg shadow-xl"
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
