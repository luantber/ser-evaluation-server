<template lang="pug">
.estructura.padding5
  img(src='~static/puntos.png')
  h2.section-title What is SER challenge
  section.whatis.estructura__derecha
    p Speech Emotion Recognition challenge ( SER Challenge ) is designed to push the state of the art in this area, allowing researchers to fairly and easily compare results. This challenge is based on some well known datasets.
    p For each dataset, you will have to train a Machine Learning / Deep Learning model to predict emotions from an audio file. You can send your results and our system will provide you the metrics on a leaderboard.
    p Each dataset has been splitted in:
    ul 
      li Train
      li Validation
      li Test
      li Challenge
    p Train and development, contain audio files and its respectively labels. Those should be used for training and local testing. Test and challenge, contain audios only. In order to get the score of your predictions you will need to send it to the system. Challenge results will be released after the Deadline.
</template>
