export const state = () => []

export const mutations = {
  add(state, title) {
    state.push(title)
  },
}

export const actions = {
  async getAll({ commit }) {
    const challenges = await this.$strapi.$challenges.find()
    // console.log(challenges)
    challenges.forEach((element) => {
      // console.log(element)
      commit('add', element)
    })
  },
}
