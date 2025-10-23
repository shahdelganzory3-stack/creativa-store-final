<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-lg-8 col-md-10">
        <div class="card shadow-lg border-0 rounded-4 p-4 bg-white">
          <h2 class="card-title text-center fw-bold mb-4 text-pink">
            <i class="fas fa-plus-circle me-2"></i> Add New Product (Admin Panel)
          </h2>
          
         
          <div v-if="isAdding" class="text-center p-5">
            <div class="spinner-border text-pink" role="status">
              <span class="visually-hidden">Adding Product...</span>
            </div>
            <p class="mt-3 text-muted">Adding item to the database...</p>
          </div>

          <div v-else>
           
            <div v-if="error" class="alert alert-danger" role="alert">
              <i class="fas fa-exclamation-triangle me-2"></i> 
              Error: {{ error }}
              <p class="small mt-1 mb-0">If this is a Permission Denied error, check Firebase security rules.</p>
            </div>
            
    
            <div v-if="successMessage" class="alert alert-success" role="alert">
              <i class="fas fa-check-circle me-2"></i> 
              {{ successMessage }}
            </div>

          
            <form @submit.prevent="submitProduct">
         
              <div class="mb-3">
                <label for="productName" class="form-label fw-semibold">Product Name</label>
                <input type="text" id="productName" class="form-control" v-model="product.name" required>
              </div>

           
              <div class="mb-3">
                <label for="productPrice" class="form-label fw-semibold">Price (EGP)</label>
                <input type="number" id="productPrice" class="form-control" v-model.number="product.price" required min="1" step="0.01">
              </div>

            
              <div class="mb-3">
                <label for="productDescription" class="form-label fw-semibold">Description</label>
                <textarea id="productDescription" class="form-control" v-model="product.description" rows="3" required></textarea>
              </div>

              
              <div class="mb-3">
                <label for="imageUrl" class="form-label fw-semibold">Image URL</label>
                <input type="url" id="imageUrl" class="form-control" v-model="product.image" placeholder="Paste a direct image link here" required>
                <div class="form-text">Use a direct image link from Pexels or Unsplash.</div>
              </div>

            
              <div class="d-grid gap-2 mt-4">
                <button type="submit" class="btn btn-pink btn-lg shadow-sm">
                  <i class="fas fa-save me-2"></i> Add Product
                </button>
                <button type="button" @click="fillDemoData" class="btn btn-outline-secondary btn-sm">
                  <i class="fas fa-magic me-2"></i> Fill Demo Data
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import useProducts from '@/components/composables/useProducts';

const router = useRouter();

const { addProduct } = useProducts(); 

const product = ref({
  name: '',
  price: null,
  description: '',
  image: '',
});
const isAdding = ref(false);
const error = ref(null);
const successMessage = ref('');


const fillDemoData = () => {
    product.value.name = 'Chic Summer Dress';
    product.value.price = 799.99;
    product.value.description = 'A light, breathable cotton dress perfect for summer outings and beach days. Available in multiple sizes.';
   
    product.value.image = 'https://placehold.co/400x400/F06292/white?text=Fashion+Item'; 
};


const submitProduct = async () => {
  isAdding.value = true;
  error.value = null;
  successMessage.value = '';

 
  if (typeof product.value.price !== 'number' || product.value.price <= 0) {
    error.value = 'Please enter a valid price.';
    isAdding.value = false;
    return;
  }
  
  try {
  
    await addProduct(product.value); 

    successMessage.value = 'Product added successfully! Redirecting...';
    
    
    setTimeout(() => {
      router.push('/');
    }, 1500);

  } catch (err) {
    console.error('Submission error:', err);
    
    error.value = err.message || 'An unexpected error occurred while adding the product.';
  } finally {
    isAdding.value = false;
  }
};
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
</style>
