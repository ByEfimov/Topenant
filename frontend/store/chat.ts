import { defineStore } from 'pinia';
import { useAuthStore } from './auth';
import type { IMessage } from '~/interfaces/chat';
import { welcomeMessages } from '~/static/chats';

interface IConfigure {
    type: 'input' | 'select' | 'phone' | 'email';
    values?: { value: string; label: string }[];
}

interface IState {
    massages: IMessage[];
    formData: Record<string, any>;
    currentInput: string;
    typingText: string;
    configure: IConfigure | null;
}

export const useChatStore = defineStore('chat', {
    state: (): IState => ({
        typingText: '',
        massages: welcomeMessages,
        currentInput: 'name',
        formData: {},
        configure: null,
    }),

    actions: {
        changeTypingText(newValue: string) {
            this.typingText = newValue;
        },
        sendMessage(
            nextInput: string | null,
            nextMassage?: IMessage,
            action?: () => void,
            configure?: IConfigure,
            customValue?: { value: string; label: string }
        ) {
            console.log(customValue);
            if (customValue?.value || this.typingText) {
                const authSore = useAuthStore();
                this.formData[this.currentInput] =
                    customValue?.value || this.typingText;
                this.massages.push({
                    author: authSore.user?.name || 'Я',
                    content: customValue?.label || this.typingText,
                    delay: 0,
                });
                if (nextInput) {
                    this.currentInput = nextInput;
                }
                if (configure) {
                    this.configure = configure;
                }
                this.typingText = '';

                if (nextMassage) {
                    this.massages.push(nextMassage);
                }
            }
            action && action();
        },
    },
});
