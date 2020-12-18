import express from "express";
import cors from "cors";

import ChallengeRoutes from "./routes/challenge.route";
import UserRoutes from "./routes/users.route";
import PassportRoutes from "./routes/passport.route";

// mids
import { adminBro, routerAdminBro } from "./adminbro";
import fileUpload from "express-fileupload";

import "./auth/auth";

const app = express();
app.set("port", process.env.PORT || 1337);

// CORS
app.use(cors());

// Admin Bro
if ((process.env.DEBUG || "FALSE") === "TRUE") {
  app.use(adminBro.options.rootPath, routerAdminBro);
}

// Json
app.use(express.json());
app.use(fileUpload({ debug: false }));

// Routes
app.use("/", PassportRoutes);
app.use("/users", UserRoutes);
app.use("/challenges", ChallengeRoutes);

export default app;
