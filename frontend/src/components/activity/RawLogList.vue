<template>
    <div class="raw-log-list">
        <div class="raw-log-title">原始日志</div>
        <Table size="small" border :columns="columns" :data="current_data" @on-row-click="row_click"></Table>
        <Page :total="total" :page-size="page_size" :current.sync="page" size="small" />
    </div>
</template>

<script>
import {mapState} from 'vuex'
import ExpandRow from "@/components/common/ExpandRow";
export default {
	name: "raw-log-list",
    props: {
        log_list: {
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
                    title: "名称",
                    key: "task",
                    align: "center"
                },
                {
                    title: "事件ID",
                    key: "event_id",
                    align: "center"
                },
                {
                    title: "处理域控",
                    key: "beat",
                    align: "center",
                    render: (h, params) => {
                        return h(
                            'div', 
                            params.row["beat"]["hostname"]
                        );
                    }
                },
                {
                    title: "日志编号",
                    key: "record_number",
                    align: "center"
                },
                {
                    title: "操作",
                    align: "center",
                    key: "record_number",
                    render: (h, params) => {
                        return h('Button', 
                        {
                            props: {
                                type: 'primary',
                                size: 'small'
                            },
                            on: {
                                click: () => {
                                    this.$Modal.info({
                                        title: "格式化显示",
                                        width: 800,
                                        closable: true,
                                        'mask-closable': true,
                                        render: (h) => {
                                            return h('div',
                                                {
                                                    class: "text-wrapper"
                                                },
                                                params.row.message
                                            )
                                        }
                                    });
                                }
                            }
                        }, 
                        '格式化')
                    }
                },
                {
                    title: "展开详情",
                    align: "center",
                    type: 'expand',
                    width: 100,
                    render: (h, params) => {
                        return h(ExpandRow, {
                            props: {
                                row: params.row.event_data
                            }
                        })
                    }
                }
            ]
        },
        current_data() {
            if (!this.log_list) {
                return [];
            }
            let start = (this.page - 1) * this.page_size;
            let end = this.page * this.page_size;
            return this.log_list.slice(start, end);
        },
        total() {
            if (!this.log_list) {
                return 0;
            }
            return this.log_list.length;
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
.raw-log-list {
    padding: 0px 50px 20px 50px;
    border-bottom: 1px solid #e9ebec
}

.raw-log-title {
    font-size: 25px;
    margin: 10px 0px 10px -20px;
}
</style>