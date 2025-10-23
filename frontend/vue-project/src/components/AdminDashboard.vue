<template>
  <div class="container my-5">
   
    <h1 class="text-center mb-5 display-5 text-warning">Product Management</h1>
    
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h3 class="text-secondary">Current Product List ({{ products.length }} products)</h3>
      <router-link to="/admin/add" class="btn btn-success shadow-sm">
        <i class="fas fa-plus me-2"></i> Add New Product
      </router-link>
    </div>

    
    <div v-if="!isAuthReady" class="alert alert-info text-center">
      Loading database data...
    </div>

    <div v-else-if="products.length === 0" class="alert alert-warning text-center">
      No products currently added to the store. Please add a new product.
    </div>

   
    <div v-else class="card shadow-lg p-3">
      <div class="table-responsive">
       
        <table class="table table-hover align-middle text-center" dir="ltr"> 
          <thead>
            <tr class="table-primary">
              <th scope="col">#ID</th>
              <th scope="col">Name</th>
              <th scope="col">Price</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
           
            <tr v-for="product in products" :key="product.id">
              <td>{{ product.id }}</td>
              <td class="text-start">{{ product.name }}</td>
              <td>{{ product.price }} EGP</td>
              <td>
                <button @click="editProduct(product.id)" class="btn btn-sm btn-info text-white me-2 shadow-sm">
                  <i class="fas fa-edit"></i> Edit
                </button>
                
              
                <button 
                  @click="confirmDelete(product)" 
                  class="btn btn-sm btn-danger shadow-sm"
                  :disabled="product.isDeleting"
                >
                  <i class="fas fa-trash"></i> {{ product.isDeleting ? 'Deleting...' : 'Delete' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="text-center mt-5">
      <router-link to="/admin" class="btn btn-outline-secondary btn-lg">
        Back to Admin Dashboard
      </router-link>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import useProducts from '@/components/composables/useProducts';

const router = useRouter();

const { products, isAuthReady, deleteProduct } = useProducts(); 



const editProduct = (productId) => {
 
  router.push(`/admin/edit/${productId}`);
};

const confirmDelete = async (productToDelete) => {

  if (window.confirm(`Are you sure you want to delete the product: ${productToDelete.name}? This action cannot be undone.`)) {
    
    productToDelete.isDeleting = true; 
    
    
    const success = await deleteProduct(productToDelete.id);
    
    if (success) {
      alert(`Product "${productToDelete.name}" successfully deleted from the database.`);
    } else {
      alert('An error occurred while deleting the product. Please try again.');
    }
  }
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

.table {
    font-size: 0.95rem;
}
.table-primary {
    background-color: #e0f7fa !important;
    color: #00796b;
}

.text-start {
  text-align: left !important;
}

.text-end {
    text-align: right !important;
}
</style>
