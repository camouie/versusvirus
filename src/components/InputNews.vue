<template>
  <div>
    <div><input class="input-message" type="text" v-model="value" placeholder="Copy/paste your text to be checked..."/></div>
    <div><button @click="$emit('addMessage', {message : value, class : 'input-message'})"> send </button></div>
  </div>
</template>

<script>
export default {
  name: 'InputNews',
  /*data () {
    return {
      text : {message: ""}
    }
  }*/
}
</script>
<style>
.input-message{
  width : 60%;
  margin : 0 auto;
  min-height : 40px;
}
</style>
