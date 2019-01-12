import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home'
import Results from '@/components/results'
import Result from '@/components/result'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
    	name: 'Home',
    	path: '/',
    	component: Home
    },
    {
    	name: 'Results',
    	path: '/results',
    	component: Results
    },
    {
    	name: 'Result',
    	path: '/result',
    	component: Result
    },
  ]
})