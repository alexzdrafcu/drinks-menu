<template>
  <div class="recipe-page">
    <!-- <div class="image"></div>
    <q-img
      src="https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg"
    /> -->
    <div class="header" />
    <div class="recipe column items-center justify-center">
      <div class="title q-pt-md q-mb-lg">
        <div class="text-h5 text-bold text-center">DRY MARTINI</div>
        <div class="text-caption text-center">Extreme Strong 30%</div>
      </div>

      <div class="ingrediente column items-center justify-center q-pt-md q-mb-lg">
        <div class="text-h6 text-bold text-center q-my-sm">INGREDIENTE</div>
        <div
          class="ingredient row items-center q-px-md q-my-xs text-weight-medium"
        >
          50 ml Gin
        </div>
        <div
          class="ingredient row items-center q-px-md q-my-xs text-weight-medium"
        >
          50 ml Gin
        </div>
        <div
          class="ingredient row items-center q-px-md q-my-xs text-weight-medium"
        >
          50 ml Gin
        </div>
      </div>
      <div class="steps column items-center justify-center q-pt-md q-pb-xl">
        <div class="text-h6 text-bold text-center q-my-sm">PREPARARE</div>
        <div class="step q-px-md q-py-xs q-my-xs">
          <div class="text-caption text-bold text-grey-6">Pasul #1/3</div>
          <div class="text-weight-medium">
            Adaugă gheața în paharul pentru mixat.
          </div>
        </div>
        <div class="step q-px-md q-py-xs q-my-xs">
          <div class="text-caption text-bold text-grey-6">Pasul #1/3</div>
          <div class="text-weight-medium">
            Adaugă gheața în paharul pentru mixat.
          </div>
        </div>
      </div>
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
.recipe-page {
  font-family: "Raleway", sans-serif;
  height: 500px;
  background-image: url("https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg");
  background-color: #cccccc; /* Used if the image is unavailable */
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
  box-shadow: inset -6px 6px 0px #0AB69F;
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
  box-shadow: inset -6px 6px 0px #EAB833;
}
.step {
  width: 90%;
  max-width: 352px;
  border-radius: 10px;
  border: 2px solid #000000;
  box-sizing: border-box;
  border-radius: 10px;
}
</style>


