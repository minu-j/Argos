import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/views/HomeView'
import TicketView from '@/views/TicketView'
import PlayView from '@/views/PlayView'
import NewsView from '@/views/NewsView'
import LoginView from '@/views/LoginView'
import SignUpView from '@/views/SignUpView'
import MyPageView from '@/views/MyPageView'
import NotFound404 from '@/views/NotFound404'
import MovieRating from '@/components/MovieRating'
import MovieDetail from '@/components/MovieDetail'


Vue.use(Router)

export const constantRoutes = [
  {
    path: '/home',
    name: 'HomeView',
    component: HomeView,
    meta: {
      title: 'ARGOS'
    }
  },
  {
    path: '/ticket',
    name: 'TicketView',
    component: TicketView,
    meta: {
      title: 'ARGOS Ticket'
    }
  },
  {
    path: '/play',
    name: 'PlayView',
    component: PlayView,
    meta: {
      title: 'ARGOS Play'
    }
  },
  {
    path: '/news',
    name: 'NewsView',
    component: NewsView,
    meta: {
      title: 'ARGOS News'
    }
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    meta: {
      title: 'ARGOS 회원가입'
    }
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    meta: {
      title: 'ARGOS 로그인'
    }
  },
  {
    // path: '/mypage/:username',
    path: '/mypage/:username',
    name: 'MyPageView',
    component: MyPageView,
    meta: {
      title: 'ARGOS 마이페이지'
    }
  },
  {
    path: '/rating',
    name: 'MovieRating',
    component: MovieRating,
    meta: {
      title: 'ARGOS'
    }
  },
  {
    path: '/movie/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail,
    meta: {
      title: 'ARGOS'
    },
    props: true
  },
  {
    path: '*',
    name: 'NotFound404',
    component: NotFound404,
    meta: {
      title: 'ARGOS?'
    }
  },
]

const createRouter = () => new Router({
  mode: 'history',
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

router.afterEach((to) => {
  const title = to.meta.title === undefined ? 'ARGOS' : to.meta.title;
  Vue.nextTick(() => {
    document.title = title;
  });
});


export default router
