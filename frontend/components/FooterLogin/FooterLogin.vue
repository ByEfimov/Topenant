<template>
    <footer
        v-motion
        class="footer"
        :delay="100"
        :clearable="false"
        :filterable="false"
        :autoscroll="false"
        :clear-search-on-select="false"
        :search="false"
        :initial="{
            opacity: 0,
        }"
        :enter="{
            opacity: 1,
        }"
    >
        <form @submit.prevent="sendMessage">
            <input
                v-if="
                    configure?.type !== 'select' && configure?.type !== 'phone'
                "
                v-model="typingText"
                :type="configure?.type === 'email' ? 'email' : 'text'"
                placeholder="Введи текст..."
                class="input"
                @input="chatStore.changeTypingText(typingText)"
            />
            <input
                v-if="configure?.type === 'phone'"
                v-model="typingText"
                v-maska="'+7 (###) ###-##-##'"
                placeholder="Введи текст..."
                class="input"
                @input="chatStore.changeTypingText(typingText)"
            />
            <vSelect
                v-else-if="configure?.type === 'select'"
                v-model="selectValue"
                :options="configure?.values"
            >
            </vSelect>

            <button type="submit">
                <NuxtIcon
                    name="send"
                    :class="[
                        'send',
                        { active: typingText.length > 0 || selectValue?.value },
                    ]"
                />
            </button>
        </form>
    </footer>
</template>

<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import vSelect from 'vue-select';
import { useAuthStore } from '~/store/auth';
import { useChatStore } from '~/store/chat';
import { loginMessages } from '~/static/chats';

const chatStore = useChatStore();
const authStore = useAuthStore();
const { typingText, formData, configure } = storeToRefs(chatStore);
const router = useRouter();
const selectValue = ref();

// REMAKE < time

const sendMessage = () => {
    const { name, role, email, phone, password } = formData.value;

    console.log(selectValue.value);
    if (!name) {
        chatStore.sendMessage('role', loginMessages.role, () => {}, {
            type: 'select',
            values: [
                { value: 'employer', label: 'Работодатель' },
                { value: 'applicant', label: 'Рабочий' },
            ],
        });
        return;
    } else if (!role) {
        chatStore.sendMessage(
            'email',
            loginMessages.email,
            () => {},
            {
                type: 'email',
            },
            selectValue.value
        );
        return;
    } else if (!email) {
        chatStore.sendMessage('phone', loginMessages.phone, () => {}, {
            type: 'phone',
        });
        return;
    } else if (!phone) {
        chatStore.sendMessage('password', loginMessages.password, () => {}, {
            type: 'input',
        });
        return;
    }

    if (!password) {
        chatStore.sendMessage(null, loginMessages.welcome, async () => {
            await authStore.registerUser();
            router.push('/');
        });
        return;
    }
};
</script>

<style scoped lang="scss">
@import url('./footer.scss');
</style>
