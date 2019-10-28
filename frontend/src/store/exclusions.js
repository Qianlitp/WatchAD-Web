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
        exclusion_list: []
    },
    mutations: {
        set_exclusion_list(state, payload) {
            state.exclusion_list = payload.data
        }
    },
    actions: {
        get_exclusion_list({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "setting/exclusion";
            Vue.http.get(url, {}
            ).then(response => {
                commit('set_exclusion_list', {
                    data: response.body.data
                })
            }, response => {
                Notice.error({
                    title: "请求数据出错",
                    desc: response.body.errmsg
                });
            });
        },
        new_exclusion({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "setting/exclusion";
            Vue.http.put(url, {
                ...payload.data
            }
            ).then(response => {
                commit('set_exclusion_list', {
                    data: response.body.data
                })
                Notice.success({
                    title: "New Exclusion Success."
                });
            }, response => {
                Notice.error({
                    title: "Failed.",
                    desc: response.body.errmsg
                });
            });
        },
        update_exclusion({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "setting/exclusion";
            Vue.http.post(url, {
                ...payload
            }
            ).then(response => {
                commit('set_exclusion_list', {
                    data: response.body.data
                })
                Notice.success({
                    title: "Update Exclusion Success."
                });
            }, response => {
                Notice.error({
                    title: "Failed.",
                    desc: response.body.errmsg
                });
            });
        },
        delete_exclusion({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "setting/exclusion/delete/" + payload.id;
            Vue.http.delete(url, {}
            ).then(response => {
                commit('set_exclusion_list', {
                    data: response.body.data
                })
                Notice.success({
                    title: "Delete Success."
                });
            }, response => {
                Notice.error({
                    title: "Delete Failed.",
                    desc: response.body.errmsg
                });
            });
        }
    }
}

export default actions_module;