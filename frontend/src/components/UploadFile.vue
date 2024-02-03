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
                outlined
                v-model="video"
                @change="handle"
              >
              </v-file-input>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn right @click="submitFile">Read File</v-btn>
            </v-card-actions>
          </v-card>
          <!-- Loading Indicator -->
          <v-dialog v-model="loading" hide-overlay persistent width="300">
            <v-card>
              <v-card-text>
                <v-progress-circular indeterminate size="50"></v-progress-circular>
                <span class="pl-2">Loading...</span> <!-- pl-2 is padding left 2 (8px) -->
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    video: null,
    data: null,
    loading: false,
  }),
  methods: {
    async submitFile() {
    if (!this.video) {
      this.data = "No File Chosen";
      return;
    }
    this.loading = true; // Start loading
    let formData = new FormData();
    formData.append('video', this.video);

    try {
      const response = await axios.post('http://localhost:5001/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log(response);
      this.$router.push('/analysis');
    } catch (error) {
      console.error(error);
    } finally {
      this.loading = false; // Stop loading whether request succeeds or fails
    }
  },
    handle(event) {
      this.video = event.target.files.length > 0 ? event.target.files[0] : null;
    }
  }
}
</script>
