<template>
    <div class="sag-notifications">
            <div 
            class="notification"
            v-for="notif in notifications"
            :class="ctx[notif.type]"
            :key="notif.id"
            >
                <button class="delete"></button>
                {{  notif.message }}
            </div>
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType } from "vue";
import INotification, { NotificationType } from "@/interfaces/INotification";
import { useStore } from "@/store";

export default defineComponent({
    name: 'NotificationComponent',
    props: {
        notification: {
            type: Object as PropType<INotification>,
        },
    },
    data() {
        return {
            ctx: {
                [NotificationType.SUCCESS]: 'is-success',
                [NotificationType.WARNING]: 'is-warning',
                [NotificationType.DANGER]: 'is-danger',
            }
        }
    },
    setup() {
        const store = useStore();

        return {
            notifications: computed(() => store.state.notifications),
        }
    }
})
</script>