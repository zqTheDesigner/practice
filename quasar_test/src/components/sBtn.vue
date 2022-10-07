<template>
  <div>
    <button :style="btnStyle" style="border-radius: 4px" class="q-pa-sm">
      {{ label }}
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  label: {},
  outline: { default: false },
  color: {},
});

const evaluateBgColor = () => {
  if (props.outline) {
    return '#fff';
  } else {
    return props.color;
  }
};

const evaluateTextColor = () => {
  if (props.color && !props.outline) {
    return '#fff';
  } else {
    return props.color;
  }
};

const evaluateOutline = () => {
  if (props.color && props.outline) {
    return `1px solid ${props.color};`;
  } else {
    return 'none;';
  }
};

const btnStyle =
  `border:${evaluateOutline()};` +
  `background-color:${evaluateBgColor()};` +
  `color:${evaluateTextColor()};`;
</script>

<style lang="scss" scoped>

</style>
