<template>
  <v-app>
    <v-main>
      <p>
        <router-link to="/">Go to Home</router-link>
        <router-link to="/upload">Go to Upload</router-link>
      </p>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
  //
</script>
