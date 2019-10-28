<template>
    <setting-base title="Domain Controller List" @save="save()">
        <div class="ldap-setting">
            <div class="netbios-domain-list">
                <Tag 
                    v-for="domain in domain_list" 
                    type="dot" 
                    :color="active_color(domain)"
                    style="cursor: pointer;"
                    @click.native="change_current_domain(domain)">{{netbios_domain(domain)}}</Tag>
            </div>
            <div >
                <div class="dc-list">
                    <Tag 
                        v-for="dc in current_dc_name_list" 
                        :key="current_domain + '\\' + dc" 
                        :name="current_domain + '\\' + dc" 
                        closable 
                        type="border"
                        @on-close="remove_dc_name">
                            <entry-name 
                                :value="dc" 
                                :domain="current_domain" 
                                entry_type="computer" 
                                :disable_poptip="false">  
                            </entry-name>
                    </Tag>
                </div>
            </div>
            <div style="margin-top: 20px;">
                <Input 
                    v-model="current_input" 
                    placeholder="Enter new domain controller name" 
                    style="width: 300px"
                    @keyup.enter.native="add_dc_name()">
                    <Button slot="append" icon="ios-add-circle-outline" @click="add_dc_name()"></Button>
                </Input>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
import EntryName from '@/components/common/EntryName';
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "domain-controller-list-setting",
    data() {
        return {
            current_input: "",
            current_domain: ""
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "domain_list"
        });
        this.$store.dispatch("get_setting", {
            name: "dc_name_list"
        });
    },
    watch: {
        domain_list(new_domain_list, old) {
            this.current_domain = new_domain_list[0]
        }
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        domain_list() {
            return this.setting["domain_list"];
        },
        dc_name_list() {
            return this.setting["dc_name_list"];
        },
        current_dc_name_list() {
            if (this.dc_name_list.hasOwnProperty(this.netbios_domain(this.current_domain))) {
                return this.dc_name_list[this.netbios_domain(this.current_domain)];
            } else {
                return []
            }
        }
    },
    methods: {
        save() {
            this.$store.dispatch("change_setting", {
                name: "dc_name_list",
                value: this.dc_name_list
            });
        },
        add_dc_name() {
            if (this.current_input.length == 0) {
                this.$Message.error('no input content');
                return
            } 
            this.$store.dispatch("check_entry", {
                action: "add_dc_name",
                type: "computer",
                name: this.current_input,
                domain: this.netbios_domain(this.current_domain)
            });
            this.current_input = "";
        },
        remove_dc_name(event, name) {
            let [domain, dc_name] = name.split("\\");
            this.$store.commit("remove_dc_name", {
                domain: this.netbios_domain(domain),
                name: dc_name
            })
        },
        active_color(domain) {
            if (domain == this.current_domain) {
                return "primary"
            } else {
                return
            }
        },
        change_current_domain(domain) {
            this.current_domain = domain;
        },
        netbios_domain(domain) {
            return get_netbios_domain(domain)
        }
    },
    components: {
        'setting-base': SettingBase,
        'entry-name': EntryName
    }
}
</script>

<style scoped>
.domain-controller-list-setting {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.domain-controller-list-setting>div {
    display: flex;
    align-items: center;
}

.label {
    width: 100px;
    margin-right: 20px;
}

.dc-list {
    margin-top: 20px;
    display: flex;
    flex-wrap: wrap;
}

</style>