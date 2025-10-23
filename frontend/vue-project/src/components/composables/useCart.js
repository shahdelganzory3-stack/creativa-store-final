import { ref, computed } from 'vue';


const cart = ref([]);


export default function useCart() {

    const addToCart = (product, quantity = 1) => {
        const existingItem = cart.value.find(item => item.id === product.id);

        if (existingItem) {
            
            existingItem.quantity += quantity;
            console.log(`Updated quantity for ${product.name}. New count: ${existingItem.quantity}`);
        } else {
         
            cart.value.push({ ...product, quantity });
            console.log(`Added new product to cart: ${product.name}`);
        }
    };

    const removeFromCart = (productId) => {
        cart.value = cart.value.filter(item => item.id !== productId);
    };

    const updateQuantity = (productId, newQuantity) => {
        const item = cart.value.find(item => item.id === productId);
        if (item && newQuantity > 0) {
            item.quantity = newQuantity;
        } else if (item && newQuantity <= 0) {
            removeFromCart(productId);
        }
    };

    const clearCart = () => {
        cart.value = [];
    };

    const totalPrice = computed(() => {
        return cart.value.reduce((total, item) => total + (item.price * item.quantity), 0);
    });
    return {
        cart,
        addToCart,
        removeFromCart,
        updateQuantity,
        clearCart,
       
        totalItems: computed(() => cart.value.reduce((total, item) => total + item.quantity, 0)),
    };
}
