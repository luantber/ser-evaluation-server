<template lang="pug">
    div
      div(v-if="error")
        h3 Not FOUND
      div(v-else)
        h3 Challenge: {{ this.challenge.name}}
        div {{ this.challenge.description}}
        //- div {{ this.challenge }}

        h4 Envía tus resultados:
        
        form
          input(type="file")
          button(type="submit")

        
</template>

<script>
export default {
  data() {
    return {
      challenge: '',
      error: '',
    }
  },
  async fetch() {
    try {
      this.challenge = await this.$strapi.$challenges.findOne(
        this.$route.params.id
      )
    } catch (error) {
      this.error = error
    }
  },
}
</script>
