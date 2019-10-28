<script>
import {mapState} from 'vuex';
export default {
	name: "description-base",
    props: {
        render_func: {
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
        return this.render_func(createElement)
    }
}
</script>

<style scoped>

</style>