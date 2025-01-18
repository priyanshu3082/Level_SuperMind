import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import "@fontsource/poppins";
import { Scrollbars } from "react-custom-scrollbars-2";

const KundliPage = () => {
  const [loading, setLoading] = useState(true);

  // Simulate data loading with a timeout (or API call here)
  useEffect(() => {
    setTimeout(() => {
      setLoading(false); // Set loading to false after 3 seconds (simulating data load)
    }, 3000); // 3 seconds loader time
  }, []);

  return (
    <div className="bg-gradient-to-b from-purple-900 to-black text-white min-h-screen flex items-center">
      <div className="container mx-auto px-4 py-12">
        <div className="flex flex-col lg:flex-row items-center justify-between h-full">
          {/* Left Section */}
<motion.div
  className="lg:w-1/2 space-y-6"
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 1 }}
>
  <h1 className="text-4xl lg:text-6xl font-extrabold">
    {/* Skeleton with glowing effect */}
    {loading ? (
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1, repeat: Infinity, repeatType: "reverse" }}
        className="skeleton-glow w-4/5 h-12 bg-gray-400 rounded-md"
      />
    ) : (
      'Here is your personalized Kundli'
    )}
  </h1>
  <p className="text-lg lg:text-xl mt-4">
    {/* Skeleton with glowing effect */}
    {loading ? (
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1, repeat: Infinity, repeatType: "reverse" }}
        className="skeleton-glow w-3/5 h-6 bg-gray-400 rounded-md"
      />
    ) : (
      'आपका व्यक्तिगत कुंडली यहाँ है'
    )}
  </p>

  {/* Generate Insights Button */}
  {!loading && (
    <motion.button
      className="mt-6 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-lg transition-all duration-300"
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.9 }}
      onClick={() => {
        alert("Insights are being generated...");
      }}
    >
      Generate Insights
    </motion.button>
  )}
