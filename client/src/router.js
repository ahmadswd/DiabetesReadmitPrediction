import Vue from 'vue'
import Router from 'vue-router'
import Ping from './components/Ping.vue'
import HW from './components/HelloWorld.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(Router)
Vue.use(BootstrapVue)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'ping',
      component: Ping,
    },
    {
      path: '/Result',
      name: 'result',
      component: HW,
    }
  ],
});
