<template>
    <div class="activity-item" :style="{'width': width+'px'}">
        <div class="level" :class="level_color_class(activity['level'])"></div>
        <div class="right" :class="{'small-right': small}">
            <div class="item-nav" :class="{'small-item-nav': small}">
                <div class="item-title">
                    <a class="title" @click="detail(activity['_id'])" :class="{'small-title': small}">{{activity["title"]}}</a>
                    <div class="status">
                        <Tag color="primary">{{activity["classify"]}}</Tag>
                    </div>
                    <div class="status">
                        <Tag :color="status_color">{{status_name}}</Tag>
                    </div>
                </div>
                <div v-if="actions_show" class="item-actions">
                    <span title="已处理" v-if="status == 'pending'" style="margin-top: -2px;" @click="finish_activity()">
                        <Icon color="#a4a6a9" size="18" custom="iconfont icon-ok" />
                    </span>
                    <span title="忽略" v-if="status == 'pending'" @click="ignore_activity()">
                        <Icon color="#a4a6a9" size="18" custom="iconfont icon-hulve" />
                    </span>
                    <span title="误报" v-if="status == 'pending'" @click="mistake_activity()">
                        <Icon color="#a4a6a9" size="20" custom="iconfont icon-exclude" />
                    </span>
                    <span title="关闭" v-if="status == 'pending'"  @click="close_activity()">
                        <Icon color="#a4a6a9" size="18" custom="iconfont icon-no"/>
                    </span>
                    <span title="删除" @click="delete_activity()">
                        <Icon color="#a4a6a9" size="18" custom="iconfont icon-delete"/>
                    </span>
                </div>
            </div>
            <div class="item-content" :class="{'small-item-content': small}">
                <description :desc_template="description" :desc_data="desc_data" :domain="domain"/>
            </div>
            <div class="item-footer">
                <div v-if="start_time != end_time">
                    <span>从 </span>
                    <span>{{start_time}}</span>
                    <span> 至 </span>
                    <span>{{end_time}}</span>
                </div>
                <span v-else>{{end_time}}</span>
            </div>
        </div>
    </div>
</template>

<script>
import {dateFormat} from "@/assets/js/common";
import Description from "@/components/activity/Description";
export default {
	name: "activity-item",
    props: {
        activity: {
            type: Object,
            required: true
        },
        actions_show: {
            type: Boolean,
            default: true
        },
        width: {
            type: String,
            default: "1000"
        },
        small: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {

        }
    },
    created(){

    },
    computed: {
        domain() {
            if (this.activity.hasOwnProperty("domain")) {
                return this.activity["domain"]
            } else {
                return ""
            }
        },
        description() {
            if (this.activity.hasOwnProperty("description")) {
                return this.activity["description"]
            } else {
                return ""
            }
        },
        desc_data() {
            if (this.activity.hasOwnProperty("desc_data")) {
                return this.activity["desc_data"]
            } else {
                return []
            }
        },
        status() {
            return this.activity["status"];
        },
        status_name() {
            let status = this.status;
            if (status == "pending") {
                return "待处理";
            } else if (status == "ignore") {
                return "已忽略";
            } else if (status == "auto_ignore") {
                return "自动忽略";
            } else if (status == "mistake") {
                return "误报";
            } else if (status == "finished") {
                return "已处理";
            } else if (status == "closed") {
                return "已关闭"
            }
        },
        status_color() {
            let status = this.activity["status"];
            if (status == "pending") {
                return "success";
            } else if (status == "ignore") {
                return "default";
            } else if (status == "auto_ignore") {
                return "default";
            } else if (status == "mistake") {
                return "error";
            } else if (status == "finished") {
                return "default";
            } else if (status == "closed") {
                return "default"
            }
        },
        start_time() {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(this.activity["start_time"]))
        },
        end_time() {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(this.activity["end_time"]))
        }
    },
    methods: {
        level_color_class(level) {
            if (level === "low") {
                return {"low-level": true};
            } else if (level === "medium") {
                return {"middle-level": true};
            } else if (level === "high") {
                return {"high-level": true};
            } 
        },
        level_name(level) {
            if (level === "low") {
                return "低危";
            } else if (level === "medium") {
                return "中危";
            } else if (level === "high") {
                return "高危";
            } 
        },
        do_alert() {

        },
        finish_activity() {
            this.$emit("finish", {
                activity: this.activity
            });
        },
        mistake_activity() {
            this.$emit("mistake", {
                activity: this.activity
            });
        },
        ignore_activity() {
            // 忽略选择
            this.$emit("ignore", {
                activity: this.activity
            });
        },
        delete_activity() {
            // 删除确认
            this.$Modal.confirm({
                title: '删除确认',
                content: '<p>删除该威胁活动将会同时删除其包含的告警。</p><strong>确认要删除吗？</strong>',
                onOk: () => {
                    this.$store.dispatch('delete_activity', {
                        "_id": this.activity['_id']
                    });
                },
                onCancel: () => {
                    
                }
            });
        },
        close_activity() {
            // 关闭确认
            this.$Modal.confirm({
                title: '关闭确认',
                content: '<p>关闭当前威胁活动，不影响之后的告警。</p><strong>确认要关闭吗？</strong>',
                onOk: () => {
                    this.$store.dispatch('close_activity', {
                        "_id": this.activity['_id']
                    });
                },
                onCancel: () => {
                    
                }
            });
        },
        detail(activity_id) {
            window.open("/activity.html#/" + activity_id)
        }
    },
    components: {
        "description": Description
    }
}
</script>

<style scoped>
.activity-item {
    display: flex;
    flex-direction: row;
    box-shadow: 0 2px 2px rgba(0,0,0,.1);
    border-radius: 5px;
}

.level {
    width: 10px;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
}

.low-level {
    background: #c5c8ce;
}

.middle-level {
    background: #ff9900;
}

.high-level {
    background: #ed4014;
}

.right {
    display: flex;
    flex-direction: column;
    flex: 1;
    background: #fff;
    padding: 20px 10px 20px 30px;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
}

.small-right {
    padding: 10px 10px 10px 10px;
}

.item-nav {
    display: flex;
    line-height: 30px;
    height: 30px;
    justify-content: space-between;
}

.small-item-nav {
    line-height: 20px;
    height: 20px;
}

.item-content {
    margin: 10px 120px 15px 0px; 
    font-size: 14px;
}

.small-item-content {
    margin: 5px 5px 5px 0px; 
    font-size: 12px;
}

.item-nav-right {
    display: flex;
    flex-direction: row;
    width: 320px;
    justify-content: space-between;
}

.item-nav-classify {
    margin-right: 20px;
    color: #8a8a8a
}

.item-actions {
    display: flex;
    align-items: center;
    margin-top: -20px;
}

.item-actions>span {
    margin: 0px 5px; 
    cursor: pointer;
}

.item-title {
    display: flex;
}

.item-footer {
    display: flex;
    color: #a4a6a9;
    justify-content: space-between;
    margin-right: 20px;
}

.status {
    display: flex;
    align-items: center;
}

.title {
    margin-right: 10px;
    line-height: 30px;
    font-size: 18px;
    font-family: PingFangSC, sans-serif;
    color: #606673
}

.small-title {
    line-height: 20px;
    font-size: 16px;
}

.confidence {
    display: flex;
    align-items: center;
}

.confidence-bar {
    margin-left: 5px;
    width: 150px;
}
</style>