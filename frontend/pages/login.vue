<template lang="pug">
div
  .title(v-if='this.$auth.loggedIn') 
    p Usuario Logeado
    Logout
  template(v-else)
    form.container-small
      .field
        .label Email

        input.input(
          type='email',
          placeholder='email',
          required,
          name='email',
          v-model='loginData.email'
        )
      .field
        .label Password

        input.input(
          type='password',
          placeholder='password',
          required,
          name='password',
          v-model='loginData.password'
        )
      center
        button.button.is-link(@click.prevent='login()', type='button') Login

    p
      ul.has-text-danger(v-for='error in errores')
        li {{ error }}
    p If you don't have an account.
      NuxtLink(to='/register') Register
</template>

<script>
export default {
  data() {
    return {
      loginData: {
        email: '',
        password: '',
      },
      errores: [],
    }
  },

  methods: {
    async login() {
      try {
        await this.$auth.login({ data: this.loginData })
      } catch (error) {
        console.log(error)
        this.errores = []
        this.errores.push('User or pass wrong')
      }

      // this.$auth.setUser(resp.data.user)
    },
  },
}
</script>
