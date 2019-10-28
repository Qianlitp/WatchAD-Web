<template>
    <div class="search-result">
        <div class="search-input">
            <Input 
                prefix="ios-search" 
                v-model="input_content" 
                size="large" 
                placeholder="查询用户、计算机、用户组..."
                @keyup.enter.native="search()" />
        </div>
        <div class="search-tips">
            <div>"{{current_search}}" 的搜索结果：</div>
            <div class="tips-total">
                <div style="margin-right: 10px">返回最多 
                    <InputNumber size="small" :min="1" v-model="page_size" style="width: 60px;"></InputNumber> 条结果
                </div>
                <div>，当前共<span style="color: #1890FF;"> {{fuzz_search_result.length}}</span> 条结果</div>
            </div>
        </div>
        <div class="result-list">
            <entry-item
                v-for="entry in fuzz_search_result"
                :name="entry['cn']"
                :entry_type="entry['entry_type']"
                :domain="entry['domain']"
                :is_sensitive="entry['is_sensitive']"
                :is_disabled="entry['is_disabled']"
                :alert_count="entry['alert_count']"
                :second_text="entry['description']"
                :key="entry['cn']"
                ></entry-item>
            <Spin v-show="loading" style="margin-top: 200px;">
                <Icon type="ios-loading" size=50 class="spin-icon-load"></Icon>
                <div class="loading-text">loading</div>
            </Spin>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import EntryItem from '@/components/entry_search/EntryItem';
export default {
    name: "search-result",
    data() {
        return {
            input_content: this.$route.params.entry_name,
            current_search: this.$route.params.entry_name,
            page_size: 20
        }
    },
    created(){
        this.search();
    },
    computed: {
        ...mapState({
            loading: state => state.index.loading
        }),
        fuzz_search_result() {
            return this.$store.getters.fuzz_search_result;
        }
    },
    watch: {

    },
    methods: {
        search() {
            this.current_search = this.input_content;
            this.$store.dispatch("fuzz_search_entry", {
                name: this.current_search,
                page_size: this.page_size
            })
        }
    },
    components: {
        'entry-item': EntryItem
    }
}
</script>

<style scoped>
.search-result {
    display: flex;
    flex-direction: column;
    width: 900px;
}

.search-input {
    width: 600px;
}

.search-tips {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #273142;
}

.result-list {
    display: flex;
    flex-direction: column;
}

.result-list>div {
    margin: 10px 0px;
}

.tips-total {
    display: flex;
}

.spin-icon-load {
    animation: ani-demo-spin 1s linear infinite;
}
</style>