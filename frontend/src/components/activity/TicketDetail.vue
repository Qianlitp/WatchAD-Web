<template>
	<div class="ticket-content">
        <div>
            <span>票据类型：</span>
            <span class="ticket-value">{{form_data["ticket_type"]}}</span>
        </div>
        <div>
            <span>目标服务账户：</span>
            <span class="ticket-value">{{form_data["service_name"]}}</span>
        </div>
        <div v-if="exceptional_domain_show">
            <span>域名格式规范：</span>
            <span class="ticket-value">
            	<Icon v-if="!form_data['exceptional_domain_format']" type="ios-checkmark-circle-outline" size="20" color="#19be6b"/>
            	<Icon v-else type="ios-close-circle-outline" size="20" color="#ef6a6a"/>
            </span>
        </div>
        <div>
            <span>加密类型：</span>
            <span class="ticket-value">{{current_ticket_info["encryption_type"]}} ({{current_ticket_info["encryption_type_detail"]}})</span>
        </div>
        <div>
            <span>票据选项：</span>
            <div class="ticket-value ticket-options">
            	<span>{{current_ticket_info["options"]}}</span>
            	<Icon type="ios-help-circle-outline" size="20" style="margin-left: 5px;"/>
            </div>
        </div>
        <div v-if="tools_match">
        	<span>已知工具匹配：</span>
        	<span class="ticket-value"><span :class="tools_flag_class">{{tools_match}}</span></span>
        </div>
        <div>
            <span>请求结果：</span>
            <span class="ticket-value">{{current_ticket_info["status"]}}</span>
        </div>
    </div>
</template>

<script>
export default {
	name: "ticket-detail",
    props: {
        form_data: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            
        }
    },
    computed: {
        current_ticket_info() {
            return this.form_data["ticket_info"];
        },
        options_detail() {
        	let result = []
        	for (let each of this.current_ticket_info["options_detail"]) {
        		result.push(each["name"])
        	}
        	return result.join("，");
        },
        tools_match() {
            if (!this.form_data.hasOwnProperty("kekeo_flag")) {
                return false;
            }

        	let tools = ["kekeo_flag", "impacket_flag"];
        	for (let one of tools) {
        		if (this.form_data[one]) {
        			return one.replace("_flag", "");
        		}
        	}
        	return "无";
        },
        exceptional_domain_show() {
            if (!this.form_data.hasOwnProperty("exceptional_domain_format")) {
                return false;
            } else {
                return true;
            }
        },
        tools_flag_class() {
            if (this.tools_match && this.tools_match != "无") {
                return {
                    "tools-flag": true
                }
            }
        }
    },
    methods: {

    }
}
</script>

<style scoped>
.ticket-content {
    color: #a4a6a9;
}

.ticket-content>div {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

.ticket-value {
	width: 180px;
}

.ticket-options {
	display: flex;
	flex-direction: row;
	align-items: center;
}

.tools-flag {
    color: #f90;
    font-weight: 700;
}
</style>