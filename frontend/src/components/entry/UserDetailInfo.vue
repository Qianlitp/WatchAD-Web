<template>
    <div class="user-detail-info">
        <div class="base-info">
            <div class="account-info">
                <div class="title">账号信息</div>
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
                        <div class="item-name">UPN</div> 
                        <div class="item-value">{{detail_data["userPrincipalName"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">DN</div> 
                        <div class="item-value">{{detail_data["distinguishedName"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">SPNs</div> 
                        <div class="item-value">
                            <div v-for="each in detail_data['servicePrincipalName']">{{each}}</div>
                        </div>
                    </div>
                    <div>
                        <div class="item-name">创建于</div> 
                        <div class="item-value">{{detail_data["whenCreated"]}}</div>
                    </div>
                    <div>
                        <div class="item-name">约束委派</div> 
                        <div class="item-value">
                            <div v-for="each in detail_data['msDS-AllowedToDelegateTo']">{{each}}</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="user-account-control">
                <div class="title">用户访问控制</div>
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
            <div class="group-info">
                <div class="title">用户组信息</div>
                <div class="group-content">
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
                    <div class="recursive-group">
                        <div class="sub-title">递归用户组（{{recursive_groups.length}}）</div>
                        <div class="item-list">
                            <multi-entry-item 
                            v-for="group in recursive_groups" 
                            :keys="group['cn']"
                            :icon_name="group_icon_name"
                            :name="group['cn']"
                            :domain="domain"
                            :is_sensitive="group['is_sensitive']"
                            :second_text="group['description']"
                            :disable_poptip="false"
                            entry_type="group"
                            :other_info="group['recursive_count'] + 'nd'"></multi-entry-item>
                        </div>
                    </div>
                </div>
            </div>
            <div class="organization-structure">
                <div class="title">组织架构</div>
                <div class="structure-content">
                    <div class="manager">
                        <div class="sub-title">上级/经理</div>
                        <div class="item-list">
                            <multi-entry-item 
                            v-if="manager"
                            :icon_name="user_icon_name"
                            :name="manager['cn']"
                            :domain="domain"
                            :is_sensitive="manager['is_sensitive']"
                            :is_disabled="manager['is_disabled']"
                            :disable_poptip="false"
                            entry_type="user"></multi-entry-item>
                        </div>
                        
                    </div>
                    <div class="direct-reports">
                        <div class="sub-title">直接下属（{{direct_reports.length}}）</div>
                        <div class="item-list">
                            <multi-entry-item 
                            v-for="user in direct_reports" 
                            :keys="user['cn']"
                            :icon_name="user_icon_name"
                            :name="user['cn']"
                            :domain="domain"
                            :is_sensitive="user['is_sensitive']"
                            :is_disabled="user['is_disabled']"
                            :disable_poptip="false"
                            entry_type="user"></multi-entry-item>
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
    name: "user-detail-info",
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
        this.$store.dispatch("get_detail_user");
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
        recursive_groups() {
            if (!this.detail_data["recursive_groups"]) {
                return [];
            }
            return this.detail_data["recursive_groups"];
        },
        manager() {
            return this.detail_data["manager"];
        },
        direct_reports() {
            if (!this.detail_data["directReports"]) {
                return [];
            }
            return this.detail_data["directReports"];
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
.user-detail-info {
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

.group-info, .organization-structure{
    flex: 1;
}

.group-info {
    background: #fff;
    border: 0 solid #E6EAEE;
    border-radius: 4px;
}

.organization-structure {
    margin-left: 30px;
    background: #fff;
    border: 0 solid #E6EAEE;
    border-radius: 4px;
}

.group-content, .structure-content {
    height: 560px;
}

.user-account-control .content {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    justify-content: space-between;
    padding: 10px 20px;

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

.direct-group {

}

.item-list {
    overflow: auto;
    max-height: 210px;
    padding: 0px 20px;
    display: flex;
    flex-direction: column;
    align-items: stretch;
}
</style>