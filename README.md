# twentyOneSongs

Song recommender for songs by the Twenty One Pilots using structured song data.

# What it is
A very simple song recommender and browser for songs by the Twenty One Pilots. It can plug in and out multiple technologies of your liking once they're implemented with one click.

# Status
Server backends:
- [DONE] Python/Django
- [TODO] Python/Flask
- [TODO] Ruby on Rails
- [TODO] Node.js

Frontends:
- [DONE] Static HTML
- [IN PROGRESS] React.js
- [IN PROGRESS] AngularJS
- [TODO] Meteor.js
- [TODO] Ember.js
- [TODO] Backbone.js

APIs:
- [DONE] Python/Django handmade
- [TODO] Python/Django REST
- [TODO] Node.js
- [TODO] Firebase

# Recommendation
Using good old business intelligence knowledge, the idea is that if we structure the songs using more dimensions than usual, we can provide a higher level of recommendation. I decided to add moods, instruments, pacing and other elements so we have more data dimensions for recommendation, which is viable for a small dataset of ~30 songs, and make an elite recommendation system for any song by the TØP.

# Data
I also open-sourced the data I manually input - both the actual database scaffolded by Django and JSON exports are available for you to use in any pet projects of your liking.
