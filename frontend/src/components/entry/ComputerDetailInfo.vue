<template>
    <div class="computer-detail-info">
        <div class="base-info">
            <div class="account-info">
                <div class="title">Account Info</div>
                <div class="account-content">
                    <div>
                        <div class="item-name">SAM 名称</div> 
                        <div class="item-value">{{detail_data["sAMAccountName"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">SID</div> 
                        <div class="item-value">{{detail_data["objectSid"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">DN</div> 
                        <div class="item-value">{{detail_data["distinguishedName"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">DNS Name</div> 
                        <div class="item-value">{{detail_data["dNSHostName"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">Res-Based Delegation</div> 
                        <div class="item-value">
                            <div v-for="item in detail_data['msDS-AllowedToActOnBehalfOfOtherIdentity']">
                                {{item["type_name"]}}: <span style="font-weight: 700">{{item["user_name"]}}</span> ({{item["sid"]}})
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="item-name">SPNs</div> 
                        <div class="item-value">
                            <div v-for="each in detail_data['servicePrincipalName']">{{each}}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="user-account-control">
                <div class="title">User Access Control</div>
                <div class="uac-content">
                    <div 
                        v-for="(value, name) in uac_obj" 
                        class="uac-item" 
                        :class="{'enable': value}"
                        :title="name">{{readable_name_map[name]}}</div>
                </div>
            </div>
        </div>
        <div class="member-info">
            <div class="member-of">
                <div class="title">Member Of</div>
                <div class="memberof-content">
                    <div class="direct-group">
                        <div class="sub-title">直属用户组（{{memberOf.length}}）</div>
                        <div class="item-list">
                            <multi-entry-item 
                            v-for="group in memberOf" 
                            :keys="group['cn']"
                            :icon_name="group_icon_name"
                            :name="group['cn']"
                            :domain="domain"
                            :is_sensitive="group['is_sensitive']"
                            :second_text="group['description']"
                            :disable_poptip="false"
                            entry_type="group"></multi-entry-item>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import MultiEntryItem from '@/components/common/MultiEntryItem';
export default {
    name: "computer-detail-info",
    data() {
        return {
            readable_name_map: {
                "ACCOUNT_DISABLE": "禁用账户",
                "LOCKOUT": "锁定",
                "PASSWD_NOTREQD": "允许空密码",
                "PASSWD_CANT_CHANGE": "密码无法修改",
                "ENCRYPTED_TEXT_PWD_ALLOWED": "允许保存文本密码",
                "NORMAL_ACCOUNT": "普通账号",
                "DONT_EXPIRE_PASSWORD": "密码永不过期",
                "SMARTCARD_REQUIRED": "要求智能卡",
                "TRUSTED_FOR_DELEGATION": "可无约束委派",
                "NOT_DELEGATED": "该账户无法被委派",
                "USE_DES_KEY_ONLY": "只能使用DES加密",
                "DONT_REQ_PREAUTH": "不要求Kerberos预身份认证",
                "TRUSTED_TO_AUTH_FOR_DELEGATION": "可约束委派",
                "PASSWORD_EXPIRED": "密码已过期"
            },
            group_icon_name: "iconfont icon-group",
            user_icon_name: "iconfont icon-user"
        }
    },
    mounted() {
        this.$store.dispatch("get_detail_computer");
    },
    computed: {
        ...mapState({
            detail_data: state => state.index.detail_data,
            domain: state => state.index.domain
        }),
        uac_obj() {
            return this.detail_data["userAccountControl"];
        },
        memberOf() {
            if (!this.detail_data["memberOf"]) {
                return [];
            }
            return this.detail_data["memberOf"];
        },
        direct_members() {
            if (!this.detail_data["member"]) {
                return [];
            }
            return this.detail_data["member"];
        }
    },
    methods: {

    },
    components: {
        'multi-entry-item': MultiEntryItem
    }
}
</script>

<style scoped>
.computer-detail-info {
    display: flex;
    flex-direction: column;
    height: 930px;
    flex: 1;
    margin-left: 30px;
    justify-content: space-between;
    width: 100%;
}

.base-info {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: space-between;
}

.title {
    height: 40px;
    font-size: 14px;
    color: #9FA9BA;
    font-family: PingFangSC-Regular;
    padding: 20px;
}

.account-info {
    background: #fff;
    border: 0 solid #E6EAEE;
    border-radius: 4px;
    height: 300px;
    flex: 1;
    margin-right: 30px;
}

.account-content {
    display: flex;
    flex-direction: column;
    padding-bottom: 30px;
    padding-top: 10px;
    max-height: 240px;
    overflow: auto;
}

.account-content>div {
    display: flex;
    margin: 5px 30px;
}

.item-name {
    width: 150px;
    font-size: 12px;
    color: #9FA9BA;
}

.user-account-control {
    width: 420px;
    background: #fff;
    border: 0 solid #E6EAEE;
    border-radius: 4px;
    height: 300px;
}

.member-info {
    display: flex;
    justify-content: space-between;
}

.member-of {
    background: #fff;
    border: 0 solid #E6EAEE;
    border-radius: 4px;
}

.members {
    margin-left: 30px;
    background: #fff;
    border: 0 solid #E6EAEE;
    border-radius: 4px;
}

.member-of, .members{
    flex: 1;
}

.memberof-content, .members-content {
    height: 560px;
}

.uac-content {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    justify-content: space-between;
    padding: 10px 20px;

}

.uac-item {
    width: 180px;
    margin: 10px 0px;
    height: 27px;
    border: 1px solid #a9c4de;
    border-radius: 20px;
    text-align: center;
    line-height: 27px;
    color: #a9c4de;
}

.enable {
    background: #0294FF;
    color: #fff;
    border: 1px solid #0294FF;
}

.sub-title {
    font-size: 12px;
    font-weight: 700;
    padding: 10px 0px 10px 20px;
    font-family: PingFangSC-Medium
}

.item-list {
    overflow: auto;
    padding: 0px 20px;
    display: flex;
    max-height: 500px;
    flex-direction: column;
    align-items: stretch;
}
</style>