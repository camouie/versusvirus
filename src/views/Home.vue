<template>
  <div class="profile-page">
      <section class="section-profile-cover section-shaped my-0">
          <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>
          </div>
      </section>
      <section class="section section-skew">
          <div class="container">
              <card shadow class="card-profile mt--300" no-body>
                  <div class="px-4">
                      <div class="row justify-content-center">
                        <!-- content -->
                        <transition name="fade">
                        <div class="chatbot-container" ref="chatContainer">
                          <div v-for="item in dialog" v-bind:key="item.message">
                            <div :class="item.class"><p> {{item.message}} </p></div>
                            <div v-if="item.id > 1 && item.id < 7">
                              <input type="radio" :name=item.id class="my-radio" v-on:change="nextQuestion(item.id)"/>Yes, I did.

                              <input type="radio" :name=item.id class="my-radio" v-on:change="nextQuestion(item.id)" />I don't know.

                              <input type="radio" :name=item.id class="my-radio" v-on:change="nextQuestion(item.id)" />No !
                            </div>
                          </div>
                          <InputNews v-on:addMessage="addMessageToDialog" v-bind:enabled="inputEnabled"/>
                        </div>
                      </transition>
                        <!-- end of content -->
                      </div>

                  </div>
              </card>
          </div>
      </section>
  </div>
</template>

<script>
import InputNews from '../components/InputNews';
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    InputNews
  },
  data () {
    return {
      cpt : 1,
      dialog : [],
      botDialogs : [
        { id: 1, message : "Hello, before checking your news to see whether it's trustable or not, please answer this 5 questions for me.", class : "box sb3" },
        { id: 2, message : "Did you check the source of information ?", class : "box sb3" },
        { id: 3, message : "Did you check the spelling and grammar ?", class : "box sb3" },
        { id: 4, message : "Did you check the author ?", class : "box sb3" },
        { id: 5, message : "Did you check the type of media (who is publishing) ?", class : "box sb3" },
        //{ message : "Did you check date & time ?", class : "chat-bot" },
        { id: 6, message : "Did you check the domain name (.com.co // .org //) ?", class : "box sb3" },
        { id: 7, message : "Thank you.", class : "box sb3" },
        { id: 8, message : "You can now copy/paste the news you want me to check.", class : "box sb3" },

      ],
      inputEnabled:false,
      info : null,
      confidenceMessage: "",
    }
  },
  methods : {
    addMessageToDialog (text) {
      this.dialog.push(text);
      this.isItFake(text);
    },
    nextQuestion (id) {
      var contains = this.dialog.filter(it => it.id == id+1).length;
      if(contains == 0){
        this.dialog.push(this.botDialogs[id]);
        this.cpt += 1;
      }
    },
    isItFake (message) {
      axios.post(`http://datasemlab.ch:5310/sams/api/detect`, {
        text : message.message
      })
      .then(response => {
        console.log(response);
        var prob = response.data.OK.probability * 100;
        prob > 90 ? this.confidenceMessage = "very confident" : prob > 70 ? this.confidenceMessage = "pretty confident" : this.confidenceMessage = "not very sure";
        var responseToAdd = { message : "So...with a propability of " + response.data.OK.probability * 100 + "%, I can say that I am " + this.confidenceMessage +" that it is " + response.data.OK.class + ".", class : "box sb3 "+ response.data.OK.class}
        //http://datasemlab.ch:5310/sams/api/recommend
        //var responseToAdd = { message : response.data.OK.doc + ".", class : "box sb3 "+ response.data.OK.class}

        this.dialog.push(responseToAdd);
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
  },
  created () {
    this.dialog.push(this.botDialogs[0]);
    this.dialog.push(this.botDialogs[1]);
  },
  watch: {
    cpt () {
      if (this.cpt == 6) {
        this.dialog.push(this.botDialogs[7]);
        this.inputEnabled = true;
      }
    },
  },
  updated: function(){
    var container = this.$refs.chatContainer;
    container.scrollTop = container.scrollHeight;
  },

}
</script>

<style>
.chat-bot {
  width : 60%;
  margin : 10px auto;
  background-color: #42b983;
  border-radius: 15px;
  padding: 10px 10px;
}

.padded {
  padding: 10px 10px;
}

.my-radio{
  padding: 5px 5px;
  margin: 10px 10px;
}

.chatbot-container {
  overflow:scroll;
  height:500px;
}

.card.card-profile{
  min-height: 500px !important;
}

@media only screen and (max-width: 900px) {
  .profile-page .card-profile {
    height:100% !important;
    margin-top: -300px !important;
  }
}

.box {
  width: 80%;
  margin: 25px auto;
  background: #086788;
  padding: 10px;
  text-align: center;
  font-weight: 900;
  color: #fff;
  font-family: arial;
  position: relative;
}

.person-message {
  background : #069fc2;
}

.False{
  background : #FF0000;
}

.Real {
  background : #2dce89;
}

.sb3:before {
  content: "";
  width: 0px;
  height: 0px;
  position: absolute;
  border-left: 10px solid #086788;
  border-right: 10px solid transparent;
  border-top: 10px solid #086788;
  border-bottom: 10px solid transparent;
  left: 19px;
  bottom: -19px;
}
.sb3.Real:before {
  border-left: 10px solid #2dce89;
  border-top: 10px solid #2dce89;
}
.sb3.False:before {
  border-left: 10px solid #FF0000;
  border-top: 10px solid #FF0000;
}
.sb4:before {
  content: "";
  width: 0px;
  height: 0px;
  position: absolute;
  border-left: 10px solid transparent;
  border-right: 10px solid #069fc2;
  border-top: 10px solid #069fc2;
  border-bottom: 10px solid transparent;
  right: 19px;
  bottom: -19px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}

</style>
