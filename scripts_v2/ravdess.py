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

    folder_name = 'Audio_Speech_Actors_01-24'
    input_folder = "../../datasets/ravdess"

    files_wav = glob.glob(os.path.join(
        input_folder, folder_name) + '/**/*.wav', recursive=True)

    with open("output/ravdess_general.csv", mode='w') as new_csv_file:
        new_csv_file = csv.writer(new_csv_file, delimiter=',')
        new_csv_file.writerow(features)
        for f in files_wav:
            filename = os.path.basename(f)
            file_features = filename[:-4].split('-')
            file_features = [int(f)-1 for f in file_features]
            new_csv_file.writerow([f] + file_features[2:3])  # solo emotion


create_csv()
g = Generator("output/ravdess_general.csv",
              "", "output", "ravdess")

g.deploy()
