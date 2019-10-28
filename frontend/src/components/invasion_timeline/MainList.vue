<template>
    <div class="main-list">
        <Timeline class="time-line">
            <TimelineItem v-for="invasion in invasion_list" :key="invasion['_id']">
                <div class="invasion-time">
                    <Time :time="new Date(invasion['end_time'])" />
                </div>
                <invasion-item 
                    :invasion="invasion" 
                    @mistake="mistake" 
                    @ignore="ignore"
                    @finish="finish"
                    width="900"></invasion-item>
            </TimelineItem>
            <TimelineItem v-show="!null_data_show">
                <span class="show-more" @click="show_more">查看更多</span>
            </TimelineItem>
        </Timeline>
        <mistake-confirm :show="mistake_confirm_show" :activity="confirm_invasion" @visible_change="mistake_show_change"></mistake-confirm>
        <ignore-confirm :show="ignore_confirm_show" :activity="confirm_invasion" @visible_change="ignore_show_change"></ignore-confirm>
        <finish-confirm :show="finish_confirm_show" :activity="confirm_invasion" @visible_change="finish_show_change"></finish-confirm>
        <div v-show="null_data_show && !loading" class="null_data">
            <img class="null_img" :src="timeline_null_img">
            <div class="null_text">No results, please change your filter conditions</div>
        </div>
        <Spin fix v-show="loading">
            <Icon type="ios-loading" size=50 class="spin-icon-load"></Icon>
            <div class="loading-text">loading</div>
        </Spin>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import timeline_null_img from '@/assets/img/timeline_null.png';
import InvasionItem from '@/components/invasion_timeline/InvasionItem';
import MistakeConfirm from '@/components/actions/MistakeConfirm';
import IgnoreConfirm from '@/components/actions/IgnoreConfirm';
import FinishConfirm from '@/components/actions/FinishConfirm';
export default {
	name: "main-list",
    data() {
        return {
        	time1: (new Date()).getTime() - 60 * 3 * 1000,
            mistake_confirm_show: false,
            ignore_confirm_show: false,
            finish_confirm_show: false,
            confirm_invasion: {},
            timeline_null_img: timeline_null_img
        }
    },
    computed: {
    	...mapState({
            invasion_list: state => state.index.invasion_list,
            loading: state => state.index.loading
        }),
        null_data_show() {
            return this.invasion_list.length == 0;
        }
    },
    created() {

    },
    methods: {
        mistake(params) {
            this.mistake_confirm_show = true;
            this.confirm_invasion = params.activity;
        },
        mistake_show_change(params) {
            this.mistake_confirm_show = params.visible;
        },
        ignore(params) {
            this.ignore_confirm_show = true;
            this.confirm_invasion = params.activity;
        },
        ignore_show_change(params) {
            this.ignore_confirm_show = params.visible;
        },
        finish(params) {
            this.finish_confirm_show = true;
            this.confirm_invasion = params.activity;
        },
        finish_show_change(params) {
            this.finish_confirm_show = params.visible;
        },
        show_more() {
            this.$store.commit("add_page");
            this.$store.dispatch('get_invasion_list');
        }
    },
    components: {
    	'invasion-item': InvasionItem,
        'mistake-confirm': MistakeConfirm,
        'ignore-confirm': IgnoreConfirm,
        'finish-confirm': FinishConfirm
    }
}
</script>

<style scoped>
.scroll-content {
    min-width: 900px;
}

.main-list {
    display: flex;
    flex: 1;
    margin-top: 30px;
    position: relative;
    flex-direction: column;
    align-items: center;
    min-height: 800px;
}

.time-line {

}

.invasion-time {
	margin: 0px 0px 5px 5px;
}

.show-more {
    font-size: 15px;
    color: #2d8cf0;
    cursor: pointer;
}

.null_data {
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.null_img {
    height: 200px;
}

.null_text {
    font-size: 16px;
    color: #273142;
    margin-top: 25px;
}
.loading-text {
    font-size: 20px;
}

.spin-icon-load{
    animation: ani-demo-spin 1s linear infinite;
}
</style>