<template>
    <div class="card-view">
        <activity-item :activity="activity" @mistake="mistake" @ignore="ignore"></activity-item>
        <div class="flow-graph-content">
            <flow-graph :graph="graph" :domain="domain"></flow-graph>
        </div>
        <div class="alert-table">
            <alert-detail-select></alert-detail-select>
        </div>
        <div>
            <raw-log-list :log_list="raw_log_list"></raw-log-list>
        </div>
        <div>
            <recommendation></recommendation>
        </div>
        <mistake-confirm :show="mistake_confirm_show" :activity="activity" @visible_change="mistake_show_change"></mistake-confirm>
        <ignore-confirm :show="ignore_confirm_show" :activity="activity" @visible_change="ignore_show_change"></ignore-confirm>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import ActivityItem from '@/components/activity_timeline/ActivityItem';
import FlowGraph from '@/components/activity/FlowGraph';
import AlertDetailSelect from '@/components/activity/AlertDetailSelect';
import RawLogList from '@/components/activity/RawLogList';
import Recommendation from '@/components/activity/Recommendation';
import MistakeConfirm from '@/components/actions/MistakeConfirm';
import IgnoreConfirm from '@/components/actions/IgnoreConfirm';
export default {
    name: "card-view",
    data(){
        return {
            mistake_confirm_show: false,
            ignore_confirm_show: false,
            confirm_activity: {}
        }
    },
    created(){
        this.$store.dispatch('get_activity_detail', {
            activity_id: this.$route.params.activity_id
        });
    },
    computed: {
        ...mapState({
            activity: state => state.index.activity
        }),
        domain() {
            if (this.activity.hasOwnProperty("domain")) {
                return this.activity["domain"];
            } else {
                return ""
            }
        },
        alert_code() {
            if (!this.activity['alert_code']) {
                return ""
            } else {
                return this.activity['alert_code']
            }
        },
        alert_list() {
            if (!this.activity['alert_list']) {
                return []
            } else {
                return this.activity['alert_list']
            }
        },
        graph() {
            if (this.activity.hasOwnProperty("graph")) {
                return this.activity['graph']
            } else {
                return [];
            }
        },
        raw_log_list() {
            let result = [];
            for (let each of this.alert_list) {
                result.push(each["raw_log"])
            }
            return result;
        },
        raw_krb_list() {
            let result = [];
            for (let each of this.alert_list) {
                result.push(each["raw_krb"])
            }
            return result;
        }
    },
    methods: {
        mistake() {
            this.mistake_confirm_show = true;
        },
        mistake_show_change(params) {
            this.mistake_confirm_show = params.visible;
        },
        ignore() {
            this.ignore_confirm_show = true;
        },
        ignore_show_change(params) {
            this.ignore_confirm_show = params.visible;
        }
    },
    components: {
        'activity-item': ActivityItem,
        'flow-graph': FlowGraph,
        'alert-detail-select': AlertDetailSelect,
        'raw-log-list': RawLogList,
        'recommendation': Recommendation,
        'mistake-confirm': MistakeConfirm,
        'ignore-confirm': IgnoreConfirm
    }
}
</script>

<style scoped>
.card-view {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.card-view>div {
    background: #fff;
    width: 1000px;
}
.flow-graph-content {
    border-top: 1px solid #e9ebec
}

.alert-table {
    padding: 0px 50px 20px 50px;
    border-bottom: 1px solid #e9ebec
}
</style>