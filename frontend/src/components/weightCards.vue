<template>
    <v-card class="mx-auto" max-width="400">
  
        <v-card-text>
        <div v-for="(item, index) in text" :key="index">
            <strong>{{ item.title }}:</strong> {{ item.value }}
        </div>
        </v-card-text>
    </v-card>
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
        this.text = this.parseDataForCard(response.data)
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
  