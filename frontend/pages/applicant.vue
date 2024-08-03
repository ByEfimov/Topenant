<template>
    <div v-if="!approvedTicket" class="content">
        <Work v-for="work in data" :key="work.id" :work="work" />
    </div>
    <div v-else class="content">
        <Work :work="approvedTicket.work" />
        <div class="centerText">
            Через {{ approvedTicket.work.timeToJob }} часов ты получишь от
            работодателя {{ approvedTicket.work.pointsToGive }} очков!
        </div>
        <div>Сейчас у тебя: {{ user?.points || 0 }} очков, ты на 1 месте</div>
    </div>
</template>

<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { useAuthStore } from '~/store/auth';
import { useWorksStore } from '~/store/works';

const worksStore = useWorksStore();
const { approvedTicket } = storeToRefs(worksStore);
const authStore = useAuthStore();
const { user } = storeToRefs(authStore);
const { data } = useAsyncData(async () => {
    if (!approvedTicket.value) {
        return await worksStore.getWorks();
    }
});
</script>

<style lang="scss" scoped>
@import url('@/assets/styles/pages/index.scss');
</style>
