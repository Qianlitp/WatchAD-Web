import Vue from 'vue'
import VueRouter from 'vue-router'
import SettingsView from './views/SettingsView'


Vue.use(VueRouter)

const routes = [
    {
    	path: '/', 
    	component: SettingsView
    }
]

export default new VueRouter({
    routes: routes
})