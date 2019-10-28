<template>
    <setting-base title="Honeypot Account" @save="save()">
        <div class="honeypot-account">
            <div class="account-list">
                <Tag 
                    v-for="account in honeypot_account" 
                    :key="account['sid']" 
                    :name="account['sid']" 
                    closable 
                    type="border"
                    @on-close="remove_account">
                        <entry-name 
                            :value="account['name']" 
                            :domain="account['domain']" 
                            entry_type="user" 
                            :disable_poptip="false">  
                        </entry-name>
                </Tag>
            </div>
            <div class="add-input">
                <div>Add honeypot account:</div>
                <Select v-model="input_domain" style="width:150px" placeholder="select domain">
                    <Option v-for="domain in domain_list" :value="domain" :key="domain">{{ domain }}</Option>
                </Select>
                <Input v-model="input_account" placeholder="enter entry name" style="width: 200px" />
                <Button type="primary" icon="ios-add-circle-outline" @click="add_honeypot_account()">Add</Button>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import EntryName from '@/components/common/EntryName';
import {mapState} from 'vuex';
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "honeypot-account",
    data() {
        return {
            input_domain: "",
            input_account: ""
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "domain_list"
        });
        this.$store.dispatch("get_setting", {
            name: "honeypot_account"
        });
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        domain_list() {
            return this.setting["domain_list"]
        },
        honeypot_account() {
            return this.setting["honeypot_account"]
        },
        format_data() {
            return this.honeypot_account
        }
    },
    methods: {
        save() {
            this.$store.dispatch("change_setting", {
                name: "honeypot_account",
                value: this.format_data
            });
        },
        remove_account() {
            this.$store.commit("remove_honeypot_account", {
                sid: name
            })
        },
        add_honeypot_account() {
            if (this.input_domain.length == 0) {
                this.$Message.error('no domain select');
                return
            } else if (this.input_account.length == 0) {
                this.$Message.error('no account input');
                return
            }
            this.$store.dispatch("check_entry", {
                action: "add_honeypot_account",
                type: "user",
                name: this.input_account,
                domain: this.netbios_domain(this.input_domain)
            });
            this.input_account = "";
            this.input_domain = "";
        },
        netbios_domain(domain){
            return get_netbios_domain(domain);
        }
    },
    components: {
        'setting-base': SettingBase,
        'entry-name': EntryName
    }
}
</script>

<style scoped>
.honeypot-account {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.add-input {
    margin-top: 20px;
    display: flex;
    align-items: center;
}

.add-input>div {
    margin-right: 10px;
}

.account-list {
    display: flex;
    flex-wrap: wrap;
}
</style>