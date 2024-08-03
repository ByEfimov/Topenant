import { useAuthStore } from '~/store/auth';
import { useWorksStore } from '~/store/works';

export default defineNuxtPlugin(async () => {
    if (process.server) {
        return;
    }
    const authStore = useAuthStore();
    const workStore = useWorksStore();
    await authStore.me();
    await workStore.getTicketsByUser(authStore.user?.id);
});
