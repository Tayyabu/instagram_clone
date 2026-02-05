<script lang="ts" setup>
import Post from '../components/Post.vue';




</script>

<template>
  

  <div class="w-1/2 flex">
    <div class="grow">
      <Post authorName="someauthor" imageUrl="/dummy.jpg" :likes="50" :comments="50"/>

    </div>
    <h1 class="p-3">Suggested</h1>
  </div>

</template>
