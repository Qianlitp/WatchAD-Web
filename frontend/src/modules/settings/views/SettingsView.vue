<template>
    <index-view>
        <div class="settings-view">
            <setting-menu></setting-menu>
            <div class="main">
                <component :is="now_part"></component>
            </div>
            <div></div>
        </div>
    </index-view>
</template>

<script>
import IndexView from '@/views/IndexView';
import SettingMenu from '@/components/settings/SettingMenu';
import DomainList from '@/components/settings/DomainList';
import DomainControllerList from '@/components/settings/DomainControllerList';
import LdapSetting from '@/components/settings/LdapSetting';
import RawData from '@/components/settings/RawData';
import SensitiveEntry from '@/components/settings/SensitiveEntry';
import HoneypotAccount from '@/components/settings/HoneypotAccount';
import Kerberos from '@/components/settings/Kerberos';
import Exclusions from '@/components/settings/Exclusions';
import AlarmsMerge from '@/components/settings/AlarmsMerge';
import MailServer from '@/components/settings/MailServer';
import Notifications from '@/components/settings/Notifications';
import About from '@/components/settings/About';
import {mapState} from 'vuex'
export default {
    name: "settings-view",
    data(){
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            now_part: state => state.index.now_part
        })
    },
    methods: {
        
    },
    components: {
        'index-view': IndexView,
        'setting-menu': SettingMenu,
        'domain-list': DomainList,
        'dc-name-list': DomainControllerList,
        'ldap': LdapSetting,
        'raw-data': RawData,
        'sensitive-entry': SensitiveEntry,
        'honeypot-account': HoneypotAccount,
        'kerberos': Kerberos,
        'exclusions': Exclusions,
        'alarms-merge': AlarmsMerge,
        'mail-server': MailServer,
        'notifications': Notifications,
        'about': About
    }
}
</script>

<style scoped>
.settings-view {
    margin-top: 35px;
    display: flex;
    flex-direction: row;
}

.main {
    margin-left: 100px;
}
</style>