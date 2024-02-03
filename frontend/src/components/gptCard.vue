<template>
        <v-card-text>
            {{ this.text }}
        </v-card-text>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
        text: null
    };
  },
  props:[
    'filename',
  ],
  async mounted() {
    await this.fetchAndParseCSV();
  },
  methods: {
    parseDataForCard(jsonString) {
        // Parse the JSON string
        const data = JSON.parse(jsonString);

        // Format the data for the card
        const formattedData = Object.entries(data).map(([key, value]) => {
            return { title: key, value: value };
        });

        return formattedData;
    },
    async fetchAndParseCSV() {
      try {
        // Fetching the CSV file from the server
        const response = await axios.get('http://localhost:5001/' + this.filename, { responseType: 'text' });
        console.log(response.data)
        // console.log(this.chartOptions)
        // this.text = this.parseDataForCard(response.data)
        this.text = response.data
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
  