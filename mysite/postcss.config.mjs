export default {
  plugins: {
    "@tailwindcss/postcss": {},
  }
}

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './ecom/templates/**/*.html',
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}


