var React = require('react');

var Recommender = React.createClass({

  componentWillMount: function(){
    $('#slider').hide();
  },
  
  render: function() {

    return (
      <div>
        <p>Recommender</p>
      </div>
    );
  }
});

module.exports = Recommender;
