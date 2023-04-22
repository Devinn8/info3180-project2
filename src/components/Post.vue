<template>
  <div class="post">
    <div class="post-header mr-auto">
      <img :src="profile-photo" alt="Image of profile photo" class="img-fluid">
      <p><b><a href="#" @click.prevent="viewProfile(id)">{{username}}</a></b></p>
    </div>
    <div class="post-body">
      <img :src="photo" alt="Image of post" class="img-fluid">
      <p>{{ caption }}</p>
    </div>
    <div class="post-footer">
      <div class="post-likes mr-auto">
        <span class="material-icons" style="color: rgb(0, 0, 0);">favorite_border</span>
        <span class="material-icons" style="color: rgb(255, 0, 0);">favorite</span>
        <p>{{`${likes} Likes`}}</p>
      </div>
      <div class="post-date ms-auto">
        <p>{{ formatDate(date) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['profile-photo', 'username', 'photo', 'caption', 'likes', 'date'],
  methods: {
      viewProfile(id){
          this.$router.push(`/users/${id}`)
      },
      formatDate(date){
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      const dateObj = new Date(date);
      const day = dateObj.getDate().toString().padStart(2, '0');
      const month = months[dateObj.getMonth()];
      const year = dateObj.getFullYear().toString();
      return `${day} ${month} ${year}`;
    }
  }
}
</script>

<style scoped>
.post{
  width: 300px;
  height: 400px;
}
.post-info{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
</style>