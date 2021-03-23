export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'SER Challenge | Kusisqa',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.jpg' },
      // {rel:"stylesheet",href:"https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css"},
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/icon?family=Material+Icons',
      },
      {
        rel:"preconnect",
        href:"https://fonts.gstatic.com"
      },
      {
        href:"https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Roboto:wght@400;700&display=swap",
        rel:"stylesheet"
      }
    ],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: ['@/assets/sass/main.sass'],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [],

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

  target: 'static',
 

  server: {
    port: 3001,
  },
}
