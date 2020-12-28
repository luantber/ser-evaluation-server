import os
import functools
import pandas as pd

import torch
import torchaudio

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
        self.name_dataset = name_dataset
        self.output_folder = os.path.join(
            output_folder, self.name_dataset)  # Where to locate the output files

        self.modes = {
            'train': {
                "percentage": 0.55,
                "labels": True
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

    def generate_partitions(self):
        end = 0
        suma = 0
        for k in self.modes:
            begin = int(end)
            end = int(begin + self.modes[k]["percentage"]* len(files_wav))    
    
