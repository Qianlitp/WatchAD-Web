<template>
    <div class="group-entry">
        <div class="abstract-info">
            <div class="avatar-wrapper">
                <div class="avatar">
                    <Icon color="#fff" class="avatar-icon" size="40" custom="iconfont icon-group" />
                </div>
                <Icon title="敏感组" v-if="info['is_sensitive']" color="#19be6b" class="avatar-privilege" size="30" custom="iconfont icon-privilege-o" />
            </div>

            <div class="abstract">
                <div class="name">{{name}}</div>
                <div class="desc" :title="info['description']">{{info["description"]}}</div>
            </div>
        </div>
        <div class="detail-info">
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">类型</div>
                    <div class="detail-value">{{info["type"]}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">成员数量</div>
                    <div class="detail-value">{{info["member_count"]}}</div>
                </Col>
            </Row>
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">范围</div>
                    <div class="detail-value">{{info["scope"]}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">域</div>
                    <div class="detail-value">{{info["domain"]}}</div>
                </Col>
            </Row>
            <Row class="detail-row">
                <Col span="12">
                    <div class="detail-title">SAM名称</div>
                    <div class="detail-value" style="white-space: normal;">{{info["sAMAccountName"]}}</div>
                </Col>
                <Col span="12">
                    <div class="detail-title">创建于</div>
                    <div class="detail-value">{{whenCreated}}</div>
                </Col>
            </Row>
        </div>
        <Spin fix v-show="loading"></Spin>
    </div>
</template>

<script>
import {dateFormat} from '@/assets/js/common';
import {mapState} from 'vuex'
export default {
    name: "group-entry",
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
        whenCreated() {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(this.info["whenCreated"]))
        }
    },
    created() {

    },
    components: {
        
    }
}
</script>

<style scoped>
.group-entry {
    width: 300px;
    margin: 10px;
    position: relative;
}

.abstract-info {
    height: 80px;
    display: flex;
}

.avatar-wrapper {
    display: flex;
    width: 90px;
    align-items: flex-end;
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
    margin-left: -30px;
}

.abstract {
    padding-left: 20px;
}

.name {
    color: #2d8cf0;
    font-size: 16px;
    font-weight: 700;
    overflow: hidden;
    white-space: normal;
}

.title {
    margin-top: 5px;
    color: #9FA9BA;
}

.desc {
    color: #9FA9BA;
    overflow: hidden;
    white-space: normal;
    max-height: 50px;
    max-width: 200px;
}

.detail-info {
    margin-top: 30px;
}

.detail-row {
    margin-top: 20px;
}

.detail-title {
    font-size: 12px;
    color: #9FA9BA;
}

.detail-value {

}
</style>