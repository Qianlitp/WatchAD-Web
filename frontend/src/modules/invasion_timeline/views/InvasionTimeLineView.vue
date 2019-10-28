<template>
    <index-view>
        <div class="main">
            <main-list></main-list>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import MainList from '@/components/invasion_timeline/MainList';
export default {
    data(){
        return {

        }
    },
    created(){
        this.$store.dispatch('get_invasion_list');
    },
    methods: {

    },
    components: {
        'index-view': IndexView,
        'main-list': MainList
    }
}
</script>

<style scoped>

.main {
    display: flex;
    flex: 1;
    flex-direction: row;
    justify-content: space-between;
}

.left {
    flex: 0 0 20em;
}

.right {
    flex: 0 0 30em;
}

</style>