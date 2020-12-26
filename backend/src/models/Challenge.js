import { Schema, model } from "mongoose";

const challengeSchema = new Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },

    description: {
      type: String,
    },

    results: [{ type: Schema.Types.ObjectId, ref: "Result" }],

    train: {
      type: String,
    },

    val: {
      type: String,
    },
    test: {
      type: String,
    },
    challenge: {
      type: String,
    },

    secret_test: {
      type: String,
    },
    secret_challenge: {
      type: String,
    },

    //productos: [{ type: Schema.Types.ObjectId, ref: "Producto" }],
  },
  {
    // versionKey: false,
    timestamps: true,
  }
);

export default model("Challenge", challengeSchema);
