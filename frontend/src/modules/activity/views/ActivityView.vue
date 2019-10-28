<template>
    <index-view>
        <div class="detail-main">
            <card-view></card-view>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import CardView from './CardView';
export default {
    data(){
        return {

        }
    },
    created(){

    },
    components: {
        'index-view': IndexView,
        'card-view': CardView
    }
}
</script>

<style scoped>
.detail-main {
    margin-top: 60px;
    display: flex;
    flex: 1;
    justify-content: center;
}
</style>