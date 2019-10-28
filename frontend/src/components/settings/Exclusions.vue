<template>
    <setting-base title="Exclusions" :show_save="false">
        <div class="exclusions">
            <Table border :columns="columns" :data="exclusion_list"></Table>
            <div style="margin-top: 20px;text-align: right;">
                <Button type="primary" @click="show_new_confirm">New Exclusion</Button>
            </div>
        </div>
        <new-exclusion :show="new_confirm_show" @visible_change="new_visible_change"></new-exclusion>
        <edit-exclusion :show="edit_show" :pdata="edit_data" @visible_change="edit_visible_change"></edit-exclusion>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import ExclusionExpandRow from './ExclusionExpandRow';
import NewExclusion from '@/components/actions/NewExclusion';
import EditExclusion from '@/components/actions/EditExclusion';
import {mapState} from 'vuex';
import {dateFormat} from "@/assets/js/common";
export default {
    name: "exclusions",
    data() {
        return {
            new_confirm_show: false,
            edit_show: false,
            edit_data: {}
        }
    },
    mounted() {
        this.$store.dispatch("get_exclusion_list");
    },
    computed: {
        ...mapState({
            exclusion_list: state => state.exclusion.exclusion_list
        }),
        columns() {
            return [
                {
                    title: 'Title',
                    key: 'title',
                    width: 150,
                    resizable: true
                },
                {
                    title: 'Add At',
                    key: 'add_time',
                    resizable: true,
                    width: 110,
                    render: (h, params) => {
                        return h(
                            'div', 
                            this.format_time(params.row.add_time)
                        );
                    }
                },
                {
                    title: 'Update At',
                    key: 'update_time',
                    resizable: true,
                    width: 110,
                    render: (h, params) => {
                        return h(
                            'div', 
                            this.format_time(params.row.update_time)
                        );
                    }
                },
                {
                    title: 'Comment',
                    key: 'comment'
                },
                {
                    title: 'Rules',
                    key: 'rules',
                    type: 'expand',
                    resizable: true,
                    width: 80,
                    render: (h, params) => {
                        return h(ExclusionExpandRow, {
                            props: {
                                row: params.row
                            }
                        })
                    }
                },
                {
                    title: 'Action',
                    key: 'action',
                    width: 150,
                    resizable: true,
                    align: 'center',
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {
                                        this.edit(params.row)
                                    }
                                }
                            }, 'Edit'),
                            h('Button', {
                                props: {
                                    type: 'error',
                                    size: 'small'
                                },
                                on: {
                                    click: () => {
                                        this.delete(params.row)
                                    }
                                }
                            }, 'Delete')
                        ]);
                    }
                }
            ]
        }
    },
    methods: {
        edit(row) {
            this.edit_data = Object.assign({}, this.edit_data, row)
            this.edit_show = true;

        }, 
        delete(row) {
            this.$store.dispatch("delete_exclusion", {
                id: row["_id"]
            })
        },
        show_new_confirm() {
            this.new_confirm_show = true
        },
        new_visible_change(params) {
            this.new_confirm_show = params.visible
        },
        edit_visible_change(params) {
            this.edit_show = params.visible
        },
        format_time(date_str) {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(date_str));
        }
    },
    components: {
        'setting-base': SettingBase,
        'new-exclusion': NewExclusion,
        'edit-exclusion': EditExclusion
    }
}
</script>

<style scoped>
.exclusions {

}

</style>