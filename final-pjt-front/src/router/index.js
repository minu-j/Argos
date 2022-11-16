import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import TicketView from '@/views/TicketView'
import PlayView from '@/views/PlayView'
import NewsView from '@/views/NewsView'
import LoginView from '@/views/LoginView'
import MyPageView from '@/views/MyPageView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/ticket',
    name: 'TicketView',
    component: TicketView
  },
  {
    path: '/play',
    name: 'PlayView',
    component: PlayView
  },
  {
    path: '/news',
    name: 'NewsView',
    component: NewsView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/mypage',
    name: 'MyPageView',
    component: MyPageView
  },
  {
    path: '*',
    name: 'NotFound404',
    component: NotFound404
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
