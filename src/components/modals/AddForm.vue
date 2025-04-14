<template>
    <div class="flex justify-between gap-x-5">
        <input v-model="title" class="border border-slate-400 flex-1 px-2 py-1 rounded outline-0 text-slate-800 text-base"
            type="text" placeholder="title" />
    </div>
    <div  class="my-5">
        <input type="text" placeholder="description" v-model="description"
            class="border border-slate-400 w-full px-2 py-1 rounded outline-0 text-slate-800 text-base" />
    </div>
    <div  class="my-5">
        <textarea type="text" placeholder="code" v-model="code" style="height: 200px;"
            class="border border-slate-400 w-full px-2 py-1 rounded outline-0 text-slate-800 text-base">
        </textarea>
    </div>
    
</template>

<script setup>
import { storeToRefs } from "pinia";
import { useWordStore } from "../../store/word";

const wordStore = useWordStore();

const { title, description, code } = storeToRefs(wordStore);



</script>