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
              td {{ result.user.email }}
              td {{ result.name }}
              td {{ result.metrics.find((m) => m.name === "accuracy") && result.metrics.find((m) => m.name === "accuracy").result }}
              td {{ result.updatedAt }}
</template>

<script>
import axios from 'axios'
export default {
  layout: 'default',
  data() {
    return {
      challenge: '',
      error: '',
      users_challenge: [],
    }
  },

  methods: {
    username(id) {
      return this.users_challenge.find((user) => user._id === id).username
    },
  },
  async fetch() {
    // const respUsers = await axios.get(
    //   'http://localhost:1337/users?results.id=' + this.$route.params.id
    // )
    const resp = await axios.get(
      'http://localhost:1337/challenges/' + this.$route.params.id
    )

    // this.users_challenge = respUsers.data
    this.challenge = resp.data
  },
}
</script>
