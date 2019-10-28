<template>
    <index-view>
        <div class="group-view">
            <group-left-info></group-left-info>
            <group-activity-data v-show="data_type == 'activity'"></group-activity-data>
            <group-detail-info v-show="data_type == 'data'"></group-detail-info>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import GroupLeftInfo from '@/components/entry/GroupLeftInfo';
import GroupActivityData from '@/components/entry/GroupActivityData';
import GroupDetailInfo from '@/components/entry/GroupDetailInfo';
import {mapState} from 'vuex'
export default {
    name: "group-view",
    data() {
        return {

        }
    },
    created(){
        this.$store.commit("set_entry_info", {
            name: this.$route.params.group_name,
            type: "group",
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
                name: this.$route.params.group_name,
                type: "group"
            })
        }
    },
    components: {
        'group-left-info': GroupLeftInfo,
        'group-activity-data': GroupActivityData,
        'group-detail-info': GroupDetailInfo,
        'index-view': IndexView
    }
}
</script>

<style scoped>
.group-view {
    margin: 50px;
    display: flex;
    flex: 1;
}

</style>