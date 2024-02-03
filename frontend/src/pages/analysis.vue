<template>
    <div class="grey lighten-2">
      <v-row>
        <v-col cols="12">
          <v-card class="ma-5">
            <v-card-title class="headline">Analysis Dashboard</v-card-title>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Top Interviewee Sentiments - Face Analysis</v-card-title>
            <v-card-text>
              <bar-plot filename="face_viewee_barplot.csv" id="chart1"/>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Top Interviewee Sentiments - Face Analysis</v-card-title>
            <v-card-text>
              <bar-plot filename="face_viewer_barplot.csv" id="chart2"/>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Top Interviewee Sentiments - Speech Analysis</v-card-title>
            <v-card-text>
              <bar-plot filename="pros_viewee_barplot.csv" id="chart3"/>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Top Interviewee Sentiments - Speech Analysis</v-card-title>
            <v-card-text>
              <bar-plot filename="pros_viewer_barplot.csv" id="chart4"/>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Line Plot 1</v-card-title>
            <v-card-text>
              <line-plot filename="face_viewer_tl.csv" id="chart5"/>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Line Plot 2</v-card-title>
            <v-card-text>
              <line-plot filename="face_viewee_tl.csv" id="chart6"/>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </template>
  
  <script>
  export default {
    // Your script here
  }
  </script>
  
  <style>
  </style>
  