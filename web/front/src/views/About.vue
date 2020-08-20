<template>
    <div class="about">
        <h1>This is an about page</h1>
        <h3>{{ greet }}</h3>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'say-hi',
    data() {
        return {
            greet: '',
        };
    },
    methods: {
        getGreet() {
            let path = 'http://localhost:5000/';
            axios.get(path).then(res => {
                this.greet = res.data;
            });
        },
    },
    created() {
        this.getGreet();
    },
};
</script>
