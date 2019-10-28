<template>
    <Poptip class="multi-entry-name" trigger="hover" placement="right" :disabled="disabled" transfer>
        <span class="entry-name">{{display_name}}</span>
        <multi-entry-list slot="content" :entry_list="entry_list" :domain="domain"></multi-entry-list>
    </Poptip>
</template>

<script>
import {mapState} from 'vuex'
import MultiEntryList from './MultiEntryList'
export default {
	name: "multi-entry-name",
    props: {
        field_name: {
            type: String,
            required: true
        },
        entry_data: {
            type: Array,
            required: true
        },
        entry_type: {
            type: String,
            required: true
        },
        simple: {
            type: Boolean,
            default: false
        },
        width: {
            type: Number,
            default: 250
        },
        domain: {
            type: String,
            required: true
        }
    },
    data() {
        return {

        }
    },
    computed: {
    	...mapState({
            
        }),
        disabled() {
            return this.entry_data.length === 1;
        },
        entry_list() {
            if (this.simple) {
                let result = [];
                for (let one of this.entry_data) {
                    if (typeof(one) == 'string') {
                        result.push({
                            "name": one,
                            "type": this.entry_type
                        })
                    } else {
                        result.push({
                            "name": one["name"],
                            "type": this.entry_type
                        })
                    }
                }
                return result
            } else {
                return this.entry_data
            }
        },
        display_name() {
            if (this.entry_list.length === 1) {
                return this.entry_list[0]["name"];
            }
            return this.entry_list.length.toString() + "个" + this.get_entry_name;
        },
        get_entry_name() {
            if (this.field_name.includes("user")) {
                return "用户"
            } else if (this.field_name.includes("workstation")) {
                return "计算机"
            } else if (this.field_name.includes("dc")) {
                return "域控"
            } else if (this.field_name.includes("group")) {
                return "用户组"
            } else if (this.field_name.includes("ip")) {
                return "IP"
            } else if (this.field_name.includes("service")) {
                return "服务"
            } else if (this.field_name.includes("relative_target_name")) {
                return "名称"
            } else {
                return "名称"
            }
        }
    },
    methods: {

    },
    created() {

    },
    components: {
    	"multi-entry-list": MultiEntryList
    }
}
</script>

<style scoped>
.entry-name {
    color: #2d8cf0;
    cursor: pointer;
}

.multi-content {
    display: flex;
    flex-direction: column;
    width: 250px;
    align-items: center;
}
</style>