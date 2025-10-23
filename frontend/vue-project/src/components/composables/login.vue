<template>
    <form @submit.prevent="handleLogin">
        
        <div>
            <label for="username">user name </label>
            <input 
                type="text" 
                id="username" 
                v-model="username" 
                required 
                placeholder="enter user name "
            />
        </div>

        <div>
            <label for="password" translate="no"> password:</label>
            <input 
                type="password" 
                id="password" 
                v-model="password" 
                required 
                placeholder="enter passwoerd "
            />
        </div>

        <div v-if="authError" style="color: red;">
            {{ authError }}
        </div>

        <button type="submit">sign in </button>
    </form>
</template>
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'; 
import useAuth from './useAuth.js'; 

const { isAuthenticated, authError, login, isAdmin } = useAuth(); 
const router = useRouter(); 

const username = ref('');
const password = ref('');
const isLoading = ref(false);


const handleLogin = async () => {
    isLoading.value = true;
    
    
    const success = await login(username.value, password.value);
    
    isLoading.value = false; 
    
    if (success) {
       
        if (isAdmin.value) {
            router.push({ path: '/admin/add' });
        } else {
            router.push({ path: '/' }); 
        }
    } 
   
};
</script>
<style scoped>

.error-message {
  color: red;
  margin-bottom: 15px;
}
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}
</style>