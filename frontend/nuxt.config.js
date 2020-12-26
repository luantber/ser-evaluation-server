export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'SER Challenge',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      // {rel:"stylesheet",href:"https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css"},
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/icon?family=Material+Icons',
      },
    ],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: ['@/assets/sass/main.sass'],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [{ src: '~plugins/showdown.js' }],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
  ],
  env: {
    baseUrl: process.env.BASE_URL_API || 'http://localhost:1337',
  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  // axios: {
  //   baseURL: 'http://localhost:1337',
  // },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},

  auth: {
    redirect: {
      login: '/login',
      logout: '/',
      callback: false,
      home: '/challenges',
    },
    strategies: {
      local: {
        endpoints: {
          login: {
            url: process.env.BASE_URL_API + '/login',
            method: 'post',
            propertyName: 'token',
          },
          // logout: { url: '/api/auth/logout', method: 'post' },
          logout: false,
          // user: false,
          user: {
            url: process.env.BASE_URL_API + '/users/me',
            method: 'get',
            propertyName: false,
          },
        },
        autoFetchUser: true,
      },
    },
  },

  server: {
    port: 3001,
  },
}
