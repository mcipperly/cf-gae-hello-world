# Cloud Foundry and App Engine Hello World App

This repository contains the code necessary for deploying application code to both Cloud Foundry and App Engine

## Steps for deploying on Cloud Foundry

1. Target your Cloud Foundry installation:

   `cf login -a <cf-api-target> -o <org> -s <space>`
    
2. Deploy:

   `cf push`

## Steps for deploying on App Engine

1. Set your `gcloud` auth/project info

2. Deploy:
 
   `gcloud beta app deploy`
