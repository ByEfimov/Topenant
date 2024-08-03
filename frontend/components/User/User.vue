<template>
    <div class="user">
        <div class="icon"><NuxtIcon name="user" class="userIcon" /></div>
        <div class="content">
            <div class="title">{{ user.name }}</div>
            <div class="email">{{ user.email }}</div>
        </div>
        <button v-if="!isUserAccepted" @click="addUserToTicket">
            <NuxtIcon name="add" class="add" />
        </button>
        <button v-if="isUserAccepted && !isAddedPoints" @click="addPointToUser">
            <NuxtIcon name="gift" class="add" />
        </button>
    </div>
</template>

<script setup lang="ts">
import type { IUser } from '~/interfaces/user';
import type { ITicket } from '~/interfaces/works';
import { useWorksStore } from '~/store/works';

interface IProps {
    user: IUser;
    ticket: ITicket;
}

const { user, ticket } = defineProps<IProps>();
const isUserAccepted = ref(false);
const isAddedPoints = ref(false);

const worksStore = useWorksStore();

const addUserToTicket = async () => {
    await worksStore.changeTicket(ticket.id, { status: 'approved' });
    isUserAccepted.value = true;
};
const addPointToUser = async () => {
    await worksStore.addPoint(ticket.work.id, { user_id: user.id });
    isAddedPoints.value = true;
};
</script>

<style lang="scss" scoped>
@import url('./user.scss');
</style>
