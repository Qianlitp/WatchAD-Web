import Vue from 'vue'
import VueRouter from 'vue-router'
import EntrySearchView from './views/EntrySearchView'


Vue.use(VueRouter)

const routes = [
    {
    	name: "entry_search",
    	path: '/:entry_name', 
    	component: EntrySearchView
    }
]

export default new VueRouter({
    routes: routes
})
