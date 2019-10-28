<script>
import {mapState} from 'vuex';
import {entries} from '@/assets/js/common';
import EntryName from '@/components/common/EntryName';
import MultiEntryName from '@/components/common/MultiEntryName';
export default {
	name: "description",
    props: {
        desc_template: {
            type: String,
            required: true
        },
        desc_data: {
            type: Array,
            required: true
        },
        domain: {
            type: String,
            required: true
        }
    },
    data() {
        return {
        	
        }
    },
    computed: {
    	...mapState({
            
        })
    },
    created() {

    },
    render: function (createElement) {

        let result_list = [];
        let desc_list = this.desc_template.split(/\[.+?\]/);
        for (let i = 0; i < this.desc_data.length; i++) {
            result_list.push(desc_list[i])
            let name = this.desc_data[i]["name"];
            let value = this.desc_data[i]["value"];
            if (value.length > 1) {
                result_list.push(
                    createElement(
                        MultiEntryName, 
                        {
                            props: {
                                field_name: name,
                                entry_data: value,
                                domain: this.domain,
                                entry_type: value[0]["type"]
                            }
                        }
                    )
                )
            } else {
                result_list.push(
                    createElement(
                        EntryName, 
                        {
                            props: {
                                field_name: name,
                                value: value[0]["name"],
                                domain: this.domain,
                                entry_type: value[0]["type"]
                            }
                        }
                    )
                )
            }
        }
        result_list.push(desc_list[desc_list.length - 1]);

        return createElement(
            'p', {"style": "white-space: normal;"}, result_list
        )
    }
}
</script>

<style scoped>

</style>