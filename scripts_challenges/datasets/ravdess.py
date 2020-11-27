from os import listdir, path
from datasets.base import Generator
import glob
import random
import csv



class RavdessGenerator(Generator):
    def __init__(self, input_folder , output_folder, folder_name='Audio_Speech_Actors_01-24', random_seed = 0):
       
        self.folder_name = folder_name
        self.random_seed = random_seed
        
        self.features = [
                    "file",
                    # "mode",
                    # "channel",
                    "emotion",
                    # "intensity",
                    # "statement",
                    # "repetition",
                    # "actor"
                    ]

        super().__init__(input_folder,output_folder, "ravdess")
         


        """
        Revisar posibles errores
        """
        files_found = listdir(self.input_folder)
        
        if not self.folder_name in files_found:
            raise Exception(
                "No se encontraro la carpeta " + self.folder_name + "  " + path.abspath(self.input_folder))

    def generate_partitions(self):
        files_wav = glob.glob(path.join(
            self.input_folder, self.folder_name) + '/**/*.wav', recursive=True)

        random.seed(self.random_seed)
        random.shuffle(files_wav)
        
        end = 0
        suma = 0
        for k in self.modes:
            #iterar sobre los modos ( test, train , etc...)
            begin = int(end)
            end = int(begin + self.modes[k]["percentage"]* len(files_wav))
            # print(begin,end)
            self.modes[k]["wavs"] = files_wav[begin:end]
            suma+= len(self.modes[k]["wavs"]) #Solo por motivos de assert

            with open(path.join(self.output_folder_compose, k+"_temp.csv"), mode='w') as new_csv_file:
                new_csv_file = csv.writer(new_csv_file, delimiter=',')                
                if self.modes[k]["labels"]:
                    #se obtienen todas las features ( filename, mode, etc ...)
                    new_csv_file.writerow(self.features)
                    for f in self.modes[k]["wavs"]:
                        filename = path.basename(f)
                        file_features = filename[:-4].split('-')
                        file_features = [int(f)-1 for f in file_features]
                        new_csv_file.writerow([f] + file_features[2:3] ) #solo emotion

                else:
                    #Solo se obtiene el nombre del archivo
                    new_csv_file.writerow(self.features[:1])
                    for f in self.modes[k]["wavs"]:
                        new_csv_file.writerow([f])

            #write Answers
            if not self.modes[k]["labels"]:
                with open(path.join(self.output_folder_compose, k+"_answers_temp.csv"), mode='w') as new_csv_file:
                    new_csv_file = csv.writer(new_csv_file, delimiter=',')  
                    new_csv_file.writerow(self.features)
                    for f in self.modes[k]["wavs"]:
                        filename = path.basename(f)
                        file_features = filename[:-4].split('-')
                        file_features = [int(f)-1 for f in file_features]
                        new_csv_file.writerow([f] + file_features[2:3]) #solo emotion

                
        assert suma == len(files_wav) , "Deberia haber:"+len(files_wav)+ " , hay "+suma

        self.deploy()








