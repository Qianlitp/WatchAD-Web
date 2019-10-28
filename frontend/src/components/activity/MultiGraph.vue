<template>
    <Poptip trigger="hover" placement="right">
        <div class="graph" @mouseover="mouse_over" @mouseout="mouse_out">
            <span class="graph-icon"><Icon :custom="custom" size="60" :color="color"></Icon></span>
            <div :class="text_class">{{text_name}}</div>
        </div>
        <div slot="title">
           
       </div>
       <div class="multi-content" slot="content">
            <multi-entry-item 
                v-for="(one, index) in current_data" 
                :key="index" 
                :icon_name="custom" 
                :name="one"
                :domain="domain"></multi-entry-item>
            <div v-if="total > 5">
                <Page :total="total" :page-size="page_size" :current.sync="page" size="small" />
            </div>
       </div>
    </Poptip>
</template>

<script>
import MultiEntryItem from '@/components/common/MultiEntryItem';
export default {
	name: "multi-graph",
    props: {
        icon_name: {
            type: String,
            required: true
        },
        value: {
            type: Array,
            required: true
        }, 
        sensitive: {
            type: Boolean,
            default: false
        },
        domain: {
            type: String,
            required: true
        }
    },
    data() {
        return {
        	is_hover: false,
            page: 1,
            page_size: 5
        }
    },
    created() {

    },
    computed: {
        current_data() {
            let start = (this.page - 1) * this.page_size;
            let end = this.page * this.page_size;
            return this.value.slice(start, end);
        },
        total() {
            return this.value.length
        },
        text_name() {
            return this.value.length.toString() + "个" + this.entry_name(this.icon_name);
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
        }
    },
    methods: {
        mouse_over() {
            this.is_hover = true;
        },
        mouse_out() {
            this.is_hover = false;
        },
        entry_name(icon) {
            if (icon.includes("server")) {
                return "域控"
            } else if (icon.includes("user")) {
                return "账户"
            } else if (icon.includes("computer")) {
                return "来源"
            } else if (icon.includes("secret")) {
                return "可疑账户"
            } else if (icon.includes("file")) {
                return "文件共享"
            }
        }
    },
    components: {
    	"multi-entry-item": MultiEntryItem
    }
}
</script>

<style scoped>
.graph {
    display: flex;
    flex-direction: column;
    cursor: pointer;
    height: 90px;
    align-items: center;
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

.multi-content {
    display: flex;
    flex-direction: column;
    width: 250px;
}

</style>