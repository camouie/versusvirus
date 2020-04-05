import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Guidelines from '../views/Guidelines'
import About from '../views/About'
import graph_test from '../views/graph_test.vue'
import AppHeader from "../layout/AppHeader"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    components: {
        header: AppHeader,
        default: Home,
      },
    props : true
  },
    {
        path: '/guidelines',
        name: 'Guidelines',
        components: {
            header: AppHeader,
            default: Guidelines,
        }
    },
    {
        path: '/about',
        name: 'About',
        components: {
            header: AppHeader,
            default: About,
        }
    },
  {
    path: '/graph_test',
    name: graph_test,
    components: {
        header: AppHeader,
        default: graph_test
      },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
