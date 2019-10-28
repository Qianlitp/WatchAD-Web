<template>
    <div class="computer-entry">
        <div class="abstract-info">
            <div class="avatar">
                <Icon color="#fff" class="avatar-icon" size="40" custom="iconfont icon-computer" />
                <Icon title="敏感计算机" v-if="is_sensitive" color="#19be6b" class="avatar-privilege" size="30" custom="iconfont icon-privilege-o" />
            </div>
            <div class="abstract">
                <div class="name">{{name}}</div>
                <div v-if="is_dc" class="title">域控服务器</div>
                <div class="desc">{{desc}}</div>
            </div>
        </div>
        <div class="detail-info">
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">Domain</div>
                    <div class="detail-value">{{domain}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">Created At</div>
                    <div class="detail-value">{{whenCreated}}</div>
                </Col>
            </Row>
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">SAM Name</div>
                    <div class="detail-value">{{info["sAMAccountName"]}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">Last Logon</div>
                    <div class="detail-value">{{lastLogonTimestamp}}</div>
                </Col>

            </Row>
        </div>
        <Spin fix v-show="loading"></Spin>
    </div>
</template>

<script>
import {dateFormat} from '@/assets/js/common';
import {mapState} from 'vuex';
export default {
    name: "computer-entry",
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
        },
        desc() {
            return this.info["operatingSystem"] + " " + this.info["operatingSystemServicePack"] + " " + this.info["operatingSystemVersion"]
        },
        is_dc() {
            return this.info["is_dc"]
        },
        is_sensitive() {
            return this.info["is_sensitive"]
        },
        whenCreated() {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(this.info["whenCreated"]))
        },
        lastLogonTimestamp() {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(this.info["lastLogonTimestamp"]))
        }
    },
    methods: {
    },
    created() {

    },
    components: {
        
    }
}
</script>

<style scoped>
.computer-entry {
    width: 300px;
    margin: 10px;
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

.avatar-icon {

}

.abstract {
    padding-left: 20px;
}

.name {
    font-size: 16px;
    font-weight: 700;
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