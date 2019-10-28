<template>
    <div class="detail-filter">
        <Form :label-width="100" label-position="top">
            <FormItem label="Field Select">
                <Input v-model="filter_value">
                    <Select v-model="filter_name" slot="prepend" style="width: 150px" placeholder="Select field">
                        <Option value="source_ip">Source IP</Option>
                        <Option value="source_user_name">Source Username</Option>
                        <Option value="source_workstation">Source Computer</Option>
                        <Option value="target_user_name">Target Username</Option>
                        <Option value="dc_hostname">Domain Controller</Option>
                    </Select>
                </Input>
            </FormItem>
            <FormItem label="Time Select">
                <Row><DatePicker type="datetime" placeholder="Start time" v-model="start_time" format="yyyy-MM-dd HH:mm:ss"></DatePicker></Row>
                <Row class="">-</Row>
                <Row><DatePicker type="datetime" placeholder="End Time" v-model="end_time" format="yyyy-MM-dd HH:mm:ss"></DatePicker></Row>
            </FormItem>
            <FormItem label="Level">
                <CheckboxGroup v-model="level">
                    <Checkbox label="high">High</Checkbox>
                    <Checkbox label="medium">Medium</Checkbox>
                    <Checkbox label="low">Low</Checkbox>
                </CheckboxGroup>
            </FormItem>
            <FormItem label="Threat Types">
                <Cascader :data="alert_types_config" v-model="alert_code" placeholder="Select threat type"></Cascader>
<!--                 <Select multiple placeholder="筛选告警类型" v-model="alert_code">
                    <OptionGroup v-for="(type_group_values, type_group_name) in alert_types_config" :label="type_group_name">
                        <Option v-for="(type_name, code) in type_group_values" :value="code">{{type_name}}</Option>
                    </OptionGroup>
                </Select> -->
            </FormItem>
            <FormItem label="Status">
                <Select v-model="status" style="width: 150px" placeholder="Select status">
                    <Option value="all">all</Option>
                    <Option value="pending">pending</Option>
                    <Option value="closed">closed</Option>
                    <Option value="mistake">mistake</Option>
                    <Option value="ignore">ignore</Option>
                    <Option value="auto_ignore">auto_ignore</Option>
                    <Option value="finished">finished</Option>
                </Select>
            </FormItem>
            <FormItem>
                <Button @click="do_filter" type="primary" icon="ios-funnel-outline">Filter</Button>
            </FormItem>
        </Form>
        <div>
            
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "detail-filter",
    data() {
        return {
        	filter_name: "",
            filter_value: "",
            status: "pending",
            level: [],
            start_time: "",
            end_time: "",
            alert_code: []
        }
    },
    computed: {
    	...mapState({
            alert_types_config: state => state.actions.alert_types_config
        })
    },
    methods: {
        do_filter() {
            this.$store.commit('set_filter_params', {
                alert_code: this.alert_code[1],
                status: this.status,
                level: this.level,
                filter_name: this.filter_name,
                filter_value: this.filter_value,
                start_time: this.start_time,
                end_time: this.end_time
            });
            this.$store.dispatch('get_activity_list');
        }
    },
    created() {
        this.$store.dispatch("get_alert_types");
    },
    components: {
    	
    }
}
</script>

<style scoped>
.detail-filter {
    background: #fff;
    padding: 30px;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
    height: 600px;
}
</style>