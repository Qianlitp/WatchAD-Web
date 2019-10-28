<template>
    <setting-base title="Mail Server" @save="save()">
        <div class="mail-server">
            TODO
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "mail-server",
    data() {
        return {

        }
    },
    mounted() {
        
    },
    computed: {
        ...mapState({
            setting: state => state.index.setting
        }),
        
    },
    methods: {
        save() {

        },
        test_send_mail() {

        },
        netbios_domain(domain) {
            return get_netbios_domain(domain)
        }
    },
    components: {
        'setting-base': SettingBase
    }
}
</script>

<style scoped>
.mail-server {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.mail-server>div {
    display: flex;
    align-items: center;
}

.label {
    width: 100px;
    margin-right: 20px;
}

</style>