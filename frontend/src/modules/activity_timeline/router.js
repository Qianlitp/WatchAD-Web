import Vue from 'vue'
import VueRouter from 'vue-router'
import TimelineView from './views/ActivityTimeLineView'

Vue.use(VueRouter)

const routes = [
    { 
    	path: '/', 
    	component: TimelineView
    }
]

export default new VueRouter({
    routes: routes
})