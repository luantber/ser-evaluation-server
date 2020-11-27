<template lang="pug">
    div
        Navbar
        section

            h1.title.is-2 Título de esta página
            .columns
                .column 
                    p.subtitle Explicación de esta tabla
                    table.table.is-fullwidth.is-striped
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
                            tr.is-selected 
                                td fila 2
                                td fila 2
                .column
                    p.subtitle Esplicación de este pedazo
                    div.field
                        .control 
                            center
                                .select.is-primary
                                    select 
                                        option Select your 
                                        option Opción 2
                    .file.has-name.is-boxed.is-warning.is-medium.is-centered
                        label.file-label
                            input(class="file-input" type="file" name="resume")
                            span.file-cta
                                span.file-icon
                                    span.material-icons cloud_upload
                                span.file-label Choose a file (.json)
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
