<template>
    <Poptip trigger="hover" placement="right" :transfer="true" :disabled="disable_poptip" @on-popper-show="search()">
        <div class="multi-entry-item" :class="{'active': is_hover}" @mouseover="mouse_over" @mouseout="mouse_out" @click="detail">
            <div class="entry-info">
                <div class="item-icon">
                    <Icon :custom="real_icon_name" :size="26" color="#9dbad8"></Icon>
                    <Icon title="管理员权限" v-if="is_sensitive" color="#19be6b" class="avatar-privilege" size="17" custom="iconfont icon-privilege-o" />
                    <Icon title="禁用账户" v-if="is_disabled" color="#FB2C2C" type="ios-remove-circle" class="avatar-disabled" size="17" />
                </div>
                <div class="item-value">
                    <div class="name">
                        <span>{{name}}</span>
                        <span v-if="other_info" class="other-info">{{other_info}}</span>
                    </div>
                    <div class="second-text">{{second_text}}</div>
                    <div style="font-size: 5px;" class="domain">{{domain}}</div>
                </div>
            </div>
            <div v-if="alert_count_show" class="alert-count">
                <alert-count :count="alert_count"></alert-count>
            </div>
        </div>
        <div slot="content">
            <user-entry v-if="entry_type == 'user'" :name="name" :domain="domain"></user-entry>
            <computer-entry v-else-if="entry_type == 'computer'" :name="name" :domain="domain"></computer-entry>
            <group-entry v-else-if="entry_type == 'group'" :name="name" :domain="domain"></group-entry>
        </div>
    </Poptip>
</template>

<script>
import {mapState} from 'vuex'
import AlertCount from './AlertCount'
import UserEntry from '@/components/common/UserEntry';
import ComputerEntry from '@/components/common/ComputerEntry';
import GroupEntry from '@/components/common/GroupEntry';
export default {
	name: "multi-entry-item",
    props: {
        icon_name: {
            type: String
        },
        name: {
            type: String,
            required: true
        },
        entry_type: {
            type: String
        },
        second_text: {
            type: String
        },
        domain: {
            type: String,
            required: true
        },
        alert_count: {
            type: Number,
            default: 0
        },
        is_sensitive: {
            type: Boolean
        },
        is_disabled: {
            type: Boolean
        },
        disable_poptip: {
            type: Boolean,
            default: true
        },
        other_info: {
            type: String
        }
    },
    data() {
        return {
        	is_hover: false
        }
    },
    computed: {
    	...mapState({
            entries: state => state.entry.entries
        }),
        alert_count_show() {
            return this.alert_count != 0;
        },
        real_icon_name() {
            if (this.entry_type == "computer") {
                return "iconfont icon-computer"
            } else if (this.entry_type == "user") {
                return "iconfont icon-user"
            } else if (this.entry_type == "group") {
                return "iconfont icon-group"
            } else {
                return this.icon_name
            }
        }
    },
    methods: {
        mouse_over() {
            this.is_hover = true;
        },
        mouse_out() {
            this.is_hover = false;
        },
        search() {
            if (this.entries.hasOwnProperty(this.name)) {
                return
            }
            this.$store.dispatch("search_entry", {
                domain: this.domain,
                name: this.name,
                type: this.entry_type
            })
        },
        detail() {
            if (!["user", "group", "computer"].includes(this.entry_type)) {
                return
            }
            window.open("/entry.html#/" + this.entry_type + "/" + this.domain + "/" + this.name)
        }
    },
    created() {

    },
    components: {
        "alert-count": AlertCount,
        "user-entry": UserEntry,
        "computer-entry": ComputerEntry,
        "group-entry": GroupEntry
    }
}
</script>

<style scoped>
.multi-entry-item {
    flex: 1;
    width: 100%;
    display: flex;
    padding: 10px;
    cursor: pointer;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.entry-info {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.item-icon {
    display: flex;
    align-items: flex-end;
    width: 35px;
}

.item-value {
    display: flex;
    flex-direction: column;
    margin-left: 10px;
}

.name {
    font-size: 14px;
    color: #2d8cf0;
}

.domain {
    font-size: 12px;
    color: #a4a6a9;
}

.active {
    background: #f7f7f7;
}

.avatar-privilege {
    margin-left: -10px;
    margin-bottom: -5px;
}

.avatar-disabled {
    margin-left: -12px;
    margin-bottom: -3px;
}

.second-text {
    text-overflow: ellipsis;
    max-width: 250px;
    white-space: nowrap;
    overflow: hidden;
}

.other-info {
    margin-left: 20px;
    font-size: 12px;
    background: #e3e4e4;
    color: #000;
    padding: 2px 5px;
    border-radius: 5px;
}
</style>