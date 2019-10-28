import Vue from 'vue'; // get vue
import Vuex from 'vuex'; // get vuex
import VueResource from 'vue-resource'; // get $http
import {Notice, Message} from 'view-design';
import {sleep} from '@/assets/js/common';

Vue.use(Vuex);
Vue.use(VueResource);

Notice.config({
    top: 60,
    duration: 5
});

const entry_module = {
    state: {
    	api_root: process.env.VUE_APP_API_ROOT,
        entries: {},
        loading: false,
        fuzz_search_result: [],
        fuzz_search_content: "",
        fuzz_search_loading: 0,

    },
    mutations: {
        set_entries(state, payload) {
            Vue.set(state.entries, payload.name, payload.info);
        },
        set_multi_entries(state, payload) {
            for (let entry of payload.data) {
                Vue.set(state.entries, entry["cn"], entry);
            }
        },
        set_entry_loading(state, payload) {
            state.loading = payload.loading
        },
        set_global_fuzz_search_result(state, payload) {
            state.fuzz_search_result = payload.data
        },
        set_global_fuzz_search_content(state, payload) {
            state.fuzz_search_content = payload.data
        },
        add_global_fuzz_search_loading(state, payload) {
            state.fuzz_search_loading += 1
        },
        reduce_global_fuzz_search_loading(state, payload) {
            state.fuzz_search_loading -= 1
        }
    },
    actions: {
        search_entry({ state, commit, rootState, dispatch }, payload) {
            commit("set_entry_loading", {
                loading: true
            });
            let url = state.api_root + "entry/" + payload.type + "/" + payload.domain + "/" + payload.name;
            Vue.http.get(url, {showProgressBar: false}
            ).then(response => {
                commit("set_entries", {
                    name: payload.name,
                    info: response.body.data
                })
                commit("set_entry_loading", {
                    loading: false
                });
            }, response => {
                commit("set_entry_loading", {
                    loading: false
                });
                Notice.error({
                    title: "查询数据出错",
                    desc: response.body.error
                });
            });
        },
        async global_fuzz_search_entry({ state, commit, rootState, dispatch }, payload) {
            commit("add_global_fuzz_search_loading");
            await sleep(500);
            if (payload.name != state.fuzz_search_content) {
                commit("reduce_global_fuzz_search_loading");
                return
            }
            let url = state.api_root + "entry/fuzz_search";
            Vue.http.post(url, {
                name: payload.name,
                page_size: 5
            }, {showProgressBar: false}
            ).then(response => {
                if (state.fuzz_search_loading == 1) {
                    commit("set_global_fuzz_search_result", {
                        data: response.body.data
                    })
                }
                commit("reduce_global_fuzz_search_loading");
            }, response => {
                commit("reduce_global_fuzz_search_loading");
                Notice.error({
                    title: "模糊查询出错",
                    desc: response.body.error
                });
            });
        }
    }
}

export default entry_module;