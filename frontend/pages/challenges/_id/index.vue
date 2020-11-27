<template lang="pug">
    div
      div(v-if="error")
        h3 Not FOUND
      div(v-else)
        template(v-if="challenge")
          h3.title {{ this.challenge.name}}
          VueShowdown(:markdown="challenge.description" :options="{ emoji: true }") 
          NuxtLink(:to="$route.path +'/participate'")
            button.button.is-link.is-light Send your results 
              
          br
          br
          div.subtitle Results
              table.table.is-fullwidth.is-bordered
                  thead
                      tr
                          th Título
                          th Dataset
                  tbody 
                      tr 
                          td hola
                          td hola 2
                  tbody 
                      tr 
                          td hola
                          td hola 2
                  tbody 
                      tr 
                          td fila 2
                          td fila 2

        
</template>

<script>
import axios from 'axios'
export default {
  layout: 'default',
  data() {
    return {
      challenge: '',
      error: '',
    }
  },
  async fetch() {
    // console.log('/challenges/' + this.$route.params.id)
    const resp = await axios.get(
      'http://localhost:1337/challenges/' + this.$route.params.id
    )
    // console.log(resp.data)
    this.challenge = resp.data
    // } catch (error) {
    //   this.error = error
    // }
  },
}
</script>
