<template>
    <div class="ntlm-login">
        <div class="description">
            <description-base :render_func="description"></description-base>
        </div>
        <div class="other-info">
            <div>Domain: <span>{{domain}}</span></div>
            <div>|</div>
            <div>Source Workstation: <entry-name 
                    :value="workstation" 
                    entry_type="computer" 
                    :disable_poptip="false"
                    :domain="domain">{{workstation}}</entry-name></div>
            <div>|</div>
            <div>Source IpAddress: <span>{{ip}}</span></div>
            <div>|</div>
            <div>DC: 
                <entry-name 
                    :value="dc_hostname" 
                    entry_type="computer" 
                    :disable_poptip="false"
                    :domain="domain">{{dc_hostname}}</entry-name>
            </div>
            <div>|</div>
            <div>Logon Type: <span>{{logon_type}}</span></div>
            <div>|</div>
            <div>Logon Id: <span>{{logon_id}}</span></div>
            <div>|</div>
            <div>Lm Package Name: <span>{{lm_package_name}}</span></div>
        </div>
    </div>
</template>

<script>
import EntryName from '@/components/common/EntryName';
import DescriptionBase from './DescriptionBase';
import {mapState} from 'vuex';

export default {
    props: {
        record: {
            type: Object,
            required: true
        }
    },
    name: "ntlm-login",
    data(){
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            name: state => state.index.entry_name,
            domain: state => state.index.domain
        }),
        description() {
            let that = this;
            return function (createElement) {
                let result_list = [];
                result_list.push("用户 ")
                result_list.push(
                    createElement(
                        EntryName, 
                        {
                            props: {
                                value: that.user_name,
                                domain: that.domain,
                                disable_poptip: false,
                                entry_type: "user"
                            }
                        }
                    )
                )
                result_list.push(" 使用NTLM协议登录成功 ")
                return createElement(
                    'div', result_list
                )
            }
        },
        user_name() {
            return this.record["user_name"]
        },
        domain() {
            return this.record["domain"]
        },
        dc_hostname() {
            return this.record["dc_name"];
        },
        workstation() {
            return this.record["data"]["source_workstation"];
        },
        logon_type() {
            return this.record["data"]["logon_type"]
        },
        logon_id() {
            return this.record["data"]["logon_id"]
        },
        ip() {
            return this.record["data"]["ip"]
        },
        lm_package_name() {
            return this.record["data"]["lm_package_name"]
        }
    },
    methods: {
        
    },
    components: {
        "entry-name": EntryName,
        "description-base": DescriptionBase
    }
}
</script>

<style scoped>

.other-info {
    display: flex;
    flex-direction: row;
    color: #8DABC4;
}

.other-info>div {
    margin-right: 10px;
}

.other-info span {
    color: rgba(37,37,37,0.80);
}

.description {
    font-size: 14px;
}
</style>