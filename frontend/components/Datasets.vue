<template lang="pug">
.estructura.padding5
  img(src='~static/puntos.png', alt="icon")
  h2.section-title Datasets
  section.estructura__derecha.datasets
    .datasets__contenedor
      //- Ravdess 48000 1441 Files ,  4576 secs 76.27 mins 1.27 hours
      //- IEMOCAP 16khz 10039 Files , 39804 secs 663.4 mins 11.06 hours
      //- Kusisqa 48khz 5141 Files ,  28146 secs 469.1 mins 7.82 hours

      .datasets__contenedor__caja 
        p.datasets__contenedor__caja__title Kusisqa Dataset
        p.datasets__contenedor__caja__datos + 5141 files
        p.datasets__contenedor__caja__datos + 7.82 hours of audio
      .datasets__contenedor__caja 
        p.datasets__contenedor__caja__title IEMOCAP
        p.datasets__contenedor__caja__datos + 10039 files
        p.datasets__contenedor__caja__datos + 11.06 hours of audio
      .datasets__contenedor__caja 
        p.datasets__contenedor__caja__title RAVDESS
        p.datasets__contenedor__caja__datos + 1441 files
        p.datasets__contenedor__caja__datos + 1.27 hour of audio

    h4 Datasets format:
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
    p The audios are .wav files with a sampling rate of 48khz (  IEMOCAP 16khz ) and mono channel. The “file.csv”, is the list of files and the labels in a CSV format, using the following format:
    ul 
      li file,emotion
      li 1009.wav,4
      li 1010.wav,3
      li . . .  
    p Test and challenge files don’t contain the “emotion” column.
    p The details of the code of emotions are posted in each challenge site.
</template>
