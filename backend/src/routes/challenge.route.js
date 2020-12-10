import { Router } from "express";
import * as ChallengeController from "../controllers/challenge.controller";
const router = Router();

// GET challenges/
router.get("/", ChallengeController.findAll);
router.get("/:id", ChallengeController.findOne);

// POST challenges/ Enviar
router.post("/", ChallengeController.addResult);

export default router;
