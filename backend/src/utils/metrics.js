import csv from "csvtojson";

function accuracy(matrixConfusion) {
  let fail = 0;
  let correct = 0;
  for (const keyR in matrixConfusion) {
    for (const keyP in matrixConfusion) {
      if (keyR == keyP) correct += matrixConfusion[keyR][keyP];
      else fail += matrixConfusion[keyR][keyP];
    }
  }

  return { name: "accuracy", result: correct / (fail + correct) };
}

export const get_metrics = async (
  bufferResult,
  bufferReal,
  labels = [1, 2, 3, 4, 5]
) => {
  // console.log(bufferReal, bufferResult);
  const jsonResult = await csv().fromString(bufferResult.toString());
  const jsonReal = await csv().fromString(bufferReal.toString());

  let matrixConfusion = {};

  for (const labelR of labels) {
    matrixConfusion[labelR] = {};
    for (const labelP of labels) {
      matrixConfusion[labelR][labelP] = 0;
    }
  }

  console.log(jsonReal);
  // console.log(jsonResult);
  if (jsonResult.length != jsonReal.length) Error("no tienen el mismo size");

  for (let index = 0; index < jsonResult.length; index++) {
    const elementReal = jsonReal[index].emotion;
    const elementResult = jsonResult[index].emotion;

    matrixConfusion[elementReal][elementResult] += 1;
  }
  console.log(matrixConfusion);

  return [accuracy(matrixConfusion)];
};
