<template lang="pug">
  div
    h1.title.is-1 Speech Emotion Recognition Challenge
    p.subtitle This website hosts some challenges, which you can participate in.
    h2.title.is-3 Features
    .content
      ul
        li Train your models 
        li Test your model 
        li Compare with others in the leaderboard
        li Compete in a challenge with a deadline 
        li 
          span Take a look 
          NuxtLink(to="/challenges") the current challenges 
    h2.title.is-3 How to Participate
    p Register in the website and download the dataset partitions:
    .content
      ul
        li Dataset Training / Evaluation
        li Test your model with the Test Audios
        li Check your score in the leaderboard
        li Send your results for the main challenge 
    h3.title.is-3 About us
    p Designed by Luis Bernal Chahuayo and Alvaro Cuno 
    p Speech Emotion Recognition  ( Kusisqa Project )

    img.index__explanation(src="~/static/tesis.png" )



</template>

<script>
export default {
  layout: 'default',
}
</script>
