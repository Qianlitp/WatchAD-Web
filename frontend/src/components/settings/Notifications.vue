<template>
    <setting-base title="Notifications" @save="save()">
        <div class="notifications">
            TODO
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "notifications",
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
.notifications {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.notifications>div {
    display: flex;
    align-items: center;
}

.label {
    width: 100px;
    margin-right: 20px;
}

</style>