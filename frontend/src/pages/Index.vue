<template>
  <div class="column items-center justify-center window-height">
    <q-img src="../assets/cockapp_logo.svg" style="max-width: 100px" />
    <div style="font-weight: bold; font-size: 36.24px">Cockapp</div>
    <q-btn
      color="secondary text-black text-bold"
      class="btn-get-drunk"
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

.btn-get-drunk {
  height: 55px;
  width: 275px;
  border-radius: 14.35px;
  border: 2.39px solid #000000;
  font-weight: bold;
  font-size: 21.52px;
  margin-top: 160px;
}
</style>
