<template>
  <div class="container my-5">
    <h1 class="text-center display-4 mb-5 fw-bold text-pink">
      Girls' Latest Fashion
    </h1>
<div v-if="isAdmin" class="text-end mb-4">
    <button 
        @click="goToAdminAdd" 
        class="btn btn-lg btn-pink shadow"
    >
        <i class="fas fa-plus-circle me-2"></i> Add New Product
    </button>
</div>
    
    <div v-if="!isAuthReady" class="text-center p-5">
      <div class="spinner-border text-pink" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <p class="mt-3 text-muted">Connecting to the store database...</p>
    </div>

 
    <div v-else-if="products.length > 0" class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
      <div v-for="product in products" :key="product.id" class="col">
        <div class="card h-100 shadow-sm border-0 product-card">
          <img 
            :src="product.image" 
            class="card-img-top product-image" 
            alt="Product Image"
            loading="lazy"
            onerror="this.onerror=null;this.src='https://placehold.co/400x400/F06292/white?text=Image+Missing';"
          />
          <div class="card-body d-flex flex-column">
            <h5 class="card-title fw-bold text-truncate">{{ product.name }}</h5>
            <p class="card-text text-muted flex-grow-1">
            {{ product.description ? (product.description.substring(0, 70) + '...') : 'No description available.' }}
        </p>
            <div class="d-flex justify-content-between align-items-center mt-3">
              <span class="fs-4 fw-bolder text-danger">
    {{ product.price ? parseFloat(product.price).toFixed(2) : '0.00' }} EGP
</span>
             
          <router-link 
    :to="{ 
        name: 'ProductDetail',
        params: { 
          
            category_slug: product.category?.slug, 
            product_slug: product.slug
        } 
    }" 
    v-if="product.slug && product.category?.slug"  class="btn btn-outline-pink" 
>
    <i class="fas fa-eye me-1"></i> View Details
</router-link>

<button v-else class="btn btn-secondary" disabled>Link Missing</button>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div v-else class="text-center p-5 bg-white shadow-lg rounded-3">
      <i class="fas fa-box-open fa-3x text-pink mb-3"></i>
      <h2 class="text-secondary">No Products Available</h2>
      <p class="lead text-muted">
        It looks like the store is empty. Please add products using the admin panel.
      </p>
      <router-link to="/admin/add" class="btn btn-success mt-3">
        <i class="fas fa-plus-circle me-2"></i> Add First Product
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router'; 
import useAuth from '@/components/composables/useAuth'; 
import useProducts from '@/components/composables/useProducts'; 


const router = useRouter();
const { isAdmin } = useAuth();

const { products, isAuthReady, fetchProducts } = useProducts();


const goToAdminAdd = () => {
    router.push({ path: '/admin/add' });
};


watch(products, (newProducts) => {
    console.log('Products updated. Total products:', newProducts.length);
});

onMounted(() => {
    console.log('ProductList component mounted.');
    fetchProducts(); 
});
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

.text-pink {
    color: #F06292;
}

.product-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-radius: 10px;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 1rem 3rem rgba(240, 98, 146, 0.2) !important;
}

.product-image {
    height: 300px; 
    object-fit: cover;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

.btn-outline-pink {
    color: #F06292;
    border-color: #F06292;
    transition: all 0.2s;
}

.btn-outline-pink:hover {
    background-color: #F06292;
    color: white;
}
</style>
