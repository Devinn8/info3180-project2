<script>
import { RouterLink } from "vue-router";
</script>

<template>
    <div class="home-container">
      <div class="row">
        <div class="col hero-image">
          <img src="@/assets/home.jpg" alt="Picture under bridge">
        </div>
        <div class="col info">
          <div class="hero-content">
            <div>
              <span class="material-icons-outlined" style="color: rgb(0, 0, 0);">camera_alt</span>
              <span class="company-name">Photogram</span>
            </div>
            <hr>
            <p>
              Share photos of your favourite moments with friends, family and the world.
            </p>
            <div>
              <RouterLink to="/register" class="register link">Register</RouterLink>
              <RouterLink to="/login" class="login link">Login</RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<style scoped>
.home-container{
  max-width: 100vw;
  margin: 0;
  padding: 0;
  margin-top: -1.2rem;
}
.row{
  max-width: 100%;
  margin: 0;
  height: 100%;
}
img{
  width: 100%;
  height: 100%;
}
.col{
  margin: 0;
  padding: 0;
}
.hero-image{
  height: 100%;
}
.info{
  display: flex;
  align-items: center;
  justify-content: center;
}
.info h1{
  width: 80%;
}
.info p{
  padding-bottom: 24px;
}
.hero-content{
  width: 70%;
}
.link{
  height: 44px;
  padding: 16px 32px;
  border: 1px solid #0eb881;
  border-radius: 6px;
  text-decoration: none;
  margin-right: 12px;
}
.login{
  color: #4a90e2;
}
.register{
  background: #7ed321;
  color: #fff;
}
</style>