<template>
    <div class="index-search-view">
        <index-view>
            <data-search-filter></data-search-filter>
            <data-result-table></data-result-table>
        </index-view>
    </div>
</template>

<script>
import IndexView from '@/views/IndexView';
import DataSearchFilter from '@/components/data_search/DataSearchFilter';
import DataResultTable from '@/components/data_search/DataResultTable';
import {mapState} from 'vuex'
export default {
    name: "index-search-view",
    data(){
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            
        })
    },
    methods: {
        
    },
    components: {
        'index-view': IndexView,
        'data-search-filter': DataSearchFilter,
        'data-result-table': DataResultTable
    }
}
</script>

<style scoped>
.index-search-view {

}

</style>