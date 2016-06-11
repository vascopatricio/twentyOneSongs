var React = require('react');

var About = React.createClass({

  componentWillMount: function(){
    $('#slider').hide();
  },
  
  render: function() {

    return (
      <div>
        <p>About</p>
      </div>
    );
  }
});

module.exports = About;
