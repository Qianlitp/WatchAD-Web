<template>
    <div class="record-item">
        <div class="record-time">
            {{time}}
        </div>
        <div class="record-content">
            <access-entry v-if="record['activity_type'] == 'access_entry'" :record="record"></access-entry>
            <ntlm-login v-else-if="record['activity_type'] == 'ntlm_login'" :record="record"></ntlm-login>
            <group-change v-else-if="record['activity_type'] == 'group_change'" :record="record"></group-change>
            <account-attr v-else-if="record['activity_type'] == 'account_attr'" :record="record"></account-attr>
            <spn-change v-else-if="record['activity_type'] == 'spn_change'" :record="record"></spn-change>
        </div>
    </div>
</template>

<script>
import AccountAttr from './records/AccountAttr';
import AccessEntry from './records/AccessEntry';
import GroupChange from './records/GroupChange';
import NTLMLogin from './records/NTLMLogin';
import SPNChange from './records/SPNChange';
import {mapState} from 'vuex';

export default {
    props: {
        record: {
            type: Object,
            required: true
        }
    },
    name: "record-item",
    data(){
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            
        }),
        time() {
            let d = new Date(this.record["@timestamp"])
            let seconds = d.getSeconds();
            if (seconds < 10) {
                seconds = "0" + seconds
            }
            return d.getHours() + ":" + d.getMinutes() + ":" + seconds
        }
    },
    methods: {
        
    },
    components: {
        "account-attr": AccountAttr,
        "access-entry": AccessEntry,
        "ntlm-login": NTLMLogin,
        "group-change": GroupChange,
        "spn-change": SPNChange
    }
}
</script>

<style scoped>
.record-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 78px;
    border-bottom: 1px solid #E5EEF5;
}

.record-time {
    font-size: 12px;
    color: #8DABC4;
    width: 80px;
    margin-left: 30px;
}

.record-content>div {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    height: 78px;
    padding: 10px 0px;
}

</style>