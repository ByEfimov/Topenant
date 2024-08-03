<template>
    <div class="content">
        <Company v-for="company in data" :key="company.id" :company="company" />
    </div>
</template>

<script setup lang="ts">
import { useCompanyStore } from '~/store/company';

const companyStore = useCompanyStore();
const { data } = useAsyncData(async () => {
    return await companyStore.getCompanies();
});
console.log(data);
</script>

<style lang="scss" scoped>
@import url('@/assets/styles/pages/index.scss');
</style>
