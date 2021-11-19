import os
import functools
import pandas as pd

import torch
import torchaudio

import math
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

    def __init__(self, input_path, input_folder, output_folder, name_dataset):

        self.input_path = input_path  # CSV path
        self.input_folder = input_folder
        self.name_dataset = name_dataset  # nombre dataset (ravdess)
        self.output_folder = os.path.join(
            output_folder, self.name_dataset)  # Where to locate the output files
        
        self.seconds = 0

        # self.modes = {
        #     'train': {
        #         "percentage": 0.55,
        #         "labels": True,
        #     },
        #     'validation': {
        #         "percentage": 0.15,
        #         "labels": True
        #     },
        #     'test': {
        #         "percentage": 0.15,
        #         "labels": False
        #     },
        #     'challenge': {
        #         "percentage": 0.15,
        #         "labels": False
        #     },
        # }

        self.modes = {
            'train': {
                "percentage": 1,
                "labels": True,
            }
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
            print("No existe ", input_path)

        # Crear Ouput folder si no existe
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print("No existe " + self.output_folder + " ... Creando")

    """
    This function makes copies of files and preprocess it 
    """

    def __transform(self):
        if not os.path.exists("temp"):
            os.makedirs("temp")

        data = pd.read_csv(self.input_path)
        # data = data.sample(frac=1)
        data = data.sample(frac=1, random_state=52).reset_index(drop=True)

        # Aquí irán operaciones para transformar los audios:
        for i in range(len(data)):

            name_file = os.path.join(self.input_folder, data.loc[i, "file"])

            audio, sr = torchaudio.load(name_file)
            # print(sr, audio.shape )

            if audio.shape[0] == 2: 
                # print(audio.shape , audio[0].mean() , audio[0].std(),"___" ,audio[1].mean() , audio[1].std() )
                # audio_mono = torch.mean(audio, dim=0, keepdim=True)
                audio_mono = audio[0].unsqueeze(0)
                # print(audio_mono.shape, audio_mono.mean() , audio_mono.std() )
            else: 
                audio_mono = audio
            
            self.seconds += int( audio.shape[1] / sr )
            print( self.seconds , "secs" , round(self.seconds / 60, 2) , "mins", round(self.seconds / 3600, 2 ) , "hours" )

            nuevo_name = str(i) + ".wav"
            data.loc[i, "file"] = nuevo_name
            print(name_file, nuevo_name)
            torchaudio.save("temp/"+nuevo_name, audio_mono, sr , bits_per_sample=16)

        return data

    def __generate_partitions(self, data):
        size = len(data)
        for keyMode in self.modes:
            # Esta funcion obtiene los primeros  n% de size
            partition = data.head(
                math.ceil(size * self.modes[keyMode]["percentage"]))
            # labels
            if self.modes[keyMode]["labels"]:
                # Pass with all features
                partition.to_csv("temp/"+keyMode + ".csv", index=False)
            else:
                partition["file"].to_csv("temp/"+keyMode + ".csv", index=False)
                partition.to_csv("temp/"+keyMode + "_answers.csv", index=False)

            data = data.drop(partition.index)

        print("Sobrantes despues de particiones: ", len(data))
        assert(len(data) == 0)

    def __create_bundles(self):
        for keyMode in self.modes:

            csv_file = "temp/"+keyMode + ".csv"
            data = pd.read_csv(csv_file)

            # shutil.copy(
            #     csv_file,
            #     self.output_folder
            # )

            if not self.modes[keyMode]["labels"]:
                shutil.copy(
                    "temp/"+keyMode + "_answers.csv",
                    self.output_folder
                )

            # Crear audios temporal
            # if not os.path.exists(os.path.join("temp", "audios")):
            #     os.makedirs(os.path.join("temp", "audios"))

            # zip object
            zipObj = ZipFile(os.path.join(
                self.output_folder, keyMode + ".zip"), 'w')

            # add Audios
            for i in range(len(data)):

                zipObj.write(
                    "temp/" + data.loc[i, "file"], "audios/" + data.loc[i, "file"])

            # add CSV
            zipObj.write("temp/"+keyMode + ".csv", keyMode + ".csv")

        # clean "temp" folder
        shutil.rmtree('temp')

    def deploy(self):
        data = self.__transform()
        self.__generate_partitions(data)
        self.__create_bundles()
        print("Fin")
