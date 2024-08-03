export default defineNuxtPlugin(() => {
    const config = useRuntimeConfig();

    if (process.server) {
        return;
    }
    const $api = $fetch.create({
        baseURL: config.public.apiUrl,
        timeout: 15000,
        headers: {
            Authorization: localStorage.getItem('tokens')
                ? `Bearer ${JSON.parse(localStorage.getItem('tokens') || '').access}`
                : '',
        },
    });

    return {
        provide: {
            api: $api,
        },
    };
});
