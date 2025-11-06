/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Custom colors for interview prep theme
        'code-bg': '#1e1e1e',
        'code-text': '#d4d4d4',
      },
      fontFamily: {
        mono: ['Fira Code', 'Consolas', 'Monaco', 'Courier New', 'monospace'],
      },
      keyframes: {
        'slide-in': {
          '0%': { transform: 'translateX(100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
      },
      animation: {
        'slide-in': 'slide-in 0.3s ease-out',
      },
    },
  safelist: [
    // Ensure dynamic and custom classes are preserved
    'bg-gray-750',
    'hover:bg-gray-750',
    'text-blue-500', 'bg-blue-500/10', 'bg-blue-600/20', 'text-blue-400',
    'text-purple-500', 'bg-purple-600', 'hover:bg-purple-700',
    'text-green-500', 'bg-green-500/20',
    'text-yellow-500', 'bg-yellow-500/20', 'bg-yellow-600', 'hover:bg-yellow-700',
    'text-red-500', 'bg-red-500/20', 'bg-red-600', 'hover:bg-red-700'
  ],

  },
  plugins: [],
  darkMode: 'class',
}
