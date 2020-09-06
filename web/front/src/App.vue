<template>
    <div>
        <topnav></topnav>
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <postTweet></postTweet>
                    <listTweet></listTweet>
                </div>
                <div class="col-md-4">
                    <userProfile></userProfile>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import topnav from './views/navMenu/topnav';
import postTweet from './views/main/body/postTweet';
import listTweet from './views/main/body/listTweet';
import userProfile from './views/main/profile/userProfile';

export default {
    components: { postTweet, listTweet, userProfile, topnav },
    data() {
        return {
            greet: '',
        };
    },
    methods: {},
    created() {},
};
</script>
<style></style>
