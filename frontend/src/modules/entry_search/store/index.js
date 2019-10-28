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
        _search_result: [],
        loading: false,
        type_filter: "all"
    },
    mutations: {
        set_fuzz_search_result(state, payload) {
            state._search_result = payload.data
        },
        set_fuzz_search_loading(state, payload) {
            state.loading = payload.loading
        },
        set_type_filter(state, payload) {
            state.type_filter = payload.type
        }
    },
    actions: {
        fuzz_search_entry({ state, commit, rootState, dispatch }, payload) {
            commit("set_fuzz_search_result", {
                data: []
            });
            commit("set_fuzz_search_loading", {
                loading: true
            });
            let url = state.api_root + "entry/fuzz_search";
            Vue.http.post(url, {
                name: payload.name,
                page_size: payload.page_size
            }
            ).then(response => {
                commit("set_fuzz_search_result", {
                    data: response.body.data
                })
                commit("set_fuzz_search_loading", {
                    loading: false
                });
            }, response => {
                commit("set_fuzz_search_loading", {
                    loading: false
                });
                Notice.error({
                    title: "模糊查询出错",
                    desc: response.body.error
                });
            });
        }
    },
    getters: {
        fuzz_search_result: state => {
            if (state.type_filter == "all") {
                return state._search_result;
            }
            let result = [];
            for (let entry of state._search_result) {
                if (entry["entry_type"] == state.type_filter) {
                    result.push(entry)    
                }
            }
            return result
        },
        types_count_map: state => {
            let result = {
                "user": 0,
                "computer": 0,
                "group": 0
            }
            for (let entry of state._search_result) {
                result[entry["entry_type"]] += 1
            }
            result["all"] = state._search_result.length;
            return result;
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