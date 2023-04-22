import { createStore } from 'vuex'

const store = new createStore({
  state: {
    auth: null,
    user: null,
  },
  getters: {
    getAuth(state){ return state.auth },
    getUser(state){ return state.user }
  },
  mutations: {
    setAuth(state, payload){
        state.auth = payload.auth;
    },
    setUser(state, payload){
        state.user = payload.user;
    }
  },
})
export default store