from base import Generator
import glob
import os
import csv


def create_csv():
    features = [
        "file",
        # "mode",
        # "channel",
        "valence",
        "arousal",
        "dominance"
        # "intensity",
        # "statement",
        # "repetition",
        # "actor"
    ]

    folder_name = 'kusisqa'
    input_folder = "../datasets/"

    files_wav = glob.glob(os.path.join(
        input_folder, folder_name) + '/**/*.wav', recursive=True)

    with open("output/kusisqadim_general.csv", mode='w') as new_csv_file:
        new_csv_file = csv.writer(new_csv_file, delimiter=',')
        new_csv_file.writerow(features)
        for f in files_wav:
            try:
                filename = os.path.basename(f)
                # print(">>>",filename)

                file_features = filename[:-4].split("_")[1].split('-')

                file_features = [int(f) for f in file_features]
                # print(file_features,[f] + file_features[3:4])
                new_csv_file.writerow([f] + file_features[1:4])  # solo emotion
                # break
            except:
                print(f, "can't read")
                pass


create_csv()
g = Generator("output/kusisqadim_general.csv",
              "", "output", "kusisqadim")

g.deploy()
