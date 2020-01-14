<template>
    <div class="exceptional-ticket">
        <common-table :alert_list="alert_list" :column_list="column_list" @row_click="row_click"></common-table>
        <div class="detail">
            <div class="ticket-detail">
                <Card>
                    <p slot="title" class="detail-title">票据详情</p>
                    <ticket-detail :ticket_doc="current_form_data['ticket_doc']"></ticket-detail>
                </Card>
            </div>
            <div class="ticket-detail">
                <Card>
                    <p slot="title" class="detail-title">异常原因</p>
                    <template v-for="item in exceptional_data">
                        <Tag color="default">{{item["value"]}}</Tag>
                        <p>{{item["reason"]}}</p>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
import {entries} from '@/assets/js/common.js';
import CommonTable from './CommonTable';
import TicketDetail from '@/components/activity/TicketDetail';
export default {
	name: "exceptional-ticket",
    props: {
        alert_list: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
        	index: 0,
            column_list: ["source_ip", "source_workstation", "target_user_name"]
        }
    },
    created() {

    },
    computed: {
        current_form_data() {
            return this.alert_list[this.index]["form_data"]
        },
        exceptional_data() {
            return this.current_form_data["exceptional_data"];
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
    width: 48%;
    color: #8a8a8a;
}

.detail-title {
    color: #8a8a8a;
}

.ticket-content {
    color: #a4a6a9;
}
</style>