<template lang="pug">
    div
        
        section
            h1.title.is-2 Ravdess Challenge 
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
                                    a(:href="challenge.train") Download
                            tr 
                                td Validation ( audios and labels) 
                                td 
                                    a(:href="challenge.val") Download
                            tr 
                                td Test ( audios ) 
                                td 
                                    a(:href="challenge.test") Download
                            tr 
                                td Challenge ( audios ) 
                                td 
                                    a(:href="challenge.challenge") Download

                .column(v-if="this.$auth.loggedIn")
                    p.subtitle Here you can send your results: Select between Test ( public ) or Challenge ( private even for you until deadline)
                    div.field
                        .control 
                            center
                                .select.is-primary
                                    select 
                                        option Test 
                                        option Challenge
                    
                    .file.has-name.is-boxed.is-warning.is-medium.is-centered
                        label.file-label
                            input(class="file-input" type="file" @change="preview")
                            span.file-cta
                                span.file-icon
                                    span.material-icons cloud_upload
                                span.file-label Choose a file (.csv)
                            span.file-name(v-if="this.file") {{this.file.name}}
                
                                        
    
                    br 
                    center
                        button.button.is-dark(@click="enviar_file()") Enviar
            br 
            br 
            br
            div(v-if="this.$auth.loggedIn")
                p.subtitle Your Results
                
                table.table.is-fullwidth.is-bordered
                  thead
                      tr
                          th Model Name
                          th Accuracy
                          th Date 
                  tbody(v-for="result in challenge.results")
                      tr 
                          td {{result.name}}
                          td {{result.metrics.accuracy}}
                          td {{result.created_at}}
            div(v-else)
                p.is-size-4
                    NuxtLink(to="/login") Login 
                    span to Send and check your results and submissions

</template>

<script>
import axios from 'axios'
export default {
  layout: 'default',
  data() {
    return {
      challenge: '',
      results: '',
      file: undefined,
    }
  },
  methods: {
    preview(event) {
      console.log(event.target.files[0])
      this.file = event.target.files[0]
    },
    async enviar_file() {
      const formData = new FormData()
      formData.append('file', this.file)
      formData.append('data', JSON.stringify({ algo: 3 }))

      const resp = await axios({
        url: 'http://localhost:1337/results',
        method: 'post',
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: this.$auth.$storage.getUniversal('_token.local'),
        },
      })
      console.log(resp.data)
    },
  },
  async fetch() {
    const resp = await axios.get(
      'http://localhost:1337/challenges/' + this.$route.params.id
    )
    const respResults = await axios.get(
      'http://localhost:1337/results?user=' + this.$auth.user.id
    )
    this.challenge = resp.data
    this.results = respResults.data
  },
}
</script>
