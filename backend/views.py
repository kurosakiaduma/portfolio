from django.shortcuts import render, redirect
from django.http import *

def projectDetails():
    projects = {
        "Poza": {
            "Desc": "A Django-powered health clinic that facilitates online booking and medical chatbots",
            "Github": "https://github.com/kurosakiaduma/poza",
            "Deployment": "https://poza.up.railway.app/",
            },
        "Anime Industry KPIs":{
            "Desc": "A meticulous assessment of performance factors and indicators in the success of studio releases by conducting a meticulous study of data scraped from MyAnimeList.",
            "Github": "https://github.com/kurosakiaduma/mal_analysis/",
            "Deployment": "#",
        },
        "Sentiment Analysis of WeRateDogs’ Twitter":{
            "Desc": "An in-depth study of WeRateDogs’ audience engagement model and shifts based on preference of dog breeds.",
            "Github": "https://github.com/kurosakiaduma/mal_analysis/",
            "Deployment": "#",
        },
    }
    return projects

def resourceDetails():
    resources = {
        "GeeksForGeeks": "https://geeksforgeeks.com",
        "Codepal AI": "https://codepal.ai/",
    }
    return resources