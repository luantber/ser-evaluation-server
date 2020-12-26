import { Router } from "express";
import * as ChallengeController from "../controllers/challenge.controller";
import passport from "passport";

const router = Router();

// GET challenges/
router.get("/", ChallengeController.findAll);
router.get("/:id", ChallengeController.findOne);
router.get(
  "/:id/me",
  passport.authenticate("jwt", { session: false }),
  ChallengeController.findOneMe
);

// POST challenges/ Enviar
router.post(
  "/",
  passport.authenticate("jwt", { session: false }),
  ChallengeController.addResult
);

export default router;
