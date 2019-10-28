<template>
    <div class="layout">
        <Layout>
            <Header class="nav-header">
                <img :src="logo_path" class="logo" />
                <div class="nav-title">
                    <span class="watch-ad">WatchAD</span>
                    <span style="margin-left: 10px;"> — AD Security Intrusion Detection System</span>
                </div>
                <div class="nav-menu">
                    <div class="nav-left">
                        <div><a href="/dashborad.html#/">Dashboard</a></div>
                        <div><a href="/activity_timeline.html#/">Threat Activities</a></div>
                        <div><a href="/invasion_timeline.html#/">Invasions</a></div>
                        <!-- <div><a href="/data_search.html#/">Raw Data</a></div> -->
                        <div><a href="/settings.html#/">Configuration</a></div>
                    </div>
                </div>
                <div class="nav-search">
                    <AutoComplete class="search-input" 
                        v-model="search_content"
                        icon="ios-search" 
                        placeholder="Search users, computers and groups ..."
                        @on-change="search"
                        transfer
                        clearable
                        @keyup.enter.native="go_entry_search()">
                        <div v-show="search_content.length >= 4 && search_loading == 0 && search_result.length == 0" class="search-tips">
                            no search result
                        </div>
                        <div v-show="search_loading > 0" class="search-loading">
                            <Spin fix>
                                <Icon type="ios-loading" size=20 class="spin-icon-load"></Icon>
                                <div>searching ...</div>
                            </Spin>
                        </div>
                        <div class="search-result">
                            <multi-entry-item
                                v-for="entry in search_result"
                                :name="entry['cn']"
                                :entry_type="entry['entry_type']"
                                :domain="entry['domain']"
                                :is_sensitive="entry['is_sensitive']"
                                :is_disabled="entry['is_disabled']"
                                :alert_count="entry['alert_count']"
                                :key="entry['cn']"
                                ></multi-entry-item>
                            <div></div>
                        </div>
                        <a 
                            v-show="search_result.length > 0" 
                            :href="more_url" 
                            target="_blank" 
                            class="search-more">show all results
                        </a>
                    </AutoComplete>
                </div>
            </Header>
            <Content class="main-content">
                <slot></slot>
            </Content>
            <Footer class="layout-footer-center"> Author：<a href="https://0kee.360.cn/">0KEE Team</a></Footer>
        </Layout>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import logo_path from '@/assets/img/logo.png'
import MultiEntryItem from '@/components/common/MultiEntryItem';

export default {
    data(){
        return {
            logo_path: logo_path
        }
    },
    mounted() {

    },
    computed: {
        ...mapState({
            search_result: state => state.entry.fuzz_search_result,
            search_loading: state => state.entry.fuzz_search_loading
        }),
        more_url() {
            return "/entry_search.html#/" + this.search_content;
        }, 
        search_content: {
            get() {
                return this.$store.state.entry.fuzz_search_content;
            }, 
            set(value) {
                this.$store.commit("set_global_fuzz_search_content", {
                    data: value
                })
            }
        }
    },
    methods: {
        search(value) {
            this.$store.commit("set_global_fuzz_search_result", {
                data: []
            })
            if (value.length >= 4) {
                this.$store.dispatch("global_fuzz_search_entry", {
                    name: value
                })
            }
        },
        go_entry_search() {
            if (this.$route.name == "entry_search") {
                this.$router.push({ name: 'entry_search', params: { "entry_name": this.search_content }}) 
            } else {
                window.open(this.more_url)    
            }
        }
    },
    components: {
        'multi-entry-item': MultiEntryItem
    }
}
</script>

<style scoped>
.layout {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
}

.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}

.layout-footer-center{
    flex: 1;
    text-align: center;
    background: #EFF3F6;
}

.nav-header {
    width: 100%;
    display: flex;
    flex-direction: row;
    box-shadow: 0 1px 3px rgba(0,0,0,.1);
    z-index: 1;
    height: 50px;
    line-height: 50px;
    align-items: center;
}

.nav-title {
    color: #949494;
    font-size: 15px;
    width: 500px;
    font-family: "Microsoft YaHei","黑体","宋体",sans-serif;
    display: flex;
    align-items: center;
}

.watch-ad {

    font-size: 1.5em;
}

.nav-menu {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    flex: 1;
}

.nav-left>div {
    padding: 0px 25px;
    font-size: 1.2em;
    color: #0093EE;
    font-family: PingFangSC-Medium;
}

.nav-left {
    display: flex;
}

.main-content {
    background: #EFF3F6;
    min-height: 700px;
    display: flex;
    flex: 1;
}

.rate {
    display: flex;
}

.rate>div {
    margin-right: 20px;
}

.logo {
    height: 30px;
    width: 30px;
    margin-right: 10px;
}

.search-input {
    width: 400px;
}

.search-loading {
    height: 100px;
}

.search-tips {
    display: block;
    margin: 0 auto;
    padding: 4px;
    text-align: center;
    font-size: 12px;
    color: #a4a6a9;
}

.search-result {
    display: flex;
    flex-direction: column;

}

.search-more {
    display: block;
    margin: 0 auto;
    padding: 4px;
    text-align: center;
    font-size: 12px;
}

.spin-icon-load {
    animation: ani-demo-spin 1s linear infinite;
}
</style>