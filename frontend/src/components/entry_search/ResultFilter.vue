<template>
    <div class="result-filter">
        <div class="filter-title">类型筛选</div>
        <div class="filter-list">
            <div @click="set_type_filter('all')" :class="{'active': is_active('all')}">所有 ({{types_count_map["all"]}})</div>
            <div @click="set_type_filter('user')" :class="{'active': is_active('user')}">用户 ({{types_count_map["user"]}})</div>
            <div @click="set_type_filter('computer')" :class="{'active': is_active('computer')}">计算机 ({{types_count_map["computer"]}})</div>
            <div @click="set_type_filter('group')" :class="{'active': is_active('group')}">用户组 ({{types_count_map["group"]}})</div>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
    name: "result-filter",
    data() {
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            type_filter: state => state.index.type_filter
        }),
        types_count_map() {
            return this.$store.getters.types_count_map;
        }
    },
    methods: {
        set_type_filter(type) {
            this.$store.commit("set_type_filter", {
                type: type
            })
        },
        is_active(type) {
            return this.type_filter == type;
        }
    },
    components: {

    }
}
</script>

<style scoped>
.result-filter {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 100px;
    font-size: 14px;
    margin-top: 60px;
}

.result-filter>div {
    width: 100px;
}

.filter-list {
    font-family: PingFangSC-Regular;
    font-size: 12px;
    color: #354052;
}

.filter-list>div {
    cursor: pointer;
    margin: 10px 0px;
    line-height: 20px;
}

.filter-title {
    font-size: 12px;
    color: #9FA9BA;
}

.active {
    font-weight: 700;
}
</style>