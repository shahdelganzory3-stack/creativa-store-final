<template>
  <div class="container my-5">
    
    <div v-if="isLoading" class="text-center py-5">
      <div class="spinner-border text-pink" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <p class="mt-3 text-pink">Fetching product details...</p>
    </div>
 

    <div v-else-if="!product" class="alert alert-danger text-center shadow-lg" role="alert">
      <h4 class="alert-heading">Product Not Found!</h4>
      <p>The requested product could not be located in our store.</p>
      <hr>
      <router-link to="/" class="btn btn-outline-danger">Go Back to Store</router-link>
    </div>

    
    <div v-else class="row product-details-card shadow-lg p-4 rounded-4">
      
     
      <div class="col-md-6 mb-4 mb-md-0">
        <img 
          :src="getSafeImageUrl(product.image)" 
          class="img-fluid rounded-3 product-detail-image shadow-sm" 
          :alt="product.name"
          onerror="this.onerror=null;this.src='https://placehold.co/600x750/F06292/ffffff?text=Fashion+Detail';"
        >
      </div>

   
      <div class="col-md-6 d-flex flex-column justify-content-between">
        <div>
          <h1 class="display-5 fw-bold text-pink">{{ product.name }}</h1>
          <p class="text-muted fs-6 mb-4">Product ID: {{ product.id }}</p>

          <h3 class="text-success fw-bolder mb-3">{{ parseFloat(product.price).toFixed(2) }} EGP</h3>
          <hr>

          <h4 class="text-secondary fw-semibold">Description</h4>
          <p class="lead">{{ product.description }}</p>

        
         <div class="mb-4 d-flex gap-4">
    <div style="flex-grow: 1;">
        <label for="sizeSelect" class="form-label fw-bold">Size:</label>
        <select id="sizeSelect" v-model="selectedSize" class="form-select">
            <option disabled value="">Select Size</option> 
            <option 
                v-for="size in product.available_sizes.split(',')" 
                :key="size.trim()"
                :value="size.trim()"
            >
                {{ size.trim() }}
            </option>
        </select>
    </div>

    <div style="flex-grow: 1;">
        <label for="colorSelect" class="form-label fw-bold">Color:</label>
        <select id="colorSelect" v-model="selectedColor" class="form-select">
            <option disabled value="">Select Color</option>
            <option 
                v-for="color in product.available_colors.split(',')" 
                :key="color.trim()"
                :value="color.trim()"
            >
                {{ color.trim() }}
            </option>
        </select>
    </div>
</div> 
        </div>

        <div class="mt-4 pt-3 border-top">
          <div class="d-flex align-items-center mb-3">
            <label for="quantity" class="form-label me-3 mb-0 fw-bold">Quantity:</label>
            <input 
              type="number" 
              id="quantity" 
              v-model.number="quantity" 
              min="1" 
              max="10" 
              class="form-control w-25 text-center"
            >
          </div>

          <button 
            @click="addToCartHandler(product)" 
            class="btn btn-pink btn-lg w-100 shadow-lg"
          >
            <i class="fas fa-shopping-cart me-2"></i> Add {{ quantity }} to Cart
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import useCart from '@/components/composables/useCart';

const route = useRoute();
const { addToCart } = useCart(); 

const product = ref(null);
const isLoading = ref(true);
const quantity = ref(1); 
const selectedSize = ref('');
const selectedColor = ref('');

const getProduct = async () => {
   
    const productSlug = route.params.product_slug;
    
    isLoading.value = true;
    product.value = null;
    
    try {
       
        const response = await axios.get(`/api/products/${productSlug}/`);
        
        product.value = response.data;
        
     
        document.title = product.value.name + ' | Your Store';

    } catch (error) {
        console.error('Failed to fetch product:', error);
        product.value = null;
    }
    
    isLoading.value = false;
};


const addToCartHandler = (item) => {
   
    const itemWithDetails = {
        ...item, 
        selectedSize: selectedSize.value, 
        selectedColor: selectedColor.value 
    };
    addToCart(itemWithDetails, quantity.value);
    alert(`${quantity.value}x "${item.name}" (${selectedSize.value}, ${selectedColor.value}) added to your cart!`);
    quantity.value = 1;
  };


const getSafeImageUrl = (url) => {
    const placeholder = 'https://placehold.co/600x750/F06292/ffffff?text=Fashion+Detail';
    return url && url.startsWith('http') ? url : placeholder;
};


onMounted(() => {
    getProduct();
});
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');


.text-pink {
    color: #F06292;
}
.btn-pink {
    background-color: #F06292;
    border-color: #F06292;
    color: white;
}
.btn-pink:hover {
    background-color: #d64d84;
    border-color: #d64d84;
}

.product-details-card {
    background-color: #ffffff;
}

.product-detail-image {
    max-height: 750px;
    object-fit: cover;
    background-color: #fce4ec; 
}
</style>
