<template lang="pug">
    div
        h1.title.is-2 Challenges
        p Currently we're supporting the following datasets:         
        
        .content
          ul(v-for="(challenge, index) in challenges")
            li 
              Nuxt-link(:to="'/challenges/'+challenge._id")
                p {{challenge.name}}
</template>

<script>
export default {
  data() {
    return {
      challenges: [],
    }
  },

  

  async fetch() {
    const challengesRes = await this.$axios.$get('/challenges')

    this.challenges = challengesRes
  },
}
</script>
