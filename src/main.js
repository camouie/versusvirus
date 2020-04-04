import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Argon from "./plugins/argon-kit"
import { library } from '@fortawesome/fontawesome-svg-core'
import { faRobot, faSearchLocation,  faUserEdit, faFileAlt, faSpellCheck} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faRobot, faSearchLocation, faUserEdit, faFileAlt, faSpellCheck)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(Argon)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
