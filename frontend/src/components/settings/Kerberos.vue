<template>
    <setting-base title="Kerberos" @save="save()">
        <div class="kerberos">
            <div class="expire">
                <div class="title">Ticket Lifetime</div>
                <div>
                    <div class="label">TGT maximum lifetime</div>
                    <InputNumber :min="1" v-model="tgt_expire"></InputNumber>
                    <div style="margin-left: 5px;">hours</div>
                </div>
                <div>
                    <div class="label">ST maximum lifetime</div>
                    <InputNumber :min="1" v-model="st_expire"></InputNumber>
                    <div style="margin-left: 5px;">mins</div>
                </div>
            </div>
            <div class="spn_list">
                <div class="title">High Risk SPN Prefix</div>
                <div>
                    <Tag 
                    v-for="spn_prefix in high_risk_spn_prefix" 
                    :key="spn_prefix" 
                    :name="spn_prefix" 
                    closable 
                    type="border"
                    @on-close="remove_spn_prefix">{{ spn_prefix }}</Tag>
                </div>
                <div>
                    <Input 
                        v-model="input_spn_prefix" 
                        placeholder="enter spn prefix" 
                        style="width: 200px" 
                        search 
                        enter-button="Add"
                        @on-search="add_spn_prefix()"/>
                </div>
            </div>
            <div class="delegation_list">
                <div class="title">High Risk Delegation Prefix</div>
                <div>
                    <Tag 
                    v-for="delegation_prefix in high_risk_delegation_prefix" 
                    :key="delegation_prefix" 
                    :name="delegation_prefix" 
                    closable 
                    type="border"
                    @on-close="remove_delegation_prefix">{{ delegation_prefix }}</Tag>
                </div>
                <div>
                    <Input 
                        v-model="input_delegation_prefix" 
                        placeholder="enter delegation prefix" 
                        style="width: 200px" 
                        search 
                        enter-button="Add"
                        @on-search="add_delegation_prefix()"/>
                </div>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex';
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "kerberos",
    data() {
        return {
            input_spn_prefix: "",
            input_delegation_prefix: ""
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "kerberos"
        });
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        kerberos() {
            return this.setting["kerberos"]
        },
        tgt_expire: {
            get() {
                return this.kerberos["TGT_maximum_lifetime"]
            },
            set(value) {
                this.$store.commit("set_tgt_expire", {
                    value: value 
                })
            }
        },
        st_expire: {
            get() {
                return this.kerberos["ST_maximum_lifetime"]
            },
            set(value) {
                this.$store.commit("set_st_expire", {
                    value: value 
                })
            }
        },
        high_risk_spn_prefix() {
            return this.kerberos["high_risk_spn_prefix"]
        },
        high_risk_delegation_prefix() {
            return this.kerberos["high_risk_delegation_prefix"]
        },
        format_data() {
            return {
                "TGT_maximum_lifetime": this.tgt_expire,
                "ST_maximum_lifetime": this.st_expire,
                "high_risk_spn_prefix": this.high_risk_spn_prefix,
                "high_risk_delegation_prefix": this.high_risk_delegation_prefix
            }
        }
    },
    methods: {
        save() {
            this.$store.dispatch("change_setting", {
                name: "kerberos",
                value: this.format_data
            });
        },
        add_spn_prefix() {
            this.$store.commit("add_spn_prefix", {
                prefix: this.input_spn_prefix
            });
            this.input_spn_prefix = ""
        },
        add_delegation_prefix() {
            this.$store.commit("add_delegation_prefix", {
                prefix: this.input_delegation_prefix
            })
            this.input_delegation_prefix = ""
        },
        remove_spn_prefix(event, name) {
            this.$store.commit("remove_spn_prefix", {
                prefix: name
            });
        }, 
        remove_delegation_prefix(event, name) {
            this.$store.commit("remove_delegation_prefix", {
                prefix: name
            })
        }
    },
    components: {
        'setting-base': SettingBase
    }
}
</script>

<style scoped>
.kerberos {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.kerberos>div {
    margin-bottom: 20px;
}

.expire>div {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.raw-data>div {
    display: flex;
    align-items: center;
}

.label {
    margin-right: 20px;
    font-size: 14px;
}

.spn_list>div {
    margin-bottom: 20px;
}

.delegation_list>div {
    margin-bottom: 20px;
}

.title {
    font-size: 16px;
    padding-bottom: 5px;
    border-bottom: solid 1px #97979747;
}
</style>