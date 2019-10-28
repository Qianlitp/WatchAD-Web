<template>
    <div class="edit-exclusion">
        <Modal width="900" :value="show" title="Edit Exclusion" @on-ok="update_exclusion" @on-visible-change="visible_change">
            <div class="edit-exclusion-modal">
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
import {mapState} from 'vuex';
import {entries} from '@/assets/js/common';
export default {
	name: "edit-exclusion",
    props: {
        show: {
            type: Boolean,
            required: true
        },
        pdata: {
            type: Object,
            required: true
        }
    },
    watch: {
        pdata(new_data, old) {
            this.id = new_data["_id"];
            this.alert_type = this.get_cascader_value_by_code(new_data["alert_code"]);
            this.rules = new_data["rules"];
            this.comment = new_data["comment"];
        }
    },
    data() {
        return {
            id: "",
            alert_type: [],
            field_types: ["string", "ip"],
            match_types: ["term", "regex", "ip"],
        	rules: [],
            comment: ""
        }
    },
    computed: {
        ...mapState({
            alert_types_config: state => state.actions.alert_types_config,
        }),
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
        },
        new_data() {
            return {
                "alert_code": this.alert_type[1],
                "comment": this.comment,
                "rules": this.rules
            }
        }
    },
    created() {
        this.$store.dispatch("get_alert_types");
    },
    methods: {
        update_exclusion() {
            if (this.alert_type.length < 2) {
                this.$Message.error('Threat Activity Type not select.');
                return
            }
            if (!this.validate_rules) {
                this.$Message.error('rule content error.');
                return 
            }
            this.$store.dispatch("update_exclusion", {
                id: this.id,
                data: this.new_data
            })
        },
        visible_change(visible) {
            this.$emit("visible_change", {
                visible: visible
            });
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
        get_cascader_value_by_code(code) {
            for (let item of this.alert_types_config) {
                for (let sub_item of item["children"]) {
                    if (sub_item["value"] == code) {
                        return [item["value"], code]
                    } 
                }
            }
            return [];
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

.edit-exclusion-modal {
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