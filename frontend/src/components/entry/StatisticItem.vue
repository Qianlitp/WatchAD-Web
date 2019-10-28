<template>
    <Poptip trigger="click" placement="bottom" :disabled="disabled">
        <div class="statistic-item" title="点击查看数据">
            <img class="img" :src="img_path"></img>
            <div class="name-count">
                <div class="name">{{name}}</div>
                <div class="count" :class="{'disabled': data_list.length == 0}">{{data_list.length}}</div>
            </div>
            <div class="right"></div>
        </div>
        <div v-if="type == 'activities'" class="activities-content" slot="content">
            <activity-item 
                v-for="ac in data_list"
                width="500" 
                :activity="ac"
                :actions_show="false"
                :small="true"></activity-item>
        </div>
        <div v-else-if="type == 'access_entries'" class="statistic-content" slot="content">
            <multi-entry-item
                v-for="entry in data_list"
                :name="entry['entry_name']"
                :entry_type="entry['entry_type']"
                :domain="domain"
                ></multi-entry-item>
        </div>
        <div v-else class="statistic-content" slot="content">
            <multi-entry-item
                v-for="entry in data_list"
                :name="entry"
                :icon_name="icon_name"
                :entry_type="entry_type"
                :domain="domain"
                ></multi-entry-item>
        </div>
    </Poptip>
</template>

<script>
import {mapState} from 'vuex'
import ActivityItem from '@/components/activity_timeline/ActivityItem'
import MultiEntryItem from '@/components/common/MultiEntryItem'
export default {
    name: "statistic-item",
    props: {
        img_path: {
            type: String,
            required: true
        },
        name: {
            type: String,
            required: true
        },
        type: {
            type: String,
            required: true
        },
        data_list: {
            type: Array,
            required: true
        }
    },
    data(){
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            domain: state => state.index.domain
        }),
        disabled() {
            return this.data_list.length == 0;
        },
        icon_name() {
            if (this.type == "logon_ips") {
                return "iconfont icon-dizhidingwei"
            } 
            return ""
        },
        entry_type() {
            if (this.type == "logon_users") {
                return "user"
            } else if (this.type == "used_computers") {
                return "computer"
            } 
            return ""
        }
    },
    methods: {
        
    },
    components: {
        "multi-entry-item": MultiEntryItem,
        "activity-item": ActivityItem
    }
}
</script>

<style scoped>
.statistic-item {
    background: #fff;
    border: 1px solid rgba(0,0,0,0.08);
    box-shadow: 0 3px 12px 0 rgba(224,224,224,0.12);
    border-radius: 4px;
    border-radius: 4px;
    width: 350px;
    height: 130px;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    cursor: pointer;
}

.img {
    width: 50px;
}

.name {
    color: rgba(37,37,37,0.50);
}

.count {
    font-family: DIN-Regular;
    font-size: 46px;
    color: rgba(37,37,37,0.80);
    letter-spacing: 0;
}

.name-count {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.activities-content>div {
    margin: 10px 5px 10px 0px;
}

.activities-content { 
    max-height: 500px;
    overflow: auto;
}

.statistic-content {
    width: 300px;
    display: flex;
    flex-direction: column;
    max-height: 300px;
    overflow: auto;
}

.disabled {
    color: rgba(37,37,37,0.40);
}
</style>