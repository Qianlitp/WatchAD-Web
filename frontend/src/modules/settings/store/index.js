import Vue from 'vue'; // get vue
import Vuex from 'vuex'; // get vuex
import VueResource from 'vue-resource'; // get $http
import md5 from 'js-md5';
import {Notice, Message} from 'view-design';
import actions_module from '@/store/actions';
import entry_module from '@/store/entry';
import exclusion_module from '@/store/exclusions';

Vue.use(Vuex);
Vue.use(VueResource);

Notice.config({
    top: 60,
    duration: 5
});

const index_module = {
    state: {
    	api_root: process.env.VUE_APP_API_ROOT,
        now_part: "domain-list",
        setting: {
            domain_list: [],
            dc_name_list: {},
            ldap: {},
            raw_data_expire: {
                "dc_log": 0,
                "dc_krb5": 0
            },
            sensitive_entry: {
                "user": [],
                "computer": [],
                "group": []
            },
            honeypot_account: [],
            kerberos: {},
            alarms_merge: {
                "activity": 0,
                "invasion": 0
            }
        }
    },
    mutations: {
        set_now_part(state, payload) {
            state.now_part = payload.part;
        },
        set_setting(state, payload) {
            Vue.set(state.setting, payload.name, payload.data);
        },
        remove_entry(state, payload) {
            let setting = state.setting;
            let index = setting.sensitive_entry[payload.type].findIndex(item => item.domain === payload.domain && item.name === payload.name);
            setting.sensitive_entry[payload.type].splice(index, 1);
        },
        add_entry(state, payload) {
            let setting = state.setting;
            setting.sensitive_entry[payload.type].push(payload.entry);
        },
        add_dc_name(state, payload) {
            let setting = state.setting;
            if (setting.dc_name_list.hasOwnProperty(payload.domain)) {
                setting.dc_name_list[payload.domain].push(payload.dc_name);
            } else {
                Vue.set(setting.dc_name_list, payload.domain, [payload.dc_name]);
            }
        },
        remove_dc_name(state, payload) {
            let setting = state.setting;
            let index = setting.dc_name_list[payload.domain].findIndex(item => item === payload.name);
            setting.dc_name_list[payload.domain].splice(index, 1);
        },
        add_honeypot_account(state, payload) {
            let setting = state.setting;
            setting.honeypot_account.push(payload.entry);
        },
        remove_honeypot_account(state, payload) {
            let setting = state.setting;
            let index = setting.honeypot_account.findIndex(item => item.sid === payload.sid);
            setting.honeypot_account.splice(index, 1);
        },
        add_spn_prefix(state, payload) {
            state.setting.kerberos.high_risk_spn_prefix.push(payload.prefix);
        },
        add_delegation_prefix(state, payload) {
            state.setting.kerberos.high_risk_delegation_prefix.push(payload.prefix);
        },
        remove_spn_prefix(state, payload) {
            let setting = state.setting;
            let index = setting.kerberos.high_risk_spn_prefix.findIndex(item => item === payload.prefix);
            setting.kerberos.high_risk_spn_prefix.splice(index, 1);
        },
        remove_delegation_prefix(state, payload) {
            let setting = state.setting;
            let index = setting.kerberos.high_risk_delegation_prefix.findIndex(item => item === payload.prefix);
            setting.kerberos.high_risk_delegation_prefix.splice(index, 1);
        }
    },
    actions: {
        get_setting({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "setting/" + payload.name;
            Vue.http.get(url, {}
                ).then(response => {
                    commit("set_setting", {
                        name: payload.name,
                        data: response.body.data
                    })
                }, response => {
                Notice.error({
                    title: "get setting data fail.",
                    desc: response.body.error
                });
            });
        },
        change_setting({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "setting/" + payload.name;
            Vue.http.post(url, {
                value: payload.value
            }
            ).then(response => {
                Notice.success({
                    title: "Modify Success."
                });
                commit("set_setting", {
                    name: payload.name,
                    data: []
                });
                dispatch("get_setting", {
                    name: payload.name
                });
            }, response => {
                Notice.error({
                    title: "Save Failed.",
                    desc: response.body.error
                });
            });
        },
        test_ldap_con({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "test_setting/test_ldap_con";
            Vue.http.post(url, {
                setting: payload.setting
            }
            ).then(response => {
                Notice.success({
                    title: "Connetion Success."
                });
            }, response => {
                Notice.error({
                    title: "Connetion Failed.",
                    desc: response.body.errmsg
                });
            });
        },
        check_entry({ state, commit, rootState, dispatch }, payload) {
            let url = state.api_root + "entry/check_entry/" + payload.type + "/" + payload.domain + "/" + payload.name;
            Vue.http.get(url, {}
            ).then(response => {
                let sid = response.body.data;
                if (payload.type == "computer") {
                    payload.name = payload.name.toUpperCase()
                }
                if (payload.action == "add_dc_name") {
                    commit(payload.action, {
                        domain: payload.domain,
                        dc_name: payload.name
                    })
                } else {
                    commit(payload.action, {
                        type: payload.type,
                        entry: {
                            "sid": sid,
                            "name": payload.name,
                            "domain": payload.domain
                        }
                    })
                }
                
            }, response => {
                Notice.error({
                    title: "No Such Entry.",
                    desc: response.body.errmsg
                });
            });
        }
    }
}


const store = new Vuex.Store({
    modules:{
        index: index_module,
        actions: actions_module,
        entry: entry_module,
        exclusion: exclusion_module
    }
});

export default store;