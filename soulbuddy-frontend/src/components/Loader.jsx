import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { FaSpinner } from 'react-icons/fa';

const Loader = ({ isLoading }) => {
  const messages = [
    'Loading your personalized Kundali...',
    'Analyzing astrological data...',
    'Calculating planetary positions...',
    'Preparing spiritual guidance...',
    'Fetching horoscope insights...',
  ];

  const [currentMessage, setCurrentMessage] = useState(messages[0]);

  useEffect(() => {
    let messageInterval;

    if (isLoading) {
      messageInterval = setInterval(() => {
        setCurrentMessage(messages[Math.floor(Math.random() * messages.length)]);
      }, 2000);
    }

    return () => clearInterval(messageInterval);
  }, [isLoading, messages]);

  if (!isLoading) return null;

  return (
    <motion.div
      className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-70 flex items-center justify-center z-50"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      <div className="text-center text-white space-y-4">
        <FaSpinner className="text-5xl animate-spin mx-auto" />
        <p className="text-lg">{currentMessage}</p>
      </div>
    </motion.div>
  );
};

export default Loader;
