<template lang="pug">
    div
        h1 Register
        form
            input(type="text" required v-model="user.username")
            input(type="email" required v-model="user.email")
            input(type="password" required v-model="user.password")
            button(@click.prevent="register()") Register
        div(v-if="error") Error {{ error.name }}
</template>

<script>
export default {
  data() {
    return {
      algo: 'asd',
      user: {
        username: '',
        email: '',
        password: '',
      },
      error: null,
    }
  },

  methods: {
    async register() {
      console.log('Apo')
      try {
        await this.$strapi.register({
          email: this.user.email,
          username: this.user.username,
          password: this.user.password,
        })

        this.$router.push('/')
      } catch (error) {
        this.error = error
        console.log('name', error)
      }
    },
  },
}
</script>
