<template>
  <div>
      <v-card-text v-if="interviewData">
        <div v-if="interviewData.interviewee_transcript && interviewData.interviewer_emotions">
          <strong>Transcript Highlights</strong> When you said "{{ interviewData.interviewee_transcript }}", the interviewer expressed {{ interviewData.interviewer_emotions }}.
        </div>
        <div v-if="interviewData.chat_gpt_repsonse">
          <strong>Recommendations:</strong> <div v-html="formattedChatGptResponse"></div>
        </div>
      </v-card-text>
      <v-card-text v-else>
        Loading data...
      </v-card-text>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
        interviewData: null
    };
  },
  props:[
    'filename',
  ],
  async mounted() {
    await this.fetchAndParseCSV();
  },
  computed: {
    formattedChatGptResponse() {
      return this.interviewData.chat_gpt_repsonse.replace(/\n\n/g, '<br>');
    }
  },
  methods: {
    parseInterviewData(jsonString) {
        // Parse the JSON string
        const data = JSON.parse(jsonString);

        // Extract and format the data
        let text = '';
        
        if (data.interviewee_transcript) {
            text += `When you said "${data.interviewee_transcript}", `;
        }

        if (data.interviewer_emotions) {
            text += `the interviewer felt ${data.interviewer_emotions}.\n\n`;
        }

        if (data.chat_gpt_repsonse) {
            text += `Here's some feedback for improvement:\n ${data.chat_gpt_repsonse}\n\n`;
        }

        return text;
    },
    async fetchAndParseCSV() {
      try {
        // Fetching the CSV file from the server
        const response = await axios.get('http://localhost:5001/' + this.filename, { responseType: 'text' });
        console.log("data", response.data)
        // console.log(this.chartOptions)
        this.interviewData = JSON.parse(response.data)
        console.log("interviewData", this.interviewData)
        // this.text = response.data
      } catch (error) {
        console.error('Error loading the CSV file:', error);
      }
    }
  }
}
  </script>
  
  <style>
  /* Your CSS here */
  </style>
  