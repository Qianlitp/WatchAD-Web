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
    },
    mutations: {
        
    },
    actions: {
        
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