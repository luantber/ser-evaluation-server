<template lang="pug">
div
  .navbarfull
    .navbarfull__logo
      NuxtLink(to='/')
        img(src='~static/logo_final.png')

    .navbarfull___item 
      NuxtLink(to='/') Datasets

    //- template(v-if='this.$auth.loggedIn')
    //-   .navbarfull___item Your Submissions

    //-   .navbarfull___item
    //-     Logout

    //- template(v-else)
    //-   .navbarfull___item
    //-     NuxtLink(to='/login') Login

    .navbarfull___item
      NuxtLink(to='/')
        button.boton Register

      //- .navbarfull___item
      //-     span.material-icons.navbarfull__store person

  .navbarmov
    .navbarmov__logo
      NuxtLink(to='/')
        img(src='~static/logo_final.png')

    .navbarmov__item
      span.material-icons(@click='barra()') {{ boton }}

  .menumov(v-if='boton !== "menu"')
    .menumov___item Datasets
    //- .menumov___item Your Submission
    .menumov___item Registerw
    //- .menumov___item Login 
    //- .menumov___item
    //-   span.material-icons.navbarmov__store persone
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
