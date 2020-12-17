import { Schema, model } from "mongoose";

const resultSchema = new Schema(
  {
    name: String,
    mode: {
      type: String,
      required: true,
      default: "test",
    },
    metrics: [
      {
        name: String,
        result: Number,
      },
    ],
    user: { type: Schema.Types.ObjectId, ref: "User" },
    challenge: { type: Schema.Types.ObjectId, ref: "Challenge" },
  },
  {
    // versionKey: false,
    timestamps: true,
  }
);

export default model("Result", resultSchema);
