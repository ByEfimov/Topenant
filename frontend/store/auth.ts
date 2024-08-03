import { defineStore } from 'pinia';
import { useChatStore } from './chat';
import type { IUser, IUserForm } from '~/interfaces/user';

interface IState {
    isAuthenticated: boolean;
    user: IUser | null;
}

export const useAuthStore = defineStore('auth', {
    state: (): IState => ({
        isAuthenticated: false,
        user: null,
    }),

    actions: {
        async registerUser() {
            const chatStore = useChatStore();
            const { $api } = useNuxtApp();

            const userResponse = await $api<IUser>(`/auth/users/`, {
                method: 'POST',
                body: chatStore.formData,
            });
            const jwtResponse = await $api('/auth/jwt/create/', {
                method: 'POST',
                body: chatStore.formData,
            });
            localStorage.setItem('tokens', JSON.stringify(jwtResponse));
            this.user = userResponse;
            this.isAuthenticated = true;
        },
        async loginUser(formData: IUserForm) {
            const { $api } = useNuxtApp();

            const jwtResponse = await $api('/auth/jwt/create/', {
                method: 'POST',
                body: formData,
            });

            if (jwtResponse) {
                localStorage.setItem('tokens', JSON.stringify(jwtResponse));
                this.user = await $api('/auth/users/me/');
                this.isAuthenticated = true;
            }
        },
        async me() {
            const { $api } = useNuxtApp();

            if (
                localStorage.getItem('tokens') &&
                JSON.parse(localStorage.getItem('tokens') || '').access
            ) {
                await $api('/auth/jwt/verify/', {
                    method: 'POST',
                    body: {
                        token: JSON.parse(localStorage.getItem('tokens') || '')
                            .access,
                    },
                })
                    .catch(async () => {
                        const refreshResponse = await $api<Object>(
                            '/auth/jwt/refresh/',
                            {
                                method: 'POST',
                                body: {
                                    refresh: JSON.parse(
                                        localStorage.getItem('tokens') || ''
                                    ).refresh,
                                },
                            }
                        );
                        localStorage.setItem(
                            'tokens',
                            JSON.stringify({
                                ...refreshResponse,
                                refresh: JSON.parse(
                                    localStorage.getItem('tokens') || ''
                                ).refresh,
                            })
                        );
                        this.user = await $api<IUser>('/auth/users/me/');
                        this.isAuthenticated = true;
                    })
                    .then(async () => {
                        this.user = await $api<IUser>('/auth/users/me/');
                        this.isAuthenticated = true;
                    });
            }
        },
    },
});
