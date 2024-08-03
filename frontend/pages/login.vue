<template>
    <div class="content">
        <div
            v-for="massage in massages"
            :key="massage.content"
            v-motion
            :class="[
                'comment',
                {
                    authorIsCurrentUser:
                        massage.author === 'Я' || massage.author === user?.name,
                },
            ]"
            :initial="{
                opacity: 0,
                y: 50,
            }"
            :enter="{
                opacity: 1,
                y: 0,
                transition: { delay: massage.delay },
            }"
        >
            <div class="author">{{ massage.author }}</div>

            <VueWriter
                v-if="massage.author !== 'Я' && massage.author !== user?.name"
                :type-speed="30"
                :iterations="1"
                :start="massage.delay"
                :array="[massage.content]"
            />
            <p v-else>{{ massage.content }}</p>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { VueWriter } from 'vue-writer';
import { useAuthStore } from '../store/auth';

import { useChatStore } from '~/store/chat';

const chatStore = useChatStore();
const authStore = useAuthStore();
const { user, isAuthenticated } = storeToRefs(authStore);
const { massages } = storeToRefs(chatStore);

const router = useRouter();

onMounted(() => {
    if (isAuthenticated.value) {
        router.push('/');
    }
});

definePageMeta({
    layout: 'login',
});
</script>

<style lang="scss">
@import url('@/assets/styles/pages/login.scss');
</style>
