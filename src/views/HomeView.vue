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
            <div class="heading">
              <span class="material-icons-outlined" style="color: rgb(0, 0, 0);">camera_alt</span>
              <span class="company-name">Photogram</span>
            </div>
            <hr>
            <p>
              Share photos of your favourite moments with friends, family and the world.
            </p>
            <div class="buttons">
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
  background: #f5efe6;
}
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
  border-radius: 5px;
}
.col{
  margin: 5rem 4.5rem;
  padding: 0;
  border-radius: 5px;
  max-height: 40%;
  max-width: 40%;
  border: 1.5px #989898 solid;
}
.hero-image{
  height: 100%;
  margin-left: 9.5rem;
  margin-right: 1.5rem;
}
.info{
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  margin-left: 1.5rem;
  margin-right: 5.5rem;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.info .heading{
  text-align: center;
}
.company-name{
  font-family: 'Oleo Script Swash Caps', cursive;
  font-size: 45px;
  padding: 1rem;
}
.info h1{
  width: 80%;
}
.info p{
  padding-top: 12px;
  padding-bottom: 36px;
  font-size: 20px;
  font-weight: 600;
  font-family: Arial, Helvetica, sans-serif;
}
.hero-content{
  padding: 0;
  margin: 0;
  width: 85%;
  height: 85%;
}

.buttons{
  width: 100%
}
.link{
  height: 44px;
  width: 40%;
  padding: 16px 64px;
  border: 1px solid #0eb881;
  border-radius: 6px;
  text-decoration: none;
  margin-right: 12px;
  font-weight: 600;
}
.login{
  background: #4a90e2;
  color: #fff;
  padding: 16px 20.5%;
}
.register{
  background: #7ed321;
  color: #fff;
  padding: 16px 19%;
}
</style>