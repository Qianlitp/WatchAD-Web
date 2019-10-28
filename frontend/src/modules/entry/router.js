import Vue from 'vue'
import VueRouter from 'vue-router'
import UserView from './views/UserView'
import ComputerView from './views/ComputerView'
import GroupView from './views/GroupView'


Vue.use(VueRouter)

const routes = [
    {
    	path: '/user/:domain/:user_name', 
    	component: UserView
    },
    {
    	path: '/computer/:domain/:computer_name', 
    	component: ComputerView
    },
    {
    	path: '/group/:domain/:group_name', 
    	component: GroupView
    }
]

export default new VueRouter({
    routes: routes
})