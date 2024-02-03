<template>
  <div id="upload">
          <v-container fill-height>
            <v-row justify="center">
              <v-col cols="auto">
                <v-card width="800" height="300" raised>
                  <v-card-title>Congratulations on finishing your interview! Upload your recording here:</v-card-title>
                  <br>
                  <v-card-text>
                    <v-file-input
                      accept=".mp4"
                      label="Click here to select a .mp4 file"
                      outlined-v-model="video"
                      @change="handle"
                    >
                    </v-file-input>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn right @click="submitFile">Read File</v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
              <!-- <v-col cols="auto">
                <v-card width="800" height="300" raised>
                  <v-card-title>File contents:</v-card-title>
                  <v-card-text><p>{{ data }}</p></v-card-text>
                </v-card>
              </v-col> -->
            </v-row>
          </v-container>
    </div>
  </template>

<script>
import axios from "axios";
export default{
  data: ()=>({
      video:null,
      data: null,
  }),
  methods:{
    submitFile(){
      if (!this.video) {
        this.data = "No File Chosen"
      }
      // this.data = "successful upload"
      console.log(this.video)
      let formData = new FormData();
      formData.append('video', this.video);
      // axios.post( 'http://localhost:5001/upload',
      //         formData,
      //         {
      //         headers: {
      //             'Content-Type': 'multipart/form-data'
      //         }
      //       }
      //     ).then(function(){
      //   console.log('SUCCESS!!');
      // })
      // .catch(function(){
      //   console.log('FAILURE!!');
      // });
      axios.post('http://localhost:5001/upload', formData, {
          headers: {
              'Content-Type': 'multipart/form-data'
          }
      })
      .then(response => {
          console.log(response);
      })
      .catch(error => {
          console.error(error);
      });
    },
    handle(event){
      this.video = event.target.files.length > 0 ? event.target.files[0] : null;
    }
  }
}
</script>