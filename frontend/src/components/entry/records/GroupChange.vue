<template>
    <div class="group-change">
        <div class="description">
            <description-base :render_func="description"></description-base>
        </div>
        <div class="other-info">
            <div>Domain: <span>{{domain}}</span></div>
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
    name: "group-change",
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
            if (this.operator_type == 'add') {
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
                    result_list.push(" 被添加到了用户组 ")
                    result_list.push(
                        createElement(
                            EntryName, 
                            {
                                props: {
                                    value: that.group_name,
                                    domain: that.domain,
                                    disable_poptip: false,
                                    entry_type: "group"
                                }
                            }
                        )
                    )
                    result_list.push(" 中")
                    return createElement(
                        'div', result_list
                    )
                }
            } else {
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
                    result_list.push(" 被从用户组 ")
                    result_list.push(
                        createElement(
                            EntryName, 
                            {
                                props: {
                                    value: that.group_name,
                                    domain: that.domain,
                                    disable_poptip: false,
                                    entry_type: "group"
                                }
                            }
                        )
                    )
                    result_list.push(" 中移除")
                    return createElement(
                        'div', result_list
                    )
                }
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
        operator_type() {
            return this.record["data"]["operator_type"];
        },
        group_name() {
            return this.record["data"]["group_name"]
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