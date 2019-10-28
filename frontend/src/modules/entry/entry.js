import Vue from 'vue'
import App from './App.vue'
import iView from 'view-design';
import store from './store';
import router from './router';
import VueProgressBar from 'vue-progressbar'
import VueResourceProgressBarInterceptor from 'vue-resource-progressbar-interceptor'
import 'view-design/dist/styles/iview.css';
import './assets/css/common.css';
import '@/assets/css/common.css'


Vue.use(VueProgressBar, {
    color: '#2d8cf0',
    failedColor: '#ed3f14',
    thickness: '3px',
    transition: {
        speed: '0.2s',
        opacity: '0.6s',
        termination: 300
    },
    autoRevert: true,
    location: 'top',
    inverse: false
})

Vue.use(VueResourceProgressBarInterceptor,{
    latencyThreshold: 0, // Number of ms before progressbar starts showing, 100 is default
    responseLatency: 50, // Number of ms before progressbar starts reacting to response, 50 is default
                         // Can be used to wait for more requests to kick in under single progress bar
})

Vue.use(iView)
Vue.config.productionTip = true;

const app = new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');