

import { ref, onMounted } from 'vue';
import axios from 'axios';

const products = ref([]);
const isAuthReady = ref(true);



export default function useProducts() {

    const fetchProducts = async () => {

       
        products.value = [];

        
        try {
            
            const response = await axios.get('/api/products/');
            products.value = response.data;
            console.log("Successfully fetched products from Django API:", products.value.length);
        } catch (error) {
            console.error("Error fetching products from Django API:", error);
        }
    };

   
    const getProductBySlug = async (productSlug) => {
        try {
           
            const response = await axios.get(`/api/products/${productSlug}/`);
            return response.data;
        } catch (error) {
            console.error(`Error fetching product with Slug ${productSlug}:`, error);
            return null;
        }
    };
  
    onMounted(() => {
        fetchProducts();
    });

  
    return {
        products,
        isAuthReady,
        fetchProducts,
       
        getProductBySlug,
    };
}