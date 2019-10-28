<template>
    <div class="alert-count" v-if="count != 0">
        <Icon size="15" custom="iconfont icon-kulou"></Icon>
        <div class="number">{{count}}</div>
   </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "alert-count",
    props: {
        count: {
            type: Number,
            default: 0
        }
    },
    data() {
        return {
        	
        }
    },
    computed: {
    	...mapState({
            
        }),

    },
    methods: {

    },
    created() {

    },
    components: {
    	
    }
}
</script>

<style scoped>
.alert-count {
    padding: 2px 6px;
    color: #FB2C2C;
    display: flex;
    background: #efefef;
    border-radius: 10px;
    justify-content: space-between;

}

.number {
    margin-left: 5px;
}

</style>