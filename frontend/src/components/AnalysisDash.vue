<template>
  <div>
    <div id="chart"></div>
  </div>
</template>

<script>
import axios from 'axios';
import ApexCharts from 'apexcharts';

export default {
  data() {
    return {
      chartOptions: {},
    };
  },
  async mounted() {
    await this.fetchAndParseCSV();
    this.createChart()
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
        const response = await axios.get('http://localhost:5001/data.csv', { responseType: 'text' });
        console.log(response)
        this.chartOptions = this.parseCsvToChartOptions(response.data)
        console.log(this.chartOptions)
      } catch (error) {
        console.error('Error loading the CSV file:', error);
      }
    },
    createChart() {
      if (this.chartOptions) {
        const chart = new ApexCharts(document.querySelector("#chart"), this.chartOptions);
        chart.render();
      }
    }
  }
}
</script>

<style>
/* Your styles here */
</style>
