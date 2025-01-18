import React, { useState } from 'react';
import { FaUser, FaCalendarAlt, FaClock, FaMapMarkerAlt } from 'react-icons/fa';
import { motion } from 'framer-motion';
import Loader from '../components/Loader';
import '@fontsource/poppins';

const FormPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    dateOfBirth: '',
    timeOfBirth: '',
    gender: "",
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
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 5000));
      console.log('Form submitted:', formData);
    } catch (error) {
      console.error('Error submitting form:', error);
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

                {/* Gender */}
              <div>
                <label className="block text-lg font-semibold">Gender</label>
                <div className="flex items-center space-x-6 mt-2">
                  <div className="flex items-center space-x-2">
                    <input
                      type="radio"
                      id="male"
                      name="gender"
                      value="Male"
                      onChange={handleChange}
                      checked={formData.gender === "Male"}
                    />
                    <label htmlFor="male" className="text-lg">Male</label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      type="radio"
                      id="female"
                      name="gender"
                      value="Female"
                      onChange={handleChange}
                      checked={formData.gender === "Female"}
                    />
                    <label htmlFor="female" className="text-lg">Female</label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      type="radio"
                      id="other"
                      name="gender"
                      value="Other"
                      onChange={handleChange}
                      checked={formData.gender === "Other"}
                    />
                    <label htmlFor="other" className="text-lg">Other</label>
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
                      <option value="Bihar">Bihar</option>
                      <option value="Chhattisgarh">Chhattisgarh</option>
                      <option value="Goa">Goa</option>
                      <option value="Gujarat">Gujarat</option>
                      <option value="Haryana">Haryana</option>
                      <option value="Himachal Pradesh">Himachal Pradesh</option>
                      <option value="Jharkhand">Jharkhand</option>
                      <option value="Karnataka">Karnataka</option>
                      <option value="Kerala">Kerala</option>
                      <option value="Madhya Pradesh">Madhya Pradesh</option>
                      <option value="Maharashtra">Maharashtra</option>
                      <option value="Manipur">Manipur</option>
                      <option value="Meghalaya">Meghalaya</option>
                      <option value="Mizoram">Mizoram</option>
                      <option value="Nagaland">Nagaland</option>
                      <option value="Odisha">Odisha</option>
                      <option value="Punjab">Punjab</option>
                      <option value="Rajasthan">Rajasthan</option>
                      <option value="Sikkim">Sikkim</option>
                      <option value="Tamil Nadu">Tamil Nadu</option>
                      <option value="Telangana">Telangana</option>
                      <option value="Tripura">Tripura</option>
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
                    <option value="Ahmedabad">Ahmedabad</option>
                    <option value="Bengaluru">Bengaluru</option>
                    <option value="Chennai">Chennai</option>
                    <option value="Delhi">Delhi</option>
                    <option value="Hyderabad">Hyderabad</option>
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
