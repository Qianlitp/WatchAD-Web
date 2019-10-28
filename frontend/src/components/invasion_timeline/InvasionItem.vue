<template>
    <div class="invasion-item">
        <div class="invasion-banner">
            <div class="title">{{invasion["title"]}}</div>
        </div>
        <div class="activity-list">
            <activity-item
                v-for="activity in activity_list"
                :small="true"
                :actions_show="false"
                width="800"
                :activity="activity">
            </activity-item>
        </div>
    </div>
</template>

<script>
import ActivityItem from "@/components/activity_timeline/ActivityItem";
export default {
	name: "invasion-item",
    props: {
        invasion: {
            type: Object,
            required: true
        }
    },
    data() {
        return {

        }
    },
    created(){

    },
    computed: {
        activity_list() {
            return this.invasion["activity_list"];
        },
        domain() {
            if (this.invasion.hasOwnProperty("domain")) {
                return this.invasion["domain"]
            } else {
                return ""
            }
        },
        status() {
            return this.invasion["status"];
        },
        status_name() {
            let status = this.status;
            if (status == "pending") {
                return "待处理";
            } else if (status == "ignore") {
                return "已忽略";
            } else if (status == "mistake") {
                return "误报";
            } else if (status == "finished") {
                return "已处理";
            } else if (status == "closed") {
                return "已关闭"
            }
        },
        status_color() {
            let status = this.invasion["status"];
            if (status == "pending") {
                return "success";
            } else if (status == "ignore") {
                return "default";
            } else if (status == "auto_ignore") {
                return "default";
            } else if (status == "mistake") {
                return "error";
            } else if (status == "finished") {
                return "info";
            } else if (status == "closed") {
                return "info"
            }
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
        finish_invasion() {
            this.$emit("finish", {
                invasion: this.invasion
            });
        },
        mistake_invasion() {
            this.$emit("mistake", {
                invasion: this.invasion
            });
        },
        ignore_invasion() {
            // 忽略选择
            this.$emit("ignore", {
                invasion: this.invasion
            });
        },
        delete_invasion() {
            // 删除确认
            this.$Modal.confirm({
                title: '删除确认',
                content: '<p>删除该入侵事件将会同时删除其包含的所有告警。</p><strong>确认要删除吗？</strong>',
                onOk: () => {
                    this.$store.dispatch('delete_invasion', {
                        "_id": this.invasion['_id']
                    });
                },
                onCancel: () => {
                    
                }
            });
        },
        close_invasion() {
            // 关闭确认
            this.$Modal.confirm({
                title: '关闭确认',
                content: '<p>关闭当前入侵事件，不影响之后的告警。</p><strong>确认要关闭吗？</strong>',
                onOk: () => {
                    this.$store.dispatch('close_invasion', {
                        "_id": this.invasion['_id']
                    });
                },
                onCancel: () => {
                    
                }
            });
        }
    },
    components: {
        "activity-item": ActivityItem
    }
}
</script>

<style scoped>
.invasion-item {
    padding: 20px;
    background: #fff;
    box-shadow: 0 2px 2px rgba(0,0,0,.1);
    border-radius: 5px;
}

.invasion-banner {
    display: flex;
    flex-direction: row;
    height: 40px;
    line-height: 40px;
    margin-bottom: 10px;
}

.title {
    font-size: 20px;
    font-family: PingFangSC, sans-serif;
}

.activity-list {
    max-height: 600px;
    overflow: auto;
}

.activity-list>div {
    margin-bottom: 10px;
}
</style>