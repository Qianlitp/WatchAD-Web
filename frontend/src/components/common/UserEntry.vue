<template>
    <div class="user-entry">
        <div class="abstract-info">
            <div class="avatar">
                <Icon color="#fff" class="avatar-icon" size="40" custom="iconfont icon-user" />
                <Icon title="敏感账户" v-if="info['is_sensitive']" color="#19be6b" class="avatar-privilege" size="30" custom="iconfont icon-privilege-o" />
                <Icon title="禁用账户" v-if="info['is_disabled']" color="#FB2C2C" type="ios-remove-circle" class="avatar-disabled" size="30" />
            </div>
            <div class="abstract">
                <div class="name">{{info["displayName"]}}</div>
                <div class="title">{{info["title"]}}</div>
                <div class="desc">{{info["department"]}}</div>
                <div class="desc" v-if="info['department'] == ''">{{info["description"]}}</div>
            </div>
        </div>
        <div class="detail-info">
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">域账号</div>
                    <div class="detail-value">{{info["sAMAccountName"]}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">所属域</div>
                    <div class="detail-value">{{domain}}</div>
                </Col>
            </Row>
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">上级</div>
                    <div class="detail-value">{{info["manager"]}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">邮箱</div>
                    <div class="detail-value">{{info["mail"]}}</div>
                </Col>
            </Row>
        </div>
        <Spin fix v-show="loading"></Spin>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
	name: "user-entry",
    props: {
        name: {
            type: String,
            required: true
        },
        domain: {
            type: String,
            required: true
        }
    },
    data() {
        return {
        	loading: true
        }
    },
    computed: {
    	...mapState({
            entries: state => state.entry.entries
        }),
        info() {
            if (this.entries.hasOwnProperty(this.name)) {
                this.loading = false;
                return this.entries[this.name];
            } else {
                return {}
            }
        }
    },
    created() {

    },
    components: {
    	
    }
}
</script>

<style scoped>
.user-entry {
    width: 270px;
    margin: 15px;
    position: relative;
}

.abstract-info {
    height: 80px;
    display: flex;
}

.avatar {
    width: 80px;
    height: 80px;
    background: #285786;
    border-radius: 40px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.avatar-privilege {
    position: absolute;
    left: 50px;
    top: 50px;
}

.avatar-disabled {
    position: absolute;
    left: 50px;
    top: 50px;
}

.abstract {
    padding-left: 20px;
}

.name {
    color: #2d8cf0;
    font-size: 16px;
    font-weight: 700;
    font-family: PingFangSC-Semibold;
}

.title {
    margin-top: 5px;
    color: #888;
}

.desc {
    white-space: normal;
    color: #888;
}

.detail-info {
    margin-top: 40px;
}

.detail-row {
    margin-top: 10px;
}

.detail-title {
    font-size: 14px;
    color: #888;
}

.detail-value {

}
</style>