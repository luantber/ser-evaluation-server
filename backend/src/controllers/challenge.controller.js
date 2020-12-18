import Result from "../models/Result";
import Challenge from "../models/Challenge";
import User from "../models/User";
import path from "path";
import { promises as fs } from "fs";
import { get_metrics } from "../utils/metrics";

export const findAll = async (req, res) => {
  try {
    const challenges = await Challenge.find().populate({
      path: "results",
      match: { mode: "test" },
      // options: { sort: { updatedAt: "asc" } },
    });

    res.json(challenges);
  } catch (error) {
    res.status(400).json(error);
  }
};

export const findOne = async (req, res) => {
  try {
    const challenge = await Challenge.findById(req.params.id).populate({
      path: "results",
      populate: [
        {
          path: "user",
          model: "User",
        },
        { path: "metrics" },
      ],
    });

    res.json(challenge);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};

export const findOneMe = async (req, res) => {
  try {
    const challenges = await Challenge.findById(req.params.id).populate({
      path: "results",
      match: {
        user: req.user._id,
      },
    });

    res.json(challenges);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};

export const addResult = async (req, res) => {
  try {
    // Parseo de req
    console.log(req.body);
    const resultReq = JSON.parse(req.body.result);
    console.log(resultReq);

    // Si no existen archivos return 400
    if (!req.files || Object.keys(req.files).length === 0) {
      return res.status(400).json("No files were uploaded.");
    }

    // Encontrar el challenge

    const challenge = await Challenge.findById(req.body.id);

    // const resultFile = req.files.file;
    // const pathFile = path.resolve(
    //   "files/uploads/" +
    //     challenge.name +
    //     "_" +
    //     req.body.result.mode +
    //     "_" +
    //     resultFile.md5 +
    //     ".csv"
    // );
    // console.log(pathFile);

    // Load both Buffers
    const bufferResult = req.files.file.data;
    const bufferReal = await fs.readFile(
      // path.resolve("/secret", challenge.name, req.body.result.mode + ".csv")
      path.resolve("files/secret", "test", resultReq.mode + ".csv")
    );

    const metrics = await get_metrics(bufferResult, bufferReal);
    // resultFile.mv(pathFile);

    // const newChallenge = new Challenge(req.body);

    const user = await User.findById(req.user._id);
    const result = new Result({ metrics, ...resultReq });

    result.challenge = challenge;
    result.user = req.user._id;
    await result.save();

    challenge.results.push(result._id);
    await challenge.save();
    // console.log("asdasd ***************+");
    user.results.push(result._id);
    // console.log("asdasd");
    await user.save();
    // console.log("asdasd xxxxxx");
    // console.log(challenge);
    res.json(challenge);
  } catch (error) {
    console.log(error);
    res.status(400).json(error);
  }
};
