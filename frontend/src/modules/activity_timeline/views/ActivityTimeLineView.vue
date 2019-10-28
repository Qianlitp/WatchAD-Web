<template>
    <index-view>
        <div class="main">
            <fast-filter class="left"></fast-filter>
            <main-list></main-list>
            <detail-filter class="right"></detail-filter>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import MainList from '@/components/activity_timeline/MainList';
import FastFilter from '@/components/activity_timeline/FastFilter';
import DetailFilter from '@/components/activity_timeline/DetailFilter'
export default {
    data(){
        return {

        }
    },
    created(){
        this.$store.dispatch('get_activity_list');

        // setInterval(this.get_activity_list_no_bar, 1000);
    },
    methods: {
        get_activity_list_no_bar() {
            this.$store.dispatch('get_activity_list', {"show_progress_bar": false});
        }
    },
    components: {
        'index-view': IndexView,
        'main-list': MainList,
        'detail-filter': DetailFilter,
        'fast-filter': FastFilter
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