<template>
    <div class="modify-acl">
        <common-table :alert_list="alert_list" :column_list="column_list" @row_click="row_click"></common-table>
        <div class="detail">
            <div class="detail-title">异常ACL详情</div>
            <div class="acl-object">
                <div>ACL主体</div>
                <div>DN： {{object_info["dn"]}}</div>
                <div>Group SID： {{acl_info["group_sid"]}}</div>
                <div>Owner SID： {{acl_info["owner_sid"]}}</div>
            </div>
            <ace-detail :form_data="current_form_data"></ace-detail>
        </div>
    </div>
</template>

<script>
import AceDetail from '@/components/activity/AceDetail';
import CommonTable from '@/components/alert_detail/CommonTable';
export default {
	name: "modify-acl",
    props: {
        alert_list: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
        	index: 0,
            column_list: ["source_ip", "source_workstation", "source_user_name", "object_class", "abnormal_users"]
        }
    },
    computed: {
        current_form_data() {
            return this.alert_list[this.index]["form_data"]
        },
        acl_info() {
            return this.current_form_data["parsed_sddl"]
        },
        object_info() {
            return this.current_form_data["object_info"]
        }
    },
    methods: {
        row_click(params) {
            this.index = params["index"];
        }
    },
    components: {
    	"common-table": CommonTable,
        "ace-detail": AceDetail
    }
}
</script>

<style scoped>
.detail {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
}

.detail-title {
    font-size: 25px;
    margin: 10px 0px 10px -20px;
}

.acl-object {
    font-size: 15px;
    margin-top: 20px;
    margin-bottom: 20px;
}
</style>