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
                        <div class="chatbot-container">
                          <div v-for="item in dialog" v-bind:key="item.message">
                            <p :class=item.class> {{item.message}}</p>
                          </div>
                          <InputNews v-on:addMessage="addMessageToDialog"/>
                        </div>
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
        { message : "Hello, before checking your news to see whether it's trustable or not, please answer some questions for me.", class : "chat-bot" },
        { message : "Did you check the source of information ?", class : "chat-bot" },
        { message : "Did you check the spelling and grammar ?", class : "chat-bot" },
        { message : "Did you check the author ?", class : "chat-bot" },
        { message : "Did you check the type of media (who is publishing) ?", class : "chat-bot" },
        //{ message : "Did you check date & time ?", class : "chat-bot" },
        { message : "Did you check the domain name (.com.co // .org //) ?", class : "chat-bot" },
      ],
    }
  },
  methods : {
    addMessageToDialog (text) {
      this.dialog.push(text);
      this.cpt += 1;
      if(this.cpt < this.botDialogs.length){
        this.dialog.push(this.botDialogs[this.cpt]);
      }
    }
  },
  created () {
    this.dialog.push(this.botDialogs[0]);
    this.dialog.push(this.botDialogs[1]);
  }
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

.input-message{
  width : 60%;
  margin : 0 auto;
  min-height : 40px;
}
</style>
