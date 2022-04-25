<template>
  <div class="drinks column items-center window-height">
    <div style="width:100%; max-width: 600px">
      <div class="text-h3 title q-mx-md q-my-lg">{{ title }}</div>
      <div class="row items-center justify-center q-gutter-md">
        <q-card
          v-for="drink in drinks"
          :key="drink.id"
          clickable
          @click="router.push('/drink/' + drink.id)"
          class="card row q-pb-md"
        >
          <q-card-section avatar class="q-pa-xs">
            <q-avatar class="avatar" size="110px">
              <img :src="drink.image" />
            </q-avatar>
          </q-card-section>

          <q-card-section class="col q-px-sm">
            <div class="uppercase text-h5 text-bold">{{ drink.name }}</div>
            <div class="text-body2 text-weight-medium q-mt-xs">
              {{ drink.description }}
            </div>
          </q-card-section>
        </q-card>
      </div>
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
      drinks.value.sort((a: Drink, b: Drink) => {
        let fa = a.name.toLowerCase(),
          fb = b.name.toLowerCase();

        if (fa < fb) {
          return -1;
        }
        if (fa > fb) {
          return 1;
        }
        return 0;
      });
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
.drinks {
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


