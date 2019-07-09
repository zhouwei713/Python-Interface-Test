import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import './plugins/element.js'
import Table from './components/Table/Table.vue'
import Navi from './components/Navi/Navi.vue'
import router from './router/index'

Vue.config.productionTip = false

Vue.use(ElementUI)

new Vue({
	el: '#app',
	router,
	render: h => h(Table)
})

// new Vue({
//   render: h => h(App),
// }).$mount('#app')
