from base import Generator
import glob
import os
import csv


def create_csv():
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

    folder_name = 'CORPUS_ESPANOL-PERU'
    input_folder = "../datasets/"

    files_wav = glob.glob(os.path.join(
        input_folder, folder_name) + '/**/*.wav', recursive=True)

    with open("output/kusisqa_general.csv", mode='w') as new_csv_file:
        new_csv_file = csv.writer(new_csv_file, delimiter=',')
        new_csv_file.writerow(features)
        for f in files_wav:
            try:
                filename = os.path.basename(f)
                file_features = filename[:-4].split('-')
                # print(f)
                file_features = [int(f)-1 for f in file_features]
                new_csv_file.writerow([f] + file_features[2:3])  # solo emotion
            except:
                print(f, "can't read")
                pass


create_csv()
g = Generator("output/kusisqa_general.csv",
              "", "output", "kusisqa")

g.deploy()
