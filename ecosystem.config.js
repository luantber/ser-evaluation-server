module.exports = {
  apps: [
    {
      name: "ser_frontend",
      cwd: "./frontend/",
      script: "npm run start",
      watch: ".nuxt",
    },

    {
      name: "ser_backend",
      cwd: "./backend/",
      script: "build/index.js",
      watch: "build",
    },
  ],
};