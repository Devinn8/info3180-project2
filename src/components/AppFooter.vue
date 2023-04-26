<template>
      <footer>
          <div class="container">
              <p>Copyright &copy {{ year }} Flask Inc.</p>
          </div>
      </footer>
</template>

<script setup>
import { ref } from "vue";

const year = (new Date).getFullYear();
</script>

<style>
footer{
  background: #f5efe6;
  padding-top: 4rem!important;
  padding-bottom: 2rem!important;
}
</style>