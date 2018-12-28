import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home'
import Results from '@/components/results'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      name: 'HelloWorld',
      path: '/hello',
      component: HelloWorld
    },
    {
    	name: 'Home',
    	path: '/',
    	component: Home
    },
    {
    	name: 'Home',
    	path: '/home',
    	component: Home
    },
    {
    	name: 'Results',
    	path: '/results',
    	component: Results
    },
  ]
})