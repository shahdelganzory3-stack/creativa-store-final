<template>
  <div class="container my-5">
    <h1 class="text-center mb-5 display-5 text-warning">إدارة المنتجات (Products Management)</h1>
    
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h3 class="text-secondary">List of current products({{ products.length }} )product</h3>
      <router-link to="/admin/add" class="btn btn-success shadow-sm">
        <i class="fas fa-plus me-2"></i> add new product 
      </router-link>
    </div>

   
    <div class="card shadow-lg p-3">
      <div class="table-responsive">
        <table class="table table-hover align-middle text-center" dir="rtl">
          <thead>
            <tr class="table-primary">
              <th scope="col">#ID</th>
              <th scope="col">name</th>
              <th scope="col">price</th>
              <th scope="col">procedures</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in products" :key="product.id">
              <td>{{ product.id }}</td>
              <td class="text-end">{{ product.name }}</td>
              <td>{{ product.price }} EGP</td>
              <td>
               
                <button @click="editProduct(product.id)" class="btn btn-sm btn-info text-white me-2 shadow-sm">
                  <i class="fas fa-edit"></i> edit 
                </button>
                
                
                <button @click="confirmDelete(product)" class="btn btn-sm btn-danger shadow-sm">
                  <i class="fas fa-trash"></i> delet
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

 
    <div class="text-center mt-5">
      <router-link to="/admin" class="btn btn-outline-secondary btn-lg">
        Return to the control panel
      </router-link>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();


const products = ref([
  { 
    id: 101, 
    name: 'Printed Summer Dress - Pink', 
    price: 350, 
    description: 'A light, comfortable dress for summer outings.', 
    image: 'https://placehold.co/100x100/A0E7E5/fff?text=Dress',
    category: 'Dresses',
    sizes: ['S', 'M', 'L']
  },
  { 
    id: 102, 
    name: 'Wide leg top and pants set', 
    price: 580, 
    description:'A modern set suitable for university and work.', 
    image: 'https://placehold.co/100x100/F08080/fff?text=Set',
    category: 'Kits',
    sizes: ['M', 'L', 'XL']
  },
  { 
    id: 103, 
    name:'Basic Cotton Blouse - White', 
    price: 150, 
    description: 'A basic blouse that is a must-have in any wardrobe.', 
    image: 'https://placehold.co/100x100/C0C0C0/fff?text=Blouse',
    category: 'Repent',
    sizes: ['XS', 'S', 'M']
  },
]);



const editProduct = (productId) => {
 
  router.push(`/admin/edit/${productId}`);
};

const confirmDelete = (product) => {
  
  if (window.confirm(`Are you sure you want to delete the product?: ${product.name}؟`)) {
    deleteProduct(product.id);
  }
};

const deleteProduct = (productId) => {
  
  const initialLength = products.value.length;
  products.value = products.value.filter(p => p.id !== productId);
  
  if (products.value.length < initialLength) {
    console.log(`Product with ID ${productId} deleted.`);
 
    alert(`The product has been successfully deleted.`);
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
</style>
