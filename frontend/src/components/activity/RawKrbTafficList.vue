<template>
    <div class="raw-krb-traffic-list">
        <div class="raw-krb-traffic-title">原始流量</div>
        <Table size="small" border :columns="columns" :data="current_data" @on-row-click="row_click"></Table>
        <Page :total="total" :page-size="page_size" :current.sync="page" size="small" />
    </div>
</template>

<script>
import {mapState} from 'vuex'
import ExpandJson from "@/components/common/ExpandJson";
export default {
	name: "raw-krb-traffic-list",
    props: {
        krb_list: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
        	page: 1,
            page_size: 10
        }
    },
    created() {

    },
    computed: {
    	...mapState({
            
        }),
        columns() {
            return [
                {
                    title: "时间",
                    key: "@timestamp",
                    align: "center",
                    sortable: true,
                    width: 180
                }, 
                {
                    title: "消息类型",
                    key: "msgType",
                    align: "center"
                },
                {
                    title: "处理域控",
                    key: "host",
                    align: "center",
                    render: (h, params) => {
                        return h(
                            'div', 
                            params.row["host"]["hostname"]
                        );
                    }
                },
                {
                    title: "uuid",
                    key: "uuid",
                    align: "center"
                },
                {
                    title: "显示完整流量",
                    align: "center",
                    type: 'expand',
                    width: 100,
                    render: (h, params) => {
                        return h(
                            "div",
                            {
                                style: "display:flex; "
                            },
                            [
                                h(ExpandJson, {
                                    props: {
                                        json_data: params.row.req
                                    }
                                }),
                                h(ExpandJson, {
                                    props: {
                                        json_data: params.row.rep
                                    }
                                })
                            ]
                        )
                    }
                }
            ]
        },
        current_data() {
            if (!this.krb_list) {
                return [];
            }
            let start = (this.page - 1) * this.page_size;
            let end = this.page * this.page_size;
            return this.krb_list.slice(start, end);
        },
        total() {
            if (!this.krb_list) {
                return 0;
            }
            return this.krb_list.length;
        }
    },
    methods: {
        row_click() {

        }
    },
    components: {
    	
    }
}
</script>

<style scoped>
.raw-krb-traffic-list {
    padding: 0px 50px 20px 50px;
    border-bottom: 1px solid #e9ebec
}

.raw-krb-traffic-title {
    font-size: 25px;
    margin: 10px 0px 10px -20px;
}

.raw-krb-expand {
    display: flex;
}
</style>