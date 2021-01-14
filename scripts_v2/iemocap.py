from base import Generator
import glob
import os
import csv
import pandas as pd


def generar_csv():

    features = [
        "file",
        # "mode",
        # "channel",
        "emotion",
        # "intensity",
        # "statement",
        # "repetition",
        # "actor"
    ]

    # dialog/EmoEvaluation/Categorical

    input_folder = "../../datasets/IEMOCAP_full_release"

    files_wav = glob.glob(os.path.join(
        input_folder, "") + '/**/sentences/wav/**/*.wav', recursive=True)

    files_cat = glob.glob(os.path.join(
        input_folder, "") + '/**/dialog/EmoEvaluation/Categorical/*.txt', recursive=True)

    # print(files_wav)
    # print(files_cat)

    dic = {}

    for f in files_wav:
        filename = os.path.basename(f)
        dic[filename[:-4]] = [f, 0]
        print(filename[:-4])

    for f in files_cat:
        data = pd.read_csv(f, delimiter=":", header=None,
                           names=["file", "emotion", "emotion2"])
        print(data)

        for i in range(len(data)):
            file_ = data.loc[i, "file"].strip()
            emotion_ = data.loc[i, "emotion"].strip().split(";")[0]
            dic[file_][1] = emotion_

    with open("output/iemocap_general.csv", mode='w') as new_csv_file:
        new_csv_file = csv.writer(new_csv_file, delimiter=',')
        new_csv_file.writerow(features)

        for k, v in dic.items():
            # filename = os.path.basename(f)
            # file_features = filename[:-4].split('-')
            # file_features = [int(f)-1 for f in file_features]
            new_csv_file.writerow(v)  # solo emotion

    # print(dic)


generar_csv()

g = Generator("output/iemocap_general.csv",
              "", "output", "iemocap")

g.deploy()
