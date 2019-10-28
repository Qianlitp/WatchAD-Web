<template>
    <div class="access-entry">
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
            <div>Service: <span>{{service}}</span></div>
            <div>|</div>
            <div>DC: 
                <entry-name 
                    :value="dc_hostname" 
                    entry_type="computer" 
                    :disable_poptip="false"
                    :domain="domain">{{dc_hostname}}</entry-name>
            </div>
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
    name: "access-entry",
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
        is_passive() {
            return this.name == this.record["data"]["target_user_name"]
        },
        description() {
            let that = this;
            if (this.is_passive) {
                return function (createElement) {
                    let result_list = [];
                    result_list.push("当前用户 ")
                    result_list.push(
                        createElement(
                            EntryName, 
                            {
                                props: {
                                    value: that.target_user_name,
                                    domain: that.domain,
                                    disable_poptip: false,
                                    entry_type: "user"
                                }
                            }
                        )
                    )
                    result_list.push(" 被 ")
                    result_list.push(
                        createElement(
                            EntryName, 
                            {
                                props: {
                                    value: that.source_user_name,
                                    domain: that.domain,
                                    disable_poptip: false,
                                    entry_type: "user"
                                }
                            }
                        )
                    )
                    result_list.push(" 访问接触")
                    return createElement(
                        'div', result_list
                    )
                }
            } else {
                return function (createElement) {
                    let result_list = [];
                    result_list.push("当前用户 ")
                    result_list.push(
                        createElement(
                            EntryName, 
                            {
                                props: {
                                    value: that.source_user_name,
                                    domain: that.domain,
                                    disable_poptip: false,
                                    entry_type: "user"
                                }
                            }
                        )
                    )
                    result_list.push(" 访问了用户 ")
                    result_list.push(
                        createElement(
                            EntryName, 
                            {
                                props: {
                                    value: that.target_user_name,
                                    domain: that.domain,
                                    disable_poptip: false,
                                    entry_type: "user"
                                }
                            }
                        )
                    )
 
                    return createElement(
                        'div', result_list
                    )
                }
            }
        },
        source_user_name() {
            return this.record["data"]["source_user_name"]
        },
        target_user_name() {
            return this.record["data"]["target_user_name"]
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
        service() {
            return this.record["data"]["service_name"]
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