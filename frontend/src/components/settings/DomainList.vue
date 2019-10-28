<template>
    <setting-base title="Domain List" @save="save()">
        <div class="domain-list">
            <div class="domain-tags">
                <Tag 
                    v-for="domain in current_domain_list"
                    type="dot" 
                    closable 
                    color="primary"
                    @on-close="remove_domain"
                    >{{domain}}</Tag>
            </div>
            <div style="margin-top: 20px;">
                <Input 
                    v-model="input_domain" 
                    placeholder="Enter FQDN domain" 
                    style="width: 300px"
                    @keyup.enter.native="add_domain()">
                    <Button slot="append" icon="ios-add-circle-outline" @click="add_domain()"></Button>
                </Input>
            </div>
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
export default {
    name: "domain-list",
    data() {
        return {
            input_domain: "",
            current_domain_list: []
        }
    },
    mounted() {
        this.$store.dispatch("get_setting", {
            name: "domain_list"
        });
    },
    watch: {
        domain_list: function(new_domain_list, old) {
            this.current_domain_list = this.current_domain_list.concat(new_domain_list);        
        }
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        domain_list() {
            return this.setting["domain_list"];
        }
    },
    methods: {
        save() {
            if (this.current_domain_list == this.domain_list) {
                this.$Message.error('no changes.');
                return
            }
            if (this.current_domain_list.length == 0) {
                this.$Message.error('no domain input.');
                return
            }
            this.$store.dispatch("change_setting", {
                name: "domain_list",
                value: this.current_domain_list
            })
            this.current_domain_list = []
        },
        add_domain() {
            if (this.input_domain == "" || this.input_domain.includes(".") < 1) {
                this.$Message.error('Invalide domain format.');
                return
            }
            this.current_domain_list.push(this.input_domain);
            this.input_domain = "";
        },
        remove_domain(_, name) {
            this.current_domain_list.splice(this.current_domain_list.findIndex(item => item === name), 1)
        }
    },
    components: {
        'setting-base': SettingBase
    }
}
</script>

<style scoped>
.domain-list {

}

.domain-tags {
    display: flex;
    flex-wrap: wrap;
}

</style>