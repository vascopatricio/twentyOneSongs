var React = require('react');

var Home = React.createClass({

  componentWillMount: function(){
    $('#slider').show();
  },

  render: function() {

    return (
      <div>
      <p>Home</p>
      </div>
    );
  }
});

module.exports = Home;
