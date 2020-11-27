<template lang="pug">
    div
        .navbarfull
            .navbarfull__logo
                img(src="~static/logo.png")
            .navbarfull___item
              NuxtLink(to="/") Index
            .navbarfull___item 
              NuxtLink(to="/challenges") Challenges
            .navbarfull___item Your Submissions
            //- .navbarfull___item Register
            //- .navbarfull___item Login
            .navbarfull___item
                span.material-icons.navbarfull__store person

        .navbarmov
            .navbarmov__logo
                img(src="~static/logo.png")
            .navbarmov__item
                span.material-icons(@click="barra()") {{boton}}
        
        .menumov(v-if="boton!=='menu'")
            .menumov___item
              NuxtLink(to="/") Index
            .menumov___item Challenges
            .menumov___item Your Submission
            //- .menumov___item Register
            //- .menumov___item Login 
            .menumov___item
                span.material-icons.navbarmov__store persone

</template>

<script>
export default {
  data() {
    return {
      boton: 'menu',
    }
  },
  methods: {
    barra() {
      this.boton = this.boton === 'menu' ? 'clear' : 'menu'
      console.log(this.boton)
    },
  },
}
</script>
