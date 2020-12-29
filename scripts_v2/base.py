import os
import functools
import pandas as pd

import torch
import torchaudio


import shutil
from zipfile import ZipFile
'''
Esta clase leera un archivo inicial .csv de la forma:

file, feature1, feature2, ....
archivo.wav, 1, 3
'''


class Generator():
    '''
    ouput_folder = path folder que contendra el output por ejemplo:    /output/
    name_dataset = "ravdess"

    Los resultados se ubicarán en /output/ravdes/ 
    '''

    def __init__(self, input_path, output_folder, name_dataset):

        self.input_path = input_path  # CSV path
        self.name_dataset = name_dataset  # nombre dataset (ravdess)
        self.output_folder = os.path.join(
            output_folder, self.name_dataset)  # Where to locate the output files

        self.modes = {
            'train': {
                "percentage": 0.55,
                "labels": True,
            },
            'validation': {
                "percentage": 0.15,
                "labels": True
            },
            'test': {
                "percentage": 0.15,
                "labels": False
            },
            'challenge': {
                "percentage": 0.15,
                "labels": False
            },
        }

        """
        Assert modes
        """
        suma = functools.reduce(
            lambda acc, key: self.modes[key]["percentage"]+acc, self.modes, 0)
        assert suma == 1.0, "La suma es: " + str(suma)

        """
        Revisar errores 
        """
        if not os.path.isfile(input_path):
            print("No existe", input_path)

        # Crear Ouput folder si no existe
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print("No existe" + self.output_folder + " ... Creando")

    """
    This function makes copies of files and preprocess it 
    """

    def __transform(self):
        os.makedirs(self.output_folder, "temp")

        data = pd.read_csv(self.input_path)
        data = data.sample(frac=1)
        # data = data.sample(frac=1).reset_index(drop=True)

        # Aquí irán operaciones para transformar los audios:
        for i in range(len(data)):

            name_file = data.loc[i, "file"]

            audio, sr = torchaudio.load(name_file)

            nuevo_name = "temp/" + str(i) + ".wav"
            data.loc[i, "file"] = nuevo_name

            torchaudio.save(nuevo_name, audio, sr)

        return data

    def __generate_partitions(self, data):
        size = len(data)
        for keyMode in self.modes:
            # Esta funcion obtiene los primeros  n% de size
            partition = data.head(size * self.modes[keyMode]["percentage"])
            # labels
            if self.modes[keyMode]["labels"]:
                # Pass with all features
                partition.to_csv("temp/"+keyMode + ".csv")
            else:
                partition["file"].to_csv("temp/"+keyMode + ".csv")
                partition.to_csv("temp/"+keyMode + "_answers.csv")

            data.drop(partition.index)

        assert(len(data) == 0)

    def __create_bundles(self):
        for keyMode in self.modes:

            csv_file = "temp/"+keyMode + ".csv"
            data = pd.read_csv(csv_file)

            # Crear audios temporal
            os.makedirs(os.path.join("temp", "audios"))

            # zip object
            zipObj = ZipFile("temp/" + keyMode + ".zip", 'w')

            # add Audios
            for i in range(len(data)):
                shutil.copy(
                    "temp/" + data.loc[i, "file"],
                    "temp/audios"
                )
                zipObj.write("temp/audios", "audios/" + data.loc[i, "file"])

            # add CSV
            zipObj.write("temp/"+keyMode + ".csv", keyMode + ".csv")

        # clean "temp" folder
        shutil.rmtree('temp')

    def deploy(self):
        data = self.__transform()
        self.__generate_partitions(data)
        self.__create_bundles()
        print("Fin")
