<template>
    <div class="user-activity-data">
        <div class="data-statistic">
            <statistic-item :img_path="activity_img" name="威胁活动" type="activities" :data_list="activities"></statistic-item>
            <statistic-item :img_path="resource_img" name="访问实体" type="access_entries" :data_list="access_entries"></statistic-item>
            <statistic-item :img_path="ip_img" name="登录IP" type="logon_ips" :data_list="logon_ips"></statistic-item>
            <statistic-item :img_path="computer_img" name="使用计算机" type="used_computers" :data_list="used_computers"></statistic-item>
        </div>
        <div class="user-activity-records">
            <div class="top-info">
                <div class="filter">
                    <DatePicker 
                        v-model="record_filter['start_time']" 
                        type="datetime" 
                        placeholder="Start time"
                        @on-change="search()">
                    </DatePicker>
                    <DatePicker 
                        style="margin-left: 20px;"
                        v-model="record_filter['end_time']" 
                        type="datetime" 
                        placeholder="End time"
                        @on-change="search()">
                    </DatePicker>
                    <Select @on-change="search()" v-model="record_filter['activity_type']" multiple style="min-width: 150px;margin-left: 20px;">
                        <Option value="threat_activities">威胁活动</Option>
                        <Option value="account_attr">账户属性更改</Option>
                        <Option value="group_change">用户组更改</Option>
                        <Option value="access_entry">访问实体</Option>
                        <Option value="ntlm_login">NTLM登录</Option>
                        <Option value="spn_change">SPN修改</Option>
                    </Select>
                </div>
                <div class="right-info">
                    <div v-if="activities.length > 0" class="alert-count">
                        <Icon size="15" custom="iconfont icon-kulou"></Icon>
                        <div style="margin-left: 5px;">存在 {{activities.length}} 个相关的威胁活动</div>
                    </div>
                    <div class="total">
                        共查询到 {{records.length}} 条相关的域内活动记录
                    </div>
                </div>
            </div>
            <div :class="{'records-null-content': real_data.length == 0}">
                <Scroll v-show="real_data.length > 0" :on-reach-bottom="more" height="716">
                    <div class="records-list" style="margin-top: -10px;">
                        <template v-for="each in real_data">
                            <div v-if="typeof(each) == 'string'" class="record-item-time">
                                {{each}}
                            </div>
                            <record-item v-else :record="each"></record-item>
                        </template>
                        <div class="load-more">向下滚动加载更多</div>
                    </div>
                </Scroll>
                <div v-show="real_data.length == 0">
                    <img class="records-null-img" :src="records_null_img"></img>
                    <div class="records-null-text">无相关域内活动记录</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import activity_img from '@/assets/img/alert.svg'
import resource_img from '@/assets/img/resource.svg'
import ip_img from '@/assets/img/ip.svg'
import computer_img from '@/assets/img/computer.svg'
import records_null from '@/assets/img/records_null.png'
import StatisticItem from './StatisticItem'
import RecordItem from './RecordItem'
import {mapState} from 'vuex'
import {entries} from '@/assets/js/common';
export default {
    name: "user-activity-data",
    data() {
        return {
            activity_img: activity_img,
            resource_img: resource_img,
            ip_img: ip_img,
            computer_img: computer_img,
            records_null_img: records_null,
            record_filter: {
                entry_type: "user",
                start_time: "",
                end_time: "",
                activity_type: [],
                page: 1,
                page_size: 20,
                more: false
            }
        }
    },
    created() {
        this.$store.dispatch("get_entry_activities");
        this.$store.dispatch("get_entry_logon_ips");
        this.$store.dispatch("get_entry_used_computers");
        this.$store.dispatch("get_entry_access_entries");
        this.search()
    },
    computed: {
        ...mapState({
            activities: state => state.index.activities,
            logon_ips: state => state.index.logon_ips,
            used_computers: state => state.index.used_computers,
            access_entries: state => state.index.access_entries,
            records: state => state.index.records,
            entry_name: state => state.index.entry_name,
            domain: state => state.index.domain
        }),
        real_data() {
            let result = [];
            let last_time = new Date();
            for (let each of this.records) {
                let now_time = new Date(each["@timestamp"]);
                if (last_time.getDate() != now_time.getDate() || result.length == 0) {
                    result.push(this.dispaly_time(each["@timestamp"]))
                }
                result.push(each);
                last_time = now_time
            }
            return result
        }
    },
    methods: {
        dispaly_time(time) {
            let target_date = new Date(time.split("T")[0]);
            let now_time = new Date();
            if (this.getInervalHour(target_date, now_time) < 24) {
                return "今天"
            } else {
                return time.split("T")[0]
            }
        },
        getInervalHour(startDate, endDate) {
            var ms = endDate.getTime() - startDate.getTime();
            if (ms < 0) return 0;
            return Math.floor(ms/1000/60/60);
        },
        search() {
            this.record_filter["entry_name"] = this.entry_name;
            this.record_filter["domain"] = this.domain;
            this.$store.dispatch("get_entry_records", this.record_filter);
        },
        more() {
            this.record_filter["entry_name"] = this.entry_name;
            this.record_filter["domain"] = this.domain;
            this.record_filter["page"] = this.record_filter["page"] + 1;
            this.record_filter["more"] = true;
            this.$store.dispatch("get_entry_records", this.record_filter);
        }
    },
    components: {
        'statistic-item': StatisticItem,
        'record-item': RecordItem
    }
}
</script>

<style scoped>
.user-activity-data {
    margin-left: 30px;
    display: flex;
    flex-direction: column;
    flex: 1;
}

.data-statistic {
    flex: 1;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.user-activity-records {
    height: 780px;
    background: #fff;
    border: 1px solid rgba(183,210,229,0.80);
    border-radius: 4px;
    border-radius: 4px;
}

.top-info {
    height: 64px;
    padding: 0px 20px;
    border-bottom: 1px solid #D8E5EE;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.filter {

}

.alert-count {
    cursor: pointer;
    padding: 4px 8px;
    color: #FB2C2C;
    display: flex;
    background: #efefef;
    border-radius: 10px;
    justify-content: space-between;

}

.record-item-time {
    background: #FAFBFC;
    height: 42px;
    line-height: 42px;
    font-size: 12px;
    color: #8DABC4;
    padding-left: 30px;
}

.load-more {
    text-align: center;
    margin: 20px 0px; 
    color: #2d8cf0;
}

.total {
    margin-left: 20px;
    margin-right: 10px;
    color: rgba(37,37,37,0.50);
}

.right-info {
    display: flex;
    align-items: center;
}

.records-null-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.records-null-img {
    margin-top: 150px;
    width: 170px;
    align-self: center;
}

.records-null-text {
    font-family: PingFangSC-Regular;
    font-size: 16px;
    text-align: center;
    margin-top: 20px;
}
</style>