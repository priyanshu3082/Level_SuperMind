module.exports = {
  darkMode: 'class', // Enables dark mode using the 'dark' class
  content: ['./index.html', './src/**/*.{js,jsx}'], // Ensure all files are scanned
  theme: {
    extend: {
      colors: {
        darkBlack: '#0d1117',
        darkViolet: '#5a189a',
        navyBlue: '#1e3a8a',
      },
    },
  },
  plugins: [],
};
