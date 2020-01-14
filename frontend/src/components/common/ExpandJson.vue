<template>
    <div class="expand-json">
        <div class="title">{{json_data["MsgType"]}}</div>
        <pre>{{format_data}}</pre>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "expand-json",
    props: {
        json_data: {
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
            
        }),
        format_data() {
            return JSON.stringify(this.json_data, null, 2)
        }
    },
    created() {

    },
    components: {
    	
    }
}
</script>

<style scoped>
.expand-json {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
}

.title {
    font-weight: 700;
    font-size: 16px;
}
</style>