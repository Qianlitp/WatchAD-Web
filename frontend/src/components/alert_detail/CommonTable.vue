<template>
    <div class="common-table">
        <Table size="small" border :columns="columns" :data="alert_data" @on-row-click="row_click"></Table>
        <Page :total="total" :page-size="page_size" :current.sync="page" size="small" />
    </div>
</template>

<script>
import {mapState} from 'vuex'    
import {entries, dateFormat} from '@/assets/js/common.js';
import EntryName from '@/components/common/EntryName';
import MultiEntryName from '@/components/common/MultiEntryName';
export default {
	name: "common-table",
    props: {
        column_list: {
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
            activity: state => state.index.activity
        }),
        alert_code() {
            if (!this.activity['alert_code']) {
                return ""
            } else {
                return this.activity['alert_code']
            }
        },
        alert_list() {
            if (!this.activity['alert_list']) {
                return []
            } else {
                return this.activity['alert_list']
            }
        },
        domain() {
            return this.activity['domain']
        },
        columns() {
            let base = [
                {
                    title: "时间",
                    key: "time",
                    align: "center",
                    sortable: true,
                    width: 130,
                    render: (h, params) => {
                        if (params.row.start_time == params.row.end_time) {
                            return h(
                                'div', 
                                this.format_time(params.row.start_time)
                            );
                        } else {
                            return h(
                                'div', 
                                [
                                    h('div', this.format_time(params.row.start_time)),
                                    h('div',"|"),
                                    h('div', this.format_time(params.row.end_time))
                                ]
                            );
                        }
                    }
                }
            ];

            for (let name of this.column_list) {
                let obj = {
                    title: this.get_title(name),
                    key: name,
                    align: "center"
                }

                let render = this.get_render(name);
                if (render) {
                    obj["render"] = render
                }

                base.push(obj);
            }

            return base;

        },
        current_data() {
            if (!this.alert_list) {
                return [];
            }
            let start = (this.page - 1) * this.page_size;
            let end = this.page * this.page_size;
            return this.alert_list.slice(start, end);
        },
        alert_data() {
            let result = [];
            for (let each of this.current_data) {
                let base = {
                    start_time: each["start_time"],
                    end_time: each["end_time"]
                };

                for (let name of this.column_list) {
                    base[name] = each["form_data"][name]
                }
                result.push(base);
            }
            return result;
        },
        total() {
            if (!this.alert_list) {
                return 0;
            }
            return this.alert_list.length;
        }
    },
    methods: {
        format_time(date_str) {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(date_str))
        },
        row_click(currentRow, index) {
            this.$emit('row_click', {
                currentRow: currentRow,
                index: index
            });
        },
        get_title(name) {
            let title_map = {
                source_ip: "来源IP",
                relay_ip: "中继者IP",
                source_workstation: "来源计算机",
                source_user_name: "使用身份",
                target_user_name: "目标用户",
                group_name: "用户组名称",
                dc_hostname: "域控",
                relative_target_name: "文件共享名称",
                alert_rule: "告警规则",
                abnormal_users: "异常用户名",
                object_class: "对象类名",
                brute_force_type: "爆破类型",
                brute_force_target_users: "爆破目标",
                normal_enc: "正常加密",
                exceptional_enc: "当前加密"
            }
            if (title_map.hasOwnProperty(name)) {
                return title_map[name];
            } else {
                return name
            }
        },
        get_render(name) {
            if (name == "dc_hostname") {
                return (h, params) => {
                    return h(
                        EntryName,
                        {
                            props: {
                                field_name: name,
                                icon_name: "icon-server",
                                value: params.row.dc_hostname,
                                domain: this.domain
                            }
                        }
                    );
                }
            } else if (["source_workstation", "target_computer", "relay_workstation"].includes(name)) {
                return (h, params) => {
                    return h(
                        EntryName,
                        {
                            props: {
                                field_name: name,
                                icon_name: "icon-computer",
                                value: params.row[name],
                                domain: this.domain
                            }
                        }
                    );
                }
            } else if (name == "group_name") {
                return (h, params) => {
                    return h(
                        EntryName,
                        {
                            props: {
                                field_name: name,
                                icon_name: "icon-group",
                                value: params.row.group_name,
                                domain: this.domain
                            }
                        }
                    );
                }
            } else if (["source_user_name", "target_user_name"].includes(name)) {
                return (h, params) => {
                    let value = params.row[name];
                    let icon_name = "icon-user";
                    if (value.endsWith("$")) {
                        icon_name = "icon-computer"
                    }
                    return h(
                        EntryName,
                        {
                            props: {
                                field_name: name,
                                icon_name: icon_name,
                                value: value,
                                domain: this.domain
                            }
                        }
                    );
                }
            } else if (["abnormal_users", "brute_force_target_users"].includes(name)) {
                return (h, params) => {
                    return h(
                        MultiEntryName,
                        {
                            props: {
                                field_name: name,
                                entry_data: params.row[name],
                                simple: true,
                                domain: this.domain,
                                entry_type: "user"
                            }
                        }
                    );
                }
            } else {
                return null;
            }
        }
    },
    components: {
    	
    }
}
</script>

<style scoped>

</style>