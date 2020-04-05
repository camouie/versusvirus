<template>
  <div>
    <div><textarea class="input-message form-control" v-model="value" placeholder="Copy/paste your text to be checked..." :disabled="!this.enabled"/></div>
    <p v-if="value.length < 50 && this.enabled" class="alert alert-danger mt-3 sized">{{info}}</p>
    <div class="mt-3">
      <base-button type="danger" size="sm" class="mb-4" @click="$emit('addMessage', {message : value, class : 'box sb4 person-message'}), clear()" :disabled="!this.enabled || value.length < 50"> Send </base-button>
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
    value : '',
    info : 'Please provide at least 50 characters.'
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
.input-message {
  width : 80% !important;
  margin : 0 auto;
  min-height : 40px;
}
.sized {
  width : 80% !important;
  margin : 0 auto;
}
</style>
