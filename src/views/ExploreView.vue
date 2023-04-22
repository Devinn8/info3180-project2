<template>
  <div class="about container">
    <div class="posts-view">
      <Post 
        v-for="post in posts"
        :key="post.id"
        :id="post.id"
        :profile-photo="`../uploads/${post.profile-photo}`"
        :username="post.username"
        :photo="`../uploads/${post.photo}`"
        :caption="post.caption"
        :likes="post.likes"
        :date="post.date"
      />
    </div>
    <div class="make-post-container">
      <RouterLink to="/posts/new" class="make-post link">New Post</RouterLink>
    </div>
  </div>
</template>
<script>
import { RouterLink } from "vue-router";
import PostService from '@/services/cars.service.js'
import Post from '../components/Post.vue'
export default {
    components: { Post },
    data(){
        return {
            make: '',
            model: '',
            error: false,
            message: '',
            cars: []
        }
    },
    async beforeMount(){
      let res = await CarService.getAll()
      if(res){
        this.cars = [...res.data.slice(-3)]
      } else {
        this.error = true
        AuthService.handleLogout()
      }
    },
    methods: {
        async searchCars(){
            let res = await CarService.querySearch(this.make, this.model)
            if(res){
              this.error = false
              this.cars = [...res]
              console.log(res)
            } else {
              this.error = true
              AuthService.handleLogout()
            }
        }
    }
}
</script>

<style scoped>
.search-bar{
  margin: 0 auto;
  padding: 1rem 0;
  box-shadow: 10px 0 40px rgba(19, 19, 19, 0.1);
}
form{
  padding: 1rem;
}
input{
  display: block;
  border: 1px solid rgba(19, 19, 19, 0.1);
  border-radius: 5px;
}
.col{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
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
.cards-view{
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 2rem;
  margin: 4rem 0;
}
.link{
  height: 44px;
  padding: 16px 32px;
  border: 1px solid #0eb881;
  border-radius: 6px;
  text-decoration: none;
  margin-right: 12px;
}
.make-post{
  color: #4a90e2;
}
</style>