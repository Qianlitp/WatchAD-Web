<template>
    <setting-base title="Raw Data Expire" @save="save()">
        <div class="raw-data">
            <div>
                <div class="label">DC event log data expire</div>
                <InputNumber :min="7" v-model="log_expire"></InputNumber>
                <div style="margin-left: 5px;">days</div>
            </div>
            <div>
                <div class="label">DC krb5 traffic data expire</div>
                <InputNumber :min="7" v-model="krb5_expire"></InputNumber>
                <div style="margin-left: 5px;">days</div>
            </div>
            <div>
                <div class="label">Krb5 tickets records expire</div>
                <InputNumber :min="7" v-model="krb5_ticket"></InputNumber>
                <div style="margin-left: 5px;">days</div>
            </div>
            <div>
                <div class="label">User activity records expire</div>
                <InputNumber :min="7" v-model="user_activity"></InputNumber>
                <div style="margin-left: 5px;">days</div>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex';
export default {
    name: "raw-data",
    data() {
        return {
            log_expire: 0,
            krb5_expire: 0,
            krb5_ticket: 0,
            user_activity: 0
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "raw_data_expire"
        });
    },
    watch: {
        raw_data_expire(new_data, old) {
            this.log_expire = new_data["dc_log"];
            this.krb5_expire = new_data["dc_krb5"];
            this.krb5_ticket = new_data["krb5_ticket"];
            this.user_activity = new_data["user_activity"];
        }
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        raw_data_expire() {
            return this.setting["raw_data_expire"]
        },
        format_data() {
            return {
                "dc_log": this.log_expire,
                "dc_krb5": this.krb5_expire,
                "krb5_ticket": this.krb5_ticket,
                "user_activity": this.user_activity
            }
        }
    },
    methods: {
        save() {
            this.$store.dispatch("change_setting", {
                name: "raw_data_expire",
                value: this.format_data
            });
        }
    },
    components: {
        'setting-base': SettingBase
    }
}
</script>

<style scoped>
.raw-data {
    display: flex;
    flex-direction: column;
    height: 200px;
    justify-content: space-around;
}

.raw-data>div {
    display: flex;
    align-items: center;
}

.label {
    margin-right: 20px;
    font-size: 14px;
}
</style>