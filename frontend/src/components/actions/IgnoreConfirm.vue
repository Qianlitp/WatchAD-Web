<template>
    <div class="ignore-confirm">
        <Modal width="800" :value="show" title="忽略确认" @on-ok="do_ignore" @on-visible-change="visible_change">
            <div class="ignore-text">确认要 <span class="ignore-name">忽略</span> 本威胁活动吗？</div>
            <div class="ignore-title"><i-switch class="rule-switch" v-model="is_add_rule" @on-change="add_rule_switch" />添加忽略规则：</div>
            <div v-show="is_add_rule" class="ignore-rules">
                <div class="refer">
                    <div>当前威胁活动的字段值参考：</div>
                    <div>
                        <div v-for="one in desc_data">{{get_title(one["name"])}}： {{array_to_str(one["value"])}}</div>
                    </div>
                </div>
                <div class="ignore-rule-item" v-for="(rule, index) in rules" :key="index">
                    <div class="item-name">规则{{index+1}}：</div>
                    <Select v-model="rule['field_name']" style="width:150px" placeholder="选择字段名">
                        <Option v-for="field in field_list" :value="field" :key="field">{{ get_title(field) }}</Option>
                    </Select>
                    <Select v-model="rule['field_type']" style="width:100px" placeholder="字段类型">
                        <Option v-for="type in field_types(index)" :value="type" :key="type">{{ type }}</Option>
                    </Select>
                    <Select v-model="rule['match_type']" style="width:100px" placeholder="匹配类型">
                        <Option v-for="type in match_types(index)" :value="type" :key="type">{{ type }}</Option>
                    </Select>
                    <Input v-model="rule['value']" placeholder="请输入匹配值" style="width: 150px" />
                    <span class="remove-rule" @click="remove_rule(index)"><Icon type="ios-close-circle-outline" size="30"/></span>
                </div>
            </div>
            <Button v-show="is_add_rule" type="primary" @click="add_rule">添加规则</Button>
        </Modal>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "ignore-confirm",
    props: {
        show: {
            type: Boolean,
            required: true
        },
        activity: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            is_add_rule: false,
        	rules: [
                {
                    "field_name" : "", 
                    "field_type" : "", 
                    "match_type" : "", 
                    "value" : ""
                }
            ]
        }
    },
    computed: {
    	...mapState({
            
        }),
        alert_code() {
            return this.activity["alert_code"];
        },
        desc_data() {
            if (this.activity.hasOwnProperty("desc_data")) {
                return this.activity["desc_data"];
            } else {
                return [];
            }
        },
        field_list() {
            let result = [];
            for (let each of this.desc_data) {
                result.push(each["name"])
            }
            return result;
        },
        ignore_type() {
            if (this.is_add_rule) {
                return "add_rule"
            } else {
                return "ignore_once"
            }
        }
    },
    created() {

    },
    methods: {
        do_ignore() {
            this.$store.dispatch("ignore_activity", {
                id: this.activity["_id"],
                alert_code: this.alert_code,
                ignore_type: this.ignore_type,
                rules: this.rules
            })
        },
        visible_change(visible) {
            this.$emit("visible_change", {
                visible: visible
            });
            this.rules = [
                {
                    "field_name" : "", 
                    "field_type" : "", 
                    "match_type" : "", 
                    "value" : ""
                }
            ];
            this.is_add_rule = false;
        },
        field_types(index) {
            let field_name = this.rules[index]["field_name"];
            if (!field_name) {
                return
            }
            if (field_name.includes("ip")) {
                return ["ip", "string"];
            } else {
                return ["string"]
            }
        },
        match_types(index) {
            let field_type = this.rules[index]["field_type"];
            if (!field_type) {
                return
            }
            if (field_type === "string"){
                return ["term", "regex"];
            } else if (field_type === "ip") {
                return ["term", "ip"];
            }
        },
        add_rule() {
            this.rules.push({
                "field_name" : "", 
                "field_type" : "", 
                "match_type" : "", 
                "value" : ""
            })
        },
        remove_rule(index) {
            this.rules.splice(index, 1);
        },
        add_rule_switch(status) {
            this.is_add_rule = status;
        },
        get_title(name) {
            if (name == "source_ip") {
                return "来源IP"
            } else if (name == "relay_ip") {
                return "中继者IP"
            } else if (name == "source_workstation") {
                return "来源计算机"
            } else if (name == "relay_workstation") {
                return "中继计算机"
            } else if (name == "source_user_name") {
                return "使用身份"
            } else if (name == "target_user_name") {
                return "目标用户"
            } else if (name == "group_name") {
                return "用户组名称"
            } else if (name == "exceptional_type") {
                return "异常类型"
            } else if (name == "dc_hostname") {
                return "域控"
            } else if (name == "relative_target_name") {
                return "文件共享名称"
            } else if (name == "encryption") {
                return "加密方式"
            } else if (name == "ticket_type") {
                return "票据类型"
            } else if (name == "method") {
                return "攻击方式"
            } else if (name == "alert_rule") {
                return "告警规则"
            } else if (name == "tool_name") {
                return "工具名称"
            } else if (name == "brute_force_type") {
                return "爆破类型"
            } else {
                return name
            }
        },
        array_to_str(value) {
            let result = [];
            for (let each of value) {
                result.push(each["name"])
            }
            return result.join("、");
        }
    },
    components: {
    	
    }
}
</script>

<style scoped>
.ignore-text {
    font-size: 16px;
}

.ignore-title {
    margin-top: 20px;
    font-size: 16px;
}

.ignore-name {
    font-size: 18px;
    color: #a5a5a5;
}

.ignore-rules {
    margin: 10px 0px; 
    display: flex;
    flex-direction: column;
}

.ignore-rule-item {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 10px 0px; 
    margin: 3px 0px;
    border: 1px dashed #9e9e9e;
}

.item-name {
    font-size: 16px;
    font-weight: 700;
    line-height: 32px;
}

.remove-rule {
    cursor: pointer;
}

.rule-switch {
    margin-right: 10px;
}

.refer {
    padding: 10px;
    font-size: 15px;
}

</style>