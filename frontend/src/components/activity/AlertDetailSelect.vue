<script>
import {mapState} from 'vuex';
import ACLModify from '@/components/alert_detail/401_acl_modify';
import CommonDetail from '../alert_detail/CommonDetail';
export default {
	name: "alert-detail-select",
    data() {
        return {
        	
        }
    },
    created() {

    },
    computed: {
        ...mapState({
            activity: state => state.index.activity
        }),
        alert_list() {
            return this.activity["alert_list"];
        }, 
        alert_code() {
            return this.activity["alert_code"];
        }
    },
    methods: {
        get_column_list(code) {
            if (!code) {
                return []
            }
            let col_map = {
                "101": ["source_ip", "source_workstation", "source_user_name", "group_name"],
                "102": ["source_ip", "source_workstation", "source_user_name", "target_user_name"],
                "103": ["source_ip", "source_workstation", "source_user_name", "dc_hostname"],
                "104": ["source_ip", "source_workstation", "target_user_name"],
                "201": ["source_ip", "source_workstation", "target_user_name", "spn"],
                "202": ["source_ip", "source_workstation", "target_user_name"],
                "203": ["source_ip", "source_workstation", "source_user_name", "dc_hostname"],
                "301": ["source_ip", "source_workstation", "brute_force_type", "brute_force_target_users"],
                "302": ["source_ip", "source_workstation", "target_user_name", "target_server_name"],
                "303": ["source_ip", "source_workstation", "source_user_name", "dc_hostname", "tool_name"],
                "304": ["source_ip", "source_workstation", "source_user_name", "dc_hostname", "relative_target_name"],
                "305": ["source_ip", "source_workstation", "target_user_name", "normal_enc", "exceptional_enc", "dc_hostname"],
                "306": ["source_ip", "source_workstation", "target_user_name"],
                "401": ["source_ip", "source_workstation", "source_user_name", "object_class", "abnormal_users"],
                "402": ["source_ip", "source_workstation", "target_user_name", "target_user_sid"],
                "403": ["source_ip", "source_workstation", "dc_hostname"],
                "404": ["source_ip", "source_workstation", "source_user_name", "gpo_guid"],
                "405": ["source_ip", "source_workstation", "relay_ip", "relay_workstation", "target_user_name", "dc_hostname", "ntlm_version"],
                "406": ["source_ip", "source_workstation", "source_user_name", "target_computer", "target_user_name", "target_user_sid"],
                "407": ["source_ip", "source_workstation", "source_user_name", "dc_hostname"],
                "408": ["source_ip", "source_workstation", "target_user_name", "dc_hostname"],
                "409": ["source_ip", "source_workstation", "source_user_name", "target_computer", "target_user_name", "target_service"],
                "410": ["source_ip", "source_workstation", "source_user_name", "dc_hostname"],
                "501": ["source_ip", "source_workstation", "source_user_name"],
                "502": ["source_ip", "source_workstation", "source_user_name", "dc_hostname", "alert_rule"],
                "503": ["source_ip", "source_workstation", "source_user_name", "dc_hostname"],
                "504": ["source_ip", "source_workstation", "source_user_name", "abnormal_users"],
                "505": ["source_ip", "source_workstation", "source_user_name", "target_user_name", "new_delegation_list"],
                "506": ["source_ip", "source_workstation", "source_user_name", "target_user_name", "group_name"],
                "507": ["source_ip", "source_workstation", "source_user_name", "service_name", "dc_hostname"],
                "508": ["source_ip", "source_workstation", "source_user_name", "task_name", "dc_hostname"],
                "509": ["source_ip", "source_workstation", "source_user_name", "target_user_name"],
                "510": ["source_ip", "source_workstation", "target_user_name", "detect_type", "dc_hostname"],
                "511": ["source_ip", "source_workstation", "target_user_name", "service_name", "enc_type"],
                "512": ["source_ip", "source_workstation", "target_user_name", "detect_type", "dc_hostname"],
                "601": ["source_ip", "source_workstation", "source_user_name", "dc_hostname"],
                "602": ["dc_hostname"]
            }
            return col_map[code];
        }
    },
    render: function (createElement) {
        let detail_map = {
            "401": ACLModify
        };

        if (this.alert_code in detail_map) {
            return createElement(
                detail_map[this.alert_code],
                {
                    props: {
                        alert_list: this.alert_list
                    }
                }
            )
        }

        return createElement(
            CommonDetail,
            {
                props: {
                    alert_list: this.alert_list,
                    alert_code: this.alert_code,
                    column_list: this.get_column_list(this.alert_code)
                }
            }
        )
    }
}
</script>

<style scoped>

</style>