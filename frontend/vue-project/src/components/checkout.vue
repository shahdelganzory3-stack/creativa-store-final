<template>
    <div class="container my-5">
        <h1 class="text-center mb-5 display-5 text-primary">Complete purchase</h1>
        
        <div v-if="cart.length === 0" class="alert alert-warning text-center p-5">
            <h4 class="alert-heading">Shopping cart is empty!</h4>
            <p>Products must be added before completing the purchase.</p>
            <router-link to="/" class="btn btn-primary mt-3">Back to shopping</router-link>
        </div>

        <div v-else class="row justify-content-center">
            
            <div class="col-md-7">
                <div class="card shadow p-4 mb-4">
                    <h4 class="card-title text-success mb-4">Customer data</h4>
                    <form @submit.prevent="submitOrder">
                        
                        <div class="mb-3">
                            <label for="customerName" class="form-label">Customer Name</label>
                            <input 
                                type="text" 
                                class="form-control" 
                                id="customerName" 
                                v-model="customerInfo.name" 
                                required
                            >
                        </div>
                        
                        <div class="mb-3">
                            <label for="phoneNumber" class="form-label">Phone Number</label>
                            <input 
                                type="tel" 
                                class="form-control" 
                                id="phoneNumber" 
                                v-model="customerInfo.phone" 
                                required
                            >
                        </div>
                        
                        <div class="mb-3">
                            <label for="customerAddress" class="form-label">Full Address</label>
                            <input 
                                type="text" 
                                class="form-control" 
                                id="customerAddress" 
                                v-model="customerInfo.address" 
                                required
                            >
                        </div>
                        
                        <button type="submit" :disabled="isSubmitting" class="btn btn-success btn-lg mt-4 w-100">
                            <span v-if="isSubmitting">Sending request...</span>
                            <span v-else>Confirm order now</span>
                        </button>
                    </form>
                </div>
            </div>

            <div class="col-md-5">
                <div class="card p-4 shadow-lg bg-light">
                    <h4 class="card-title text-primary mb-3">Summary of your request</h4>
                    <ul class="list-group list-group-flush mb-3">
                        <li v-for="item in cart" :key="item.id" class="list-group-item d-flex justify-content-between">
                            <div>
                                {{ item.name }} (x{{ item.quantity }})
                                <span v-if="item.selectedSize || item.selectedColor" class="text-muted small d-block">
                                    Size: {{ item.selectedSize || 'N/A' }} | Color: {{ item.selectedColor || 'N/A' }}
                                </span>
                            </div>
                            <strong>{{ item.price * item.quantity }} EGP</strong>
                        </li>
                    </ul>
                    <hr>
                <div class="d-flex justify-content-between align-items-center">
                     <p class="h4 mb-0">Total:</p>
                     <p class="display-6 text-danger fw-bold mb-0">{{ totalPrice }} EGP</p>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import useCart from '@/components/composables/useCart';
import axios from 'axios';

const { cart, totalPrice, clearCart } = useCart();
const router = useRouter();

const customerInfo = ref({
    name: '',
    phone: '',
    address: '' 
});

const isSubmitting = ref(false);

const submitOrder = async () => { 
    if (cart.value.length === 0) {
        alert("Cannot submit an empty order.");
        return;
    }
    
    isSubmitting.value = true;
    
    const orderData = {
        name: customerInfo.value.name,
        phone: customerInfo.value.phone,
        address: customerInfo.value.address,
        
        items: cart.value.map(item => ({
            product: item.id,
            price: item.price,
            quantity: item.quantity,
            size: item.selectedSize || '', 
            color: item.selectedColor || '' 
        }))
    };

    try {
        const response = await axios.post('/api/orders/', orderData);
        
        console.log("Order submitted successfully:", response.data);

        clearCart(); 
        
        alert('Your request has been sent successfully! Order ID: ' + response.data.id);
        
        router.push('/'); 
        
    } catch (error) {
        console.error('Order submission failed:', error.response ? error.response.data : error.message);
        alert('Failed to submit order. Please try again.');
    } finally {
        isSubmitting.value = false;
    }
};
</script>

<style scoped>

.card-title {
  border-bottom: 2px solid #ccc;
  padding-bottom: 10px;
}
.list-group-item {
  border: none;
  border-bottom: 1px dashed #eee;
}
.list-group-flush .list-group-item:last-child {
  border-bottom: none;
}
</style>