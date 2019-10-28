<template>
    <index-view>
        <div class="computer-view">
            <computer-left-info></computer-left-info>
            <computer-activity-data v-show="data_type == 'activity'"></computer-activity-data>
            <computer-detail-info v-show="data_type == 'data'"></computer-detail-info>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import ComputerLeftInfo from '@/components/entry/ComputerLeftInfo';
import ComputerActivityData from '@/components/entry/ComputerActivityData';
import ComputerDetailInfo from '@/components/entry/ComputerDetailInfo';
import {mapState} from 'vuex'
export default {
    name: "computer-view",
    data(){
        return {

        }
    },
    created(){
        this.$store.commit("set_entry_info", {
            name: this.$route.params.computer_name.replace("$", ""),
            type: "computer",
            domain: this.$route.params.domain
        })
        this.search();
    },
    computed: {
        ...mapState({
            entries: state => state.entry.entries,
            data_type: state => state.index.data_type
        })
    },
    methods: {
        search() {
            if (this.entries.hasOwnProperty(this.value)) {
                return
            }
            this.$store.dispatch("search_entry", {
                domain: this.$route.params.domain,
                name: this.$route.params.computer_name.replace("$", ""),
                type: "computer"
            })
        }
    },
    components: {
        'index-view': IndexView,
        'computer-left-info': ComputerLeftInfo,
        'computer-activity-data': ComputerActivityData,
        'computer-detail-info': ComputerDetailInfo
    }
}
</script>

<style scoped>
.computer-view {
    margin: 50px;
    display: flex;
    flex: 1;
}

</style>