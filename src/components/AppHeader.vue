<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" style="background-color: #4a90e2;">
      <div class="container-fluid">
        <a class="navbar-brand company-logo" href="/">
          <span class="material-icons-outlined" style="color: rgb(0, 0, 0);">camera_alt</span>
          <span class="company-name">Photogram</span>
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" >
          <ul class="navbar-nav ms-auto" v-if="currentUser">
            <li class="nav-item">
              <RouterLink to="/cars/new" class="nav-link">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="`/users/${userId}`">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto" v-else>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
             <li class="nav-item">
              <RouterLink to="/register" class="nav-link register-link">Register</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
import store from '@/store/store.js'
export default {
  computed: {
    currentUser(){
      return  store.getters.getAuth !== null || localStorage.getItem("authToken")
    },
    userId(){
      return store.getters.getUser || localStorage.getItem("id")
    }
  }
}
</script>

<style scoped>
/* Add any component specific styles here */
.company-logo{
  display: flex;
  align-items: center;
  gap: 10px;
}
@font-face {
  font-family: 'Altoysjustpersonalonly-Italic';
  src: url('@/assets/fonts/Altoysjustpersonalonly-Italic.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

.company-name {
  font-family: 'Oleo Script Swash Caps', cursive;
  color: #fff;
}

.nav-link{
  color: #fff!important;
  font-weight: 600;
}
</style>