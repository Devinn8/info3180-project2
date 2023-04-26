<template>
  <div class="profile container">
        <div class="card" v-if="user">
            <div class="row">
                <div class="col-5 d-flex justify-content-center">
                    <img 
                      :src="`../../uploads/${user.photo}`" 
                      class="img-fluid profile-img" 
                      alt="User's profile"
                    >
                </div>
                <div class="col-7">
                    <div class="card-body">
                        <h6 class="card-title">{{ user.name }}</h6>
                        <p class="card-text text-muted">{{ user.location }}</p>
                        <p class="card-text text-muted">{{ `Member since ${formattedDate(user.joined_on) }` }}</p>
                        <p class="card-text text-muted">{{ user.biography }}</p>    
                    </div>
                </div>
                <div class="col-5 d-flex justify-content-center">
                  <div class="row">
                    <div class="col">
                      <p class="col">{{ user.posts }}</p>
                      <p class="col-2">Posts</p>
                    </div>
                    <div class="col">
                      <p class="col">{{ user.followers }}</p>
                      <p class="col-2">Followers</p>
                    </div>
                  </div>
                  <div class="row">
                    <div v-if="car.favourited" class="d-flex">
                      <button class="follow-btn">Follow</button>
                    </div>
                    <div v-else  class="d-flex" role="button" @click="FollowUser(user.id)">
                      <button class="follow-btn">Following</button>
                    </div>
                  </div>
                </div>
            </div>
        </div>
        <div class="post-container">
          <div class="post-view">
            <div v-for="post in posts" :key="post.user_id">
              <img :src="`../uploads/${post.photo}`" alt="Image of post">
            </div>
          </div>
      </div>
  </div>
</template>

<script>
import ProfileService from '@/services/profile.service.js'
import AuthService from '@/services/auth.service.js'
import store from '@/store/store'
export default {
  data(){
    return {
      user: null,
      posts: [],
      error: false,
      message: '',
    }
  },
  methods: {
    formattedDate(date_joined) {
      const dateObj = new Date(date_joined);
      const options = { year: 'numeric', month: 'long' };

      return dateObj.toLocaleDateString('en-US', options);
    },
    async FollowUser(id){
            let response = await TokenService.getCrsfToken()
            let res = await CarService.addFav(id, response.csrf_token)
             if(res){
                console.log(res)
                await this.fetchCatchDetails()
            } else {
                this.error = true
                AuthService.handleLogout()
            }
        }
  },
  async beforeMount(){
    let id = store.getters.getUser || localStorage.getItem('id')
    let user = await ProfileService.getUser(id)
    if(user){
      this.user = {...user}
      console.log(user.photo)
      let favourites = await ProfileService.getFav(id)
      if(favourites){
        this.error = false
        this.favourites = [...favourites]
      }else{
        AuthService.handleLogout()
      }
    }else{
      AuthService.handleLogout()
    }
  }
}
</script>

<style scoped>
.profile{
  width: 70%;
  height: 100%;
}
@media screen and (max-width: 840px) {
  .profile{
    width: 100%;
  }
}
.post-container{
  margin: 2rem 0;
}
.post-container h1{
  margin: 1rem 0;
}
.profile-img{
  width: 15rem;
  height: 15rem;
  border-radius: 50%;
}
</style>