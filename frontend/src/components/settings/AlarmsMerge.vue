<template>
    <setting-base title="Alarms Merge" @save="save()">
        <div class="alarms-merge">
            <div>
                <div class="label">Threat Activity Merge</div>
                <InputNumber :min="1" v-model="activity_merge_input" style="width: 50px;"></InputNumber>
                <div style="margin-left: 5px;">hours</div>
            </div>
            <div style="margin-top: 20px;">
                <div class="label">Invasion Merge</div>
                <InputNumber :min="1" v-model="invasion_merge_input" style="width: 50px;"></InputNumber>
                <div style="margin-left: 5px;">hours</div>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
export default {
    name: "alarms-merge",
    data() {
        return {
            activity_merge_input: 1,
            invasion_merge_input: 1
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "alarms_merge"
        });
    },
    watch: {
        alarms_merge: function(new_data, old) {
            this.activity_merge_input = new_data["activity"];
            this.invasion_merge_input = new_data["invasion"];  
        }
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        alarms_merge() {
            return this.setting["alarms_merge"];
        },
        form_data() {
            return {
                "activity": this.activity_merge_input,
                "invasion": this.invasion_merge_input
            }
        }
    },
    methods: {
        save() {
            if (!this.activity_merge_input || this.activity_merge_input < 1) {
                this.$Message.error('alarms merge number must be greater than 1 ');
                return
            }
            if (!this.invasion_merge_input || this.invasion_merge_input < 1) {
                this.$Message.error('alarms merge number must be greater than 1 ');
                return
            }
            this.$store.dispatch("change_setting", {
                name: "alarms_merge",
                value: this.form_data
            })
        }
    },
    components: {
        'setting-base': SettingBase
    }
}
</script>

<style scoped>
.alarms-merge {

}

.alarms-merge>div {
    display: flex;
    align-items: center;
}

.label {
    margin-right: 20px;
    font-size: 14px;
}

</style>