<template>
  <div class="categories">
    <div class="text-h3 text-bold q-mx-lg q-my-xl">Meniu</div>
    <div class="cards row items-center justify-center q-gutter-md">
      <q-card class="card column">
        <q-img class="col-9" src="../assets/nu-cocktails.png" fit="none" />
        <p class="col text-body2 text-bold text-center">NU COCKTAILURI</p>
      </q-card>
      <q-card class="card column">
        <q-img class="col-9" src="../assets/shots.png" fit="none" />
        <p class="col text-body2 text-bold text-center">SHOTURI</p>
      </q-card>
      <q-card class="card column">
        <q-img class="col-9" src="../assets/long-drinks.png" fit="none" />
        <p class="col text-body2 text-bold text-center">LONG DRINKS</p>
      </q-card>
      <q-card class="card column">
        <q-img class="col-9" src="../assets/cocktails.png" fit="none" />
        <p class="col text-body2 text-bold text-center">COCKTAILURI</p>
      </q-card>
    </div>
    <div class="row items-center justify-center q-ma-lg">
      <q-btn flat class="btn-nimic" color="black" label="Nimic" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "PageCategories",
  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap");
.categories {
  font-family: "Raleway", sans-serif;
}
.card {
  width: 100%;
  max-width: 165px;
  height: 188px;
  border-radius: 36px;
  border: 5px solid #000000;
  box-shadow: 7px -4px 0px 0px #eab833;
}

.btn-nimic {
  height: 61px;
  width: 367px;
  border-radius: 20px;
  border: 5px solid #000000;
  font-weight: bold;
}
</style>


