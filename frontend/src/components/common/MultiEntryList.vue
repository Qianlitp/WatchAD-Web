<template>
    <div class="multi-entry-list" :style="{width: width + 'px' }">
        <multi-entry-item 
            v-for="(one, index) in current_data" 
            :key="index" 
            :icon_name="get_icon_name(one['type'])" 
            :entry_type="one['type']"
            :name="one['name']"
            :domain="domain" >
        </multi-entry-item>
        <div v-if="total > 5">
            <Page 
                :total="total" 
                :page-size="page_size" 
                :current.sync="page" 
                size="small" />
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import MultiEntryItem from './MultiEntryItem';
export default {
	name: "multi-entry-list",
    props: {
        entry_list: {
            type: Array,
            required: true
        },
        width: {
            type: Number,
            default: 300
        },
        domain: {
            type: String,
            required: true
        }
    },
    data() {
        return {
        	page: 1,
            page_size: 5
        }
    },
    computed: {
    	...mapState({
            
        }),
        current_data() {
            let start = (this.page - 1) * this.page_size;
            let end = this.page * this.page_size;
            return this.entry_list.slice(start, end);
        },
        total() {
            return this.entry_list.length
        }
    },
    methods: {
        get_icon_name(type) {
            if (type == "computer") {
                return "iconfont icon-computer";
            } else if (type == "server") {
                return "iconfont icon-server";
            } else if (type == "user") {
                return "iconfont icon-user";
            } else if (type == "group") {
                return "iconfont icon-group";
            } else if (type == "ip") {
                return "iconfont icon-dizhidingwei";
            } else if (type == "service") {
                return "iconfont icon-ServiceGroup";
            } else {
                return "iconfont icon-file";
            }
        }
    },
    created() {

    },
    components: {
    	"multi-entry-item": MultiEntryItem
    }
}
</script>

<style scoped>
.entry-name {
    color: #2d8cf0;
    cursor: pointer;
}

.multi-entry-list {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>