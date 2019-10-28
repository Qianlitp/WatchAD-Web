<template>
    <index-view>
        <div class="user-view">
            <user-left-intro></user-left-intro>
            <user-activity-data v-show="data_type == 'activity'"></user-activity-data>
            <user-detail-info v-show="data_type == 'data'"></user-detail-info>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import UserLeftIntro from '@/components/entry/UserLeftIntro'
import UserActivityData from '@/components/entry/UserActivityData'
import UserDetailInfo from '@/components/entry/UserDetailInfo'
import {mapState} from 'vuex'
export default {
    name: "user-view",
    data(){
        return {

        }
    },
    created(){
        this.$store.commit("set_entry_info", {
            name: this.$route.params.user_name,
            type: "user",
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
                name: this.$route.params.user_name,
                type: "user"
            })
        }
    },
    components: {
        'index-view': IndexView,
        'user-left-intro': UserLeftIntro,
        'user-activity-data': UserActivityData,
        'user-detail-info': UserDetailInfo
    }
}
</script>

<style scoped>
.user-view {
    margin: 50px;
    display: flex;
    flex: 1;
}

</style>