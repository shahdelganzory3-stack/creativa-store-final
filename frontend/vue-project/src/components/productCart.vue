<template>
        <div class="product-card">
        <img :src="product.image" :alt="product.name" class="product-image"/>
        <h3>{{product.name}}</h3>
        <p class="product-price">{{product.price}}</p>
        </div>
 </template>
 <script setup>
import {defineProps} from 'vue';
const props = defineProps({
    product:{
        type: Object,
        required:true,
    }
});
</script>
<style scoped>
.product-card{
    border:lid #ccc;
    border-radius:8px;
    padding:15px;
    width:200px;
    text-align:center;
    box-shadow:0 4px 6px rgba(0,0,0,0.1);
      transition:transform0.3s;
}
.product-card:hover{
    transform:translateY(-5px);
}
 .product-image{
  width:100%;
  height:200px;
  object-fit:cover;
  border-radius:4px;
}
h3{
  margin-top:10px;
  margin-bottom:5px;
}
.product-price{
    color:#888;
    font-weight:bold;
}
</style>








