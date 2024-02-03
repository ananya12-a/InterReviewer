<template>
    <div class="grey lighten-2">
      <v-row>
        <v-col cols="12">
            <div class="text-h3 ma-3">Analysis Dashboard</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card class="ma-3">
            <v-card-title>Recommendations for Improvement</v-card-title>
            <v-card-text>
              <gpt-card filename="gpt_recs.json"/>
            </v-card-text>
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
            <v-card-title>Top Interviewer Sentiments - Face Analysis</v-card-title>
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
            <v-card-title>Top Interviewer Sentiments - Speech Analysis</v-card-title>
            <v-card-text>
              <bar-plot filename="pros_viewer_barplot.csv" id="chart4"/>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Interviewee Sentiment Timeline</v-card-title>
            <v-card-text>
              <line-plot filename="face_viewee_tl.csv" id="chart6"/>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="ma-3">
            <v-card-title>Interviewer Sentiment Timeline</v-card-title>
            <v-card-text>
              <line-plot filename="face_viewer_tl.csv" id="chart5"/>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
    <!-- Each card takes up 3 columns on medium and larger screens -->
    <v-col cols="12" md="3">
      <v-card class="ma-3">
        <v-card-title>Interviewee Impression <br/> (Face)</v-card-title>
        <v-card-text>
          <weight-cards filename="interviewee_weight_face.csv"/>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" md="3">
      <v-card class="ma-3">
        <v-card-title>Interviewee Mood <br/> (Speech)</v-card-title>
        <v-card-text>
          <weight-cards filename="interviewee_weight_prosody.csv"/>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" md="3">
      <v-card class="ma-3">
        <v-card-title>Interviewer Impression <br/> (Face)</v-card-title>
        <v-card-text>
          <weight-cards filename="interviewer_weight_face.csv"/>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" md="3">
      <v-card class="ma-3">
        <v-card-title>Interviewer Mood <br/> (Speech)</v-card-title>
        <v-card-text>
          <weight-cards filename="interviewer_weight_prosody.csv"/>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
    </div>
  </template>
  
  <script>
import GptCard from '../components/gptCard.vue'
import weightCards from '../components/weightCards.vue'
  export default {
  components: { weightCards, GptCard },
    // Your script here
  }
  </script>
  
  <style>
  </style>
  