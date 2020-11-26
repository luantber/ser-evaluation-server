<template lang="pug">
    div
        h1 Login
        div(v-if="this.$strapi.user") Usuario Logeado
        form
            
            input(type="email" required v-model="user.email")
            input(type="password" required v-model="user.password")
            button(@click.prevent="login()" type="button") Register
</template>

<script>
export default {
  data() {
    return {
      user: {
        email: '',
        password: '',
      },
    }
  },

  methods: {
    async login() {
      try {
        await this.$strapi.login({
          identifier: this.user.email,
          password: this.user.password,
        })
      } catch (error) {
        console.log(error)
      }
    },
  },
}
</script>
