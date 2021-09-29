<template>
  <div class="index-page row items-center justify-evenly">
      <q-btn
        color="white text-black text-bold"
        flat
        rounded
        class=""
        label="Get drunk"
        to="/categories"
      />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "PageIndex",
  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap");

.index-page {
  font-family: "Raleway", sans-serif;
  background: #f3bfdf;
  height: 100vh;
  
  background-image: url("../assets/indexpage.png");
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
  background-size: 350px;
}

.q-btn {
  background: #ffffff;
  box-shadow: 4px 4px 0px #0926d3;
  top: 255px;
  left: 80px;
}
</style>
