<template>
    <setting-base title="Sensitive Entry" @save="save()">
        <div class="sensitive-entry">
            <div class="user">
                <div class="title">Users</div>
                <div class="entries">
                    <Tag 
                        v-for="user in sensitive_entry['user']" 
                        :key="user['domain'] + '\\' + user['name']" 
                        :name="user['domain'] + '\\' + user['name']" 
                        closable 
                        type="border"
                        @on-close="remove_user">
                            <entry-name 
                                :value="user['name']" 
                                :domain="user['domain']" 
                                entry_type="user" 
                                :disable_poptip="false">  
                            </entry-name>
                    </Tag>
                </div>
            </div>
            <div class="group">
                <div class="title">Groups</div>
                <div class="entries">
                    <Tag 
                        v-for="group in sensitive_entry['group']" 
                        :key="group['domain'] + '\\' + group['name']" 
                        :name="group['domain'] + '\\' + group['name']" 
                        closable 
                        type="border"
                        @on-close="remove_group">
                            <entry-name 
                                :value="group['name']" 
                                :domain="group['domain']" 
                                entry_type="group" 
                                :disable_poptip="false">  
                            </entry-name>
                    </Tag>
                </div>
            </div>
            <div class="computer">
                <div class="title">Computers</div>
                <div class="entries">
                    <Tag 
                        v-for="computer in sensitive_entry['computer']" 
                        :key="computer['domain'] + '\\' + computer['name']" 
                        :name="computer['domain'] + '\\' + computer['name']" 
                        closable 
                        type="border"
                        @on-close="remove_computer">
                            <entry-name 
                                :value="computer['name']" 
                                :domain="computer['domain']" 
                                entry_type="computer" 
                                :disable_poptip="false">  
                            </entry-name>
                    </Tag>
                </div>
            </div>
            <div class="add-input">
                <div>Add sensitive entry:</div>
                <Select v-model="input_entry_type" style="width:150px" placeholder="select entry type">
                    <Option v-for="domain in entry_types" :value="domain" :key="domain">{{ domain }}</Option>
                </Select>
                <Select v-model="input_domain" style="width:150px" placeholder="select domain">
                    <Option v-for="domain in domain_list" :value="domain" :key="domain">{{ domain }}</Option>
                </Select>
                <Input v-model="input_entry_name" placeholder="enter entry name" style="width: 200px" />
                <Button type="primary" icon="ios-add-circle-outline" @click="add_entry()">Add</Button>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import EntryName from '@/components/common/EntryName';
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
import {mapState} from 'vuex';
export default {
    name: "sensitive-entry",
    data() {
        return {
            entry_types: ["user", "group", "computer"],
            input_entry_type: "",
            input_domain: "",
            input_entry_name: ""
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "domain_list"
        });
        this.$store.dispatch("get_setting", {
            name: "sensitive_entry"
        });
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        domain_list() {
            return this.setting["domain_list"]
        },
        sensitive_entry() {
            return this.setting["sensitive_entry"]
        },
        format_data() {
            return {
                "user": this.sensitive_entry["user"],
                "group": this.sensitive_entry["group"],
                "computer": this.sensitive_entry["computer"]
            }
        }
    },
    methods: {
        save() {
            this.$store.dispatch("change_setting", {
                name: "sensitive_entry",
                value: this.format_data
            });
        },
        add_entry() {
            if (this.input_entry_type.length == 0) {
                this.$Message.error('no entry type select');
                return
            } else if (this.input_domain.length == 0) {
                this.$Message.error('no domain select');
                return
            } else if (this.input_entry_name.length == 0) {
                this.$Message.error('no entry name input');
                return
            }
            this.$store.dispatch("check_entry", {
                action: "add_entry",
                type: this.input_entry_type,
                name: this.input_entry_name,
                domain: this.netbios_domain(this.input_domain)
            });
            this.input_entry_type = "";
            this.input_entry_name = "";
            this.input_domain = "";
        },
        remove_user(event, name) {
            let [domain, entry_name] = name.split("\\");
            this.$store.commit("remove_entry", {
                type: "user",
                domain: domain,
                name: entry_name
            })
        },
        remove_group(event, name) {
            let [domain, entry_name] = name.split("\\");
            this.$store.commit("remove_entry", {
                type: "group",
                domain: domain,
                name: entry_name
            })
        },
        remove_computer(event, name) {
            let [domain, entry_name] = name.split("\\");
            this.$store.commit("remove_entry", {
                type: "computer",
                domain: domain,
                name: entry_name
            })
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
.sensitive-entry {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.sensitive-entry>div {
    margin-bottom: 20px;
}

.add-input {
    margin-top: 20px;
    display: flex;
    align-items: center;
}

.add-input>div {
    margin-right: 10px;
}

.title {
    padding-bottom: 5px;
    border-bottom: solid 1px #97979747;
}

.entries {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
}
</style>