<template>
    <div class="common-detail">
        <common-table :column_list="column_list"></common-table>
    </div>
</template>

<script>
import CommonTable from '@/components/alert_detail/CommonTable';
export default {
	name: "common-detail",
    props: {
        column_list: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
        	
        }
    },
    components: {
    	"common-table": CommonTable
    }
}
</script>

<style scoped>

</style>