<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4 display-5"> shopping cart 🛒</h1>
    
    <div v-if="cart.length > 0" class="row">
      
     
      <div class="col-md-8">
        <div class="card shadow-sm p-3 mb-4">
          <table class="table align-middle">
            <thead>
              <tr>
                <th scope="col">product</th>
                <th scope="col">price</th>
                <th scope="col">Quantity</th>
                <th scope="col">Subtotal</th>
                <th scope="col">remove</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in cart" :key="item.id">
                <td>
                  <div class="d-flex align-items-center">
                    <img :src="item.image" :alt="item.name" class="rounded me-3" style="width: 50px; height: 50px; object-fit: cover;">
                    <strong>{{ item.name }}</strong>
                  </div>
                </td>
                <td>{{ item.price }} EGP</td>
                
                <td>
                  <span class="badge bg-secondary">{{ item.quantity }}</span>
                </td>
                
                <td>{{ item.price * item.quantity }} EGP</td>
                
                <td>
                  <button @click="removeFromCart(item.id)" class="btn btn-sm btn-outline-danger border-0">
                    <i class="fas fa-trash-alt"></i>remove
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    
      <div class="col-md-4">
        <div class="card p-4 shadow-lg bg-light sticky-top" style="top: 20px;">
          <h4 class="card-title text-primary mb-3">Invoice summary</h4>
          <hr>
          <div class="d-flex justify-content-between mb-3">
            <p class="h5">Total:</p>
            <p class="display-6 text-success fw-bold">{{ totalPrice }} EGP</p>
          </div>
          
          <router-link to="/checkout" class="btn btn-success btn-lg mt-3 shadow-sm">
           Continue to complete your purchase
          </router-link>
          
          <router-link to="/" class="btn btn-outline-secondary mt-2">
             Back to the store
          </router-link>
        </div>
      </div>
    </div>
    
    <div v-else class="alert alert-warning text-center p-5 shadow-sm" role="alert">
      <h4 class="alert-heading">Your shopping cart is completely empty!</h4>
      <p>Add some great products to get the shopping started.</p>
      <hr>
      <router-link to="/" class="btn btn-warning mt-3">staer shopping now</router-link>
    </div>
  </div>
</template>

<script setup>
import useCart from '@/components/composables/useCart';

const { cart, removeFromCart, totalPrice } = useCart();
</script>

<style scoped>
.card-title {
  font-weight: 600;
}
.table {
  text-align: right;
  direction: rtl;
}
.sticky-top {
  align-self: flex-start;
}
</style>
