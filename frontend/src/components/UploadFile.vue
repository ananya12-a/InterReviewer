<template>
  <div id="upload">
    <v-container fill-height>
      <v-row justify="center">
        <v-col cols="auto">
          <v-card width="800" height="400" raised> <!-- Adjusted height for dropdowns -->
            <v-card-title>Congratulations on finishing your interview! Upload your recording here:</v-card-title>
            <br>
            <v-card-text>
              <!-- Dropdown for who spoke first -->
              <v-select
                v-model="whoSpokeFirst"
                :items="speakers"
                label="Who spoke first?"
                outlined
              ></v-select>
              <!-- Dropdown for position of interviewer -->
              <v-select
                v-model="whoIsOnTheLeft"
                :items="speakers"
                label="Who was on the left?"
                outlined
              ></v-select>
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
                <span class="pl-2">Loading...</span>
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
    loading: false,
    whoSpokeFirst: null, // Selected value for who spoke first
    whoIsOnTheLeft: null, // Selected value for interviewer's position
    speakers: ['Interviewer', 'Interviewee'], // Items for who spoke first dropdown
  }),
  methods: {
    async submitFile() {
      if (!this.video) {
        return;
      }
      this.loading = true; // Start loading
      let formData = new FormData();
      formData.append('video', this.video);
      formData.append('whoSpokeFirst', this.whoSpokeFirst);
      formData.append('whoIsOnTheLeft', this.whoIsOnTheLeft);

      try {
        // Sending a POST request to the server with formData
        const response = await axios.post('http://localhost:5001/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log(response);
        // Redirecting to /analysis route on successful upload
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

