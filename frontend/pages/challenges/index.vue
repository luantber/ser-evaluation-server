<template lang="pug">
    div
        h1 Challenges 
        
        ul(v-for="(challenge, index) in $store.state.challenges")
            li 
              Nuxt-link(:to="'/challenges/'+challenge.id")
                p {{challenge.id }}
        
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {}
  },
  created() {},
  methods: {
    ...mapActions('challenges', ['getAll']),
  },
  async fetch() {
    await this.getAll()
  },
}
</script>
