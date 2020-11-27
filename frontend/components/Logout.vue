<template lang="pug">
    div
        button.button.is-link(@click="logout()") Logout
</template>

<script>
export default {
  methods: {
    async logout() {
      await this.$auth.reset()
    },
  },
}
</script>
