import Vue from 'vue'
import VueRouter from 'vue-router'
import ActivityView from './views/ActivityView'

Vue.use(VueRouter)

const routes = [
    { 
    	path: '/:activity_id', 
    	component: ActivityView
    }
]

export default new VueRouter({
    routes: routes
})