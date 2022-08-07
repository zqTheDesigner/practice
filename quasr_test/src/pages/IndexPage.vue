<template>
  <!-- Landing Page -->
  <div
    style="
      background-color: #ff9494;
      width: 100vw;
      height: 100vh;
      flex-direction: column;
      display: flex;
      gap: 30px;
      justify-content: space-between;
    "
  >
    <!-- Header -->
    <div style="background-color: #d9d9d9; height: 88px">Header Box</div>
    <!-- Main Content -->
    <div
      style="
       height:100%
       flex-direction: row;
       display:flex;
       justify-content:space-between;
       gap: 30px;
    ">
      <!-- Side Nav -->
      <div style="background-color: #d9d9d9; width: 342px; height: 100%"></div>
      <!-- Body -->
      <div style="background-color: #d9d9d9; width: 100vw; height: 100%"></div>
      <!-- Side Nav -->
      <div style="background-color: #d9d9d9; width: 342px; height: 100%"></div>
    </div>
    <!-- Fotter -->
    <div style="background-color: #d9d9d9; height: 219px">Footer</div>
  </div>
</template>

<script setup lang="ts"></script>
