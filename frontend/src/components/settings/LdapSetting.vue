<template>
    <setting-base title="LDAP Setting" @save="save()">
        <div class="ldap-setting">
            <div class="netbios-domain-list">
                <Tag 
                    v-for="domain in domain_list" 
                    type="dot" 
                    :color="active_color(domain)"
                    @click.native="change_current_domain(domain)">{{netbios_domain(domain)}}</Tag>
            </div>
            <div>
                <div class="label">Server</div>
                <Input v-model="server" placeholder="LDAP Server address" style="width: 300px">
                    <span slot="prepend">ldap://</span>
                </Input>
            </div>
            <div>
                <div class="label">Username</div>
                <Input v-model="user_name" placeholder="Username for ldap" style="width: 300px" />
            </div>
            <div>
                <div class="label">Password</div>
                <Input v-model="password" type="password" placeholder="Enter password" style="width: 300px" />
            </div>
            <Button style="width: 200px;" @click="testCon()">Test Connection</Button>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "ldap-setting",
    data() {
        return {
            current_domain: "",
            server: "",
            user_name: "",
            password: ""
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "domain_list"
        });
        this.$store.dispatch("get_setting", {
            name: "ldap"
        });
    },
    watch: {
        domain_list(new_domain_list, old) {
            this.current_domain = new_domain_list[0];
        },
        current_ldap(new_ldap, old) {
            this.server = new_ldap["server"].replace("ldap://", "");
            this.user_name = new_ldap["user"];
            this.password = new_ldap["password"];
        }
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        ldap() {
            return this.setting["ldap"];
        },
        current_ldap() {
            let netbios_domain = this.netbios_domain(this.current_domain);
            if (!this.ldap.hasOwnProperty(netbios_domain)) {
                return {"server": "", "user": "", "password": ""}
            } else {
                return this.ldap[netbios_domain];
            }
        },
        domain_list() {
            return this.setting["domain_list"];
        },
        format_data() {
            let domain = this.netbios_domain(this.current_domain)
            return {
                domain: {
                    server: "ldap://" + this.server,
                    user: this.user_name,
                    password: this.password,
                    dn: this.current_dn
                }
            }
        },
        current_dn() {
            let temp = [];
            let parts = this.current_domain.split(".");
            for (let part of parts) {
                temp.push("DC=" + part)
            }
            return temp.join(",");
        }
    },
    methods: {
        save() {
            this.$store.dispatch("change_setting", {
                name: "ldap",
                value: this.format_data
            });
        },
        testCon() {
            this.$store.dispatch("test_ldap_con", {
                setting: this.format_data
            });
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
        'setting-base': SettingBase
    }
}
</script>

<style scoped>
.ldap-setting {
    display: flex;
    flex-direction: column;
    height: 300px;
    justify-content: space-around;
}

.ldap-setting>div {
    display: flex;
    align-items: center;
}

.label {
    width: 100px;
    margin-right: 20px;
}

</style>