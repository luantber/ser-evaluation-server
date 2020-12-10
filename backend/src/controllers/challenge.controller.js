import Challenge from "../models/Challenge";

export const findAll = async (req, res) => {
  try {
    const challenges = await Challenge.find();
    res.json(Challenges);
  } catch (error) {
    res.status(400).json(error);
  }
};

export const findOne = async (req, res) => {
  try {
    // console.log(req.params.id);
    const challenge = await Challenge.findById(req.params.id);
    // console.log("algo", challenge);
    res.json(challenge);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};

export const addResult = async (req, res) => {
  try {
    // const newChallenge = new Challenge(req.body);
    const newchallenge = await Challenge.findById(req.params.id);
    await newChallenge.save();
    res.json(newChallenge);
  } catch (error) {
    res.status(400).json(error);
  }
};
