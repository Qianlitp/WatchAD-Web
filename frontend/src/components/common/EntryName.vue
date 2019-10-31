<template>
    <Poptip trigger="hover" placement="right" :transfer="true" :disabled="disabled" @on-popper-show="search()">
        <div class="entry-container" @click="detail()">
            <Icon v-if="icon_name" :custom="custom_icon" size="22" class="entry-icon"></Icon>
            <span class="entry-name">{{value}}</span>
        </div>
        <div slot="content">
            <user-entry v-if="choose_entry == 'user'" :name="value" :domain="domain"></user-entry>
            <computer-entry v-else-if="choose_entry == 'computer'" :name="value" :domain="domain"></computer-entry>
            <group-entry v-else-if="choose_entry == 'group'" :name="value" :domain="domain"></group-entry>
        </div>
    </Poptip>
</template>

<script>
import {mapState} from 'vuex'
import UserEntry from '@/components/common/UserEntry';
import ComputerEntry from '@/components/common/ComputerEntry';
import GroupEntry from '@/components/common/GroupEntry';
export default {
	name: "entry-name",
    props: {
        value: {
            type: String,
            required: true
        },
        field_name: {
            type: String,
            required: false
        },
        icon_name: {
            type: String,
            required: false
        },
        domain: {
            type: String,
            required: true
        },
        disable_poptip: {
            type: Boolean,
            default: true
        },
        entry_type: {
            type: String,
            required: false
        }
    },
    data() {
        return {
        	
        }
    },
    computed: {
    	...mapState({
            entries: state => state.entry.entries
        }),
        custom_icon() {
            return "iconfont " + this.icon_name;
        },
        disabled() {
            if (!this.disable_poptip) {
                return false
            }

            for (let name of ["user", "workstation", "hostname", "group", "computer"]) {
                if (this.field_name.includes(name)) {
                    return false
                }
            }

            return true
        },
        choose_entry() {
            if (this.entry_type) {
                return this.entry_type
            }

            if (["source_user_name", "target_user_name"].includes(this.field_name)) {
                if (this.value.endsWith("$")) {
                    return "computer"
                }
                return "user"
            } else if (["source_workstation", "relay_workstation", "dc_hostname"].includes(this.field_name)) {
                return "computer"
            } else if (["group_name"].includes(this.field_name)) {
                return "group"
            } else {
                return ""
            }
        }
    },
    methods: {
        search() {
            if (this.entries.hasOwnProperty(this.value)) {
                return
            }
            if (this.choose_entry == "") {
                return
            }
            this.$store.dispatch("search_entry", {
                domain: this.domain,
                name: this.value,
                type: this.choose_entry
            })
        },
        detail() {
            if (!["user", "group", "computer"].includes(this.choose_entry)) {
                return
            }
            window.open("/entry.html#/" + this.choose_entry + "/" + this.domain + "/" + this.value);
        }
    },
    created() {

    },
    components: {
    	"user-entry": UserEntry,
        "computer-entry": ComputerEntry,
        "group-entry": GroupEntry
    }
}
</script>

<style scoped>
.entry-container {
    display: flex;
    align-items: center;
}

.entry-icon {
    margin-right: 5px;
}

.entry-name {
    color: #2d8cf0;
    cursor: pointer;
}
</style>