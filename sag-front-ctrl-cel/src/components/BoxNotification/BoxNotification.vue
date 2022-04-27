
<template>
    <div class="notification is-info">
        {{ message }}
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: 'BoxNotificationComponent',
    props: {
        message: {
            type: String,
            required: true,
        }
    }
})
</script>