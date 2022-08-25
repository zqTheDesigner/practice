<template>
  <!-- Start of parent -->
  <div
    style="
      width: 100vw;
      height: 100vh;
      display: flex;
      gap: 24px;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    "
  >
    <!-- Start of children -->

    <!-- Child group 1 -->
    <div style="width: 900px; display: flex; justify-content: end;">
      <div class="child"></div>
    </div>
    <!-- Child group 2 -->
    <div style="width: 900px; display: flex; justify-content: center">
      <div class="child"></div>
    </div>
    <!-- Child group 3 -->
    <div style="width: 900px; display: flex; justify-content: start">
      <div class="child"></div>
    </div>
    
    <!-- End of children -->


  </div>

  <!-- End of parent -->
</template>

<style scoped>
.child {
  width: 200px;
  height: 200px;
  background-color: #ff7575;
}
</style>
