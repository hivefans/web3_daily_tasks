<template>
    <div class="mt-2">
       
        <div class="my-2 p-4 bg-slate-100 rounded text-slate-900 relative">
            <p class="text-sm text-slate-400">{{wordStore.getWordDetails(id).created_at }}</p>
            <p class="text-sm text-slate-400">{{wordStore.getWordDetails(id).title }}</p>
            <p>{{wordStore.getWordDetails(id).description }}</p>
            <div class="bg-white p-4 mt-2 rounded">
                <p class="text-sm">{{wordStore.getWordDetails(id).code }}</p>
            </div>
        </div>
        
    </div>
</template>

<script setup>
import { useWordStore } from "../store/word.js";
import { defineProps } from "vue";

const wordStore = useWordStore();

const props = defineProps({
    id: Number
});




</script>

<style scoped></style>