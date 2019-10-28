<template>
    <div class="group-left-intro">
        <div class="avatar-info">
            <div class="avatar-outer">
                <div class="avatar-wrapper">
                    <Icon color="#0294FF" class="avatar-icon" size="35" custom="iconfont icon-group" />
                </div>
                <div>
                    <Icon v-if="sensitive" title="敏感用户组" color="#19be6b" class="avatar-flag" size="30" custom="iconfont icon-privilege-o" />
                </div>
            </div>
            <div class="name">
                {{displayName}}
            </div>
            <div class="desc">
                <div class="detail">{{info["description"]}}</div>
            </div>
        </div>
        <div class="detail-info">
            <div class="base-info">
                <Row>
                    <Col span="12">
                        <div class="item-name">Type</div>
                        <div class="item-value">{{info["type"]}}</div>
                    </Col>
                    <Col span="12">
                        <div class="item-name">Direct Members</div>
                        <div class="item-value">{{info["member_count"]}}</div>
                    </Col>
                </Row>
                <Row>
                    <Col span="12">
                        <div class="item-name">Scope</div>
                        <div class="item-value">{{info["scope"]}}</div>
                    </Col>
                    <Col span="12">
                        <div class="item-name">Domain</div>
                        <div class="item-value">{{domain}}</div>
                    </Col>
                </Row>
                <Row>
                    <Col span="12">
                        <div class="item-name">SAM Name</div>
                        <div class="item-value">{{info["sAMAccountName"]}}</div>
                    </Col>
                    <Col span="12">
                        <div class="item-name">Created At</div>
                        <div class="item-value">{{whenCreated}}</div>
                    </Col>
                </Row>
            </div>
            <div class="other-selection">
                <div :class="{'active': is_active('activity')}" @click="change_type('activity')">
                    <Badge dot :count="activities.length">
                        <div class="avatar-kulou">
                            <Icon size="25" type="md-time"></Icon>
                        </div>
                    </Badge>
                    <div class="other-selection-name">
                        <div class="other-selection-title">活动</div>
                        <div>域内的相关活动记录</div>
                    </div>
                    <div v-if="activities.length > 0" class="activity-count"><alert-count :count="activities.length"></alert-count></div>
                </div>
                <div :class="{'active': is_active('data')}" @click="change_type('data')">
                    <div class="avatar-data">
                        <Icon size="25" custom="iconfont icon-mulu"></Icon>
                    </div>
                    <div class="other-selection-name">
                        <div class="other-selection-title">详细信息</div>
                        <div>具体的活动目录信息</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {dateFormat} from '@/assets/js/common';
import {mapState} from 'vuex'
import AlertCount from '@/components/common/AlertCount'
export default {
    name: "group-left-intro",
    data() {
        return {

        }
    },
    created(){

    },
    computed: {
        ...mapState({
            activities: state => state.index.activities,
            entries: state => state.entry.entries,
            name: state => state.index.entry_name,
            domain: state => state.index.domain,
            data_type: state => state.index.data_type
        }),
        info() {
            if (this.entries.hasOwnProperty(this.name)) {
                return this.entries[this.name];
            } else {
                return {}
            }
        },
        loading() {
            return !this.entries.hasOwnProperty(this.name)
        },
        sensitive() {
            return this.info["is_sensitive"]
        },
        disabled() {
            return this.info["is_disabled"]
        },
        displayName() {
            if (this.loading) {
                return "查询中..."
            } else {
                return this.info["cn"]
            }
        },
        whenCreated() {
            return dateFormat("YYYY-mm-dd HH:MM:SS", new Date(this.info["whenCreated"]))
        }
    },
    methods: {
        is_active(type) {
            return this.data_type === type
        },
        change_type(type) {
            this.$store.commit("set_data_type", {
                data_type: type
            })
        }
    },
    components: {
        "alert-count": AlertCount
    }
}
</script>

<style scoped>
.group-left-intro {
    display: flex;
    flex-direction: column;
    width: 270px;
    height: 930px;
}

.avatar-outer {
    display: flex;
    align-items: flex-end;
}

.avatar-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 75px;
    width: 75px;
    background: #fff;
    border-radius: 50px;
}

.avatar-info {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 270px;
    height: 230px;
    padding: 20px 30px;
    background: #0294FF;
    border-radius: 2px 2px 0 0;
    border-radius: 2px 2px 0px 0px;

}

.avatar-flag {
    margin-left: -25px;
}


.name {
    color: #fff;
    font-size: 24px;
    text-align: left;
    font-family: PingFangSC-Semibold;
}

.desc {
    color: #fff;
    color: rgba(255,255,255,0.80);
}

.detail-info {
    display: flex;
    flex-direction: column;
    width: 270px;
    height: 700px;
    background: #fff;
    border-radius: 0 0 2px 2px;
    border-radius: 0px 0px 2px 2px;
}

.base-info {
    padding: 20px 20px;
}

.base-info>div {
    margin: 30px 0px;
}

.item-name {
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: rgba(37,37,37,0.50);
}

.other-selection>div {
    height: 88px;
    width: 270px;
    padding: 20px;
    display: flex;
    flex-direction: row;
    cursor: pointer;
}

.active {
    background: #FAFBFC;
}

.avatar-kulou {
    color: #FD7B1F;
    background: #fd7b1f47;
    border-radius: 12px;
    height: 48px;
    width: 48px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.avatar-data {
    color: #0093EE;
    background: rgba(0,147,238,0.20);
    border-radius: 12px;
    height: 48px;
    width: 48px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.other-selection-name {
    margin-left: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.other-selection-title {
    font-size: 14px;
    color: rgba(37,37,37,0.50);
}

.activity-count {
    display: flex;
    flex: 1;
    align-items: center;
    justify-content: flex-end;
}
</style>