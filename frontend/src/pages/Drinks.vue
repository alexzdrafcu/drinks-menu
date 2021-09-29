<template>
  <div class="categories">
    <div class="text-h3 text-bold q-mx-lg q-my-lg q-py-sm">{{ title }}</div>
    <div class="cards row items-center justify-center q-gutter-md">
      <q-card
        v-for="drink in drinks"
        :key="drink.id"
        clickable
        @click="fct"
        class="card row q-pb-md"
      >
        <q-card-section avatar class="q-pa-xs">
          <q-avatar class="avatar" size="110px">
            <img
              src="https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg"
            />
          </q-avatar>
        </q-card-section>

        <q-card-section class="col q-px-sm">
          <div class="uppercase text-h5 text-bold">{{ drink.name }}</div>
          <div class="text-body2 text-weight-medium q-mt-xs">
            {{ drink.description }}
          </div>
        </q-card-section>
      </q-card>
      <q-card clickable @click="fct" class="card row q-pb-md">
        <q-card-section avatar class="q-pa-xs">
          <q-avatar class="avatar" size="110px">
            <img
              src="https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg"
            />
          </q-avatar>
        </q-card-section>

        <q-card-section class="col q-px-sm">
          <div class="uppercase text-h5 text-bold">DRY MARTINI</div>
          <div class="text-body2 text-weight-medium q-mt-xs">
            Extreme Strong (30%)
          </div>
        </q-card-section>
      </q-card>
            <q-card clickable @click="fct" class="card row q-pb-md">
        <q-card-section avatar class="q-pa-xs">
          <q-avatar class="avatar" size="110px">
            <img
              src="https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg"
            />
          </q-avatar>
        </q-card-section>

        <q-card-section class="col q-px-sm">
          <div class="uppercase text-h5 text-bold">DRY MARTINI</div>
          <div class="text-body2 text-weight-medium q-mt-xs">
            Extreme Strong (30%)
          </div>
        </q-card-section>
      </q-card>
            <q-card clickable @click="router.push('/drink')" class="card row q-pb-md">
        <q-card-section avatar class="q-pa-xs">
          <q-avatar class="avatar" size="110px">
            <img
              src="https://www.acouplecooks.com/wp-content/uploads/2020/04/Martini-003.jpg"
            />
          </q-avatar>
        </q-card-section>

        <q-card-section class="col q-px-sm">
          <div class="uppercase text-h5 text-bold">DRY MARTINI</div>
          <div class="text-body2 text-weight-medium q-mt-xs">
            Extreme Strong (30%)
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { Drink } from "../components/models";

export default defineComponent({
  name: "PageCategories",
  setup() {
    let router = useRouter();
    let title = ref("");
    let category = ref("");
    let categoryid = ref(0);
    let drinks = ref<Drink[]>([]);
    let fct = () => {
      console.log("fct de test");
      console.log(drinks.value);
    };
    // router.currentRoute.value.path.toString().split("/")[2])
    const loadCategories = async () => {
      const response = await fetch(
        "https://drinks-menu-backend.herokuapp.com/api/drinks/get_drink_by_category/" +
          categoryid.value
      );
      const data: Drink[] = await response.json();
      drinks.value = data;
    };
    onMounted(async () => {
      category.value = router.currentRoute.value.path.toString().split("/")[2];

      switch (category.value) {
        case "nucocktailuri":
          title.value = "Nu Cocktailuri";
          categoryid.value = 1;
          break;
        case "shoturi":
          title.value = "Shoturi";
          categoryid.value = 2;
          break;
        case "longdrinks":
          title.value = "Long drinks";
          categoryid.value = 3;
          break;
        case "cocktailuri":
          title.value = "Cocktailuri";
          categoryid.value = 4;
          break;
      }
      await loadCategories();
    });
    return {
      router,
      title,
      drinks,
      fct,
    };
  },
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap");
.categories {
  font-family: "Raleway", sans-serif;
}
.card {
  width: 90%;
  max-width: 380px;
  height: 136px;
  border-radius: 36px;
  border: 5px solid #000000;
  box-shadow: 0px -9px 0px 0px #0ab69f inset;
}

.avatar {
  border-radius: 36px;
}
.uppercase {
  text-transform: uppercase;
}
</style>


