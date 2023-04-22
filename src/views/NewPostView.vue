<template>
  <div class="new-post-container">
      <div class="new-post-content">
          <h1>New Post</h1>
          <NewPostForm />  
      </div>
  </div> 
</template>

<script>
import NewPostForm from '../components/NewPostForm.vue'
export default {
  components: { NewPostForm }
}
</script>

<style scoped>
.new-post-container{
  min-height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.new-post-content{
  width: 40%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
</style>