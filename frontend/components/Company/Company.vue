<template>
    <div class="company">
        <div class="header">
            <div class="image"><img :src="company.image" alt="" /></div>
            <p class="title">{{ company.name }}</p>
        </div>
        <div class="works">
            <Work v-for="work in company.works" :key="work.id" :work="work" />
        </div>
    </div>
</template>

<script setup lang="ts">
import type { ICompany } from '~/interfaces/company';

interface IProps {
    company: ICompany;
}

const { company } = defineProps<IProps>();
</script>

<style scoped lang="scss">
@import url('./company.scss');
</style>
