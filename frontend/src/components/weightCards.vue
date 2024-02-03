<template>
    <v-card class="mx-auto" max-width="400">
      <v-img
        src="https://example.com/image.jpg"
        height="200px"
      ></v-img>
  
      <v-card-title>
        Card Title
      </v-card-title>
  
      <v-card-text>
        This is some text within a card. You can put any content here you like, such as text, images, or other Vue components.
      </v-card-text>
  
      <v-card-actions>
        <v-btn color="primary" text>Button 1</v-btn>
        <v-btn color="secondary" text>Button 2</v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
    };
  },
  props:[
    'filename',
  ],
  async mounted() {
    await this.fetchAndParseCSV();
  },
  methods: {
      parseCsvToChartOptions(csvString) {
          // Split the string into lines
          const lines = csvString.trim().split('\n');

          // Extract categories and values
          const categories = [];
          const values = [];

          // Skip the header line, start from the first data line
          for (let i = 1; i < lines.length; i++) {
              const [category, value] = lines[i].split(',');
              categories.push(category);
              values.push(parseFloat(value));
          }

          // Construct the options object for the chart
          const options = {
              chart: {
              type: 'bar' // or 'line' if you want a line chart
              },
              series: [{
              name: 'Emotion Score',
              data: values
              }],
              xaxis: {
              categories: categories
              }
          };

          return options;
      },
    async fetchAndParseCSV() {
      try {
        // Fetching the CSV file from the server
        const response = await axios.get('http://localhost:5001/' + this.filename, { responseType: 'text' });
        // console.log(response)
        this.chartOptions = this.parseCsvToChartOptions(response.data)
        // console.log(this.chartOptions)
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
  