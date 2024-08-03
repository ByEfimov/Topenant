import { defineStore } from 'pinia';
import { useAuthStore } from './auth';
import type { ICompany } from '~/interfaces/company';

interface IState {
    companies: ICompany[];
}

export const useCompanyStore = defineStore('company', {
    state: (): IState => ({
        companies: [],
    }),

    actions: {
        async getCompanies() {
            const { $api } = useNuxtApp();
            const authStore = useAuthStore();
            const worksResponse = await $api<ICompany[]>(
                `/company/?employer__in=${authStore.user?.id}`
            );
            this.companies = worksResponse;
            return worksResponse;
        },
    },
});
