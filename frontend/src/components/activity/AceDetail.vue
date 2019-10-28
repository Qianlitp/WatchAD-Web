<template>
	<div class="ace-detail">
        <Tabs :value="first_tab_name">
            <TabPane v-for="one in current_ace_list" :label="one['user_name']" :name="one['user_name']">
                <Card>
                    <p slot="title" class="ace-title">异常 ACE 详情</p>
                    <div>
                        <div v-for="(value, key) in one" class="ace-content">
                            <div v-if="key != 'permissions'">
                                <span>{{key}}：</span>
                                <span class="ace-value">{{value}}</span>
                            </div>
                        </div>
                        <div class="permission">
                            <div class="permission-title">permission：</div>
                            <div class="permission-detail">
                                <div v-for="(value, key) in one['permissions']" class="">
                                    <span>{{key}}：</span>
                                    <div class="ace-value">
                                        <div v-for="each in value">{{each}}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </Card>
            </TabPane>
        </Tabs>
    </div>
</template>

<script>
export default {
	name: "ace-detail",
    props: {
        form_data: {
            type: Object,
            required: true
        }
    },
    data() {
        return {

        }
    },
    computed: {
        current_ace_list() {
            return this.form_data["abnormal_ace_list"];
        },
        first_tab_name() {
            return this.current_ace_list[0]["user_name"];
        }
    },
    methods: {
        format_value(value) {
            return value.join(",")
        }
    }
}
</script>

<style scoped>
.ace-detail {
    color: #a4a6a9;
    display: flex;
    flex-direction: row;
    width: 800px;
}

.ace-content>div {
	display: flex;
	flex-direction: row;
    justify-content: space-between;
}

.ace-title {
    color: #8a8a8a;
}

.ace-value {
    
}

.permission {
    width: 80%;
    display: flex;
    flex-direction: column!important;
}

.permission-title {
    width: 100%;
}

.permission-detail {
    margin-left: 20px;
    
}

.permission-detail>div {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>