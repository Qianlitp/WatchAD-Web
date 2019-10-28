<template>
    <div class="setting-menu">
        <div>
            <div class="title">System</div>
            <div class="setting-items">
                <div :class="is_active('domain-list')" @click="set_part('domain-list')">Domain List</div>
                <div :class="is_active('dc-name-list')" @click="set_part('dc-name-list')">DC Name List</div>
                <div :class="is_active('ldap')" @click="set_part('ldap')">LDAP Setting</div>
                <div :class="is_active('raw-data')" @click="set_part('raw-data')">Raw Data Expire</div>
            </div>
        </div>
        <div>
            <div class="title">Detection</div>
            <div class="setting-items">
                <div :class="is_active('sensitive-entry')" @click="set_part('sensitive-entry')">Sensitive Entry</div>
                <div :class="is_active('honeypot-account')" @click="set_part('honeypot-account')">Honeypot Account</div>
                <div :class="is_active('kerberos')" @click="set_part('kerberos')">Kerberos</div>
                <div :class="is_active('exclusions')" @click="set_part('exclusions')">Exclusions</div>
            </div>
        </div>
        <div>
            <div class="title">Notifications and Reports</div>
            <div class="setting-items">
                <div :class="is_active('alarms-merge')" @click="set_part('alarms-merge')">Alarms Merge</div>
                <div :class="is_active('notifications')" @click="set_part('notifications')">Notifications</div>
                <div :class="is_active('mail-server')" @click="set_part('mail-server')">Mail Server</div>
            </div>
        </div>
        <div>
            <div class="title">Other</div>
            <div class="setting-items">
                <div :class="is_active('about')" @click="set_part('about')">About</div>
            </div>
        </div>
    </div>
</template>

<script>

import {mapState} from 'vuex'
export default {
    name: "setting-menu",
    data() {
        return {

        }
    },
    created() {

    },
    computed: {
        ...mapState({
            now_part: state => state.index.now_part
        })
    },
    methods: {
        is_active(part) {
            if (this.now_part == part) {
                return {'active': true};
            } else {
                return {'active': false};
            }
        },
        set_part(part) {
            this.$store.commit("set_now_part", {
                part: part
            })
        }
    },
    components: {

    }
}
</script>

<style scoped>
.setting-menu {
    width: 200px;
    margin-left: 150px;

}

.setting-menu>div {
    padding: 25px 0px;
    border-bottom: 1px solid #97979747
}

.setting-items {
    margin-top: 15px;
}

.setting-items>div {
    line-height: 30px;
    height: 30px;
    font-size: 12px;
    color: #171C22;
    width: 150px;
    padding-left: 20px;
    cursor: pointer;
}

.title {
    font-family: PingFangSC-Regular;
    font-size: 12px;
    color: #9FA9BA;
}

.active {
    background: rgba(2,148,255,0.08);
    border: 1px solid #0294FF;
    border-radius: 4px;
    color: #0294FF!important;
}

</style>