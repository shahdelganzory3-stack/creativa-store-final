<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h1 class="text-center mb-4 display-5 text-info">Edit Product</h1>
        <p class="text-center text-muted mb-5">
          Editing Product ID: <strong>{{ productId }}</strong>
        </p>

      
        <div v-if="isLoading" class="alert alert-info text-center">
          Loading product details...
        </div>
        <div v-else-if="!product" class="alert alert-danger text-center">
          Product not found or database error occurred.
        </div>

      
        <div v-else class="card shadow-lg p-5">
          <form @submit.prevent="updateProductHandler">
            
           
            <div class="mb-4">
              <label for="name" class="form-label fw-bold">Product Name</label>
              <input 
                type="text" 
                class="form-control" 
                id="name" 
                v-model="product.name" 
                required
              >
            </div>

           
            <div class="mb-4">
              <label for="price" class="form-label fw-bold">Price (EGP)</label>
              <input 
                type="number" 
                class="form-control" 
                id="price" 
                v-model.number="product.price" 
                required
                min="0.01"
                step="0.01"
              >
            </div>

           
            <div class="mb-4">
              <label for="description" class="form-label fw-bold">Description</label>
              <textarea 
                class="form-control" 
                id="description" 
                v-model="product.description" 
                rows="3" 
                required
              ></textarea>
            </div>

          
            <div class="mb-4">
              <label for="image" class="form-label fw-bold">Image URL</label>
              <input 
                type="url" 
                class="form-control" 
                id="image" 
                v-model="product.image" 
                required
              >
            </div>
            
            <div class="d-grid gap-2">
              <button 
                type="submit" 
                :disabled="isSaving" 
                class="btn btn-info btn-lg text-white mt-3 shadow-sm"
              >
                <span v-if="isSaving">Saving Changes...</span>
                <span v-else><i class="fas fa-save me-2"></i> Save Changes</span>
              </button>
            </div>
          </form>
        </div>
        
        <div class="text-center mt-4">
          <router-link to="/admin/products" class="btn btn-outline-secondary">
            Back to Product Management
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import useProducts from '@/components/composables/useProducts';

const route = useRoute();
const router = useRouter();
const { getProductById, updateProduct } = useProducts();

const productId = route.params.id;
const product = ref(null);
const isLoading = ref(true);
const isSaving = ref(false);

onMounted(async () => {
    if (!productId) {
        console.error("Product ID is missing.");
        isLoading.value = false;
        return;
    }

   
    const fetchedProduct = await getProductById(productId);
    
    if (fetchedProduct) {
       
        product.value = fetchedProduct;
    } else {
    
        alert(`Error: Product with ID ${productId} was not found.`);
        router.push('/admin/products');
    }
    isLoading.value = false;
});


const updateProductHandler = async () => {
    if (!product.value) return;

    isSaving.value = true;
    
    
    const success = await updateProduct(productId, {
        name: product.value.name,
        price: product.value.price,
        description: product.value.description,
        image: product.value.image,
    });

    isSaving.value = false;

    if (success) {
        alert(`Product "${product.value.name}" updated successfully!`);
     
        router.push('/admin/products');
    } else {
        alert('An error occurred while saving changes. Please try again.');
    }
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

.form-label {
    color: #495057;
}
.card {
    border-radius: 15px;
}
</style>
