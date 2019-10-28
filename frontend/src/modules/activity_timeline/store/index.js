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
    	activity_list: [],
        alert_code: "",
        status: "pending",
        level: "all",
        start_time: "",
        end_time: "",
        filter_name: "",
        filter_value: "",
        page: 1,
        statistic: {},
        loading: false
    },
    mutations: {
    	set_activity_list(state, payload) {
    		state.activity_list = payload.activity_list;
    	},
        add_activity_list(state, payload) {
            state.activity_list.push(...payload.activity_list);
        },
        set_filter_params(state, payload) {
            state.alert_code = payload.alert_code;
            state.status = payload.status;
            state.level = payload.level;
            state.filter_name = payload.filter_name;
            state.filter_value = payload.filter_value;
            state.start_time = payload.start_time;
            state.end_time = payload.end_time;
            state.page = 1;
        },
        set_status_level(state, payload) {
            state.status = payload.status;
            state.level = payload.level;
        },
        set_alert_types(state, payload) {
            state.alert_types_config = payload.alert_types_config;
        },
        set_page(state, payload) {
            state.page = payload.page;
        },
        add_page(state, payload) {
            state.page += 1;
        }, 
        set_statistic(state, payload) {
            Vue.set(state, "statistic", payload.data)
        },
        set_loading(state, payload) {
            state.loading = payload.loading;
        }
    },
    actions: {
        get_activity_list({ state, commit, rootState }, payload) {
            commit("set_loading", {loading: true});
            let url = state.api_root + "activity/list";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                page: state.page,
                status: state.status,
                alert_code: state.alert_code,
                level: state.level,
                filter_name: state.filter_name,
                filter_value: state.filter_value,
                start_time: state.start_time,
                end_time: state.end_time
            }, {showProgressBar: showProgressBar}).then(response => {
                commit("set_loading", {loading: false});
                if (state.page !== 1) {
                    if (response.body.data.length === 0) {
                        Notice.info({
                            title: "无数据返回",
                            desc: "没有更旧的数据返回了"
                        });
                    } else {
                        commit('add_activity_list', {
                            activity_list: response.body.data
                        })
                    }

                } else {
                    commit('set_activity_list', {
                        activity_list: response.body.data
                    });
                }
            }, response => {
                commit("set_loading", {loading: false});
                Notice.error({
                    title: "查询数据出错",
                    desc: response.body.error
                });
            });
        },
        get_statistic({ state, commit, rootState }, payload) {
            let url = state.api_root + "activity/statistic";
            Vue.http.get(url, {}
            ).then(response => {
                commit("set_statistic", {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "获取快速筛选的统计数据出错",
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