<template>
  <div class="column items-center window-height">
    <div style="max-width: 600px">
      <div class="text-h3 title q-mx-lg q-my-xl">Menu</div>
      <div class="cards row items-center justify-center q-gutter-md">
        <q-card
          clickable
          @click="router.push('/categories/nucocktailuri')"
          class="card column"
        >
          <q-img class="col-9" src="../assets/category_new.svg" :ratio="1" />
          <p class="card-label text-center">NEW</p>
        </q-card>
        <q-card
          clickable
          @click="router.push('/categories/shoturi')"
          class="card column"
        >
          <q-img
            class="col-9"
            src="../assets/category_soft_drinks.svg"
            :ratio="1"
          />
          <p class="card-label text-center">SOFT DRINKS</p>
        </q-card>
        <q-card
          clickable
          @click="router.push('/categories/longdrinks')"
          class="card column"
        >
          <q-img class="col-9" src="../assets/category_shots.svg" :ratio="1" />
          <p class="card-label text-center">SHOTS</p>
        </q-card>
        <q-card
          clickable
          @click="router.push('/categories/cocktailuri')"
          class="card column"
        >
          <q-img
            class="col-9"
            src="../assets/category_cocktails.svg"
            :ratio="1"
          />
          <p class="card-label text-center">COCKTAILS</p>
        </q-card>
        <q-card
          clickable
          @click="router.push('/categories/cocktailuri')"
          class="card column"
        >
          <q-img
            class="col-9"
            src="../assets/category_beer_and_wine.svg"
            :ratio="1"
          />
          <p class="card-label text-center">BEER&WINE</p>
        </q-card>
        <q-card
          clickable
          @click="router.push('/categories/cocktailuri')"
          class="card column"
        >
          <q-img
            class="col-9"
            src="../assets/category_coffee_and_tea.svg"
            fit="none"
            :ratio="1"

          />
          <p class="card-label text-center">COFFEE&TEA</p>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "PageCategories",
  setup() {
    let router = useRouter();

    return {
      router,
    };
  },
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap");
.categories {
  font-family: "Raleway", sans-serif;
}

.title {
  font-weight: bold;
  font-size: 36px;
}

.card-label {
  font-weight: bold;
  font-size: 16px;
}

.card {
  width: 100%;
  max-width: 149px;
  border-radius: 36px;
  height: 169px;
  background: #ffffff;
  border: 3px solid #000000;
  box-shadow: 7px -4px 0px #9977de;
}
</style>


