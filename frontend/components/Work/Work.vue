<template>
    <div
        class="work"
        @click="user?.role === 'employer' ? (openCompanyModal = true) : ''"
    >
        <div class="image"><img :src="work.image" alt="" /></div>
        <div class="content">
            <p class="title">{{ work.title }}</p>
            <p class="description">{{ work.description }}</p>
            <p class="stats">
                <span>
                    Время:
                    <span class="highlight">{{ work.timeToJob }}</span>
                </span>
                <span>
                    Рейтинг:
                    <span class="highlight">{{ work.rating }}</span>
                </span>
                <span>
                    Поинты:
                    <span class="highlight">{{ work.pointsToGive }}</span>
                </span>
            </p>
            <button
                v-if="user?.role === 'applicant' && !approvedTicket"
                class="actions"
                @click="sendTicket"
            >
                {{ !ticket ? 'Хочу тут работать' : 'Вы уже откликнулись' }}
            </button>
        </div>
        <div
            v-if="openCompanyModal"
            class="modalUsers"
            @click.stop.prevent="openCompanyModal = false"
        >
            <div class="content" @click.stop.prevent="">
                <div v-for="ticket in tickets" :key="ticket.id">
                    <User :user="ticket.applicant" :ticket="ticket"></User>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { watch } from 'vue';
import type { ITicket, IWork } from '~/interfaces/works';
import { useAuthStore } from '~/store/auth';
import { useWorksStore } from '~/store/works';

interface IProps {
    work: IWork;
}

const authStore = useAuthStore();
const workStore = useWorksStore();
const { user } = storeToRefs(authStore);
const { approvedTicket } = storeToRefs(workStore);
const ticket = ref<ITicket | null>(null);
const tickets = ref<ITicket[]>([]);
const openCompanyModal = ref(false);

watch(openCompanyModal, async () => {
    if (openCompanyModal.value) {
        tickets.value = await workStore.getTickets(work.id);
    }
});

const sendTicket = async () => {
    if (user.value) {
        ticket.value = await workStore.sendTicket({
            status: 'waiting',
            work: work.id,
            applicant: user.value.id,
        });
    }
};

const { work } = defineProps<IProps>();
</script>

<style lang="scss" scoped>
@import url('./work.scss');
</style>
