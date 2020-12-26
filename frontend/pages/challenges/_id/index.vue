<template lang="pug">
div
  div(v-if='error')
    h3 Not FOUND
  div(v-else)
    template(v-if='challenge')
      h3.title {{ this.challenge.name }}
      VueShowdown(
        :markdown='challenge.description',
        :options='{ emoji: true }'
      ) 
      NuxtLink(:to='$route.path + "/participate"')
        button.button.is-link.is-light Send your results

      br
      br
      .subtitle Results
        table.table.is-fullwidth.is-bordered
          thead
            tr
              th Username
              th Model Name
              th Accuracy
              th Date
          tbody(v-for='result in challenge.results')
            tr 
              td {{ result.user.username }}
              td {{ result.name }}
              td {{ result.metrics.find((m) => m.name === "accuracy") && result.metrics.find((m) => m.name === "accuracy").result }}
              td {{ result.updatedAt }}
</template>

<script>
import axios from '~/plugins/axios'
export default {
  layout: 'default',
  async fetch() {
    const resp = await axios.get('/challenges/' + this.$route.params.id)
    this.challenge = resp.data
    this.challenge.results = this.challenge.results.sort(
      (a, b) => new Date(b.updatedAt) - new Date(a.updatedAt)
    )
  },
  data() {
    return {
      challenge: '',
      error: '',
    }
  },
}
</script>
