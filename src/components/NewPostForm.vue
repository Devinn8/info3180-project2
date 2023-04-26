<template>
  <div class="post-form">
      <div v-if="error" class="error alert alert-danger">Invalid information</div>
      <div class="alert alert-success" role="alert" v-if="message">{{ message }}</div>
      <form 
          @submit.prevent="addNewPost" 
          method="post" 
          enctype="multipart/form-data"
          id="postForm"
          ref="postForm"
      >
          <div class="form-field">
              <label for="photo">Photo</label>
              <input 
                  type="file" 
                  name="photo" 
                  id="photo" 
                  ref="photo" 
                  accept="image/png, image/jpg, image/jpeg"
                  @change="handleFileUpload"
                  required
              />
          </div>
          <div class="form-field">
              <label for="caption">Caption</label>
              <textarea 
                  name="caption" 
                  id="caption" 
                  v-model="caption" 
                  cols="30" 
                  rows="10"
                  required
                  placeholder="Write a caption..."
              ></textarea>
          </div>
          <button type="submit" class="submit-btn">Submit</button>
      </form>
  </div>
</template>

<script>
import PostService from '@/services/posts.service.js'
import AuthService from '@/services/auth.service.js'
import TokenService from '@/services/token.service.js'
import store from '@/store/store.js'
export default {
  data(){
      return {
          photo: '',
          caption: '',
          error: false,
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
      async addNewPost(){
          let form = document.getElementById("postForm")
          let postInfo = new FormData(form)
          postInfo.append('user_id', store.getters.getUser || localStorage.getItem('id'))
          let res = await PostService.add(postInfo, this.csrf)
          console.log(res)
          if(res?.errors){
              this.error = true
              AuthService.handleLogout()
          } else {
              this.message = "Post was successfully added!"
              this.$refs.postForm.reset()
          }
      }
  }
}
</script>
<style scoped>
.post-form{
  padding: 0 2rem;
  width: 100%;
}
.post-form, input, textarea, select{
  border: 1px solid rgba(19, 19, 19, 0.1);
  border-radius: 5px;
}
input[type="file"]{
  border: none;
}
.form-field, .submit-btn{
  margin: 1rem 0;
}
input, textarea, select{
  display: block;
}
.submit-btn, input, textarea, select{
  width: 100%;
  height: 44px;
}
.submit-btn{
  border: none;
  border-radius: 5px;
  background: #0eb881;
  color: #ffffff;
}
.alert{
  margin-top: 1rem;
}
</style>