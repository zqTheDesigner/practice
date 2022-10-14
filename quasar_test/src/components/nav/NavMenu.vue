<template>
  <div>
    <!-- {{ navMenu }} -->
    <!-- <li v-for="(v, k, i) in navMenu" :key="i">
      {{ v }}. {{ k }}: {{ i }}
    </li>  -->
    <div v-for="(menuCateg, idx) in navMenu" :key="idx">
      <q-expansion-item :label="menuCateg.category">
        <div v-for="menuItem in menuCateg.items" :key="menuItem">
          <p class="q-ml-md">
            {{ menuItem }}
          </p>
        </div>
      </q-expansion-item>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  navMenu: {},
});
</script>

<style lang="scss" scoped></style>
