<template lang="pug">
    div Hola mundito {{ this.algo }}
</template>

<script>
export default {
  created() {},

  async fetch() {
    this.algo = await fetch('htttp:api/algo')
  },
}
</script>
