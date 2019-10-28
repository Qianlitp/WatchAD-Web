<template>
    <div class="expand-row">
        <div class="expand-item" v-for="(value, name) in row" :key="name">
            <span class="item-key">{{name}}</span>： <span class="item-value">{{value}}</span>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "expand-row",
    props: {
        row: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
        	
        }
    },
    computed: {
    	...mapState({
            
        })
    },
    created() {

    },
    components: {
    	
    }
}
</script>

<style scoped>
.expand-row {
    display: flex;
    flex-wrap: wrap;
}

.expand-item {
    padding: 5px;
    margin-right: 30px;
    background: #e5e5e6;
    border-radius: 5px;
    margin-bottom: 10px;
}

.item-key {

}

.item-value {

}
</style>