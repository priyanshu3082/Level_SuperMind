import React, { useState } from 'react';
import axios from 'axios';
import { FaUser, FaCalendarAlt, FaClock, FaMapMarkerAlt } from 'react-icons/fa';
import { motion } from 'framer-motion';
import Loader from '../components/Loader';
import '@fontsource/poppins';

const FormPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    dateOfBirth: '',
    timeOfBirth: '',
    gender: '',
    state: '',
    city: '',
  });

  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/api/user_details', formData);
      alert(response.data.message);
    } catch (error) {
      console.error('Error submitting form:', error);
      alert('Error: ' + error.response.data.error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="relative">
      {/* Loader */}
      <Loader isLoading={isLoading} />

      {/* FormPage */}
      <div
        className={`bg-gradient-to-b from-purple-900 to-black text-white min-h-screen flex items-center ${
          isLoading ? 'blur-sm' : ''
        }`}
      >
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
                Enter Your Birth Details
              </h1>
              <p className="text-lg lg:text-xl">
                Provide your details to unlock personalized spiritual insights and guidance.
              </p>
              <form onSubmit={handleSubmit} className="space-y-6">
                {/* Name */}
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">
                    Full Name
                  </label>
                  <div className="flex items-center bg-purple-800 p-3 rounded-lg">
                    <FaUser className="text-xl text-white mr-3" />
                    <input
                      type="text"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      placeholder="Enter your full name"
                      className="w-full bg-transparent text-white placeholder-gray-400 focus:outline-none"
                      required
                    />
                  </div>
                </div>

                {/* Date of Birth & Time of Birth */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">
                      Date of Birth
                    </label>
                    <div className="flex items-center bg-purple-800 p-3 rounded-lg">
                      <FaCalendarAlt className="text-xl text-white mr-3" />
                      <input
                        type="date"
                        name="dateOfBirth"
                        value={formData.dateOfBirth}
                        onChange={handleChange}
                        className="w-full bg-transparent text-white placeholder-gray-400 focus:outline-none"
                        required
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">
                      Time of Birth
                    </label>
                    <div className="flex items-center bg-purple-800 p-3 rounded-lg">
                      <FaClock className="text-xl text-white mr-3" />
                      <input
                        type="time"
                        name="timeOfBirth"
                        value={formData.timeOfBirth}
                        onChange={handleChange}
                        className="w-full bg-transparent text-white placeholder-gray-400 focus:outline-none"
                        required
                      />
                    </div>
                  </div>
                </div>
{/* State & City */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">
                    State
                  </label>
                  <div className="flex items-center bg-purple-800 p-3 rounded-lg">
                    <FaMapMarkerAlt className="text-xl text-white mr-3" />
                    <select
                      name="state"
                      value={formData.state}
                      onChange={handleChange}
                      className="w-full bg-transparent text-white placeholder-gray-400 focus:outline-none"
                      required
                    >
                      <option value="">Select your state</option>
                      <option value="Andhra Pradesh">Andhra Pradesh</option>
                      <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                      <option value="Assam">Assam</option>
                      <option value="Uttar Pradesh">Uttar Pradesh</option>
                      <option value="Uttarakhand">Uttarakhand</option>
                      <option value="West Bengal">West Bengal</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">
                    City
                  </label>
                  <div className="flex items-center bg-purple-800 p-3 rounded-lg">
                    <FaMapMarkerAlt className="text-xl text-white mr-3" />
                    <select
                      name="city"
                      value={formData.city}
                      onChange={handleChange}
                      className="w-full bg-transparent text-white placeholder-gray-400 focus:outline-none"
                      required
                    >
                      <option value="">Select your city</option>
                      {/* Add city options here based on the selected state */}
                    <option value="Kolkata">Kolkata</option>
                    <option value="Mumbai">Mumbai</option>
                    <option value="Pune">Pune</option>
                    </select>
                  </div>
                </div>
              </div>

                <motion.button
                  type="submit"
                  className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-6 rounded-lg shadow-lg transform transition-all mt-6"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  Submit
                </motion.button>
              </form>
            </motion.div>

            {/* Right Section */}
            <motion.div
              className="lg:w-1/2 mt-8 lg:mt-0 flex justify-center"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1, delay: 0.5 }}
            >
              <img
                src="1.webp"
                alt="Form Illustration"
                className="w-full max-w-lg rounded-lg shadow-xl"
              />
            </motion.div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FormPage;
