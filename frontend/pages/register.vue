<template lang="pug">
div
  center
    h1.title.is-2 Register
  form.container-small
    .field
      label.label Username
      .control
        input.input(
          type='text',
          placeholder='username',
          required,
          name='username',
          v-model='user.username'
        )

    .field
      label.label Email
      .control
        input.input(
          type='email',
          placeholder='email@algo.com',
          required,
          name='email',
          v-model='user.email'
        )
    .field
      label.label Password
      .control
        input.input(
          type='password',
          placeholder='password',
          required,
          name='password',
          v-model='user.password'
        )
    center
      button.button.is-link(@click.prevent='register()') Register

  div(v-if='error') Error {{ error.name }}
</template>

<script>
import axios from 'axios'
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
      // console.log('Apo')
      try {
        await axios.post('http://localhost:1337/signup', {
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
