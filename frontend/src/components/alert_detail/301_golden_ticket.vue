<template>
    <div class="golden-ticket">
        <common-table alert_code="301" :alert_list="alert_list" :column_list="column_list" @row_click="row_click"></common-table>
        <div class="detail">
            <div class="ticket-detail">
                <Card>
                    <p slot="title" class="detail-title">票据详情</p>
                    <ticket-detail :form_data="current_form_data"></ticket-detail>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
import CommonTable from './CommonTable';
import TicketDetail from '@/components/activity/TicketDetail';
export default {
	name: "golden-ticket",
    props: {
        alert_list: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
        	index: 0,
            column_list: ["source_ip", "source_workstation", "target_user_name", "service_name", "login_ip"]
        }
    },
    created() {

    },
    computed: {
        current_form_data() {
            return this.alert_list[this.index]["form_data"]
        }
    },
    methods: {
        row_click(params) {
            this.index = params["index"];
        }
    },
    components: {
    	"ticket-detail": TicketDetail,
        "common-table": CommonTable
    }
}
</script>

<style scoped>
.detail {
    margin-top: 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.ticket-detail {
    width: 40%;
}

.detail-title {
    color: #8a8a8a;
}

.ticket-content {
    color: #a4a6a9;
}
</style>