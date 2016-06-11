import React from 'react'
import { render } from 'react-dom'

// First we import some modules...
import { Router, Route, DefaultRoute, IndexRoute, Link, hashHistory }
  from 'react-router'

var App = require('./components/TopLevel.jsx');

const About = React.createClass({
  render(){
    return (<p>About</p>)
  }
})
const Inbox = React.createClass({
  render(){
      return(<p>Inbox</p>)
  }
})
const Home = React.createClass({
  render(){
      return(<p>Home</p>)
  }
})

var AboutPage = require('./components/pages/About.jsx');
var BrowsePage = require('./components/pages/Browse.jsx');
var HomePage = require('./components/pages/Home.jsx');
var RecommenderPage = require('./components/pages/Recommender.jsx');

// Finally, we render a <Router> with some <Route>s.
// It does all the fancy routing stuff for us.
render((
  <Router history={hashHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={HomePage} />
      <Route path="reactHome" component={HomePage} />
      <Route path="reactBrowse" component={BrowsePage} />
      <Route path="reactRecomm" component={RecommenderPage} />
      <Route path="reactAbout" component={AboutPage} />
      <Route path="*" component={ HomePage }/>
    </Route>
  </Router>
), document.getElementById('reactApp'))
