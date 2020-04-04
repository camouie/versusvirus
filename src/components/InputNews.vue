<template>
  <div>
    <div><textarea class="input-message form-control" v-model="value" placeholder="Copy/paste your text to be checked..." :disabled="!this.enabled"/></div>
    <div class="mt-3">
      <base-button type="danger" size="sm" class="mb-4" @click="$emit('addMessage', {message : value, class : 'input-message'}), clear()"> Send </base-button>
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
  data () {
    return {
    value : ''
  }
},
methods : {
  clear () {
    this.value = '';
  }
}

}
</script>
<style>
.input-message{
  width : 80% !important;
  margin : 0 auto;
  min-height : 40px;
}
</style>
