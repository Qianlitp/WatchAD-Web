<template>
    <Poptip trigger="hover" placement="right" :disabled="disabled" @on-popper-show="search()">
        <div class="graph" @mouseover="mouse_over" @mouseout="mouse_out">
            <span class="graph-icon"><Icon :custom="custom" size="60" :color="color"></Icon></span>
            <div :class="text_class">{{text}}</div>
            <div :class="text_class" v-if="second_text != ''">{{second_text}}</div>
        </div>
        <div slot="content">
            <user-entry v-if="choose_entry == 'user'" :name="real_name" :domain="domain"></user-entry>
            <computer-entry v-else-if="choose_entry == 'computer'" :name="real_name" :domain="domain"></computer-entry>
            <group-entry v-else-if="choose_entry == 'group'" :name="real_name" :domain="domain"></group-entry>
        </div>
    </Poptip>
</template>

<script>
import {mapState} from 'vuex';
import UserEntry from '@/components/common/UserEntry';
import ComputerEntry from '@/components/common/ComputerEntry';
import GroupEntry from '@/components/common/GroupEntry';
export default {
	name: "single-graph",
    props: {
        icon_name: {
            type: String,
            required: true
        },
        text: {
            type: String,
            default: ""
        }, 
        second_text: {
            type: String,
            default: ""
        },
        sensitive: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
        	is_hover: false
        }
    },
    created() {

    },
    computed: {
        ...mapState({
            activity: state => state.index.activity,
            entries: state => state.entry.entries
        }),
        domain() {
            return this.activity["domain"];
        },
        color() {
            if (this.is_hover) {
                return "#76a0cc";
            } else {
                return "#9dbad8";
            }
        },
        text_class() {
            return {
                'graph-text': true,
                'hover-color': this.is_hover
            }
        },
        custom() {
            return "iconfont " + this.icon_name;
        },
        disabled() {
            if (["icon-computer", "icon-user", "icon-group", "icon-server", "icon-secret"].includes(this.icon_name)) {
                return false
            } else {
                return true
            }
        },
        real_name() {
            if (this.second_text) {
                return this.second_text;
            } else {
                return this.text;
            }
        },
        choose_entry() {
            if (["icon-server", "icon-computer"].includes(this.icon_name)) {
                return "computer"
            } else if (["icon-user", "icon-secret"].includes(this.icon_name)) {
                if (this.real_name.endsWith("$")) {
                    return "computer"
                }
                return "user"
            } else if (["icon-group"].includes(this.icon_name)) {
                return "group"
            } else {
                return ""
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
            if (this.entries.hasOwnProperty(this.real_name)) {
                return
            }
            if (this.choose_entry == "") {
                return
            }
            this.$store.dispatch("search_entry", {
                domain: this.domain,
                name: this.real_name,
                type: this.choose_entry
            })

        }
    },
    components: {
    	"user-entry": UserEntry,
        "computer-entry": ComputerEntry,
        "group-entry": GroupEntry
    }
}
</script>

<style scoped>
.graph {
    display: flex;
    flex-direction: column;
    cursor: pointer;
    height: 90px;
}

.graph-icon {
    margin-bottom: 10px;
    text-align: center;
}

.graph-text {
    text-align: center;
    color: #9dbad8;
    font-size: 1.2em;
}

.hover-color {
    color: #76a0cc;
}
</style>