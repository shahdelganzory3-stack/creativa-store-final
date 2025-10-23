import { createRouter, createWebHistory } from 'vue-router';
import useAuth from '@/components/composables/useAuth';


const requireAdmin = (to, from, next) => {
    const { isAuthenticated, isAdmin } = useAuth();

    if (!isAuthenticated.value) {
        console.log("Not authenticated, redirecting to login.");
        next('/login');
    }
    else if (!isAdmin.value) {
        console.log("Authenticated but not Admin, redirecting to home.");
        next('/');
    }
    else {
        console.log("Admin access granted.");
        next();
    }
};

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/home.vue'),
        children: [
            {
                path: '',
                name: 'ProductList',
                component: () => import('@/views/productList.vue'),
            },
            {
                    path: ':category_slug/:product_slug', 
                    name: 'ProductDetail',
                    component: () => import('@/views/productDetails.vue'),
                    props: true,
            },
            {
                path: 'checkout',
                name: 'Checkout',
                component: () => import('@/components/Checkout.vue'),
            },
            {
                path: '/login',
                name: 'Login',
                component: () => import('@/components/composables/login.vue'), 
            },

        ],
    },
    {
        path: '/admin',
        name: 'Admin',
        component: () => import('@/views/home.vue'),
        children: [
            {
                path: 'add',
                name: 'AddProduct',
                component: () => import('@/components/AddProduct.vue'),
                beforeEnter: requireAdmin,
            },
        ],
    },
];


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;
