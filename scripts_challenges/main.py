
from datasets.ravdess import RavdessGenerator

ravdess = RavdessGenerator("../../datasets/ravdess", "output")
ravdess.generate_partitions()