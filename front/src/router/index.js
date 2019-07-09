import Vue from 'vue'
import VueRouter from 'vue-router'
import index from '../components/index.vue'
import page1 from '../components/page1.vue'

Vue.use(VueRouter)

const router = new VueRouter({
	routers:[{
		path: '/index', components:index
	},
	{
		path: '/page1', components:page1
	}
	]
})
export default router;