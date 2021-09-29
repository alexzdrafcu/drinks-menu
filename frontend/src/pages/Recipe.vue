<template>
  <div class="recipe-page" :style="{backgroundImage:'url(' + drink?.image + ')'}">
    <!-- <div class="image"></div>
    <q-img
      src="https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg"
    /> -->
    <div class="header" />
    <div class="recipe column items-center justify-center">
      <div class="title q-pt-lg q-mb-lg">
        <div class="uppercase text-h5 text-bold text-center">{{drink?.name}}</div>
        <div class="text-caption text-center">{{drink?.description}}</div>
      </div>

      <div
        class="ingrediente column items-center justify-center q-pt-md q-mb-lg"
      >
        <div class="text-h6 text-bold text-center q-my-sm">INGREDIENTE</div>
        <div
          class="ingredient row items-center q-px-md q-my-xs text-weight-medium"
          v-for="ingredient in ingredients"
          :key="ingredient.id"
        >
          {{ ingredient.qty }} {{ ingredient.name }}
        </div>
      </div>
      <div class="steps column items-center justify-center q-pt-md q-pb-xl">
        <div class="text-h6 text-bold text-center q-my-sm">PREPARARE</div>
        <div
          class="step q-px-md q-py-xs q-my-xs"
          v-for="step in steps"
          :key="step.id"
        >
          <div class="text-caption text-bold text-grey-6">
            {{ step.name }}/{{ steps.length }}
          </div>
          <div class="text-weight-medium">
            {{ step.description }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { Drink, Ingredient, Step } from "../components/models";
import { useRoute } from "vue-router";

export default defineComponent({
  name: "PageCategories",
  setup() {
    const route = useRoute();
    let drinkId = ref("");
    let drink = ref<Drink>();
    let ingredients = ref<Ingredient[]>([]);
    let steps = ref<Step[]>([]);

    const loadDrink = async () => {
      const response = await fetch(
        "https://drinks-menu-backend.herokuapp.com/api/drinks/drinks/" +
          drinkId.value
      );
      const data: Drink = await response.json();
      drink.value = data;
    };


    const loadIngredients = async () => {
      const response = await fetch(
        "https://drinks-menu-backend.herokuapp.com/api/drinks/get_ingredients_by_drink/" +
          drinkId.value
      );
      const data: Ingredient[] = await response.json();
      ingredients.value = data;
    };

    const loadSteps = async () => {
      const response = await fetch(
        "https://drinks-menu-backend.herokuapp.com/api/drinks/get_steps_by_drink/" +
          drinkId.value
      );
      const data: Step[] = await response.json();
      steps.value = data;
    };

    onMounted(async () => {
      drinkId.value = route.params.id.toString();
      await loadDrink();
      await loadIngredients();
      await loadSteps();
    });
    return {
      drink,
      ingredients,
      steps,
    };
  },
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap");
.recipe-page {
  font-family: "Raleway", sans-serif;
  height: 500px;
  background-image: url("https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg");
  background-color: #ffffff; /* Used if the image is unavailable */
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
  background-size: cover;
}

.header {
  height: 400px; /* You must set a specified height */
}
.recipe {
  border-radius: 60px 60px 0px 0px;
  //margin-top: 400px;
  background: #fffafd;
}

.title {
  border-radius: 60px 60px 0px 0px;
  border: 3px solid #000000;
  width: 100%;
  background: #f3bfdf;
  padding-bottom: 70px;
  box-shadow: inset -6px 6px 0px #0926d3;
}

.ingrediente {
  border: 3px solid #000000;
  border-radius: 60px 60px 0px 0px;
  padding-bottom: 80px;
  width: 100%;
  background: #ffddf2;
  position: relative;
  top: -80px;
  box-shadow: inset -6px 6px 0px #0ab69f;
}

.ingredient {
  width: 90%;
  max-width: 352px;
  height: 31px;
  border-radius: 40px;
  border: 2px solid #000000;
  box-sizing: border-box;
  border-radius: 40px;
}
.steps {
  border-style: solid;
  border-width: 3px 3px 3px 3px;
  border-color: black;
  border-radius: 60px 60px 0px 0px;
  width: 100%;
  background: #fffafd;
  position: relative;
  top: -160px;
  margin-bottom: -160px;
  box-shadow: inset -6px 6px 0px #eab833;
}
.step {
  width: 90%;
  max-width: 352px;
  border-radius: 10px;
  border: 2px solid #000000;
  box-sizing: border-box;
  border-radius: 10px;
}
.uppercase {
  text-transform: uppercase;
}
</style>


