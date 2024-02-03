<template>
  <div>
    <h1>Analysis</h1>
    <div id="chart"></div>
  </div>
</template>

<script>
// import AnalysisDash from '@/components/AnalysisDash.vue';
import ApexCharts from 'apexcharts'

export default {
  data() {
    return {
        options : {
            chart: {
                type: 'bar'
            },
            plotOptions: {
                bar: {
                horizontal: true
                }
            },
            series: [{
                data: [{
                x: 'category A',
                y: 10
                }, {
                x: 'category B',
                y: 18
                }, {
                x: 'category C',
                y: 13
                }]
            }]
            }
    }
  },
  mounted() {
    this.chartStuff();
  },
  methods: {
    chartStuff(){
        var options = {
            chart: {
                type: 'bar'
            },
            series: [{
                name: 'sales',
                data: [30,40,45,50,49,60,70,91,125]
            }],
            xaxis: {
                categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
            }
        }

        var chart = new ApexCharts(document.querySelector("#chart"), options);

        chart.render();
    }
  }
}
</script>

<style>

</style>