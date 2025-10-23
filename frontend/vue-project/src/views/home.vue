<template>
  <div id="app-layout">
    
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm fixed-top">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand text-pink fw-bold fs-4">Girls Fashion</router-link>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Products</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/admin/add" class="nav-link text-success">Add Product (Admin)</router-link>
            </li>
          </ul>
          
          <div class="d-flex">
            
            <router-link to="/checkout" class="btn btn-outline-pink position-relative">
              <i class="fas fa-shopping-cart me-1"></i> 
              Cart 
              <span v-if="cartCount > 0" class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                {{ cartCount }}
                <span class="visually-hidden">items in cart</span>
              </span>
            </router-link>
          </div>
        </div>
      </div>
    </nav> 

   
    <main class="main-content">
      <router-view></router-view>
    </main>

  
    <footer class="bg-light text-center text-lg-start mt-5 shadow-sm">
      <div class="container p-4">
        <div class="text-center">
          © 2024 Girls Fashion Store | Powered by Vue & Firebase
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import useCart from '@/components/composables/useCart';


const { cart } = useCart();
const cartCount = computed(() => {
    
    return cart.value.reduce((total, item) => total + item.quantity, 0);
});


const customStyle = document.createElement('style');
customStyle.textContent = `
.text-pink { color: #F06292 !important; }
.btn-outline-pink { color: #F06292; border-color: #F06292; }
.btn-outline-pink:hover { background-color: #F06292; color: white; }
`;
document.head.appendChild(customStyle);

</script>

<style scoped>

#app-layout {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
   
    padding-top: 65px; 
}
.main-content {
    flex-grow: 1; 
}
</style>
