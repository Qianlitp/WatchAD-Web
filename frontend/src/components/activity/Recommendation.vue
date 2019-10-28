<template>
    <div class="recommendation">
        <div class="recommendation-title">处理建议</div>
        <div>
            // TODO
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "recommendation",
    props: {

    },
    data() {
        return {

        }
    },
    created() {

    },
    computed: {
    	...mapState({
            
        })
    },
    methods: {

    },
    components: {
    	
    }
}
</script>

<style scoped>
.recommendation {
    padding: 0px 50px 50px 50px;
}

.recommendation-title {
    font-size: 25px;
    margin: 10px 0px 10px -20px;
}
</style>