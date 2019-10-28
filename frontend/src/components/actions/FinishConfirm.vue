<template>
    <div class="finish-confirm">
        <Modal :value="show" title="完成确认" @on-ok="do_finish" @on-visible-change="visible_change">
            <div class="finish-text">确认要将本威胁活动状态标记为 <span class="finish-name">完成</span> 吗？</div>
        </Modal>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "finish-confirm",
    props: {
        show: {
            type: Boolean,
            required: true
        },
        activity: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
        	
        }
    },
    created() {

    },
    computed: {
    	...mapState({
            
        }),
        title() {
            return this.activity["title"];
        }
    },
    methods: {
        do_finish() {
            this.$store.dispatch("finish_activity", {
                id: this.activity["_id"]
            })
        },
        visible_change(visible) {
            this.$emit("visible_change", {
                visible: visible
            });
        }
    },
    components: {
    	
    }
}
</script>

<style scoped>
.finish-name {
    font-size: 18px;
    color: #19be6b;
}

.finish-text {
    font-size: 16px;
}

.actions-list {
    display: flex;
    flex-direction: column;
}

.action-item {
    margin: 10px 20px 0px 20px;
}

.highlight {
    font-size: 15px;
    color: #f90;
}
</style>