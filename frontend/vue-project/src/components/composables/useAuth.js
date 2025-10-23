import { ref } from 'vue';
import axios from 'axios';

const isAdmin = ref(false);
const user = ref(null);
const isAuthReady = ref(false);

const useAuth = () => {

    const checkUserStatus = async () => {
        isAuthReady.value = false; 

        
        const token = localStorage.getItem('access_token');

        if (!token) {
            isAuthReady.value = true;
            isAdmin.value = false;
            return;
        }

        try {
           
            axios.defaults.headers.common[ 'Authorization' ] = `Bearer ${token}`;

            const response = await axios.get('/api/user/');

            user.value = response.data;
            isAdmin.value = response.data.is_staff || false; 
            console.log("User Status fetched successfully.");

        } catch (error) {
            console.error("Failed to fetch user status. Assuming logged out.", error);

            localStorage.removeItem('access_token');
            isAdmin.value = false;

        } finally {
            
            isAuthReady.value = true;
        }
    };

    checkUserStatus();

    const logout = () => {
    
    };

    return {
        isAdmin,       
        isAuthReady, 
        user,
        logout,
        checkUserStatus
    };
};

export default useAuth;