<template lang="pug">
.estructura.padding5
  img(src='~static/puntos.png')
  h2.section-title Datasets
  section.estructura__derecha.datasets
    .datasets__contenedor
      .datasets__contenedor__caja 
        p.datasets__contenedor__caja__title Kusisqa Dataset
        p.datasets__contenedor__caja__datos + 500 files
        p.datasets__contenedor__caja__datos + 4gb train data
      .datasets__contenedor__caja 
        p.datasets__contenedor__caja__title IEMOCAP
        p.datasets__contenedor__caja__datos + 500 files
        p.datasets__contenedor__caja__datos + 4gb train data
      .datasets__contenedor__caja 
        p.datasets__contenedor__caja__title RAVDESS
        p.datasets__contenedor__caja__datos + 500 files
        p.datasets__contenedor__caja__datos + 4gb train data

    h5 Datasets format:
    p Each dataset is contained in a “.zip” file, example:
    ul 
      li validation.zip
      li train.zip
      li test.zip
      li challenge.zip
    p Each zip file contain the following structure:
    ul 
      li audios/
      li audios/1009.wav
      li audios/1010.wav
      li ...
      li file.csv
    p The audios are .wav files with a sampling rate of 23000hz and mono channel. The “file.csv”, is the list of files and the labels in a CSV format, using the following format:
    ul 
      li file,emotion
      li 1009.wav,4
      li 1010.wav,3
      li . . .
    p Test and challenge files don’t contain the “emotion” column.
    p The details of the code of emotions are posted in each challenge site.
</template>
