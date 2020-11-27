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


                        
                        
                        //- tbody 
                        //-     tr.is-selected 
                        //-         td fila 2
                        //-         td fila 2
                .column
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
                            input(class="file-input" type="file" name="resume")
                            span.file-cta
                                span.file-icon
                                    span.material-icons cloud_upload
                                span.file-label Choose a file (.csv)
                    br 
                    center
                        button.button.is-dark Enviar
            br 
            br 
            br 
            p.subtitle Your Results
            
            table.table.is-fullwidth.is-bordered
                thead
                    tr
                        th Título
                        th Dataset URL
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
    }
  },
  async fetch() {
    const resp = await axios.get(
      'http://localhost:1337/challenges/' + this.$route.params.id
    )
    this.challenge = resp.data
  },
}
</script>
