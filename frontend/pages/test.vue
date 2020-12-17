<template lang="pug">
div Hola mundito {{ this.algo }}
</template>

<script>
export default {
  async fetch() {
    this.algo = await fetch('htttp:api/algo')
  },
  created() {},
}
</script>
