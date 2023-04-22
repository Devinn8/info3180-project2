<template>
  <div class="login-container">
      <div class="login-content">
          <h1>Login</h1>
          <LoginForm />  
      </div>
  </div> 
</template>

<script>
import LoginForm from '../components/LoginForm.vue'
export default {
  components: { LoginForm }
}
</script>

<style scoped>
.login-container{
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.login-content{
  width: 40%;
  display: flex;
  align-items: left;
  flex-direction: column;
}
</style>