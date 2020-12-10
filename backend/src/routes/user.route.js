import { Router } from "express";
// import * as ProductoController from "../controllers/producto.controller";
const router = Router();
import passport from "passport";
// GET productos/
router.get(
  "/me",
  passport.authenticate("jwt", { session: false }),
  async (req, res) => {
    res.json({ user: { name: "Luis" } });
  }
);



export default router;
