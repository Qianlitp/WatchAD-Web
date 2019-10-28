<template>
    <div class="new-exclusion">
        <Modal width="900" :value="show" title="New Exclusion" @on-ok="new_exclusion" @on-visible-change="visible_change">
            <div class="new-exclusion-modal">
                <div class="select-ac-type">
                    <div class="label">Select Threat Activity Type:</div>
                    <Cascader 
                        style="width: 250px;margin-left: 20px;" 
                        :data="alert_types_config" 
                        v-model="alert_type"
                        placeholder="Select threat activity type"></Cascader>
                </div>
                <div>
                    <div class="label">Exclusion Rules</div>
                    <div class="exc-rules">
                        <div class="exc-rule-item" v-for="(rule, index) in rules" :key="index">
                            <div class="item-name">Rule {{index+1}}：</div>
                            <Input v-model="rule['field_name']" placeholder="Enter field name" style="width: 150px" />
                            <Select v-model="rule['field_type']" style="width:100px" placeholder="Field type">
                                <Option v-for="type in field_types" :value="type" :key="type">{{ type }}</Option>
                            </Select>
                            <Select v-model="rule['match_type']" style="width:100px" placeholder="Match type">
                                <Option v-for="type in match_types" :value="type" :key="type">{{ type }}</Option>
                            </Select>
                            <Input v-model="rule['value']" placeholder="Enter match value" style="width: 150px" />
                            <span class="remove-rule" @click="remove_rule(index)"><Icon type="ios-close-circle-outline" size="30"/></span>
                        </div>
                    </div>
                    <Button type="primary" @click="add_rule">Add Rule</Button>
                </div>
                <div class="comment">
                    <div class="label">Comment</div>
                    <Input v-model="comment" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="Comment something..." />
                </div>
            </div>
        </Modal>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import {entries} from '@/assets/js/common';
export default {
	name: "new-exclusion",
    props: {
        show: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            alert_type: [],
            field_types: ["string", "ip"],
            match_types: ["term", "regex", "ip"],
        	rules: [
                {
                    "field_name" : "", 
                    "field_type" : "", 
                    "match_type" : "", 
                    "value" : ""
                }
            ],
            comment: ""
        }
    },
    computed: {
        ...mapState({
            alert_types_config: state => state.actions.alert_types_config
        }),
        new_data() {
            return {
                "alert_code": this.alert_type[1],
                "comment": this.comment,
                "rules": this.rules
            }
        },
        validate_rules() {
            if (this.rules.length == 0) {
                return false
            } 
            for (let item of this.rules) {
                for (let [key, value] of entries(item)) {
                    if (value.length == 0) {
                        return false
                    }
                }
            }
            return true
        }
    },
    created() {
        this.$store.dispatch("get_alert_types");
    },
    methods: {
        new_exclusion() {
            if (this.alert_type.length < 2) {
                this.$Message.error('Threat Activity Type not select.');
                return
            }
            if (!this.validate_rules) {
                this.$Message.error('rule content error.');
                return 
            }
            this.$store.dispatch("new_exclusion", {
                data: this.new_data
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
            this.alert_type = [];
            this.comment = ""
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
        }
    },
    components: {
    	
    }
}
</script>

<style scoped>
.label {
    font-size: 14px;
    font-weight: 700;
}

.new-exclusion-modal {
    padding: 20px 40px;
}

.select-ac-type {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
}

.exc-rules {
    margin: 10px 0px; 
    display: flex;
    flex-direction: column;
}

.exc-rule-item {
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

.comment {
    margin-top: 20px;
}
</style>