<template>
	<div class="ticket-content">
        <div>
            <span>KVNO：</span>
            <span class="ticket-value">{{ticket_doc["KVNO"]}}</span>
        </div>
        <div>
            <span>TktVNO：</span>
            <span class="ticket-value">{{ticket_doc["TktVNO"]}}</span>
        </div>
        <div>
            <span>加密类型：</span>
            <span class="ticket-value">{{ticket_doc["encryption_type"]}} ({{ticket_doc["etype"]}})</span>
        </div>
        <div>
            <span>Realm：</span>
            <span class="ticket-value">{{ticket_doc["realm"]}}</span>
        </div>
        <div>
            <span>票据Hash：</span>
            <span class="ticket-value">{{ticket_doc["ticket_hash"]}}</span>
        </div>
<!--         <div>
            <span>票据选项：</span>
            <div class="ticket-value ticket-options">
            	<span>{{ticket_doc["options"]}}</span>
            	<Icon type="ios-help-circle-outline" size="20" style="margin-left: 5px;"/>
            </div>
        </div> -->
    </div>
</template>

<script>
export default {
	name: "ticket-detail",
    props: {
        ticket_doc: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            
        }
    },
    computed: {
        options_detail() {
        	let result = []
        	for (let each of this.ticket_doc["options_detail"]) {
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
	width: 300px;
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