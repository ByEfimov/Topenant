<template>
    <div></div>
</template>
<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useAuthStore } from '~/store/auth';

const authStore = useAuthStore();
const { isAuthenticated, user } = storeToRefs(authStore);
const router = useRouter();

onMounted(() => {
    if (!isAuthenticated.value) {
        router.push('/login');
    }
    if (user.value?.role === 'applicant') {
        router.push('/applicant');
    }
    if (user.value?.role === 'employer') {
        router.push('/employer');
    }
});
</script>
