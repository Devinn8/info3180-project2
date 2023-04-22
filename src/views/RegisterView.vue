<template>
  <div class="register-container">
      <div class="register-content">
          <h1>Register</h1>
          <RegisterForm />  
      </div>
  </div> 
</template>

<script>
import RegisterForm from '../components/RegisterForm.vue'
export default {
  components: { RegisterForm }
}
</script>

<style scoped>
.register-container{
  min-height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.register-content{
  width: 40%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
</style>