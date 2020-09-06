<template>
    <div>
        <div>
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">자유롭게 적어주세요</h5>
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="무슨 생각을 하고있나요?" />
                        <div class="input-group-append">
                            <button class="btn btn-outline-secondary" type="button" id="button-addon2">
                                전송
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br />
    </div>
</template>

<script>
export default {
    name: 'postTweet',
};
</script>

<style scoped></style>
