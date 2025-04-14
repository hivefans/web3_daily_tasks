<script setup>
import { onMounted, ref } from "vue";
import { useWordStore } from "../store/word.js";

const wordStore = useWordStore();

onMounted(() => {
    wordStore.apiWordList().then(res=>{
        document.write(JSON.stringify(res));
    })
});

</script>