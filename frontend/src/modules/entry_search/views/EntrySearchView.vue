<template>
    <index-view>
        <div class="entry-search-view">
            <result-filter class="left"></result-filter>
            <search-result></search-result>
            <div class="right"></div>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import ResultFilter from '@/components/entry_search/ResultFilter';
import SearchResult from '@/components/entry_search/SearchResult';
import {mapState} from 'vuex'
export default {
    name: "entry-search-view",
    data() {
        return {

        }
    },
    created() {

    },
    computed: {
        ...mapState({

        })
    },
    methods: {

    },
    components: {
        'index-view': IndexView,
        'result-filter': ResultFilter,
        'search-result': SearchResult
    }
}
</script>

<style scoped>
.entry-search-view {
    margin-top: 30px;
    display: flex;
    flex: 1;
    flex-direction: row;
}

.left {
    flex: 0 0 400px;
}

.right {
    flex: 0 0 15em;
}

</style>