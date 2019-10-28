<template>
    <div class="setting-base">
        <div class="setting-top">
            <div class="setting-title">{{title}}</div>
        </div>
        <div class="setting-content">
            <slot></slot>
            <div v-if="show_save" class="save">
                <Button 
                    type="primary" 
                    @click="$emit('save')">Save</Button>
            </div>
        </div>
    </div>
</template>

<script>

import {mapState} from 'vuex'
export default {
    name: "setting-base",
    props: {
        title: {
            type: String,
            required: true
        },
        show_save: {
            type: Boolean,
            default: true
        }
    },
    data(){
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
.setting-base {
    width: 900px;
    background: #fff;
    box-shadow: 0 1px 2px 0 #D4D7D9;
    border-radius: 4px;
}

.setting-top {
    height: 50px;
    line-height: 50px;
    border-bottom: solid 1px #D8E5EE;
}

.setting-title {
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #2C405A;
    margin-left: 20px;
}

.setting-content {
    padding: 20px 40px;
    display: flex;
    flex-direction: column;
}

.save {
    margin-top: 20px;
    align-self: flex-end;
}
</style>