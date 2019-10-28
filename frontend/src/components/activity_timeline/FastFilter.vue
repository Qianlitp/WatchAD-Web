<template>
    <div class="fast-filter">
        <div class="filter-warpper">
            <div class="title">Fast Filter</div>
            <div class="filter-all" :class="{'focus': is_focus('all', 'all')}" @click="do_filter('all', 'all')">All ({{total}})</div>
            <Collapse class="filter-main" :value="panelName" simple>
                <Panel :name="status_key" v-for="(level_value, status_key) in status_data" :key="status_key">
                    {{status_key}} ({{level_value["total"]}})
                    <div slot="content">
                        <div class="level" :class="{'focus': is_focus(status_key, 'all')}" @click="do_filter(status_key, 'all')">
                            <Badge status="processing"/>All ({{level_value["total"]}})
                        </div>
                        <div class="level" 
                            :class="{'focus': is_focus(status_key, level)}" 
                            @click="do_filter(status_key, level)" 
                            v-for="level in level_list">
                            <Badge :status="level_color(level)" />{{level}} ({{level_value[level]}})
                        </div>
                    </div>
                </Panel>
            </Collapse>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "fast-filter",
    data() {
        return {
            panelName: "",
            level_list: ["high", "medium", "low"]
        }
    },
    mounted() {
        setTimeout(() => {
            this.$nextTick(() => {
                this.panelName = 'pending'
            })
        }, 500)
    },
    computed: {
    	...mapState({
            status: state => state.index.status,
            level: state => state.index.level,
            statistic: state => state.index.statistic
        }),
        total() {
            return this.statistic["total"]
        }, 
        status_data() {
            return this.statistic["data"]
        }
    },
    methods: {
        do_filter(status, level) {
            this.$store.commit("set_status_level", {
                status: status,
                level: level
            })
            this.$store.dispatch('get_activity_list');
        },
        level_color(level) {
            if (level == "high") {
                return "error"
            } else if (level == "medium") {
                return "warning"
            } else if (level == "low") {
                return "default"
            }
        },
        is_focus(status, level) {
            return this.status == status && this.level == level;
        }
    },
    created() {
        this.$store.dispatch('get_statistic');
    },
    components: {
    	
    }
}
</script>

<style scoped>
.fast-filter {
    margin-top: 70px;
}

.filter-warpper {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    font-size: 12px;
    color: #354052!important;
}

.filter-all {
    height: 38px;
    line-height: 38px;
    padding-left: 47px;
    width: 160px;
    cursor: pointer;
    color: #666;
}

.filter-main {
    width: 160px;
    border: none;
    background: #EFF3F6;
}

.title {
    width: 160px;
    font-size: 15px;
    padding-left: 45px;
    color: #9FA9BA;
    margin-bottom: 10px;
}

.focus {
    background: rgba(2,148,255,0.08);
    border: 1px solid #0294FF;
    border-radius: 4px;
    border-radius: 4px;
}

.level {
    cursor: pointer;
    margin-left: 20px;
    padding-left: 20px;
    width: 120px;
    height: 30px;
    line-height: 30px;
}
</style>