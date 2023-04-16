<script setup>
    import { ref, onMounted } from "vue";
    let movies = ref([]);
    let csrf_token = ref("")
    onMounted(() => {
        getCsrfToken();
        fetchMovies();
    });
  function fetchMovies() {
    
    fetch("/api/v1/movies", {
      method: "GET",
      headers: {
        "X-CSRFToken": csrf_token.value,
      },
      })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
          movies.value = data.movies
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  function getCsrfToken() {
    fetch("/api/v1/csrf-token")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      });
  }
</script>


<template>
<div class="movies-container">
  <div class="movie-card" v-for="movie in movies">
    <div class="card mb-3" >
    <div class="row g-0">
      <div class="col-md-4">
        <img :src=movie.poster id="movie-poster" class="img-fluid rounded-start" alt="...">
      </div>
      <div class="col-md-7" >
        <div class="card-body">
          <h5 class="card-title">{{movie.title}}</h5>
          <p class="card-text">{{movie.description}}</p>
        </div>
      </div>
    </div>
  </div>
  </div>
</div>

</template>

<style>
  .movies-container{
    display: grid;
    grid-template-columns: auto auto;
    justify-content: center;
    grid-gap: 10px;
  }
  .card{
    max-width: 500px;
  }
  #movie-poster{
    height: 300px;
    width: 200px;
    object-fit: cover;
    
  }
</style>