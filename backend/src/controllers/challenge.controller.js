import Result from "../models/Result";
import Challenge from "../models/Challenge";
import User from "../models/User";

export const findAll = async (req, res) => {
  try {
    const challenges = await Challenge.find().populate({
      path: "results",
      match: { mode: "test" },
    });

    res.json(challenges);
  } catch (error) {
    res.status(400).json(error);
  }
};

export const findOne = async (req, res) => {
  try {
    // console.log(req.params.id);
    const challenge = await Challenge.findById(req.params.id).populate(
      "results"
    );

    // console.log("algo", challenge);
    res.json(challenge);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};

export const findOneMe = async (req, res) => {
  try {
    const challenges = await (await Challenge.findById(req.params.id)).populate(
      {
        path: "results",
        match: {
          user: req.user._id,
        },
      }
    );

    res.json(challenges);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};

export const addResult = async (req, res) => {
  try {
    // const newChallenge = new Challenge(req.body);
    const user = await User.findById(req.user._id);
    const challenge = await Challenge.findById(req.body.id);
    const result = await new Result(req.body.result);

    result.challenge = challenge;
    result.user = req.user;
    await result.save();

    await challenge.results.push(result);
    challenge.save();

    await user.results.push(result);
    user.save();

    res.json(challenge);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};
