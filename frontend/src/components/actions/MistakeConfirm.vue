<template>
    <div class="mistake-confirm">
        <Modal :value="show" title="误报确认" @on-ok="do_mistake" @on-visible-change="visible_change">
            <div class="mistake-text">确认要将本威胁活动标记为 <span class="mistake-name">误报</span> 吗？</div>
            <div class="mistake-list-title">系统将进行以下操作：</div>
            <ul class="actions-list">
                <li class="action-item">标记本活动为误报</li>
            </ul>
        </Modal>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "mistake-confirm",
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
        },
        second_name() {
            return this.activity["second_name"];
        },
        source_workstation_first() {
            return this.get_value_by_field("source_workstation")[0]
        },
        source_workstation_all() {
            return this.get_value_by_field("source_workstation").join("、")
        },
        target_user_name(){
            return this.get_value_by_field("target_user_name").join("、")
        },
        source_user(){
            return this.get_value_by_field("source_user_name").join("、")
        },
        source_ip(){
            return this.get_value_by_field("source_ip").join("、")
        },
        alert_code() {
            return this.activity["alert_code"];
        }
    },
    methods: {
        do_mistake() {
            this.$store.dispatch("mistake_activity", {
                id: this.activity["_id"],
                alert_code: this.alert_code
            })
        },
        visible_change(visible) {
            this.$emit("visible_change", {
                visible: visible
            });
        },
        get_value_by_field(field) {
            for (let each of this.activity["desc_data"]) {
                if (each["name"] == field) {
                    return each["value"]
                }
            }
        }
    },
    components: {
    	
    }
}
</script>

<style scoped>
.mistake-name {
    font-size: 18px;
    color: #fb6262;
}

.mistake-text {
    font-size: 16px;
}

.mistake-list-title {
    margin-top: 20px;
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