<template>
    <div class="graph">
        <div class="graph-line" :style="{width: length + 'px'}">{{text}}</div>
        <span class="arrow">
            <Icon type="md-arrow-dropright" size="20" color="#9e9e9e"/>
        </span>
    </div>
</template>

<script>
export default {
	name: "arrow-graph",
    props: {
        text: {
            type: String,
            required: true
        }, 
        length: {
            type: Number,
            default: 100
        }
    },
    data() {
        return {
        	
        }
    },
    created() {

    },
    methods: {

    },
    components: {
    	
    }
}
</script>

<style scoped>
.graph {
    display: flex;
    flex-direction: row;
    height: 90px;
}

.graph-line {
    text-align: center;
    line-height: 40px;
    font-size: 1.0em;
    color: #8a8a8a;
    border-bottom: 1px solid #9e9e9e;
    height: 40px;
}

.arrow {
    height: 20px;
    margin-top: 29px;
    margin-left: -8px;
}
</style>