import { defineStore } from "pinia";
import { supabase } from "../supabase.js";
import { ref, watch } from "vue";

export const useWordStore = defineStore("word", () => {
    const wordList = ref([]);
    const word = ref(null);
    const title = ref(null);
    const description = ref(null);
    const code = ref(null);
    const filterText = ref(null);

    const setFilterText = (text) => {
        filterText.value = text;
    };    

    const setDescription = (word) => {
        description.value = word.description;
    };

    const setTitle = (word) => {
        title.value = word.title;
    };

    const setCode = (word) => {
        code.value = word.code;
    };

    const filterWordList = () => {
        if (filterText.value) {
            return wordList.value.filter((word) => {
                return word.word.word.toLowerCase().includes(filterText.value.toLowerCase());
            });
        }
        else {
            return wordList.value;
        }
    };

    const getWordDetails = (id) => {
        const selectedWord =  wordList.value.find((word) => {
            return word.id === id;
        });
        return selectedWord;
    };

    watch(filterText, () => {
        filterWordList();
    });

    async function getWordList() {
        try {
            const { data, error } = await supabase.from("articles").select("*").order('created_at', { ascending: false });

            if (error) throw error;

            wordList.value = data;
        }
        catch (error) {
            throw error;
        }
    }


    async function apiWordList() {
        try {
            const { data, error } = await supabase.from("articles").select("*").order('created_at', { ascending: false });

            if (error) throw error;

            wordList.value = data;
            return wordList.value;
        }
        catch (error) {
            throw error;
        }
    }

    async function insertWord(user_id) {
        
        try {
            const { data, error } = await supabase.from("articles").insert(
                {
                    title: title.value,
                    description: description.value,
                    code: code.value,
                }
            );

            if (error) throw error;

            title.value = null;
            description.value = null;
            code.value = null;

            getWordList();
        }
        catch (error) {
            throw error;
        }
    }

    async function deleteWord(id) {
        try {
            const { data, error } = await supabase.from("articles").delete().match({ id: id });

            if (error) throw error;

            getWordList();
        }
        catch (error) {
            throw error;
        }
    }

    return {
        wordList,
        word,
        title,
        description,
        code,
        filterText,
        setFilterText,
        filterWordList,
        setDescription,
        setCode,
        setTitle,
        getWordDetails,
        getWordList,
        apiWordList,
        insertWord,
        deleteWord,
    };
});