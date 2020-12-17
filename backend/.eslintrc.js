module.exports = {
  env: {
    node: true,
  },
  extends: ["eslint:recommended", "prettier", "plugin:prettier/recommended"],
  parser: "@babel/eslint-parser",
  plugins: ["prettier"],
  rules: { "prettier/prettier": "warn" },
};
