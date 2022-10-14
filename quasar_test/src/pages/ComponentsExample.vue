<template>
  <div style="max-width: 600px; padding: 2rem; margin: auto; border: 1px solid">
    <!-- Article -->
    <div style="display: flex; flex-direction: column; align-items: center">
      <!-- Button -->
      <div class="flex row items-center">
        <div>
          <s-btn outline="true" label="Read Less" color="green" />
        </div>

        <div>
          <s-btn label="Read More More" color="green" />
        </div>

        <div>
          <q-btn
            outline
            label="Read More"
            color="green-10"
            icon="visibility"
            size="0.75rem"
          />
        </div>

        <div>
          <q-btn
            label="Read Less"
            color="green-10"
            icon="visibility"
            size="0.75rem"
          />
        </div>
      </div>
    </div>
    <!-- End of Article -->
  </div>
</template>

<script setup>
import sBtn from 'src/components/sBtn.vue';
</script>

<style lang="scss"></style>
