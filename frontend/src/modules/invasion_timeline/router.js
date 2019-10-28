import Vue from 'vue'
import VueRouter from 'vue-router'
import InvasionTimeLineView from './views/InvasionTimeLineView'


Vue.use(VueRouter)

const routes = [
    {
    	name: "index",
    	path: '/', 
    	component: InvasionTimeLineView
    }
]

export default new VueRouter({
    routes: routes
})
