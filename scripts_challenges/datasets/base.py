import os
import functools
import pandas as pd
import shutil
import glob

from zipfile import ZipFile

'''
    Esta clase busca los siguientes archivos: 
    validation_temp.csv 
    train_temp.csv , etc... 

    En cada archivo Debe estar:

    file,emotion
    ../../datasets/ravdess/Audio_Speech_Actors_01-24/Actor_17/03-01-02-01-02-01-17.wav,1
    ../../datasets/ravdess/Audio_Speech_Actors_01-24/Actor_07/03-01-06-01-02-02-07.wav,5
    ../../datasets/ravdess/Audio_Speech_Actors_01-24/Actor_21/03-01-02-02-02-01-21.wav,1
    ../../datasets/ravdess/Audio_Speech_Actors_01-24/Actor_14/03-01-05-01-02-01-14.wav,4
    ../../datasets/ravdess/Audio_Speech_Actors_01-24/Actor_19/03-01-05-01-01-02-19.wav,4

    Se leerá y se zipearán los audios 


'''
class Generator():
    def __init__(self, input_folder, output_folder, name):

        self.input_folder = input_folder
        self.output_folder = output_folder
        self.name = name
        self.output_folder_compose = os.path.join(output_folder, self.name)

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
        Revisar posibles errores
        """
        files_found = os.listdir(self.input_folder)
        # print(files_found)
        if not files_found:
            raise Exception(
                "No se encontraron archivos en la carpeta:  " + os.path.abspath(self.input_folder))

        if not os.path.exists(self.output_folder_compose):
            os.makedirs(self.output_folder_compose)
            print("No existe" + self.output_folder_compose + " ... Creando")

    def deploy(self):

        # print(self.output_folder_compose)

        files_found = os.listdir(self.output_folder_compose)

        # print(files_found)

        if not files_found:
            raise Exception(
                "No se encontraron archivos en la carpeta:  " + os.abspath(self.output_folder_compose))

        # Para cada modo Crear Un ZIP  ( cahllenge_temp.csv , ... etc )
        for k in self.modes:

            csv_temp = os.path.join(self.output_folder_compose, k+"_temp.csv")

            data = pd.read_csv(csv_temp)

            # Crea directorio
            os.makedirs(os.path.join(self.output_folder_compose, "audios"))

            # zip object
            zipObj = ZipFile(os.path.join(
                self.output_folder_compose, k+".zip"), 'w')

            for i in range(len(data)):
                nuevo_name = self.name+"_"+k+"_"+str(i)+".wav"
                path_nuevo_name = os.path.join(
                    self.output_folder_compose, "audios", nuevo_name)

                # copy
                shutil.copy(
                    os.path.join(self.input_folder, data.loc[i, "file"]),
                    path_nuevo_name
                )
                data.loc[i, "file"] = nuevo_name
                # print(os.path.join("audios", os.path.basename(path_nuevo_name)))
                zipObj.write(path_nuevo_name, os.path.join(
                    "audios", os.path.basename(path_nuevo_name)))

            data.to_csv(os.path.join(
                self.output_folder_compose, k+".csv"), index=False)
            zipObj.write(os.path.join(self.output_folder_compose, k+".csv"),
                         os.path.basename(os.path.join(self.output_folder_compose, k+".csv")))

            shutil.rmtree(os.path.join(
                self.output_folder_compose, "audios"))  # ojoo
            os.remove(os.path.join(self.output_folder_compose, k+".csv"))

            # ANSWERS
            if not self.modes[k]["labels"]:
                csv_temp = os.path.join(
                    self.output_folder_compose, k+"_answers_temp.csv")
                data = pd.read_csv(csv_temp)
                for i in range(len(data)):
                    nuevo_name = self.name+"_"+k+"_"+str(i)+".wav"
                    path_nuevo_name = os.path.join(
                        self.output_folder_compose, "audios", nuevo_name)
                    data.loc[i, "file"] = nuevo_name
                data.to_csv(os.path.join(
                    self.output_folder_compose, k+"_answers.csv"), index=False)

        # Clean temporal files
        # for f in glob.glob(os.path.join(self.output_folder_compose, "*_temp.csv")):
        #     os.remove(f)
