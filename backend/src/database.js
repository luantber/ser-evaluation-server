import mongoose from "mongoose";
import { database } from "./config";

(async () => {
  try {
    const db = await mongoose.connect(database.mongodbUri, {
      useUnifiedTopology: true,
      useNewUrlParser: true,
    });
    console.log("Database Connection: ", db.connection.name);
  } catch (error) {
    console.log(error);
  }
})();
