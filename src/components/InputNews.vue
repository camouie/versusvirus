<template>
  <div>
    <div><input class="input-message" type="text" v-model="value" placeholder="Copy/paste your text to be checked..." :disabled="!this.enabled"/></div>
    <div class="mt-3">
      <base-button type="success" size="sm" class="mr-4" @click="$emit('addMessage', {message : value, class : 'input-message'})"> Send </base-button>
    </div>
  </div>
</template>

<script>
import BaseButton from './BaseButton.vue';

export default {
  name: 'InputNews',
  components : {
    BaseButton
  },
  props: ['enabled'],
}
</script>
<style>
.input-message{
  width : 80%;
  margin : 0 auto;
  min-height : 40px;
}
</style>
