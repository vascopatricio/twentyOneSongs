import React from 'react'

import { Link } from 'react-router'

// Then we delete a bunch of code from App and
// add some <Link> elements...
const TopLevel = React.createClass({
  render() {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
})

module.exports = TopLevel;
