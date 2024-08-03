// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2024-04-03',
    devtools: { enabled: false },
    runtimeConfig: {
        public: {
            apiUrl: process.env.NUXT_PUBLIC_API_URL || 'http://localhost/',
        },
    },
    vue: {
        propsDestructure: true,
    },
    app: {
        pageTransition: {
            name: 'fade',
            mode: 'out-in', // default
        },
    },
    css: [
        '~/assets/styles/utility/_normalize.scss',
        '~/assets/styles/app.scss',
    ],
    modules: [
        '@nuxtjs/eslint-module',
        '@pinia/nuxt',
        '@vueuse/nuxt',
        'nuxt-icons',
        '@nuxt/image',
        '@vueuse/motion/nuxt',
    ],
    ssr: false,
});
