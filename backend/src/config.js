import { config } from "dotenv";
config();

const database = {
  mongodbUri: process.env.MONGODB_URI,
};

export { database };
