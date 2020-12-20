<template lang="pug">
div
  section
    h1.title.is-2 {{ challenge.name }}
    .columns
      .column 
        p.subtitle Train your model locally using "train" and "validation". Then download the "test" set and compare your model with other researchers. Finally, use "challenge" to compete on an unbiased way. ( The challenge results will be publish after: 02/02/2021 )
        table.table.is-fullwidth.is-striped
          thead
            tr
              th Título
              th Dataset URL
          tbody 
            tr 
              td Train ( audios and labels)
              td 
                a(:href='challenge.train') Download
            tr 
              td Validation ( audios and labels)
              td 
                a(:href='challenge.val') Download
            tr 
              td Test ( audios )
              td 
                a(:href='challenge.test') Download
            tr 
              td Challenge ( audios )
              td 
                a(:href='challenge.challenge') Download

      .column(v-if='this.$auth.loggedIn')
        p.subtitle Here you can send your results: Select between Test ( public ) or Challenge ( private even for you until deadline)
        .field
          .control
          label.label Nombre de Modelo
          input.input.is-primary(type='text', v-model='result.name')
        .field
          .control 
            .select.is-primary
              select(v-model='result.mode')
                option(value='test') Test
                option(value='challenge') Challenge

        .file.has-name.is-boxed.is-warning.is-medium.is-centered
          label.file-label
            input.file-input(type='file', @change='preview')
            span.file-cta
              span.file-icon
                span.material-icons cloud_upload
              span.file-label Choose a file (.csv)
            span.file-name(v-if='this.file') {{ this.file.name }}

        br 
        center
          button.button.is-dark(@click='enviar_file()') Enviar

        p(v-if='enviando') Estamos cargando los resultados.
    br 
    br 
    br
    div(v-if='this.$auth.loggedIn')
      p.subtitle Your Results

      table.table.is-fullwidth.is-bordered
        thead
          tr
            th Model Name
            th Accuracy
            th Date
            th tipo ( test, challenge)
        tbody(v-for='result in results')
          tr 
            td {{ result.name }}
            td {{ result.metrics.find((m) => m.name === "accuracy") && result.metrics.find((m) => m.name === "accuracy").result }}
            td {{ result.updatedAt }}
            td {{ result.mode }}

    div(v-else)
      p.is-size-4
        NuxtLink(to='/login') Login
        span to Send and check your results and submissions
</template>

<script>
import axios from '~/plugins/axios'
export default {
  layout: 'default',
  async fetch() {
    const callresp = axios.get('/challenges/' + this.$route.params.id)

    // console.log(this.challenge)
    const callrespResults = axios.get(
      '/challenges/' + this.$route.params.id + '/me',
      {
        headers: {
          Authorization: this.$auth.strategy.token.get(),
        },
      }
    )

    const resp = await callresp
    const respResults = await callrespResults

    this.challenge = await resp.data
    this.results = await respResults.data.results.sort(
      (a, b) => new Date(b.updatedAt) - new Date(a.updatedAt)
    )
  },
  data() {
    return {
      results: '',
      file: undefined,
      challenge: {},
      enviando: false,
      result: {
        mode: 'test',
        name: 'Model CNN',
      },
    }
  },
  methods: {
    preview(event) {
      console.log(event.target.files[0])
      this.file = event.target.files[0]
    },
    async enviar_file() {
      this.enviando = true
      const formData = new FormData()
      formData.append('file', this.file)
      formData.append('id', this.$route.params.id)
      formData.append('result', JSON.stringify(this.result))

      const resp = await axios({
        url: '/challenges',
        method: 'post',
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: this.$auth.$storage.getUniversal('_token.local'),
        },
      })
      console.log(resp.data)

      // console.log(this.challenge)
      const respResults = await axios.get(
        '/challenges/' + this.$route.params.id + '/me',
        {
          headers: {
            Authorization: this.$auth.strategy.token.get(),
          },
        }
      )

      this.results.splice(0, this.results.length)
      for (const res of respResults.data.results.sort(
        (a, b) => new Date(b.updatedAt) - new Date(a.updatedAt)
      )) {
        this.results.push(res)
      }
      this.enviando = false
    },
  },
}
</script>
