<template>
    <div class="exceptional-ticket">
        <common-table :alert_list="alert_list" :column_list="column_list" @row_click="row_click"></common-table>
        <div class="detail">
            <div class="ticket-detail">
                <Card>
                    <p slot="title" class="detail-title">票据详情</p>
                    <ticket-detail :form_data="current_form_data"></ticket-detail>
                </Card>
            </div>
            <div class="ticket-detail">
                <Card>
                    <p slot="title" class="detail-title">异常原因</p>
                    <template v-for="name in exception_name">
                        <Tag color="default">{{exceptional_data[name]}}</Tag>
                        <p>{{exceptional_data[name + '_reason']}}</p>
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
            column_list: ["source_ip", "source_workstation", "target_user_name", "exceptional_type"]
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
        },
        exception_name() {
            let result = [];
            for (let [key, value] of entries(this.exceptional_data)) {
                if (!key.includes("reason")) {
                    result.push(key);
                }
            }
            return result;
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
    color: #8a8a8a;
}

.detail-title {
    color: #8a8a8a;
}

.ticket-content {
    color: #a4a6a9;
}
</style>