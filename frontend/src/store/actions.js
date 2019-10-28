import Vue from 'vue'; // get vue
import Vuex from 'vuex'; // get vuex
import VueResource from 'vue-resource'; // get $http
import md5 from 'js-md5';
import {Notice, Message} from 'view-design';

Vue.use(Vuex);
Vue.use(VueResource);

Notice.config({
    top: 60,
    duration: 5
});

const actions_module = {
    state: {
    	api_root: process.env.VUE_APP_API_ROOT,
        alert_types_config: []
    },
    mutations: {
        set_alert_types(state, payload) {
            state.alert_types_config = payload.alert_types_config;
        }
    },
    actions: {
        get_alert_types({ state, commit, rootState, dispatch }) {
            let url = state.api_root + "config/types";
            Vue.http.get(url, {}
            ).then(response => {
                commit("set_alert_types", {
                    alert_types_config: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "获取配置出错",
                    desc: response.body.error
                });
            });
        },
        delete_activity({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "activity/" + payload._id;
            Vue.http.delete(url, {}
            ).then(response => {
                Message.success({
                    content: '删除成功',
                    duration: 10,
                    closable: true
                })
                commit('set_page', {
                    page: 1
                })
                dispatch('get_activity_list');
            }, response => {
                Notice.error({
                    title: "删除数据出错",
                    desc: response.body.error
                });
            });
        },
        close_activity({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "activity/close";
            Vue.http.post(url, {
                id: payload._id
            }
            ).then(response => {
                Message.success({
                    content: '关闭成功',
                    duration: 10,
                    closable: true
                })
                commit('set_page', {
                    page: 1
                })
                dispatch('get_activity_list');
            }, response => {
                Notice.error({
                    title: "处理出错",
                    desc: response.body.error
                });
            });
        },
        mistake_activity({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "activity/mistake";
            Vue.http.post(url, {
                ...payload
            }
            ).then(response => {
                Message.success({
                    content: '已成功标记为误报',
                    duration: 10,
                    closable: true
                })
                commit('set_page', {
                    page: 1
                })
                dispatch('get_activity_list');
            }, response => {
                Notice.error({
                    title: "标记误报请求处理出错",
                    desc: response.body.error
                });
            });
        },
        ignore_activity({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "activity/ignore";
            Vue.http.post(url, {
                ...payload
            }
            ).then(response => {
                Message.success({
                    content: '已成功忽略该活动',
                    duration: 10,
                    closable: true
                })
                commit('set_page', {
                    page: 1
                })
                dispatch('get_activity_list');
            }, response => {
                Notice.error({
                    title: "忽略请求处理出错",
                    desc: response.body.error
                });
            });
        },
        finish_activity({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "activity/finish";
            Vue.http.post(url, {
                ...payload
            }
            ).then(response => {
                Message.success({
                    content: '已标记为完成',
                    duration: 10,
                    closable: true
                })
                commit('set_page', {
                    page: 1
                })
                dispatch('get_activity_list');
            }, response => {
                Notice.error({
                    title: "完成处理出错",
                    desc: response.body.error
                });
            });
        }
    }
}

export default actions_module;