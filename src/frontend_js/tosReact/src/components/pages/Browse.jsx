var React = require('react');

var Browse = React.createClass({

  initializeDatatables: function(){
    var printPrefix = '[InitializeDatatables] ';
    console.log(printPrefix+'Started');

    var albumsDtableUrl = getApiServerLocation() + 'datatables/albums/';
    var songsDtableUrl = getApiServerLocation() + 'datatables/songs/';

    console.log(printPrefix+'Albums URL: '+albumsDtableUrl);
    console.log(printPrefix+'Songs URL: '+songsDtableUrl);

    var self = this;

    $('#albumDtable').DataTable({
      "ajax": albumsDtableUrl,
      "fnDrawCallback": function() {
        self.forceUpdate();
      },
    });

    $('#songDtable').DataTable({
      "ajax": songsDtableUrl,
      "fnDrawCallback": function() {
        self.forceUpdate();
      },
    });
  },

  componentDidMount: function(){
    $('#slider').hide();
    console.log('Calling Initializing datatables');
    this.initializeDatatables();
  },

  render: function() {

    var textAlignCenter = {textAlign: 'center'};

    return (
      <div className="row">
      <div className="col-md-8 col-md-offset-2" style={textAlignCenter}>
      <h3>Albums</h3>
      <table id="albumDtable" className="table table-condensed">
      <thead>
      <tr>
      <th>Title</th>
      <th>Year</th>
      </tr>
      </thead>
      <tbody></tbody>
      </table>

      <h3>Songs</h3>
      <table id="songDtable" className="table table-condensed">
      <thead>
      <tr>
      <th>Title</th>
      <th>Duration</th>
      <th>Genres</th>
      <th>Topics</th>
      </tr>
      </thead>
      <tbody></tbody>
      </table>
      </div>
      </div>
    );
  }
});

module.exports = Browse;
