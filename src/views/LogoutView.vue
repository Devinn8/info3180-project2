<template>
  <div class="logout-view">
      <div v-if="logout">
          <h1>You've been successfully logged out!</h1>
          <p>Here are some useful links to regain access to the system.</p>
          <div class="d-flex justify-content-center">
              <RouterLink to="/" class="nav-link">Home</RouterLink>
              <RouterLink to="/login" class="nav-link">Login</RouterLink>
              <RouterLink to="/register" class="nav-link">Register</RouterLink>
          </div>
      </div>
      <div v-else>
          <h1>Loading...</h1>
      </div>
  </div>
</template>
<script>
import { RouterLink } from "vue-router";
import AuthService from '@/services/auth.service.js'
import TokenService from '@/services/token.service.js'
export default {
  
  data(){
      return {
          logout: false
      }
  },
  async beforeMount(){
      let token = await TokenService.getCrsfToken()
      let res = await AuthService.logout(token.csrf_token)
      if(res){
          this.logout = true
          AuthService.handleLogout()
      }
  }
}
</script>

<style scoped>
.logout-view{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  text-align: center;
}
</style>