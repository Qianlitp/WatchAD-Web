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
        activity: {}
    },
    mutations: {
        set_activity(state, payload) {
            state.activity = payload.activity;
        }
    },
    actions: {
        get_activity_detail({ state, commit, rootState }, payload) {
            let url = state.api_root + "activity/" + payload.activity_id;
            Vue.http.get(url, {}
            ).then(response => {
                commit('set_activity', {
                    activity: response.body.data
                });
            }, response => {
                Notice.error({
                    title: "查询数据出错",
                    desc: response.body.error
                });
            });
        },
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