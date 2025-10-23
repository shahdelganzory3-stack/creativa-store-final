<template>
  
  <div class="d-flex align-items-center justify-content-center vh-100 bg-light">
    <div class="text-center p-5 shadow-lg bg-white rounded-3">
      
      <h1 class="display-1 fw-bold text-danger">404</h1>
      
      <p class="fs-3"> 
        <span class="text-danger">Oops!</span> Page Not Found.
      </p>
      
      <p class="lead text-muted">
        Sorry, the page you are looking for doesn't exist.
      </p>
      
     
      <router-link to="/" class="btn btn-primary mt-4 btn-lg">Go to Home Page</router-link>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>

.bg-white {
    background-color: white;
}
</style>
