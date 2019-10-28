<template>
    <setting-base title="About" @save="save()">
        <div class="about">
            TODO
        </div>
    </setting-base>
</template>

<script>
import SettingBase from './SettingBase';
import {mapState} from 'vuex'
import {get_netbios_domain} from '@/modules/settings/assets/js/common';
export default {
    name: "about",
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
.about {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

</style>