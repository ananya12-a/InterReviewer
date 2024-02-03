<template>
    <div>
      <v-card-title>{{title}}</v-card-title>
      <div :id="id"></div>
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
    props:[
      'filename',
      'id',
      'title'
    ],
    async mounted() {
      await this.fetchAndParseCSV();
      this.createChart()
    },
    methods: {
        parseCsvToChartOptions(csvString) {
            // Split the string into lines
            const lines = csvString.trim().split('\n');
            // console.log(lines)
            // Extract categories and values
            const x_vals = [];
            const emotions = lines[0].split(',')
            emotions.shift()
            // console.log("emotions", emotions)
            let series_to_put = []


  
            // Skip the header line, start from the first data line
            for (let j=0; j<emotions.length; j++){
                let this_dict = {'name': emotions[j], 'data': []}
                for (let i=1; i<lines.length; i++){
                    this_dict['data'].push(lines[i].split(",")[j+1])
                }
                series_to_put.push(this_dict)
            }
            
            for (let i = 1; i < lines.length; i++) {
                x_vals.push(lines[i].split(',')[0]);
            }
            // Construct the options object for the chart
            const options = {
                chart: {
                type: 'line' // or 'line' if you want a line chart
                },
                series: series_to_put,
                xaxis: {
                    categories: x_vals,
                    tickAmount: 20
                },
                stroke:{
                    width:2
                }
            };
  
            return options;
        },
      async fetchAndParseCSV() {
        try {
          // Fetching the CSV file from the server
          const response = await axios.get('http://localhost:5001/' + this.filename, { responseType: 'text' });
          this.chartOptions = this.parseCsvToChartOptions(response.data)
        } catch (error) {
          console.error('Error loading the CSV file:', error);
        }
      },
      createChart() {
        if (this.chartOptions) {
          const chart = new ApexCharts(document.querySelector("#" + this.id), this.chartOptions);
          chart.render();
        }
      }
    }
  }
  </script>
  
  <style>
  /* Your styles here */
  </style>
  