</motion.div>


          {/* Right Section */}
          <motion.div
            className="lg:w-1/2 mt-8 lg:mt-0 flex justify-center"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, delay: 0.5 }} // Add a slight delay here for smooth transition
          >
            {loading ? (
              <div className="w-full h-full flex justify-center items-center space-y-6">
                {/* Skeleton Loader for whole content with glowing effect */}
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{
                    duration: 1,
                    repeat: Infinity,
                    repeatType: "reverse",
                  }}
                  className="space-y-6 w-full max-w-lg"
                >
                  <div className="skeleton-glow w-4/5 h-8 bg-gray-400 rounded-md"></div>
                  <div className="skeleton-glow w-3/5 h-6 bg-gray-400 rounded-md"></div>
                  <div className="skeleton-glow w-1/3 h-6 bg-gray-400 rounded-md"></div>
                  <div className="skeleton-glow w-full h-64 bg-gray-400 rounded-md"></div>
                </motion.div>
              </div>
            ) : (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 1, delay: 1 }} // Adding a delay for smoothness
                className="w-full max-w-lg p-8 bg-gradient-to-tl from-yellow-100 to-yellow-300 rounded-[40px] shadow-xl relative overflow-hidden"
              >
                {/* Old Paper Texture Effect */}
                <div className="absolute inset-0 bg-gradient-to-tl from-yellow-100 to-yellow-200 opacity-50 rounded-[40px]"></div>

                <div className="relative z-10 text-black font-serif">
                  {/* Title */}
                  <motion.h2
                    className="text-4xl font-bold text-center mb-6 font-serif tracking-wider"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 1, delay: 1.5 }}
                  >
                    Kundli Chart
                  </motion.h2>

                  {/* Dummy Kundli Data */}
                  <div className="text-left space-y-4 mb-6">
                    <motion.p
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ duration: 1, delay: 2 }}
                    >
                      <strong>Name:</strong> John Doe
                    </motion.p>
                    <motion.p
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ duration: 1, delay: 2.1 }}
                    >
                      <strong>Date of Birth:</strong> 01/01/1990
                    </motion.p>
                    <motion.p
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ duration: 1, delay: 2.2 }}
                    >
                      <strong>Time of Birth:</strong> 10:30 AM
                    </motion.p>
                    <motion.p
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ duration: 1, delay: 2.3 }}
                    >
                      <strong>Place of Birth:</strong> New Delhi, India
                    </motion.p>
                    <motion.p
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ duration: 1, delay: 2.4 }}
                    >
                      <strong>Gender:</strong> Male
                    </motion.p>
                  </div>

                  {/* Kundli Chart (12 Houses) */}
                  <motion.div
                    className="mt-6 border-t-2 border-gray-500 pt-4 max-h-[400px]"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 1, delay: 2.5 }}
                  >
                    <Scrollbars
                      style={{ height: 400 }}
                      renderThumbVertical={({ style }) => (
                        <div
                          style={{
                            ...style,
                            backgroundColor: "rgba(0, 0, 0, 0.3)",
                            borderRadius: "10px",
                          }}
                        />
                      )}
                      renderTrackVertical={({ style }) => (
                        <div
                          style={{
                            ...style,
                            backgroundColor: "rgba(0, 0, 0, 0.1)",
                            borderRadius: "10px",
                          }}
                        />
                      )}
                    >
                      <h3 className="text-xl font-semibold mb-2">
                        Kundli Chart:
                      </h3>
                      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                        {/* House Cards */}
                        {[
                          "1st House",
                          "2nd House",
                          "3rd House",
                          "4th House",
                          "5th House",
                          "6th House",
                          "7th House",
                          "8th House",
                          "9th House",
                          "10th House",
                          "11th House",
                          "12th House",
                        ].map((house, index) => (
                          <div
                            key={index}
                            className="bg-white p-4 rounded-2xl shadow-lg border-2 border-gray-300 font-serif"
                            style={{
                              background:
                                "url('/path/to/old-paper-texture.jpg')",
                              backgroundSize: "cover",
                            }}
                          >
                            <h4 className="text-center font-bold">{house}</h4>
                            <p className="text-center">
                              {
                                [
                                  "Aries",
                                  "Taurus",
                                  "Gemini",
                                  "Cancer",
                                  "Leo",
                                  "Virgo",
                                  "Libra",
                                  "Scorpio",
                                  "Sagittarius",
                                  "Capricorn",
                                  "Aquarius",
                                  "Pisces",
                                ][index]
                              }
                            </p>
                            <p className="text-center text-sm">
                              Ruling Planet:{" "}
                              {
                                [
                                  "Mars",
                                  "Venus",
                                  "Mercury",
                                  "Moon",
                                  "Sun",
                                  "Mercury",
                                  "Venus",
                                  "Mars",
                                  "Jupiter",
                                  "Saturn",
                                  "Uranus",
                                  "Neptune",
                                ][index]
                              }
                            </p>
                            <p className="text-center text-sm">
                              Planet:{" "}
                              {
                                [
                                  "Sun",
                                  "Moon",
                                  "Venus",
                                  "Mars",
                                  "Jupiter",
                                  "Saturn",
                                  "Mercury",
                                  "Uranus",
                                  "Neptune",
                                  "Pluto",
                                  "Earth",
                                  "Mars",
                                ][index]
                              }
                            </p>
                          </div>
                        ))}
                      </div>
                    </Scrollbars>
                  </motion.div>

                  {/* Zodiac Sign */}
                  <motion.div
                    className="mt-6 border-t-2 border-gray-500 pt-4"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 1, delay: 2.6 }}
                  >
                    <h3 className="text-xl font-semibold mb-2">Zodiac Sign:</h3>
                    <p className="text-center font-bold text-lg">Capricorn</p>
                  </motion.div>

                  {/* Additional Information */}
                  <motion.div
                    className="mt-6 border-t-2 border-gray-500 pt-4"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 1, delay: 2.7 }}
                  >
                    <h3 className="text-xl font-semibold mb-2">
                      Additional Information:
                    </h3>
                    <ul className="list-disc pl-6 text-sm">
                      <li>
                        <strong>Lucky Color:</strong> Red
                      </li>
                      <li>
                        <strong>Lucky Stone:</strong> Ruby
                      </li>
                      <li>
                        <strong>Element:</strong> Earth
                      </li>
                      <li>
                        <strong>Ruling Planet:</strong> Saturn
                      </li>
                      <li>
                        <strong>Strengths:</strong> Ambitious, Disciplined,
                        Practical
                      </li>
                      <li>
                        <strong>Weaknesses:</strong> Pessimistic, Stubborn,
                        Reserved
                      </li>
                    </ul>
                  </motion.div>
                </div>
              </motion.div>
            )}
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default KundliPage;
