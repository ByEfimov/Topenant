import { defineStore } from 'pinia';
import type {
    ISendTicket,
    ITicket,
    IWork,
    TTicketStatuses,
} from '~/interfaces/works';

interface IState {
    works: IWork[];
    approvedTicket: ITicket | null;
}

export const useWorksStore = defineStore('works', {
    state: (): IState => ({
        works: [],
        approvedTicket: null,
    }),

    actions: {
        async getWorks() {
            const { $api } = useNuxtApp();
            const worksResponse = await $api<IWork[]>('/works/');
            this.works = worksResponse;
            return worksResponse;
        },
        async sendTicket(data: ISendTicket) {
            const { $api } = useNuxtApp();
            const ticketResponse = await $api<ITicket>('/tickets/', {
                method: 'POST',
                body: data,
            });

            return ticketResponse;
        },
        async getTickets(work: number) {
            const { $api } = useNuxtApp();
            const ticketsResponse = await $api<ITicket[]>(
                `/tickets/?work__in=${work}`
            );
            return ticketsResponse;
        },
        async getTicketsByUser(user?: number) {
            const { $api } = useNuxtApp();
            const ticketsResponse = await $api<ITicket[]>(
                `/tickets/?applicant__in=${user}&status__in=approved`
            );
            this.approvedTicket = ticketsResponse[0];
            return ticketsResponse;
        },
        async addPoint(work: number, data: { user_id: number }) {
            const { $api } = useNuxtApp();
            const ticketResponse = await $api<ITicket[]>(
                `/works/${work}/give-points/`,
                {
                    method: 'POST',
                    body: data,
                }
            );
            return ticketResponse;
        },
        async changeTicket(ticket: number, data: { status: TTicketStatuses }) {
            const { $api } = useNuxtApp();
            const ticketResponse = await $api<ITicket[]>(
                `/tickets/${ticket}/`,
                {
                    method: 'PATCH',
                    body: data,
                }
            );
            return ticketResponse;
        },
    },
});
