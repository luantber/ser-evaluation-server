import express from "express";
import cors from "cors";

import ChallengeRoutes from "./routes/challenge.route";
import UserRoutes from "./routes/user.route";
import PassportRoutes from "./routes/passport.route";

import { adminBro, routerAdminBro } from "./adminbro";
import "./auth/auth";

const app = express();
app.set("port", process.env.PORT || 1337);

// CORS
app.use(cors());

// Json
app.use(express.json());

// Routes
app.use("/", PassportRoutes);
app.use("/users", UserRoutes);
app.use("/challenges", ChallengeRoutes);

// Admin Bro
if ((process.env.DEBUG || "FALSE") === "TRUE") {
  app.use(adminBro.options.rootPath, routerAdminBro);
}

export default app;
