<template>
    <div class="movie-container">
      <h2>Add a Movie</h2>
      <MovieForm/>
    </div>
</template>

<script setup>
import MovieForm from '../components/MovieForm.vue';
</script>

<style>
    .hide{
        visibility: hidden;
    }
    .show{
        visibility: visible;
    }
</style>