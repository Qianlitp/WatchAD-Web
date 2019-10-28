<template>
    <div class="down-encryption">
        <common-table alert_code="201" :alert_list="alert_list" :column_list="column_list" @row_click="row_click"></common-table>
        <div class="detail">
            <div class="ticket-detail">
                <Card>
                    <p slot="title" class="detail-title">票据详情</p>
                    <ticket-detail :form_data="current_form_data"></ticket-detail>
                </Card>
            </div>
            <div class="spn-list">
                <Card>
                    <p slot="title" class="detail-title">servicePrincipalName（SPN）列表</p>
                    <p :class="high_risk_class(one)" v-for="one in current_spn">{{one}}</p>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
import CommonTable from './CommonTable';
import TicketDetail from '@/components/activity/TicketDetail';
export default {
	name: "down-encryption",
    props: {
        alert_list: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            index: 0,
            column_list: ["source_ip", "source_workstation", "target_user_name", "service_name", "encryption"]
        }
    },
    created() {

    },
    computed: {
        current_form_data() {
            return this.alert_list[this.index]["form_data"]
        },
        current_spn() {
            return this.current_form_data["spn_list"];
        },
        current_high_risk_spn() {
            return this.current_form_data["has_high_risk_spn"];
        }
    },
    methods: {
        high_risk_class(spn) {
            if (this.current_high_risk_spn.includes(spn)) {
                return {"high-risk": true}
            } else {
                return {"high-risk": false}
            }
        },
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

.spn-list {
    width: 45%;
}

.detail-title {
    color: #8a8a8a;
}

.high-risk {
    color: #ef6a6a;
    font-weight: 700;
}

.ticket-content {
    color: #a4a6a9;
}
</style>