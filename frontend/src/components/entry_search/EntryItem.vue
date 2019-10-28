<template>
    <div class="entry-item" :class="{'active': is_hover}" @mouseover="mouse_over" @mouseout="mouse_out" @click="detail">
        <div class="entry-info">
            <div class="item-icon">
                <div class="icon-wrapper">
                    <Icon :custom="real_icon_name" :size="26" color="#fff"></Icon>
                </div>
                <Icon title="管理员权限" v-if="is_sensitive" color="#19be6b" class="avatar-privilege" size="25" custom="iconfont icon-privilege-o" />
                <Icon title="禁用账户" v-if="is_disabled" color="#FB2C2C" type="ios-remove-circle" size="25" class="avatar-disabled"/>
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
</template>

<script>
import {mapState} from 'vuex'
import AlertCount from '@/components/common/AlertCount'
export default {
	name: "entry-item",
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

        },
        detail() {
            window.open("/entry.html#/" + this.entry_type + "/" + this.domain + "/" + this.name)
        }
    },
    created() {

    },
    components: {
        "alert-count": AlertCount
    }
}
</script>

<style scoped>
.entry-item {
    flex: 1;
    width: 100%;
    display: flex;
    padding: 10px;
    cursor: pointer;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background: #FFFFFF;
    box-shadow: 0 1px 2px 0 #D4D7D9;
    border-radius: 4px;
    padding: 20px;
}

.entry-info {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.item-icon {
    display: flex;
    align-items: flex-end;
    width: 80px;
}

.icon-wrapper {
    width: 60px;
    height: 60px;
    border-radius: 30px;
    background: #285786;
    display: flex;
    justify-content: center;
    align-items: center;
}

.item-value {
    height: 70px;
    display: flex;
    flex-direction: column;
    margin-left: 10px;
    justify-content: space-around;
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
    margin-left: -20px;
}

.avatar-disabled {
    margin-left: -20px;
    margin-bottom: -3px;
}

.second-text {
    text-overflow: ellipsis;
    max-width: 400px;
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