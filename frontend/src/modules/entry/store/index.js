import Vue from 'vue'; // get vue
import Vuex from 'vuex'; // get vuex
import VueResource from 'vue-resource'; // get $http
import md5 from 'js-md5';
import {Notice, Message} from 'view-design';
import actions_module from '@/store/actions';
import entry_module from '@/store/entry';

Vue.use(Vuex);
Vue.use(VueResource);

Notice.config({
    top: 60,
    duration: 5
});

const index_module = {
    state: {
    	api_root: process.env.VUE_APP_API_ROOT,
        entry_name: "",
        entry_type: "",
        domain: "",
        data_type: "activity",
        detail_data: {},
        records: [],
        activities: [],
        logon_ips: [],
        used_computers: [],
        logon_users: [],
        access_entries: []
    },
    mutations: {
        set_entry_info(state, payload) {
            state.entry_name = payload.name.replace("$", "");
            state.entry_type = payload.type;
            state.domain = payload.domain
        },
        set_data_type(state, payload) {
            state.data_type = payload.data_type
        },
        set_detail_data(state, payload) {
            state.detail_data = payload.data;
        },
        set_entry_records(state, payload) {
            state.records = payload.data
        },
        add_entry_records(state, payload) {
            state.records = state.records.concat(payload.data);
        },
        set_entry_activities(state, payload) {
            state.activities = payload.data
        },
        set_entry_logon_ips(state, payload) {
            state.logon_ips = payload.data
        },
        set_entry_used_computers(state, payload) {
            state.used_computers = payload.data
        },
        set_entry_logon_users(state, payload) {
            state.logon_users = payload.data
        },
        set_entry_access_entries(state, payload) {
            state.access_entries = payload.data
        }
    },
    actions: {
        get_detail_user({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "entry/detail_user/" + state.domain + "/" + state.entry_name;
            Vue.http.get(url, {}
            ).then(response => {
                commit("set_detail_data", {
                    data: response.body.data
                })
                if (response.body.data["memberOf"]) {
                    commit("set_multi_entries", {
                        data: response.body.data["memberOf"]
                    })
                }
                if (response.body.data["recursive_groups"]) {
                    commit("set_multi_entries", {
                        data: response.body.data["recursive_groups"]
                    })
                }
                if (response.body.data["directReports"]) {
                    commit("set_multi_entries", {
                        data: response.body.data["directReports"]
                    })
                }
                if (response.body.data["manager"]) {
                    commit("set_entries", {
                        name: response.body.data["manager"]["cn"],
                        info: response.body.data["manager"]
                    })
                }
            }, response => {
                Notice.error({
                    title: "查询账户详细数据出错",
                    desc: response.body.error
                });
            });
        },
        get_detail_group({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "entry/detail_group/" + state.domain + "/" + state.entry_name;
            Vue.http.get(url, {}
            ).then(response => {
                commit("set_detail_data", {
                    data: response.body.data
                })
                if (response.body.data["memberOf"]) {
                    commit("set_multi_entries", {
                        data: response.body.data["memberOf"]
                    })
                }
                if (response.body.data["member"]) {
                    commit("set_multi_entries", {
                        data: response.body.data["member"]
                    })
                }
            }, response => {
                Notice.error({
                    title: "查询用户组详细数据出错",
                    desc: response.body.error
                });
            });
        },
        get_detail_computer({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "entry/detail_computer/" + state.domain + "/" + state.entry_name;
            Vue.http.get(url, {}
            ).then(response => {
                commit("set_detail_data", {
                    data: response.body.data
                })
                if (response.body.data["memberOf"]) {
                    commit("set_multi_entries", {
                        data: response.body.data["memberOf"]
                    })
                }
            }, response => {
                Notice.error({
                    title: "查询计算机详细数据出错",
                    desc: response.body.error
                });
            });
        },
        get_entry_records({ state, commit, rootState }, payload) {
            let url = state.api_root + "record/list";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, payload, {showProgressBar: showProgressBar}).then(response => {
                if (response.body.data.length == 0) {
                    Notice.info({
                        title: "没有更多的实体活动数据",
                        desc: response.body.error
                    });
                }
                if (payload.more) {
                    commit('add_entry_records', {
                        data: response.body.data
                    })
                } else {
                    commit('set_entry_records', {
                        data: response.body.data
                    })
                }
            }, response => {
                Notice.error({
                    title: "查询实体域内活动数据出错",
                    desc: response.body.error
                });
            });
        },
        get_entry_activities({ state, commit, rootState }, payload) {
            let url = state.api_root + "activity/related_list";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                domain: state.domain,
                entry_name: state.entry_name,
                entry_type: state.entry_type
            }, {showProgressBar: showProgressBar}).then(response => {
                commit('set_entry_activities', {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "查询实体相关威胁活动数据出错",
                    desc: response.body.error
                });
            });
        },
        get_entry_logon_ips({ state, commit, rootState }, payload) {
            let url = state.api_root + "record/logon_ips";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                domain: state.domain,
                entry_name: state.entry_name,
                entry_type: state.entry_type
            }, {showProgressBar: showProgressBar}).then(response => {
                commit('set_entry_logon_ips', {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "查询实体登录IP数据出错",
                    desc: response.body.error
                });
            });
        },
        get_entry_logon_users({ state, commit, rootState }, payload) {
            let url = state.api_root + "record/logon_users";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                domain: state.domain,
                entry_name: state.entry_name,
                entry_type: state.entry_type
            }, {showProgressBar: showProgressBar}).then(response => {
                commit('set_entry_logon_users', {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "查询实体登录用户数据出错",
                    desc: response.body.error
                });
            });
        },
        get_entry_used_computers({ state, commit, rootState }, payload) {
            let url = state.api_root + "record/used_computers";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                domain: state.domain,
                entry_name: state.entry_name,
                entry_type: state.entry_type
            }, {showProgressBar: showProgressBar}).then(response => {
                commit('set_entry_used_computers', {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "查询实体使用过的计算机数据出错",
                    desc: response.body.error
                });
            });
        },
        get_entry_access_entries({ state, commit, rootState }, payload) {
            let url = state.api_root + "record/access_entries";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                domain: state.domain,
                entry_name: state.entry_name,
                entry_type: state.entry_type
            }, {showProgressBar: showProgressBar}).then(response => {
                commit('set_entry_access_entries', {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "查询实体访问过的实体数据出错",
                    desc: response.body.error
                });
            });
        }
    }
}


const store = new Vuex.Store({
    modules:{
        index: index_module,
        actions: actions_module,
        entry: entry_module
    }
});

export default store;