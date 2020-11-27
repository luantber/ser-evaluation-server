<template lang="pug">
    div
        div.title(v-if="this.$auth.loggedIn") 
          p Usuario Logeado
          Logout
        template(v-else)
          h1 Login
          form.container-small
            .field
              input.input(type="email" required v-model="loginData.identifier")
            .field
              input.input(type="password" required v-model="loginData.password")
            center
              button.button.is-link(@click.prevent="login()" type="button") Login
</template>

<script>
export default {
  data() {
    return {
      loginData: {
        identifier: 'test@mail.com',
        password: 'testtest',
      },
    }
  },

  methods: {
    async login() {
      const resp = await this.$auth.login({ data: this.loginData })
      this.$auth.setUser(resp.data.user)
    },
  },
}
</script>
