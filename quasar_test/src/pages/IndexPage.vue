<template>
  <!-- Landing Page -->
  <div
    style="
      width: 100vw;
      height: 100vh;
      display: flex;
      gap: 34px;
      flex-direction: column;
      justify-content: space-between;
    "
  >
    <!-- Header -->
    <div
      style="
        background-color: #d9d9d9;
        height: 64px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
      "
    >
      <!-- MenuButton -->
      <div style="display: flex; flex-direction: row; align-items: center">
        <!-- <q-icon name="menu" /> -->
        <img
          style="width: 32px; height: 32px"
          src="../../public/menu_FILL0_wght400_GRAD0_opsz48.svg"
          alt=""
        />
      </div>
      <!-- Logo -->
      <div>
        <h6 style="color: #525252">Sentient.io</h6>
      </div>

      <!-- UerProfileBtn -->
      <div><q-icon name="account_circle" size="32px" /></div>
    </div>
    <!-- End of header -->

    <!-- Main Content -->
    <div
      style="
       height:100%;
       min-height: calc(100vh-64px-200px)
       flex-direction: row;
       display:flex;
       justify-content:space-between;
       gap: 34px;
    "
    >
      <!-- Side Nav -->
      <div style="background-color: #d9d9d9; width: 320px; height: 100%">
        <NavMenu :nav-menu="sideMenu" />
      </div>
      <!-- End of Side Nav -->

      <!-- Body -->
      <div style="background-color: #d9d9d9; width: 100vw; height: 100%">
        Main content - as much as possible, min-height: calc(100vh-64px-200px)
      </div>
    </div>
    <!-- Fotter -->
    <div style="background-color: #d9d9d9; height: 200px">
      Footer - 200px height
    </div>
  </div>
</template>

<script setup>
import NavMenu from 'src/components/nav/NavMenu.vue';
// const sideMenu_old = {
//   'Navigation Category 1': ['Nav item 1', 'Nav item 2'],
//   'Navigation Category 2': ['Nav item 1', 'Nav item 2'],
// };

// const navExample = ['val1', 'val2']
const sideMenu = [
  {
    category: 'Navigation Category 1',
    items: ['Nav item 1', 'Nav item 2'],
  },
  {
    category: 'Navigation Category 2',
    items: ['Nav item A', 'Nav item B'],
  },
  {
    category: 'Navigation Category 3',
    items: ['Nav item X', 'Nav item 1'],
  },
];
</script>
