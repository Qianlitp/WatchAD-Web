import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexSearchView from './views/IndexSearchView';


Vue.use(VueRouter)

const routes = [
    {
    	path: '/', 
    	component: IndexSearchView
    }
]

export default new VueRouter({
    routes: routes
})