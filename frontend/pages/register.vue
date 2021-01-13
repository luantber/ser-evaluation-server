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
    .field
      label.label Repeat Password Password
      .control
        input.input(
          type='password',
          placeholder='password',
          required,
          name='password',
          v-model='user.passwordR'
        )
    center
      button.button.is-link(@click.prevent='register()') Register

  div(v-if='errors.length !== 0')
    ul
    template(v-for='error in errors')
      li {{ error }}
</template>

<script>
import axios from '~/plugins/axios'
export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: '',
        passwordR: '',
      },
      errors: [],
    }
  },

  methods: {
    async register() {
      this.errors = []
      // console.log('Apo')
      if (this.user.password !== this.user.passwordR) {
        this.errors.push('Las contraseñas no coinciden')
        return
      }

      try {
        await axios.post('/signup', {
          email: this.user.email,
          username: this.user.username,
          password: this.user.password,
        })

        await this.$auth.login({
          data: { email: this.user.email, password: this.user.password },
        })
      } catch (error) {
        this.errors.push(error.response.data.txt)
        console.log('name', error.response)
      }
    },
  },
}
</script>
