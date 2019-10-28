<template>
    <div class="flow-graph">
        <template v-for="one in graph">
            <single-graph v-if="one['type'] == 'single'" :text="text(one['text'])" :icon_name="one['icon']" :second_text="second_text(one)"></single-graph>
            <arrow-graph v-else-if="one['type'] == 'arrow'" :text="one['text']" :length="one['length']"></arrow-graph>
            <multi-graph v-else-if="one['type'] == 'multi'" :value="one['text']" :icon_name="one['icon']" :domain="domain"></multi-graph>
        </template>
    </div>
</template>

<script>
import SingleGraph from './SingleGraph';
import ArrowGraph from './ArrowGraph';
import MultiGraph from './MultiGraph';
export default {
    name: "flow-graph",
    props: {
        graph: {
            type: Array,
            required: true
        },
        domain: {
            type: String,
            required: true
        }
    },
    data(){
        return {

        }
    },
    created(){

    },
    computed: {

    },
    methods: {
        text(item) {
            if (typeof(item) == "string") {
                return item
            } else {
                return item["name"]
            }
        },
        second_text(item) {
            if (item.hasOwnProperty("second_text")) {
                return item["second_text"];
            } else {
                return ""
            }
        }
    },
    components: {
        "single-graph": SingleGraph,
        "arrow-graph": ArrowGraph,
        'multi-graph': MultiGraph
    }
}
</script>

<style scoped>
.flow-graph {
    display: flex;
    flex-direction: row;
    padding: 50px;
    justify-content: space-around;
}
</style>