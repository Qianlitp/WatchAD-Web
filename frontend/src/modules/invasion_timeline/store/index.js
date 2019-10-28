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
    	invasion_list: [],
        loading: false,
        page: 1
    },
    mutations: {
    	set_invasion_list(state, payload) {
    		state.invasion_list = payload.invasion_list;
    	},
        add_invasion_list(state, payload) {
            state.invasion_list.push(...payload.invasion_list);
        },
        set_loading(state, payload) {
            state.loading = payload.loading;
        },
        set_page(state, payload) {
            state.page = payload.page;
        },
        add_page(state, payload) {
            state.page += 1;
        }
    },
    actions: {
        get_invasion_list({ state, commit, rootState }, payload) {
            commit("set_loading", {loading: true});
            let url = state.api_root + "invasion/list";
            let showProgressBar = true;
            if (payload && payload.hasOwnProperty("show_progress_bar")) {
                showProgressBar = payload.show_progress_bar;
            }
            Vue.http.post(url, {
                page: state.page
            }, {showProgressBar: showProgressBar}).then(response => {
                commit("set_loading", {loading: false});
                if (state.page !== 1) {
                    if (response.body.data.length === 0) {
                        Notice.info({
                            title: "无数据返回",
                            desc: "没有更旧的数据返回了"
                        });
                    } else {
                        commit('add_invasion_list', {
                            invasion_list: response.body.data
                        })
                    }

                } else {
                    commit('set_invasion_list', {
                        invasion_list: response.body.data
                    });
                }
            }, response => {
                commit("set_loading", {loading: false});
                Notice.error({
                    title: "查询数据出错",
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