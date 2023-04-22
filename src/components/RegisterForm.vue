<template>
  <div class="register-form">
      <div v-if="errors" class="alert alert-danger">
          <ul>
              <li v-for="error in errors" :key="errors.indexOf(error)">
                  {{ error }}
              </li>
          </ul>
      </div>
      <div class="alert alert-success" role="alert" v-if="message">{{ message }}</div>
      <form 
          @submit.prevent="registerUser" 
          method="post" 
          enctype="multipart/form-data"
          id="registerForm"
      >
          <div class="row">
              <div class="form-field col">
                  <label for="username">Username</label>
                  <input 
                      type="text" 
                      name="username" 
                      id="username" 
                      v-model="username"
                      required
                  />
              </div>
            </div>
            <div class="row">
              <div class="form-field col">
                  <label for="password">Password</label>
                  <input 
                      type="password" 
                      name="password" 
                      id="password"
                      pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                      title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" 
                      v-model="password"
                      required
                  >
              </div>
          </div>
          <div class="row">
              <div class="form-field col">
                  <label for="firstname">First Name</label>
                  <input 
                      type="text" 
                      name="firstname" 
                      id="firstname" 
                      v-model="firstname"
                      required
                  />
              </div>
            </div>
            <div class="row">
              <div class="form-field col">
                  <label for="lastname">Last Name</label>
                  <input 
                      type="text" 
                      name="lastname" 
                      id="lastname" 
                      v-model="lastname"
                      required
                  />
              </div>
            </div>
            <div class="row">
              <div class="form-field col">
                  <label for="email">Email</label>
                  <input 
                      type="email" 
                      name="email" 
                      id="email" 
                      v-model="email"
                      required
                  />
              </div>
          </div>
          <div class="row">
              <div class="form-field col">
                  <label for="location">Location</label>
                  <input 
                      type="text" 
                      name="location" 
                      id="location" 
                      v-model="location"
                      required
                  />
              </div>
              <div class="col"></div>
          </div>
          <div class="form-field">
              <label for="biography">Biography</label>
              <textarea 
                  name="biography" 
                  id="biography" 
                  v-model="biography" 
                  cols="30" 
                  rows="10"
                  required
              ></textarea>
          </div>
          <div class="form-field">
              <label for="photo">Photo</label>
              <input 
                  type="file" 
                  name="photo" 
                  id="photo"
                  ref="photo" 
                  accept="image/png, image/jpg, image/jpeg"
                  required
                  @change="handleFileUpload"
              />
          </div>

          <button type="submit" class="submit-btn">Register</button>
      </form>
  </div>
</template>

<script>
import AuthService from '@/services/auth.service.js'
import TokenService from '@/services/token.service.js'
import store from '@/store/store.js'
export default {
  data(){
      return {
          username: '',
          password: '',
          firstname: '',
          lastname: '',
          email: '',
          location: '',
          biography: '',
          photo: '',
          errors: null,
          message: '',
          csrf: ''
      }
  },
  async created(){
      let res = await TokenService.getCrsfToken()
      this.csrf = res.csrf_token
  },
  methods: {
      handleFileUpload(){
          this.photo = this.$refs.photo.files[0]
      },
      async registerUser(){
          let form = document.getElementById("registerForm")
          let userInfo = new FormData(form)
          let res = await AuthService.register(userInfo, this.csrf)
          console.log(res)
          if(res?.errors){
              this.errors = [...res.errors]
              setTimeout(() => {
                  this.errors = null
              }, 1500);
          } else {
              // console.log(res)
              this.error = null
              this.message = "Account was successfully created"
              setTimeout(() => {
                  this.$router.push("/login")
              }, 1500);
          }
      }
  }
}
</script>
<style scoped>
.register-form{
  padding: 0 2rem;
  width: 100%;
}
.register-form, input, textarea{
  border: 1px solid rgba(19, 19, 19, 0.1);
  border-radius: 5px;
}
input[type="file"]{
  border: none;
}
.form-field, .submit-btn{
  margin: 1rem 0;
}
.form-field input, .form-field textarea{
  display: block;
}
.submit-btn, input, textarea{
  width: 100%;
  height: 44px;
}
.submit-btn{
  border: none;
  border-radius: 5px;
  background: #7ed321;
  color: #ffffff;
}
ul, li{
  margin: 0;
}
.alert{
  margin-top: 1rem;
}
</style>
